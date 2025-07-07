from datetime import datetime, timezone

class User:
    def __init__(self, email, username, hashed_password):
        self.email = email
        self.username = username
        self.hashed_password = hashed_password
        self.created_at = datetime.now(timezone.utc)