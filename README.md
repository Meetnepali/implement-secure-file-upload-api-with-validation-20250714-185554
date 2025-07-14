# Guidance for Task: Secure Image Upload API with FastAPI

## Project Overview
This project provides a starting point for a campaign asset management API. Your task is to implement a robust, modular, and secure image upload endpoint using FastAPI. The endpoint should support asynchronous file uploads, validate and restrict file types and size, extract image metadata, persist both the file and control metadata to storage and a database, and log every event in a structured way.

## What You Should Implement
- An async image upload API endpoint (within a FastAPI router) that:
  - Accepts only JPEG and PNG images.
  - Enforces a maximum file size (e.g., 2 MB).
  - Validates file type/size with appropriate error handling and messaging.
  - Stores uploaded files asynchronously to a secure location (local `uploaded_images/` directory).
  - Extracts image metadata (width, height, format) using Pillow or a similar library.
  - Saves both file info and metadata to the provided SQLite database via dependency-injected SQLAlchemy session.
  - Returns user-friendly, validated Pydantic response schemas for both success and error scenarios.
  - Uses structured logging (see example in `main.py`) for each upload event, including file info, metadata, and errors.
  - Handles and reports different error types (unsupported format, oversized file, file save/database error) consistently with clear feedback.

- Organize your implementation by:
  - Using FastAPI routers for modular organization (see `api/upload_router.py`).
  - Employing Pydantic models for request and response validation (see `schemas.py`).
  - Utilizing dependency injection for database session management (see `db.py`).
  - Applying best security practices for file uploads (no unsafe filenames or paths, etc).

## Verifying Your Solution
- Ensure the endpoint correctly rejects non-image files and images over the max size with clear error messages.
- Check that images that pass validation are stored and their info appears in the database.
- Confirm that structured logs appear for each upload, success, or error.
- The codebase must be modular, maintainable, and easy to test. All responses must use Pydantic models.
- All necessary cases (valid/invalid file type, oversized file, file I/O/db errors) should be handled precisely. Testing these scenarios should be straightforward with tools like cURL or HTTP clients.

## Project Structure
- `main.py`: FastAPI app setup and router inclusion.
- `api/upload_router.py`: **You will complete/implement the main upload logic here!**
- `schemas.py`: Pydantic data models for requests and responses.
- `db.py`: Database setup and dependency logic.
- `models.py`: SQLAlchemy database models.
- `uploaded_images/`: Directory for persisting uploaded images (should exist after upload!).

Remember: You should focus on correctness, security, organization, and maintainability in your implementation.