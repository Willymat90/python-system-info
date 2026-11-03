
import platform
import socket
import sys

import datetime
print("=== SYSTEM INFORMATION ===")
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Python Version:", sys.version)
print("Architecture:", platform.machine())
print("Hostname:", socket.gethostname())
print("Current Date and Time:", datetime.datetime.now())
