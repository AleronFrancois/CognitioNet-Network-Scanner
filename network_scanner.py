import socket
import argparse
import ipaddress
import subprocess

"""
CogitioNet Network Scanner 

Open source tool for scanning networks for devices and open ports.
"""

__author__ = "Aleron Francois"
__date__ = "7/02/2025"


def manual() -> None:
    """
    Definition for all command sytax
    """
    print("----------------------CogitioNet Manual----------------------")
    print("-ip <target>     | For specifying a specific IP address for scan.")
    print("-p <start-end>   | For specifying port range.")
    print("-sn <start-end>  | For specifying subnet range.")
    print()


def commands(args_list):
    """
    Defines a command option keyword used for entering specific details
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-sn", type=str, help="IP address range")
    parser.add_argument("-ip", type=str, help="Target IP address")
    parser.add_argument("-p", type=str, help="Port range")
    
    return parser.parse_args(args_list) # Parse the command keyword


def scan_ports(ip_address, start_port, end_port) -> None:
    """
    Scans all ports within a port range
    """
    # Iterates through port range and checks if the target device responds to probe request through port stream
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip_address, port)) == 0:
                print(f"[+] Port {port} is open on {ip_address}")
            else:
                print(f"[-] Port {port} is closed on {ip_address}")
    print()


def scan_devices(start_ip, end_ip):
    """
    Scans all devices within an ip address range
    """
    try:
        start_ip_obj = ipaddress.IPv4Address(start_ip)
        end_ip_obj = ipaddress.IPv4Address(end_ip)
    except ipaddress.AddressValueError as e:
        print(f"Invalid IP address range: {e}")
        return

    # Iterates through ip address range and checks if a devices respondes to a ping request
    for i in range(int(start_ip_obj), int(end_ip_obj) + 1):
        ip = str(ipaddress.IPv4Address(i))
        response = subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = response.stdout.decode('utf-8')
        if "TTL=" in output:
            print(f"[+] Device at {ip} is online")
        else:
            print(f"[-] Device at {ip} is offline")
    print()


def prompt():
    """
    Prompt the user to enter a command
    """
    while True:
        command = input("CognitioNet > ")  # Prompt user to enter command
        print()

        # Load manual page
        if command == "man":
            manual()
            continue

        args_list = command.split()  # Splits command into options and values
        args = commands(args_list)

        if args.sn:
            start_ip, end_ip = args.sn.split("-")
            scan_devices(start_ip, end_ip)  # Scan devices
        elif args.ip and args.p:
            ip_address = args.ip  # Extract ip address
            port_range = args.p.split("-")  # Hyphen to separate start and finish of port range
            start_port = int(port_range[0])  # Start of port range
            end_port = int(port_range[1])  # End of port range
            scan_ports(ip_address, start_port, end_port)  # Scan ports
        else:
            print("Invalid command. Type 'man' for manual.")


def main():
    """
    Drives the program
    """
    prompt() # Load command prompt


if __name__ == "__main__":
    main()