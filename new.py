from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

class Students(BaseModel):
    id : int 
    name : str
    grade : int 
    
students = [
    Students(id=1, name="Ibrahim salem", grade=4), 
    Students(id=2, name="khadija ali", grade=3)
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(newStudent: Students):
    students.append(newStudent)
    return newStudent

@app.put("/students/{student_id}")
def update_students(student_id : int, update_student : Students):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = update_student
            return update_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    for i , student in enumerate(students):
        if student.id == student_id:
            del students[i]
            return {"message":"Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
