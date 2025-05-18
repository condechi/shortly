import os
import datetime
import random
import string
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Base class for ORM models\ nBase = declarative_base()
Base = declarative_base()

class Link(Base):
    """
    ORM model representing a shortened link:
    - original_url: the full URL provided by the user
    - code: unique 6-character short code
    - created_at: timestamp when record was created
    - click_count: total number of times link has been visited
    - last_accessed: timestamp of last visit
    """
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    code = Column(String(6), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    click_count = Column(Integer, default=0)
    last_accessed = Column(DateTime)

    @classmethod
    def create(cls, original_url):
        """
        Instantiate a new Link with a unique code.
        """
        code = cls._generate_unique_code()
        return cls(original_url=original_url, code=code)

    @staticmethod
    def _generate_unique_code(length=6):
        """
        Generate a random alphanumeric string for the short code.
        """
        alphabet = string.ascii_letters + string.digits
        return ''.join(random.choices(alphabet, k=length))

# Database URL from environment or default
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///shortly.db')

# Create engine and session factory
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))

# Create tables if they don't exist
Base.metadata.create_all(engine)


def get_db():
    """
    Return a new database session for request handling.
    """
    return SessionLocal()