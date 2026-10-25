from extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    type = db.Column(db.String(100), nullable=False)

    # Relationship to expenses
    expenses = db.relationship("Expense", back_populates="category", lazy=True)


