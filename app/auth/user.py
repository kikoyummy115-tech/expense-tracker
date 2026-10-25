from extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    email = db.Column(db.String(255), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Relationship to expenses
    expenses = db.relationship("Expense", back_populates="user", lazy=True)
