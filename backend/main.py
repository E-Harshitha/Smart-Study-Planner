from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/study-plan")
def get_study_plan():
    return {
        "plan": [
            {"subject": "Math", "duration": "2 hours"},
            {"subject": "Physics", "duration": "1.5 hours"},
            {"subject": "Break", "duration": "30 minutes"},
        ]
    }