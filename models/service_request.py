from models import db
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from sqlalchemy import ForeignKey
from models import customer, professional

class ServiceRequest:
    id:Mapped[int] = mapped_column(unique=True, nullable=False, autoincrement=True)
    service_id:Mapped[int] = mapped_column()