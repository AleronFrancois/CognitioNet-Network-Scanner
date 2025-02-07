![NetworkScannerScreenshot#1](https://github.com/user-attachments/assets/6b5be8c3-a954-4291-8cea-a4dcbefa6abd)

CogitioNet is a lightweight network enumiration tool designed to scan for active devices and detect open ports on specified targets.

**Commands:**
-sn <target>: Scans network
-ip <target>: Specify IP address
-p <range>: Specify port range 
man: Provides a command manual for the tool

**Example:**
Scan for active devices: -sn 192.168.0.0-192.168.0.255
Scan for open ports: -ip 192.168.0.44 -p 0-8000
