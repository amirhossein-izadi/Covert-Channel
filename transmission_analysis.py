from covert_channel import Sender, Receiver
import time
import threading
import random
import string


def generate_random_string(max_length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, max_length)))


destination_ip = '8.8.8.8'
key = b'ThisIsA16ByteKey'

sender = Sender(destination_ip, key)
receiver = Receiver(key)


def send_message(message):
    sender.send_message(message)


def receive_message():
    receiver.receive_message()


transmission_rates = []


def compute_transmission_time():
    message = generate_random_string().encode('utf-8')
    start_time = time.time()
    send_thread = threading.Thread(target=send_message,args=(message,))
    receive_thread = threading.Thread(target=receive_message)

    # Start sender and receiver threads
    send_thread.start()
    receive_thread.start()

    # Wait for the threads to finish
    send_thread.join()
    receive_thread.join()
    end_time = time.time()
    transmission_rates.append(len(message) / (end_time - start_time))


num_messages = 10  # Number of messages to send
threads = [threading.Thread(target=compute_transmission_time) for _ in range(num_messages)]

for thread in threads:
    thread.start()
    thread.join()


average_bitrate = sum(transmission_rates) / len(transmission_rates)
print("Average bit/second transmission rate:", average_bitrate)
