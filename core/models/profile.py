from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from .mixins import UserRelationMixin


class Profile(Base, UserRelationMixin):
    _user_back_populates = "profile"
    _user_id_unique = True
    _user_id_nullable = False

    first_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    last_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    bio: Mapped[str | None]
