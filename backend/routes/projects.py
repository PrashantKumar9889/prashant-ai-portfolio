import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter()


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "projects.json"


@router.get("/projects")
def get_projects():

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data