from covert_channel import Sender, Receiver
import threading

# Define the target IP address, secret message, and encryption key
destination_ip = '8.8.8.8'
secret_message = b'this is a secret message to prof Razian'
key = b'ThisIsA16ByteKey'

# Initialize Sender and Receiver instances
sender = Sender(destination_ip, key)
receiver = Receiver(key)


# Define functions to send and receive messages
def send_message():
    sender.send_message(secret_message)


def receive_message():
    receiver.receive_message()


c
# Create sender and receiver threads
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

# Start sender and receiver threads
send_thread.start()
receive_thread.start()

# Wait for the threads to finish
send_thread.join()
receive_thread.join()

# Print the received secret message
print('Received message:', receiver.secret_message)
print(len(secret_message)/)