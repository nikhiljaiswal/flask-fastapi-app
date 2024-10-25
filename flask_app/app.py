import os
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define paths for images
ANIMAL_PATHS = {
    "cat": "static/data/cat",
    "dog": "static/data/dog",
    "elephant": "static/data/elephant",
}


@app.route("/")
def index():
    return render_template("index.html")


# Endpoint to return a random animal image
@app.route("/animal/<animal>", methods=["GET"])
def get_animal_image(animal):
    if animal in ANIMAL_PATHS:
        animal_dir = ANIMAL_PATHS[animal]
        images = os.listdir(animal_dir)
        selected_image = random.choice(images)
        return jsonify({"image_url": f"/{animal_dir}/{selected_image}"})
    else:
        return jsonify({"error": "Animal not found"}), 404


# Endpoint to handle file uploads
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Get file details
    filename = file.filename
    filesize = len(file.read())
    file.seek(0)
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

    return jsonify(
        {"filename": filename, "filesize": formatted_filesize, "filetype": filetype}
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
