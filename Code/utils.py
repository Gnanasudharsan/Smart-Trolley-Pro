import cv2
import numpy as np

def preprocess_frame(frame, input_height, input_width):
    """
    Prepares the frame for TensorFlow Lite model inference.
    """
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (input_width, input_height))
    return np.expand_dims(frame_resized, axis=0)

def draw_detection(frame, box, label, score, color=(10, 255, 0)):
    """
    Draws the detection box and label on the frame.
    """
    ymin, xmin, ymax, xmax = box
    ymin, xmin, ymax, xmax = int(ymin), int(xmin), int(ymax), int(xmax)

    # Draw rectangle
    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
    
    # Display label and score
    label_text = f"{label}: {int(score * 100)}%"
    cv2.putText(frame, label_text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return frame
