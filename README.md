# TeslaCANInterpreter

This Python script is designed to read and interpret CAN messages from Tesla and other vehicles, providing insights into various vehicle parameters like charge level, climate control status, and more.

## Prerequisites
Before running this script, ensure you have the following prerequisites met:

1. **Python Environment**: Python 3.6 or newer installed on your system.
2. **python-can Library**: The `python-can` library is required for interfacing with the CAN network. Install it using pip:

    ```
    pip install python-can
    ```

3. **CAN Interface Hardware**: A compatible CAN interface device connected to your computer and vehicle. This script assumes a SocketCAN-compatible interface on Linux systems (e.g., `can0`).

4. **Proper Configuration**: The CAN interface should be correctly configured and up on your system. For SocketCAN, you might need to set up the interface with commands like:

    ```
    sudo ip link set can0 up type can bitrate 500000
    ```

    Adjust `can0` and `500000` as necessary for your setup.

5. **Permissions**: Ensure you have the necessary permissions to access the CAN interface, which may require running the script with `sudo` or adjusting user permissions.

## Installation

Clone this repository or download the script to your local machine. Ensure all prerequisites are met.

## Usage

Run the script from the command line, specifying the CAN interface and optionally the channel type. For example:

```
sudo python main.py --interface can0 --channel_type socketcan
```

## Warnings and Disclaimers

- **Warranty Voidance**: Interacting with your vehicle's CAN network can potentially void its warranty. Always check your vehicle's warranty terms and conditions before proceeding.

- **Potential for Damage**: Improper use of this script or errors in the CAN message interpretation can lead to unintended vehicle behavior. Use this script with caution and entirely at your own risk.

- **Legal Considerations**: Ensure you are compliant with local laws and regulations when interfacing with your vehicle's CAN network.

- **Testing Environment**: It is highly recommended to test the script in a safe and controlled environment before using it in practical scenarios.

By using this script, you acknowledge and accept the risks involved, including but not limited to vehicle damage, data loss, and warranty voidance.

## Contributing

Contributions to improve the script or extend its capabilities are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.
