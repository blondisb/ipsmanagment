from typing import List, Optional
from fastapi import HTTPException
from repositories.patient_repository import PatientRepository
from schemas.patient_schemas import PatientCreate, PatientUpdate, Patient

class PatientService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository
    
    def get_patient(self, patient_id: int) -> Patient:
        patient_data = self.repository.get_patient(patient_id)
        if not patient_data:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return Patient(**patient_data)
    
    def get_patients(self, skip: int = 0, limit: int = 100) -> List[Patient]:
        patients_data = self.repository.get_patients(skip, limit)
        return [Patient(**patient) for patient in patients_data]
    
    def create_patient(self, patient: PatientCreate) -> Patient:
        # Verificar si el email ya existe
        existing_patient = self.repository.get_patient_by_email(patient.email)
        if existing_patient:
            raise HTTPException(status_code=400, detail="El email ya está registrado")
        
        created_patient = self.repository.create_patient(patient)
        if not created_patient:
            raise HTTPException(status_code=500, detail="Error al crear el paciente")
        
        return Patient(**created_patient)
    
    def update_patient(self, patient_id: int, patient_update: PatientUpdate) -> Patient:
        updated_patient = self.repository.update_patient(patient_id, patient_update)
        if not updated_patient:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return Patient(**updated_patient)
    
    def delete_patient(self, patient_id: int) -> dict:
        success = self.repository.delete_patient(patient_id)
        if not success:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return {"message": "Paciente eliminado correctamente"}