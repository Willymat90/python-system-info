import platform
import socket
import sys

print("=== SYSTEM INFORMATION ===")
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Python Version:", sys.version)
print("Architecture:", platform.machine())
print("Hostname:", socket.gethostname())
