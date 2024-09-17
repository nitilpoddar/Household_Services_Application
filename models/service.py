from models import db
from sqlalchemy.orm import Mapped, mapped_column

class Service:
    id:Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    price:Mapped[int] = mapped_column(nullable=False)
    time_required:Mapped[int] = mapped_column(nullable=False)
    description:Mapped[str] = mapped_column(nullable=False)