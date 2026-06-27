from fastapi import FastAPI
from config.database import engine, Base
from routes import auth, user

# Initialize Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include Routers
app.include_router(auth.router, tags=["Authentication"])
app.include_router(user.router, tags=["Users"])
