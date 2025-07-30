# -*- coding: utf-8 -*-
"""
Driver Drowsiness Detection System with EAR and Alarm
"""
import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from threading import Thread
import playsound
import time
import queue
import sys

# Configuration
FACE_DOWNSAMPLE_RATIO = 1.5
RESIZE_HEIGHT = 480
EAR_THRESH = 0.27
BLINK_TIME = 0.15
DROWSY_TIME = 1.5
ALARM_PATH = "alarm.wav"
MODEL_PATH = "models/shape_predictor_68_face_landmarks.dat"

# Eye landmark indices
LEFT_EYE = [36, 37, 38, 39, 40, 41]
RIGHT_EYE = [42, 43, 44, 45, 46, 47]

# Variables
blink_count = 0
drowsy = False
state = 0
ALARM_ON = False
threadStatusQ = queue.Queue()

# Load models
print("[INFO] Loading models...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(MODEL_PATH)

# Functions
def play_alarm(path, q):
    while True:
        if not q.empty():
            stop = q.get()
            if stop:
                break
        playsound.playsound(path)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def get_landmarks(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=1.0/FACE_DOWNSAMPLE_RATIO, fy=1.0/FACE_DOWNSAMPLE_RATIO)
    rects = detector(resized)
    if len(rects) == 0:
        return None
    rect = dlib.rectangle(int(rects[0].left() * FACE_DOWNSAMPLE_RATIO),
                          int(rects[0].top() * FACE_DOWNSAMPLE_RATIO),
                          int(rects[0].right() * FACE_DOWNSAMPLE_RATIO),
                          int(rects[0].bottom() * FACE_DOWNSAMPLE_RATIO))
    shape = predictor(gray, rect)
    return np.array([[p.x, p.y] for p in shape.parts()])

def detect_drowsiness(landmarks):
    global state, blink_count, drowsy
    left_eye = landmarks[LEFT_EYE]
    right_eye = landmarks[RIGHT_EYE]
    ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0

    if ear < EAR_THRESH:
        state += 1
    else:
        if 2 <= state <= drowsy_limit:
            blink_count += 1
        elif state > drowsy_limit:
            drowsy = True
        state = 0

# Initialize video stream
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Cannot open webcam.")
    sys.exit()

# Calibrate
print("[INFO] Calibrating...")
total_time = 0
frames_needed = 50
for _ in range(frames_needed):
    ret, frame = cap.read()
    if not ret:
        continue
    start = time.time()
    lm = get_landmarks(frame)
    total_time += time.time() - start

spf = total_time / frames_needed
drowsy_limit = int(DROWSY_TIME / spf)

print("[INFO] Calibration complete.")

# Main loop
if __name__ == "__main__":
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = get_landmarks(frame)
        if landmarks is None:
            cv2.putText(frame, "Face not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            cv2.imshow("Drowsiness Detector", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        detect_drowsiness(landmarks)

        for idx in LEFT_EYE + RIGHT_EYE:
            cv2.circle(frame, tuple(landmarks[idx]), 2, (0, 255, 0), -1)

        if drowsy:
            cv2.putText(frame, "DROWSINESS ALERT!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
            if not ALARM_ON:
                ALARM_ON = True
                threadStatusQ.put(False)
                Thread(target=play_alarm, args=(ALARM_PATH, threadStatusQ), daemon=True).start()
        else:
            cv2.putText(frame, f"Blinks: {blink_count}", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            ALARM_ON = False

        cv2.imshow("Drowsiness Detector", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            drowsy = False
            state = 0
            threadStatusQ.put(True)

    cap.release()
    cv2.destroyAllWindows()
