from database import Base
from sqlalchemy import Column,UUID,Integer,Boolean,Text,String,DateTime,func,ForeignKey
import uuid
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__='user'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    fullname = Column(String(50))
    email = Column(String(50),unique=True)
    phone = Column(String(50),unique=True,nullable=True)
    password = Column(Text, nullable=False)
    profile = relationship('Profile',back_populates='user')
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), server_onupdate=func.now()
    )

class Profile(Base):
    __tablename__='profile'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    profile_picture = Column(Text, nullable=False)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("user.id")
    )
    user = relationship('User',back_populates='profile')