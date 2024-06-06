# Covert Channel Project

This repository contains three Python scripts for implementing a covert channel communication system using ICMP packets.

## covert_channel.py

This script defines two classes, `Sender` and `Receiver`, for sending and receiving covert messages respectively.

### Sender

The `Sender` class is responsible for encrypting and sending messages to a target IP address using ICMP packets.

#### Methods:
- `__init__(self, target_ip, key, interval=0.5)`: Initializes the sender with the target IP address, encryption key, and optional interval between packet transmissions.
- `encrypt_message(self)`: Encrypts the secret message using AES encryption.
- `compress_message(self)`: Compresses the encrypted message using zlib compression.
- `send_packet(self, data)`: Sends an ICMP packet containing the encrypted and compressed message.
- `send(self)`: Compresses, encrypts, and sends the secret message.
- `send_message(self, message)`: Sets the secret message and sends it.

### Receiver

The `Receiver` class listens for ICMP packets, decrypts and decompresses the received messages.

#### Methods:
- `__init__(self, key)`: Initializes the receiver with the decryption key.
- `decrypt_message(self)`: Decrypts the received message using AES decryption.
- `decompress_message(self)`: Decompresses the decrypted message.
- `process_packet(self, packet)`: Extracts the raw payload from the ICMP packet.
- `receive(self)`: Sniffs ICMP packets to receive messages.
- `receive_message(self)`: Receives, decrypts, and decompresses the message.

## simulation.py

This script demonstrates the usage of the covert channel by simulating sending and receiving messages between a sender and receiver.

## transmission_analysis.py

This script analyzes the transmission rate of the covert channel by sending multiple random messages and calculating the average transmission rate.

### Functions:
- `generate_random_string(max_length=20)`: Generates a random string of characters.
- `send_message(message)`: Sends a message using the covert channel.
- `receive_message()`: Receives a message using the covert channel.
- `compute_transmission_time()`: Computes the transmission time of a single message.
- `average_bitrate`: Calculates the average bit per second transmission rate.

## Usage

To use the covert channel:
1. Import the necessary classes and functions from `covert_channel.py`.
2. Initialize a `Sender` and `Receiver` instance with the appropriate parameters.
3. Call the necessary methods to send and receive messages.

## Dependencies

- `scapy`: Packet manipulation library.
- `cryptography`: Cryptography library.
- `zlib`: Compression library.
