from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run-pipeline")
def run_pipeline():

    result = subprocess.run(
        ["venv/Scripts/python.exe", "scripts/run_pipeline.py"],
        capture_output=True,
        text=True
    )

    return {
        "status": "pipeline executed",
        "stdout": result.stdout,
        "stderr": result.stderr,
        "return_code": result.returncode
    }