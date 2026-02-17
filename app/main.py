from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import health route
from app.api.routes import health

app = FastAPI(
    title="Nimora Chatbot API",
    version="1.0.0"
)

# CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register only health router
app.include_router(health.router, prefix="/health", tags=["Health"])

@app.get("/")
async def root():
    return {"message": "Nimora Chatbot running"}