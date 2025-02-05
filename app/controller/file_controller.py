from fastapi import APIRouter, HTTPException
from app.service.minio_service import upload_file, download_file
from app.service.csv_service import read_csv
from app.service.db_service import save_to_db

router = APIRouter()


@router.post("/upload/")
def upload_to__minio(bucket_name: str, file_path: str, object_name: str):
    try:
        upload_file(bucket_name, file_path, object_name)
        return {"message": f"Arquivo {object_name} subido para o bucket {bucket_name}."}
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/download/")
def download_from_minio(bucket_name: str, file_path: str, object_name: str):
    try:
        download_file(bucket_name, file_path, object_name)
        return {"message": f"Arquivo {object_name} baixado para {file_path}."}
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/process/")
def process_csv(bucket_name, object_name, download_path):
    try:
        download_file(bucket_name, object_name, download_path)
        df = read_csv(download_path)
        save_to_db(df)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
