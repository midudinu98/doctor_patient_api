from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr,Field

app=FastAPI(title="Doctor-Patient API management")

doctors=[]
patients=[]

class Doctor(BaseModel):
    name:str
    specialization:str
    email:EmailStr
    is_active:bool=True


class Patient(BaseModel):
    name:str
    age:int=Field(gt=0)
    phone:str 


@app.post("/doctors")
def create_doctor(doctor:Doctor):
    doctor_data={
                 "id":len(doctors)+1,
                 "name":doctor.name,
                 "specialization":doctor.specialization,
                 "email":doctor.email,
                 "is_active":doctor.is_active
                 }    

    doctors.append(doctor_data)

    return doctor_data

@app.get("/doctors")
def get_doctors():
    return doctors

@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id:int):
    for doctor in doctors:
        if doctor["id"]==doctor_id:
            return doctor

    raise HTTPException(status_code=404,detail="Dcotor not FOUND")   


@app.post("/patients")
def create_patient(patient:Patient):
    patient_data={
                 "id":len(patients)+1,
                 "name":patient.name,
                 "age":patient.age,
                 "phone":patient.phone
                 }    
    patients.append(patient_data)
    
    return patient_data

@app.get("/patients")
def get_patients():
    return patients
