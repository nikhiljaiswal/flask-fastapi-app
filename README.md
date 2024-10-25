# 🐾 Animal Image Selector and File Upload App

This is a simple web application that allows users to either select an animal (cat, dog, or elephant) and view a random image of that animal or upload a file and see the file details. The frontend is built using **HTML/CSS/JavaScript**, and you can choose between **Flask** or **FastAPI** for the backend.

## 🚀 Features

1. **Select Animal**  
   Choose between a cat, dog, or elephant, and the application will show a random image of the selected animal from 5 pre-stored images.
   
2. **File Upload**  
   Upload any file and the app will display its name, size, and type.




### File Structure:

```bash
├── flask_app/          # Contains Flask implementation
├── fastapi_app/        # Contains FastAPI implementation
├── requirements.txt    # Python package dependencies
└── README.md           # Documentation file
```

### Installation and Running the Application

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/nikhiljaiswal/flask-fastapi-app.git
   cd flask-fastapi-app
   
2. **Install required dependencies:**
   ```bash
    pip install -r requirements.txt

3. **Run the backend:**

   - **For Flask**:
     ```bash
     cd flask_app
     python app.py --port 5000
     ```

   - **For FastAPI**:
     ```bash
     cd fastapi_app
     uvicorn main:app --reload --host 127.0.0.1 --port 8000
     ```

4. **Access the Application**:  
   Open your browser and go to `http://localhost:5000` (Flask) or `http://localhost:8000` (FastAPI)

## 📂 Frontend Overview

The frontend is divided into two main sections:

1. **Animal Selection Section**  
   Users can choose one of the following animals: **cat**, **dog**, or **elephant** via checkboxes. After an animal is selected, the frontend will fetch a random image of that animal from the backend and display it.

2. **File Upload Section**  
   Users can upload a file in this section. Once uploaded, the frontend communicates with the backend to retrieve and display the file's **name**, **size**, and **type**.



## 🎥 Demo


[![Watch the demo](https://img.youtube.com/vi/Xj4qWDvp4pw/0.jpg)](https://www.youtube.com/watch?v=Xj4qWDvp4pw)
