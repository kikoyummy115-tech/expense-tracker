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

    # Relationships back to User and Category
    user = db.relationship("User", back_populates="expenses")
    category = db.relationship("Category", back_populates="expenses")