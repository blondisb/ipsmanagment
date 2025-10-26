from fastapi import APIRouter, Depends, HTTPException
from typing import List
from repositories.patient_repository import PatientRepository
from services.patient_service import PatientService
from schemas.patient_schemas import Patient, PatientCreate, PatientUpdate

router = APIRouter()

def get_patient_service() -> PatientService:
    repository = PatientRepository()
    return PatientService(repository)

@router.get("/", response_model=List[Patient])
def get_patients(
    skip: int = 0,
    limit: int = 100,
    service: PatientService = Depends(get_patient_service)
):
    return service.get_patients(skip, limit)

@router.get("/{patient_id}", response_model=Patient)
def get_patient(
    patient_id: int,
    service: PatientService = Depends(get_patient_service)
):
    return service.get_patient(patient_id)

@router.post("/", response_model=Patient)
def create_patient(
    patient: PatientCreate,
    service: PatientService = Depends(get_patient_service)
):
    return service.create_patient(patient)

@router.put("/{patient_id}", response_model=Patient)
def update_patient(
    patient_id: int,
    patient_update: PatientUpdate,
    service: PatientService = Depends(get_patient_service)
):
    return service.update_patient(patient_id, patient_update)

@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    service: PatientService = Depends(get_patient_service)
):
    return service.delete_patient(patient_id)