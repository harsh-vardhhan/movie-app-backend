import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.seed import seed_data
from app.database import SessionLocal
from app import models
import os

client = TestClient(app)

# Ensure data exists
@pytest.fixture(scope="module", autouse=True)
def setup_data():
    seed_data()

def get_valid_id(model):
    db = SessionLocal()
    try:
        item = db.query(model).first()
        return item.id if item else 1
    finally:
        db.close()

def test_generate_api_docs():
    routes = []
    
    # Get valid IDs for dynamic routes
    movie_id = get_valid_id(models.Movie)
    actor_id = get_valid_id(models.Actor)
    director_id = get_valid_id(models.Director)

    for route in app.routes:
        if getattr(route, "path", "").startswith("/openapi") or getattr(route, "path", "").startswith("/docs") or getattr(route, "path", "").startswith("/redoc"):
            continue
            
        path = getattr(route, "path", "")
        if not path:
            continue
            
        method = list(route.methods)[0] if route.methods else "GET"
        
        # Replace path parameters with valid IDs
        test_path = path.replace("{movie_id}", str(movie_id))\
                        .replace("{actor_id}", str(actor_id))\
                        .replace("{director_id}", str(director_id))

        response = client.request(method, test_path)
        
        status = response.status_code
        try:
            response_json = response.json()
            # Truncate long responses for readability
            response_str = str(response_json)
            if len(response_str) > 200:
                response_str = response_str[:200] + "... (truncated)"
        except:
            response_str = "Non-JSON Response"

        routes.append({
            "Method": method,
            "Path": path,
            "Status": status,
            "Response": response_str
        })

    # Sort routes by path
    routes.sort(key=lambda x: x["Path"])

    # Generate Markdown Table
    table = "| Method | Path | Status | Response |\n"
    table += "|---|---|---|---|\n"
    
    for route in routes:
        # Escape pipe characters in response string to avoid breaking table
        clean_response = route["Response"].replace("|", "\\|").replace("\n", " ")
        table += f"| {route['Method']} | {route['Path']} | {route['Status']} | `<pre>{clean_response}</pre>` |\n"

    # Update README.md
    readme_path = "README.md"
    start_marker = "<!-- API_DOCS_START -->"
    end_marker = "<!-- API_DOCS_END -->"
    
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()
    else:
        content = ""

    new_section = f"{start_marker}\n## API Documentation\n\n{table}\n{end_marker}"

    if start_marker in content and end_marker in content:
        # Replace existing section
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = before + new_section + after
    else:
        # Append if not found (or if file is empty)
        new_content = content + "\n\n" + new_section

    with open(readme_path, "w") as f:
        f.write(new_content.strip())
