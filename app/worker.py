import time
from sqlalchemy.orm import Session
from .database import SessionLocal
from .crud import update_job

def process_job(job_id: int):
    db: Session = SessionLocal()

    try:
        # Set status to in_progress
        update_job(db, job_id, "in_progress")

        # Simulate processing delay
        time.sleep(5)

        # Simulated result
        result = f"Job {job_id} completed successfully"

        update_job(db, job_id, "completed", result)

    except Exception as e:
        update_job(db, job_id, "failed", str(e))

    finally:
        db.close()