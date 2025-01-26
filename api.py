from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

# Load the data from the JSON file
with open("data.json") as f:
    students_data = json.load(f)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    marks = []
    for student_name in name:
        student = next((s for s in students_data if s["name"] == student_name), None)
        marks.append(student["marks"] if student else None)
    return JSONResponse(content={"marks": marks})
