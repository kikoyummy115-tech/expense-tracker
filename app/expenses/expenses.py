from extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    price = db.Column(db.Integer, nullable=False)

    category_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("categories.id"),
        nullable=False,
    )
    
    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id"),
        nullable=False,
    )
