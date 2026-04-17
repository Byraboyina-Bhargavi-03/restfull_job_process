from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import crud, schemas
from .worker import process_job

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Job
@app.post("/jobs/", response_model=schemas.JobResponse)
def create_job(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    job = crud.create_job(db)

    # Run background task
    background_tasks.add_task(process_job, job.id)

    return job

# Get Job Status
@app.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job
