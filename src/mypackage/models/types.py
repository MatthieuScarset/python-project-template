"""Data models for MyPackage API."""

from pydantic import BaseModel, Field


class CustomThingRequest(BaseModel):
    """Request model for custom-thing."""

    data: str = Field(
        ...,
        description="The data our API wants to read",
        max_length=10000,
    )


class CustomThingResponse(BaseModel):
    """Response model for custom-thing results."""

    status: str
    message: str
    data: dict = Field({}, description="Results from custom-thing")
