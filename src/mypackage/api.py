from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from mypackage.models import CustomThingRequest, CustomThingResponse
from mypackage.core import CustomThing

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Lifespan context manager for startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("MyPackage FastAPI app starting up...")
    # TODO: Initialize connections, load models, embeddings, etc.

    yield

    # Shutdown
    logger.info("MyPackage FastAPI app shutting down...")


# Create FastAPI app
app = FastAPI(
    title="MyPackage API",
    description="MyPackage: Python project template",
    version="0.1.0",
    lifespan=lifespan,
)


# Routes
@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "MyPackage API", "version": "0.1.0"}


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "MyPackage",
        "components": {
            "api": "ok",
            "storage": "pending",  # TODO: check connection to storage
            "database": "pending",  # TODO: check connection to database
            "model": "pending",  # TODO: check if model is loaded
            "embeddings": "pending",  # TODO: check if embeddings are loaded
        },
    }


@app.post("/custom-thing", response_model=CustomThingResponse)
async def custom_thing(request: CustomThingRequest):
    """
    Do a custom thing
    """
    logger.info(f"Doing a custom thing: {len(request.data)}")

    # TODO: Implement custom-thing logic
    # - Do something
    # - Do something else
    # - ...
    # - Return results

    # Placeholder
    custom_thing_instance = CustomThing()
    analysis = custom_thing_instance.custom_thing(request.data)
    results = {"analysis": analysis}

    return CustomThingResponse(
        status="success",
        message="custom-thing completed",
        data=results,
    )


# For running with uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
