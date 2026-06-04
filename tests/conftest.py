import sys
import os
import pytest

# Ensure project root is on sys.path so top-level modules (like app.py) import correctly
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print("[conftest] CWD:", os.getcwd())
print("[conftest] inserted project_root:", project_root)
print("[conftest] sys.path:")
for p in sys.path:
    print("[conftest]  ", p)


@pytest.fixture
def client():
    # Import here after we've adjusted sys.path
    from app import app as flask_app
    return flask_app.test_client()
