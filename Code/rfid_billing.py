import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# RFID setup
reader = SimpleMFRC522()

# Product database
products = {
    "1234567890": {"name": "Milk", "price": 50},
    "0987654321": {"name": "Bread", "price": 30},
    "1122334455": {"name": "Eggs", "price": 60}
}

# Billing
def read_rfid():
    try:
        print("Place your RFID tag...")
        id, text = reader.read()
        return str(id).strip()
    except Exception as e:
        print(f"Error reading RFID: {e}")
        return None

def main():
    total = 0
    while True:
        rfid = read_rfid()
        if rfid in products:
            product = products[rfid]
            total += product["price"]
            print(f"Added: {product['name']} - ₹{product['price']}")
            print(f"Total: ₹{total}")
        else:
            print("Unknown product. Try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()
