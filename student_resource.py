from fastapi import FastAPI
from uuid import UUID


app = FastAPI()

#create a dictionary
students = {}

#create the dictionary data
student_data = {"id": 0, "name": "", "age": 0, "sex": "", "height": 0,}


#display message
@app.get("/")
def home():
    return {"message": "Welcome to my student resouce API" }

#a. Create a Student resource
@app.post ("/students")
def create_student_resouce(
name: str, age: int, sex: str, height: float
):
    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student
    return {"message": "Student resource created successfully", "data": new_student}

#b. Retrieve a Student resource with id (one Student)
@app.get("/students/{id}")
def retrieve_student_resource(id: int):
    student = students.get(id)
    if not student:
        return {"error": "Student not found!"}
    
    return {"data": student}

#b2. Retrieve all Students resource
@app.get("/students")
def retrieve_all_students_resource():
    return students



#c. Update a Student resource
@app.put("/students{id}")
def update_student_resource(
    id: int, name: str, age: int, sex: str, height: float
):
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}
    
    student["name"] = name
    student["sex"] = sex
    student["height"] = height

    return {"message": "Student resource updated successfully", "data": student}


#d. Delete a Student resource

@app.delete("/students/{id}")  # DELETE method to delete a resource
def delete_student_resource(id: int):
    student = students.get(id)
    if not student:
        return {"error": "Student not found!"}
    
    del students[id]

    return {"message": "Student resource deleted successfully"}
