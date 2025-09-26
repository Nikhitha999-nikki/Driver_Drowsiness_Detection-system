##Driver Drowsiness Detection Key Features
->Real-time monitoring of driver's eyes using a camera
->Fatigue and drowsiness detection algorithm
->Timely alerts to prevent the driver from falling asleep
->Non-intrusive and easy to set up
->Progressive Web App (PWA) support - Install like a native app!
->Offline functionality with caching
->Fast loading with optimized performance on System


##Project Overview
The Driver Drowsiness Detection System is a non-intrusive solution designed to monitor and detect signs of fatigue in drivers. By analyzing eye states through a camera feed, the system can identify early symptoms of drowsiness and issue timely warnings, helping to prevent accidents caused by driver fatigue. This project aims to enhance road safety, especially for those driving long distances who may not recognize their own drowsiness in time.


##Technologies Used
Python
OpenCV
Dlib or Mediapipe (for facial landmark detection)
NumPy, Pandas



## Setup Instructions


##Clone the repository:

git clone https://github.com/Gagandeep-2003/Driver-Drowsiness-Detection-System.git
cd Driver-Drowsiness-Detection-System


##Install dependencies:

pip install -r requirements.txt


##Download the model:


This project requires the **shape_predictor_68_face_landmarks.dat** file for facial landmark detection.  
You can download it form this link also..

➡️ Download it from the official dlib model repository:  
- [Download shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)  
- Extract it to the project directory after downloading.



##Run the application:

python main.py


##Usage
Ensure your webcam is connected.
Run the application as shown above.
The system will start monitoring your eyes and alert you if signs of drowsiness are detected.

