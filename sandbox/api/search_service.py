"""
Search Service: In-memory search index with ACL filtering
"""
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from models import SearchIndexDocument, SearchResult


class SearchService:
    """In-memory search service with ACL filtering"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.index = self._build_index()

    def _build_index(self) -> List[SearchIndexDocument]:
        """Build search index from data sources"""
        index = []

        # Load documents
        docs_file = self.data_dir / "documents.json"
        with open(docs_file) as f:
            documents = json.load(f)

        # Load account ACLs
        acls_file = self.data_dir / "account_acls.json"
        with open(acls_file) as f:
            acls_data = json.load(f)
            acls_by_account = {acl["accountId"]: acl for acl in acls_data}

        # Add documents to index
        for doc in documents:
            account_id = doc["accountId"]
            acl_groups = acls_by_account.get(account_id, {}).get("allowedGroups", [])

            index_doc = SearchIndexDocument(
                id=doc["id"],
                accountId=account_id,
                title=doc["title"],
                content=doc["content"],
                category=doc["category"],
                source=doc["source"],
                sourceUri=doc["sourceUri"],
                aclGroups=acl_groups
            )
            index.append(index_doc)

        # Load emails
        emails_file = self.data_dir / "emails.json"
        with open(emails_file) as f:
            emails = json.load(f)

        for email in emails:
            account_id = email["accountId"]
            acl_groups = acls_by_account.get(account_id, {}).get("allowedGroups", [])

            # Create searchable document from email
            index_doc = SearchIndexDocument(
                id=email["id"],
                accountId=account_id,
                title=f"Email: {email['subject']}",
                content=f"{email['body']}\nFrom: {email['from']}\nTo: {email['to']}",
                category="email",
                source="email",
                sourceUri=email["sourceUri"],
                aclGroups=acl_groups
            )
            index.append(index_doc)

        # Load transactions
        txns_file = self.data_dir / "transactions.json"
        with open(txns_file) as f:
            transactions = json.load(f)

        for txn in transactions:
            account_id = txn["accountId"]
            acl_groups = acls_by_account.get(account_id, {}).get("allowedGroups", [])

            index_doc = SearchIndexDocument(
                id=txn["id"],
                accountId=account_id,
                title=f"Transaction: {txn['description']}",
                content=f"Amount: ${txn['amount']:,}\nCategory: {txn['category']}\nDate: {txn['date']}",
                category="transaction",
                source="transaction",
                sourceUri=txn["sourceUri"],
                aclGroups=acl_groups
            )
            index.append(index_doc)

        return index

    def search(
        self,
        query: str,
        account_id: Optional[str] = None,
        allowed_accounts: Optional[List[str]] = None,
        user_groups: Optional[List[str]] = None,
        limit: int = 10
    ) -> List[SearchResult]:
        """
        Search index with ACL filtering.
        
        Args:
            query: Search query string
            account_id: Optional specific account to search
            allowed_accounts: List of accounts user can access
            user_groups: User's groups for ACL checking
            limit: Max results to return
        
        Returns:
            Ranked search results
        """
        if user_groups is None:
            user_groups = []
        if allowed_accounts is None:
            allowed_accounts = []

        results = []
        query_lower = query.lower()

        for doc in self.index:
            # Account filtering
            if account_id and doc.accountId != account_id:
                continue
            if allowed_accounts and doc.accountId not in allowed_accounts:
                continue

            # ACL filtering: document's allowed groups must overlap with user's groups
            if doc.aclGroups and user_groups:
                if not (set(doc.aclGroups) & set(user_groups)):
                    continue
            elif doc.aclGroups and not user_groups:
                # Document has ACL but user has no groups
                continue

            # Text matching
            score = self._calculate_relevance(query_lower, doc)
            if score > 0:
                result = SearchResult(
                    id=doc.id,
                    title=doc.title,
                    content=doc.content[:200],  # Truncate for display
                    source=doc.source,
                    sourceUri=doc.sourceUri,
                    score=score,
                    aclGroups=doc.aclGroups
                )
                results.append(result)

        # Sort by relevance and apply limit
        results.sort(key=lambda x: x.score, reverse=True)
        return results[:limit]

    def get_document_by_id(self, doc_id: str, user_groups: Optional[List[str]] = None) -> Optional[SearchIndexDocument]:
        """
        Get specific document by ID with ACL check.
        """
        if user_groups is None:
            user_groups = []

        for doc in self.index:
            if doc.id == doc_id:
                # ACL check
                if doc.aclGroups and user_groups:
                    if not (set(doc.aclGroups) & set(user_groups)):
                        return None
                elif doc.aclGroups and not user_groups:
                    return None
                return doc

        return None

    def _calculate_relevance(self, query_lower: str, doc: SearchIndexDocument) -> float:
        """
        Simple relevance scoring.
        In real scenario, would use BM25 or ML-based ranking.
        """
        score = 0.0

        # Title match (higher weight)
        if query_lower in doc.title.lower():
            score += 2.0
            # Boost if query appears at start
            if doc.title.lower().startswith(query_lower):
                score += 1.0

        # Content match
        if query_lower in doc.content.lower():
            # Count occurrences
            count = doc.content.lower().count(query_lower)
            score += min(count * 0.5, 2.0)  # Cap at 2.0

        # Boost recent documents
        # (simplified - in real scenario would use actual dates)
        if "2024-10" in doc.content or "2024-10" in doc.title:
            score += 0.5

        return score

