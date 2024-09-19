from models import db
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship
from sqlalchemy import ForeignKey
from models import customer, professional,service
from datetime import datetime

class ServiceRequest(db.Model):
    id:Mapped[int] = mapped_column(unique=True, nullable=False, autoincrement=True)
    service_id:Mapped[int] = mapped_column(ForeignKey('service.id'), nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'), nullable=False)
    professional_id: Mapped[int] = mapped_column(ForeignKey('professional.id'), nullable=False)
