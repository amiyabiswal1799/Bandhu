from config.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime


class ChatSession(Base):
    __tablename__ = 'chat_sessions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(255), unique=True, nullable=False, index=True)
    user_id = Column(String(255), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    
    def __repr__(self):
        return f"<ChatSession(id={self.id}, session_id='{self.session_id}')>"


class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(255), nullable=False, index=True)
    role = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    message_metadata = Column(Text, nullable=True)
    
    def __repr__(self):
        return f"<ChatMessage(id={self.id}, session_id='{self.session_id}', role='{self.role}')>"


class FileUpload(Base):
    __tablename__ = 'file_uploads'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    s3_key = Column(String(500), nullable=True)
    session_id = Column(String(255), nullable=True, index=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    file_size = Column(Integer, nullable=True)
    content_type = Column(String(100), nullable=True)
    
    def __repr__(self):
        return f"<FileUpload(id={self.id}, file_name='{self.file_name}')>"
