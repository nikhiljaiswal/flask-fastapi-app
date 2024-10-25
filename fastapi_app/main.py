from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import random
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Mount the static directory for serving CSS, JS, and images
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("templates/index.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

# Endpoint to handle animal selection and return a random image
@app.get("/animal")
async def get_animal_image(name: str):
    base_path = Path(f"static/data/{name}")
    images = list(base_path.glob("*.jpg"))
    if not images:
        return JSONResponse({"error": "No images found"}, status_code=404)

    selected_image = random.choice(images)
    image_url = f"/static/data/{name}/{selected_image.name}"
    return {"image_url": image_url}

# Endpoint to handle file upload
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    # Get file details
    filename = file.filename
    content = await file.read()
    filesize = len(content)
    filetype = file.content_type

    # Log the upload event for debugging purposes
    print(f"Uploaded file: {filename}, Size: {filesize}, Type: {filetype}")

    # Format filesize (in bytes, KB, MB)
    if filesize < 1024:
        formatted_filesize = f"{filesize} bytes"
    elif filesize < 1024 * 1024:
        formatted_filesize = f"{filesize / 1024:.2f} KB"
    else:
        formatted_filesize = f"{filesize / (1024 * 1024):.2f} MB"

    return JSONResponse(
        {"filename": filename, "filesize": formatted_filesize, "filetype": filetype}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
