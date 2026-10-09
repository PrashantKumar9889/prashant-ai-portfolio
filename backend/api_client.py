
import os
import requests

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000",
).rstrip("/")


def get_projects():
    response = requests.get(
        f"{API_BASE_URL}/api/projects",
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def get_skills():
    response = requests.get(
        f"{API_BASE_URL}/api/skills",
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def get_profile():
    response = requests.get(
        f"{API_BASE_URL}/api/profile",
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def send_chat_message(question: str) -> str:
    response = requests.post(
        f"{API_BASE_URL}/api/chat",
        json={"question": question},
        timeout=90,
    )
    response.raise_for_status()
    return response.json()["answer"]