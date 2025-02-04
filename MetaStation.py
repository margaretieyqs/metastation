import os
import subprocess
import socket

class MetaStation:
    def __init__(self):
        self.hostname = socket.gethostname()

    def list_connections(self):
        print("Listing all network interfaces:")
        try:
            output = subprocess.check_output("ipconfig", shell=True).decode()
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error listing interfaces: {e}")

    def optimize_connection(self):
        print("Optimizing connection settings for better performance...")
        try:
            os.system("netsh interface tcp set global autotuninglevel=normal")
            os.system("netsh interface tcp set global rss=enabled")
            print("Network settings optimized.")
        except Exception as e:
            print(f"Error optimizing connection: {e}")

    def flush_dns(self):
        print("Flushing DNS cache...")
        try:
            os.system("ipconfig /flushdns")
            print("DNS cache flushed.")
        except Exception as e:
            print(f"Error flushing DNS: {e}")

    def display_network_summary(self):
        print("Displaying network summary:")
        try:
            ip_address = socket.gethostbyname(self.hostname)
            print(f"Hostname: {self.hostname}")
            print(f"IP Address: {ip_address}")
        except socket.error as e:
            print(f"Error retrieving network summary: {e}")

if __name__ == "__main__":
    meta_station = MetaStation()
    meta_station.list_connections()
    meta_station.optimize_connection()
    meta_station.flush_dns()
    meta_station.display_network_summary()