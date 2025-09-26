# Driver Drowsiness Detection System

## Key Features
- Real-time monitoring of driver's eyes using a camera  
- Fatigue and drowsiness detection algorithm  
- Timely alerts to prevent the driver from falling asleep  
- Non-intrusive and easy to set up  
- Progressive Web App (PWA) support – install like a native app  
- Offline functionality with caching  
- Fast loading with optimized system performance  

## Project Overview
The Driver Drowsiness Detection System is a non-intrusive solution designed to monitor and detect signs of fatigue in drivers. By analyzing eye states through a camera feed, the system identifies early symptoms of drowsiness and issues timely warnings, helping to prevent accidents caused by driver fatigue. This project enhances road safety, particularly for long-distance drivers who may not recognize their own drowsiness in time.

## Technologies Used
- Python  
- OpenCV  
- Dlib or Mediapipe (for facial landmark detection)  
- NumPy, Pandas  

## Setup Instructions

### 1. Clone the repository


git clone https://github.com/Gagandeep-2003/Driver-Drowsiness-Detection-System.git
cd Driver-Drowsiness-Detection-System

### 2. Install Dependencies



pip install -r requirements.txt


### 3. Download the model

This project requires the shape_predictor_68_face_landmarks.dat file for facial landmark detection. You can download it from the official dlib model repository:

Download shape_predictor_68_face_landmarks.dat.bz2

Extract it to the project directory after downloading.


### 4. Run the application


python main.py


### Usage

Ensure your webcam is connected.

Run the application as described above.

The system will monitor your eyes and alert you if signs of drowsiness are detected.

