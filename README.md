Smart Trolley with RSSI-Based Navigation and RFID Billing System

📜 Project Description

This project presents an innovative Smart Trolley designed to revolutionize shopping by reducing physical effort and streamlining the billing process. The trolley autonomously follows customers using Wi-Fi RSSI tracking and OpenCV-based person detection, while an RFID system handles real-time billing. The system is powered by Raspberry Pi and integrates sensors for collision avoidance, ensuring a smooth shopping experience.

🚀 Features
	•	Autonomous Navigation: Follows customers using Wi-Fi RSSI and a camera module.
	•	Real-Time Person Detection: Tracks customers with OpenCV and TensorFlow Lite.
	•	Instant Billing: RFID system calculates and displays the total cost of items.
	•	Collision Avoidance: Integrated sensors prevent obstacles and ensure smooth navigation.
	•	Efficient Power Usage: Designed for optimal battery performance with a 12V rechargeable battery.

🛠️ Components

Hardware
	•	Raspberry Pi 4: Main processing unit.
	•	NodeMCU ESP8266: Wi-Fi module for RSSI tracking.
	•	Raspberry Pi Camera Module: Real-time person detection.
	•	L298N Motor Driver: Controls DC motors for trolley movement.
	•	200 RPM DC Motors: Ensures smooth and agile movement.
	•	RFID Module (MFRC522): Reads RFID tags for item billing.
	•	12V 1.3Ah SMF Battery: Powers the trolley and components.

Software
	•	Python 3.x
	•	OpenCV
	•	TensorFlow Lite
	•	Tkinter for GUI
	•	Numpy

⚙️ Setup Instructions
	1.	Hardware Setup:
	•	Assemble the Raspberry Pi, motors, camera, RFID module, and NodeMCU.
	•	Connect components as per the circuit diagram.
	2.	Software Setup:
	•	Clone this repository:

git clone https://github.com/Gnanasudharsan/Smart-Trolley-Pro


Here’s the single markdown text:

## 🛠️ Installation and Setup

1. **Install Dependencies**  
   Run the following command to install the required Python libraries:
   ```bash
   pip install -r requirements.txt

2. Place TensorFlow Lite Models
Ensure you place the TensorFlow Lite model files in the models/ directory:
	```bash
	detect.tflite
 
4. Run the System
Start the main script by running:
   ```bash
   python TFLite_detection_webcam.py

This is ready to be added to your GitHub README. It ensures all steps are clear and allows users to easily copy commands.

Ensure the RFID module and Wi-Fi hotspot are configured.

## 📥 Download TensorFlow Lite Model

The `detect.tflite` model used in this project is based on the SSD MobileNet V1 model. You can download it from Kaggle using the following steps:

1. Visit the [Kaggle SSD MobileNet V1 Model](https://www.kaggle.com/models/tensorflow/ssd-mobilenet-v1) page.
2. Sign in to your Kaggle account (or create one if you don’t have one).
3. Click on **Download** to get the model files.
4. Extract the downloaded files and locate the `detect.tflite`.
5. Place the `detect.tflite` file in the `models/` folder of this repository.

Alternatively, use the Kaggle API to download the dataset programmatically:
```bash
kaggle datasets download -d tensorflow/ssd-mobilenet-v1

📊 Results
	•	Real-time Tracking: The trolley reliably follows customers within a defined RSSI range.
	•	Instant Billing: RFID tags are read seamlessly, and the total is displayed via GUI.
	•	Load Capacity: Handles up to 10 kg loads in its current configuration.

🔮 Future Enhancements
	•	Integrating an in-built payment system.
	•	Improved tracking accuracy in crowded spaces.
	•	Enhancing battery life for extended usage.
