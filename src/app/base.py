from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:1001@localhost:5432/git_gud"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
