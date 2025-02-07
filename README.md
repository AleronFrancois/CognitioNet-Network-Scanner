![NetworkScannerScreenshot#1](https://github.com/user-attachments/assets/6b5be8c3-a954-4291-8cea-a4dcbefa6abd)
![NetworkScannerScreenshot#2](https://github.com/user-attachments/assets/798e27f4-bd3f-4dda-a4b1-b85f7dff9859)

# CogitioNet

**CogitioNet** is a lightweight network enumeration tool designed to scan for active devices and detect open ports on specified targets.

## Commands
- `-sn <target>`: Scans network  
- `-ip <target>`: Specify IP address  
- `-p <range>`: Specify port range  
- `man`: Displays the command manual  

## Example Usage
- **Scan for active devices:**  
  ```sh
  -sn 192.168.0.0-192.168.0.255
- **Scan for open ports:**  
  ```sh
  -ip 192.168.0.44 -p 0-8000
