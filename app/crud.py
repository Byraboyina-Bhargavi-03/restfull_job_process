from sqlalchemy.orm import Session
from . import models

def create_job(db: Session):
    job = models.Job(status="pending")
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def update_job(db: Session, job_id: int, status: str, result: str = None):
    job = get_job(db, job_id)
    if job:
        job.status = status
        job.result = result
        db.commit()
    return job