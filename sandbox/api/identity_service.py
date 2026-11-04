"""
Identity Service: OBO token handling and ACL validation
"""
import json
from pathlib import Path
from typing import Optional, List
import uuid
from datetime import datetime

from models import UserContext, AccessCheckResult


class IdentityService:
    """Handles identity and access control"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.users_cache = self._load_users()
        self.acls_cache = self._load_acls()

    def _load_users(self) -> dict:
        """Load users from JSON"""
        users_file = self.data_dir / "users.json"
        with open(users_file) as f:
            users = json.load(f)
        return {user["oid"]: user for user in users}

    def _load_acls(self) -> dict:
        """Load account ACLs from JSON"""
        acls_file = self.data_dir / "account_acls.json"
        with open(acls_file) as f:
            acls = json.load(f)
        return {acl["accountId"]: acl for acl in acls}

    def create_user_context_from_token(self, user_oid: str) -> Optional[UserContext]:
        """
        Simulate extracting user context from OBO token.
        In real scenario, token would be validated and decoded by Entra.
        """
        if user_oid not in self.users_cache:
            return None

        user_data = self.users_cache[user_oid]
        return UserContext(
            oid=user_oid,
            name=user_data["name"],
            email=user_data["email"],
            groups=user_data.get("groups", []),
            correlationId=str(uuid.uuid4())
        )

    def check_account_access(
        self,
        account_id: str,
        user_context: UserContext
    ) -> AccessCheckResult:
        """
        Check if user has access to account based on ACL.
        
        Access is granted if:
        1. User is in allowedUsers, OR
        2. User's group is in allowedGroups
        
        AND not in denied lists.
        """
        if account_id not in self.acls_cache:
            # Account not found
            return AccessCheckResult(allowed=False, reason="Account not found")

        acl = self.acls_cache[account_id]

        # Check denied first
        if user_context.oid in acl.get("deniedUsers", []):
            return AccessCheckResult(allowed=False, reason="User is explicitly denied")

        user_denied_groups = set(user_context.groups) & set(acl.get("deniedGroups", []))
        if user_denied_groups:
            return AccessCheckResult(allowed=False, reason="User's group is explicitly denied")

        # Check allowed
        if user_context.oid in acl.get("allowedUsers", []):
            return AccessCheckResult(allowed=True)

        user_allowed_groups = set(user_context.groups) & set(acl.get("allowedGroups", []))
        if user_allowed_groups:
            return AccessCheckResult(allowed=True)

        return AccessCheckResult(allowed=False, reason="User not in allowed users or groups")

    def get_user_allowed_accounts(self, user_context: UserContext) -> List[str]:
        """
        Get all accounts accessible to a user.
        Used for search filtering.
        """
        allowed_accounts = []
        for account_id, acl in self.acls_cache.items():
            # Check denied
            if user_context.oid in acl.get("deniedUsers", []):
                continue
            user_denied_groups = set(user_context.groups) & set(acl.get("deniedGroups", []))
            if user_denied_groups:
                continue

            # Check allowed
            if user_context.oid in acl.get("allowedUsers", []):
                allowed_accounts.append(account_id)
            else:
                user_allowed_groups = set(user_context.groups) & set(acl.get("allowedGroups", []))
                if user_allowed_groups:
                    allowed_accounts.append(account_id)

        return allowed_accounts
