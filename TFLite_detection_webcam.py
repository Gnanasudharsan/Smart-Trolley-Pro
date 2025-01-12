# Import required libraries
import os
import argparse
import cv2
import numpy as np
import time
from threading import Thread
import importlib.util
import serial
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins
ena, in1, in2 = 16, 7, 1
enb, in3, in4 = 14, 15, 18

# Motor pin configuration
GPIO.setup([ena, in1, in2, enb, in3, in4], GPIO.OUT)

# PWM initialization
pwm_left = GPIO.PWM(ena, 1000)
pwm_right = GPIO.PWM(enb, 1000)
pwm_left.start(0)
pwm_right.start(0)

# Polynomial coefficients for distance calculation
X = [680, 390, 300, 232, 160, 116, 91, 80, 74, 63]
Y = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
coefficients = np.polyfit(X, Y, 2)

# Helper class for video streaming
class VideoStream:
    """Handles video stream from the camera."""
    def __init__(self, resolution=(640, 480), framerate=24):
        self.stream = cv2.VideoCapture(0)
        self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.stream.set(3, resolution[0])
        self.stream.set(4, resolution[1])
        self.grabbed, self.frame = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while not self.stopped:
            self.grabbed, self.frame = self.stream.read()
        self.stream.release()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

# Define motor control functions
def move_forward():
    pwm_left.ChangeDutyCycle(100)
    pwm_right.ChangeDutyCycle(100)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

def turn_right():
    pwm_left.ChangeDutyCycle(70)
    pwm_right.ChangeDutyCycle(60)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def turn_left():
    pwm_left.ChangeDutyCycle(60)
    pwm_right.ChangeDutyCycle(70)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

def halt():
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)
    GPIO.output([in1, in2, in3, in4], GPIO.LOW)

# Command-line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--modeldir', required=True, help='Directory containing TFLite model files')
parser.add_argument('--graph', default='detect.tflite', help='Name of the .tflite file')
parser.add_argument('--labels', default='labelmap.txt', help='Name of the label map file')
parser.add_argument('--threshold', type=float, default=0.5, help='Confidence threshold for detection')
parser.add_argument('--resolution', default='1280x720', help='Camera resolution WxH')
parser.add_argument('--edgetpu', action='store_true', help='Use Coral Edge TPU')
args = parser.parse_args()

# Load model details
model_dir = args.modeldir
graph_file = args.graph
label_file = args.labels
confidence_threshold = args.threshold
width, height = map(int, args.resolution.split('x'))

# Initialize TensorFlow Lite model
model_path = os.path.join(model_dir, graph_file)
interpreter = importlib.util.find_spec('tflite_runtime') and \
    importlib.util.find_spec('tflite_runtime.interpreter') or \
    importlib.util.find_spec('tensorflow.lite.Interpreter')

interpreter = interpreter.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_height = input_details[0]['shape'][1]
input_width = input_details[0]['shape'][2]

# Main program loop
video_stream = VideoStream(resolution=(width, height)).start()
time.sleep(2)

try:
    while True:
        frame = video_stream.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (input_width, input_height))
        input_data = np.expand_dims(frame_resized, axis=0)

        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        boxes = interpreter.get_tensor(output_details[0]['index'])[0]
        classes = interpreter.get_tensor(output_details[1]['index'])[0]
        scores = interpreter.get_tensor(output_details[2]['index'])[0]

        for i in range(len(scores)):
            if confidence_threshold < scores[i] <= 1.0:
                # Process bounding box
                ymin, xmin, ymax, xmax = boxes[i]
                label = f"Object {int(classes[i])}: {int(scores[i] * 100)}%"
                print(label)
                # Add custom movement logic here

        cv2.imshow('Smart Trolley View', frame)
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    video_stream.stop()
    cv2.destroyAllWindows()
    GPIO.cleanup()
