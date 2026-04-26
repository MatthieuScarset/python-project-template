# MyPackage API Documentation

## Overview

MyPackage is an intelligent system that provides API endpoints to do custom things.

## Endpoints

### GET /
Health check endpoint that returns basic API information.

**Response:**
```json
{
  "message": "MyPackage API is running",
  "version": "0.1.0"
}
```

### GET /health
Detailed health check including component status.

**Response:**
```json
{
  "status": "healthy",
  "service": "MyPackage",
  "components": {
    "api": "ok",
    "pattern_extraction": "pending",
    "storage": "pending"
  }
}
```

### POST /custom-thing
Do thing specific of your package.

**CustomThingRequest:**
```json
{
  "data": "data your package wants to read"
}
```

**CustomThingResponse:**
```json
{
  "status": "success",
  "message": "Custom thing completed",
  "...": "..."
}
```

## Error Responses

- `422`: Validation error (missing or invalid fields)
- `500`: Internal server error

## Rate Limiting

Currently no rate limiting is implemented. This may be added in future versions.
