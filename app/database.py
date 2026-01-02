from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
import shutil

# Determine if we are running in a Lambda environment (simple heuristic or env var)
# But safe default for this setup is to check if we can write to current dir, if not use /tmp
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = "movies.db"
# We expect the DB to be at project root in the container, so one level up from app/
SOURCE_DB = os.path.join(BASE_DIR, "..", DB_FILE)
DEST_DB = f"/tmp/{DB_FILE}"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DEST_DB}"

# Copy db to /tmp if it doesn't exist there, to avoid Read-Only errors in Lambda
if os.path.exists(SOURCE_DB) and not os.path.exists(DEST_DB):
    shutil.copy(SOURCE_DB, DEST_DB)
elif not os.path.exists(DEST_DB):
    # Fallback for local dev if not using Docker exactly as predicted
    # or if purely local run without seeded db in root
    # We'll just stick to local path if source doesn't exist (e.g. initial dev)
    # But for the artifact task, we know movies.db is in root.
    if os.path.exists(DB_FILE): # check CWD
         shutil.copy(DB_FILE, DEST_DB)
    else:
         # Fallback to local file if we can't find it to copy (allows local uv run)
         SQLALCHEMY_DATABASE_URL = f"sqlite:///./{DB_FILE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
