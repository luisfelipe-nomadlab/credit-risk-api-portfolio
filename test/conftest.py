import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

# Adiciona a raiz do projeto ao sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.main import app

@pytest.fixture
def client():
    return TestClient(app)
