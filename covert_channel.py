from scapy.all import IP, ICMP, send, sniff, Raw
import zlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import time


class Sender:
    def __init__(self, target_ip, key, interval=0.5):
        self.target_ip = target_ip
        self.key = key
        self.interval = interval
        self.secret_message = b''

    def encrypt_message(self):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(self.secret_message) + padder.finalize()
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        self.secret_message = encrypted_data

    def compress_message(self):
        self.secret_message = zlib.compress(self.secret_message)

    def send_packet(self, data):
        packet = IP(dst=self.target_ip) / ICMP() / Raw(load=data)
        send(packet, verbose=False)

    def send(self):
        self.compress_message()
        self.encrypt_message()
        self.send_packet(self.secret_message)
        time.sleep(self.interval)

    def send_message(self, message):
        self.secret_message = message
        self.send()


class Receiver:
    def __init__(self, key):
        self.key = key
        self.secret_message_chunks = []
        self.secret_message = b''

    def decrypt_message(self):
        cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(self.secret_message) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        self.secret_message = unpadded_data

    def decompress_message(self):
        self.secret_message = zlib.decompress(self.secret_message)

    def process_packet(self, packet):
        if ICMP in packet and Raw in packet:
            self.secret_message = packet[Raw].load

    def receive(self):
        sniff(filter="icmp", prn=self.process_packet, timeout=5)

    def receive_message(self):
        self.receive()
        self.decrypt_message()
        self.decompress_message()
