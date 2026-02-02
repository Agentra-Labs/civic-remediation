from fastapi import FastAPI
from pydantic import BaseModel
from app.main import run_pipeline

app = FastAPI(title="Civic Remediation System API")

class Query(BaseModel):
    query: str

@app.post("/run")
def run(query: Query):
    """
    Run the full Civic Remediation Pipeline.
    """
    result = run_pipeline(query.query)
    return {"result": result}

if __name__ == "__main__":
    print("Starting server... Open http://localhost:8000/docs to play with the agent.")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
