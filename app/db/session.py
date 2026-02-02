import ssl
from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

# Verify DATABASE_URL is set
if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Handle 'postgres://' case for SQLAlchemy compatibility and use pg8000 driver
connection_string = str(settings.DATABASE_URL)
if "postgresql+pg8000" not in connection_string:
    connection_string = connection_string.replace("postgres://", "postgresql+pg8000://").replace("postgresql://", "postgresql+pg8000://")

# Create SSL context for Neon/pg8000
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

engine = create_engine(
    connection_string, 
    echo=True,
    connect_args={"ssl_context": ssl_context}
)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
