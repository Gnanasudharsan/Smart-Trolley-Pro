## 🛠️ Wiring Instructions

This section provides the detailed wiring connections for the Smart Trolley system.

### **1. Raspberry Pi GPIO Connections**
- **Motor Driver (L298N)**:
  - **ENA (Enable A)** → GPIO 16 (Pin 36)
  - **IN1** → GPIO 7 (Pin 26)
  - **IN2** → GPIO 1 (Pin 28)
  - **ENB (Enable B)** → GPIO 14 (Pin 8)
  - **IN3** → GPIO 15 (Pin 10)
  - **IN4** → GPIO 18 (Pin 12)

- **Camera Module**:
  - Connect to the dedicated **Camera Interface** (CSI slot) on the Raspberry Pi.

- **RFID Module (MFRC522)**:
  - **SCK** → GPIO 11 (Pin 23, SPI CLK)
  - **MOSI** → GPIO 10 (Pin 19, SPI MOSI)
  - **MISO** → GPIO 9 (Pin 21, SPI MISO)
  - **SS** → GPIO 8 (Pin 24, SPI CE0)
  - **RST** → GPIO 25 (Pin 22)
  - **GND** → GND (Pin 6)
  - **VCC** → 3.3V (Pin 1)

- **NodeMCU ESP8266** (for RSSI tracking):
  - **TX (NodeMCU)** → GPIO 15 (Pin 10, RXD of Raspberry Pi)
  - **RX (NodeMCU)** → GPIO 14 (Pin 8, TXD of Raspberry Pi)
  - **GND** → GND (Pin 6)
  - **VCC** → 5V (Pin 4)

---

### **2. Power Supply**
- **12V Battery**:
  - **+12V** → L298N motor driver VIN input.
  - **GND** → L298N motor driver GND.

- **Powering Raspberry Pi**:
  - Use a 5V regulator (if needed) from the motor driver’s 5V output to power the Raspberry Pi via its 5V pin.

---

### **3. DC Motors (Connected to L298N)**
- **Left Motor**:
  - **Motor A terminals** → Connected to OUT1 and OUT2 on the L298N.
- **Right Motor**:
  - **Motor B terminals** → Connected to OUT3 and OUT4 on the L298N.

---

### **Pinout Legend**
| **Component**         | **Pin**       | **Connection**                     |
|------------------------|---------------|-------------------------------------|
| **Motor Driver (ENA)** | GPIO 16       | Pin 36                              |
| **Motor Driver (IN1)** | GPIO 7        | Pin 26                              |
| **Motor Driver (IN2)** | GPIO 1        | Pin 28                              |
| **Motor Driver (ENB)** | GPIO 14       | Pin 8                               |
| **Motor Driver (IN3)** | GPIO 15       | Pin 10                              |
| **Motor Driver (IN4)** | GPIO 18       | Pin 12                              |
| **RFID RST**           | GPIO 25       | Pin 22                              |
| **RFID SS**            | GPIO 8        | Pin 24                              |
| **RFID SCK**           | GPIO 11       | Pin 23                              |
| **RFID MOSI**          | GPIO 10       | Pin 19                              |
| **RFID MISO**          | GPIO 9        | Pin 21                              |
| **NodeMCU TX**         | GPIO 15       | Pin 10 (Raspberry Pi RXD)           |
| **NodeMCU RX**         | GPIO 14       | Pin 8 (Raspberry Pi TXD)            |

---

### **Steps to Visualize in Fritzing**
1. Open Fritzing and add the following components:
   - Raspberry Pi 4.
   - L298N Motor Driver.
   - DC Motors.
   - RFID Module (MFRC522).
   - NodeMCU ESP8266.
   - Breadboard (if needed).
   - 12V battery.

2. Connect the pins based on the instructions above.

3. Add labels to each connection for clarity.

4. Export the layout as an image (`.png`) for use in documentation.

---
