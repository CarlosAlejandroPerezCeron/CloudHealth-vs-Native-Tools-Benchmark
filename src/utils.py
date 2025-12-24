import os
from dotenv import load_dotenv

load_dotenv()

def log(msg):
    print(f"[INFO] {msg}")

def get_env(var):
    value = os.getenv(var)
    if not value:
        raise ValueError(f"Missing env var: {var}")
    return value
