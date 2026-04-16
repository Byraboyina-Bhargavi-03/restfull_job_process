from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from app.worker import process_job

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs", response_model=schemas.JobResponse)
def create_job(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    job = crud.create_job(db)
    background_tasks.add_task(process_job, job.id)
    return job
@router.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def get_job(job_id: str, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job