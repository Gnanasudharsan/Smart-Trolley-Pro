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


Install dependencies:

pip install -r requirements.txt


Place TensorFlow Lite models in the models/ directory.

Run the System:
Start the main script:

python TFLite_detection_webcam.py


Ensure the RFID module and Wi-Fi hotspot are configured.

📊 Results
	•	Real-time Tracking: The trolley reliably follows customers within a defined RSSI range.
	•	Instant Billing: RFID tags are read seamlessly, and the total is displayed via GUI.
	•	Load Capacity: Handles up to 10 kg loads in its current configuration.

🔮 Future Enhancements
	•	Integrating an in-built payment system.
	•	Improved tracking accuracy in crowded spaces.
	•	Enhancing battery life for extended usage.
