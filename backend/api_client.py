import requests


API_BASE_URL = "https://prashant-ai-portfolio.onrender.com/api"


def get_projects():
    response = requests.get(
        f"{API_BASE_URL}/projects",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_skills():
    response = requests.get(
        f"{API_BASE_URL}/skills",
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def get_profile():

    response = requests.get(
        f"{API_BASE_URL}/profile",
        timeout=10
    )

    response.raise_for_status()

    return response.json()