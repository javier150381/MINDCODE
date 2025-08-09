from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Workspace(Base):
    __tablename__ = "workspaces"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    uri = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    text = Column(Text)
    embedding = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    role = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Usage(Base):
    __tablename__ = "usage"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, index=True)
    metric = Column(String)
    value = Column(Integer)
    period_start = Column(DateTime)
    period_end = Column(DateTime)
