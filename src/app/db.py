from sqlmodel import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:1001@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)


