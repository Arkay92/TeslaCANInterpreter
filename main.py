import can
import logging
import argparse
from datetime import datetime

# Configure logging
logging.basicConfig(filename='tesla_can.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def setup_can_interface(interface, channel_type):
    """Set up the CAN interface."""
    try:
        bus = can.interface.Bus(interface, bustype=channel_type)
        logging.info("CAN interface initialized successfully")
        return bus
    except Exception as e:
        logging.error(f"Error initializing CAN interface: {e}")
        return None

def read_and_interpret_can_messages(bus):
    """Read CAN messages and print interpreted output."""
    try:
        while True:
            message = bus.recv()
            if message is not None:
                can_id = message.arbitration_id
                data = message.data
                timestamp = datetime.fromtimestamp(message.timestamp).strftime('%Y-%m-%d %H:%M:%S')

                if len(data) >= 1:
                    interpreted_data = interpret_can_message(can_id, data)
                    output = f"Time: {timestamp}, CAN ID: {hex(can_id)}, Data: {data.hex()}, Interpreted: {interpreted_data}"
                    print(output)
                    logging.info(output)
                else:
                    logging.warning(f"Received incomplete message with ID {hex(can_id)}")

    except KeyboardInterrupt:
        logging.info("Stopped reading CAN messages by user request")
    except Exception as e:
        logging.error(f"An error occurred while reading CAN messages: {e}")

def interpret_can_message(can_id, data):
    """Interpret the CAN message based on its ID and data, specifically for Tesla vehicles."""
    try:
        if can_id == 0x10C and len(data) >= 1:
            status = "On" if data[0] in [0x89, 0x88] else "Off"
            return f"Headlights: {status}"

        elif can_id == 0x2C8 and len(data) >= 1:
            charge_level = data[0]
            return f"Charge Level: {charge_level}%"

        elif can_id == 0x398 and len(data) >= 1:
            country_code = data.decode('utf-8', errors='ignore')
            return f"Country Code: {country_code}"

        elif can_id == 0x268 and len(data) >= 7:
            climate_status = "On" if data[0] == 0x55 else "Off"
            set_temperature = data[6]
            return f"Climate Control: {climate_status}, Set Temperature: {set_temperature}°C"

        else:
            return "Unknown Message"
    except Exception as e:
        return f"Error interpreting message: {e}"

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Tesla CAN Message Interpreter')
    parser.add_argument('--interface', type=str, required=True, help='CAN interface (e.g., can0)')
    parser.add_argument('--channel_type', type=str, default='socketcan', help='Channel type (default: socketcan)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    can_bus = setup_can_interface(interface=args.interface, channel_type=args.channel_type)
    if can_bus:
        read_and_interpret_can_messages(can_bus)
