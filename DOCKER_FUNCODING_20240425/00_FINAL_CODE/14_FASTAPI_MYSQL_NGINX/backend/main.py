import time
from typing import List, Optional
from fastapi import FastAPI, Depends
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal, Todo as TodoModel
from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str

class Todo(BaseModel):
    id: Optional[int] = None
    title: str

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

retries = 5
while retries > 0:
    try:
        conn = engine.connect()
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        retries -= 1
        print(f"Database connection failed. Retries left: {retries}")
        time.sleep(5)

if retries == 0:
    raise Exception("Could not connect to the database")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todos/", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = TodoModel(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos/", response_model=List[Todo])
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos
