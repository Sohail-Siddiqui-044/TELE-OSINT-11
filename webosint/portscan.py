import nmap
import json


# Path to Nmap executable
NMAP_PATH = "C:\\Program Files (x86)\\Nmap\\nmap.exe"


def DefaultPort(Xhost, Yport):

    print("\nStarting port scan with range 22-443")

    try:

        nm = nmap.PortScanner(
            nmap_search_path=(NMAP_PATH,)
        )

        result = nm.scan(Xhost, '22-443')

        display(result)

    except Exception as e:

        print("Nmap Error :", e)


def Customrange(Xhost, Yport):

    port_range = input("Enter the range : ")

    print(f"\nStarting port scan with range {port_range}")

    try:

        nm = nmap.PortScanner(
            nmap_search_path=(NMAP_PATH,)
        )

        result = nm.scan(Xhost, port_range)

        display(result)

    except Exception as e:

        print("Nmap Error :", e)


def display(result):

    try:

        scan_data = result.get('scan', {})

        if not scan_data:
            print("No hosts found")
            return

        # Get first scanned host
        new = next(iter(scan_data.values()))

        # IP Address
        ip_add = new.get('addresses', {})

        print("\nIP Address :", ip_add.get('ipv4', 'Unknown'))

        # Hostnames
        hostnames = new.get('hostnames', [])

        print("\nHostnames :")

        if not hostnames:

            print("No hostnames found")

        else:

            for i, host in enumerate(hostnames, start=1):

                print(f"Hostname {i} : {host.get('name', 'Unknown')}")

        # Port Information
        print("\nOpen Ports :\n")

        ports = new.get('tcp', {})

        if not ports:

            print("No open TCP ports found")
            return

        for port, info in ports.items():

            print(f"Port : {port}")
            print(f"State : {info.get('state')}")
            print(f"Service : {info.get('name')}")
            print(f"Product : {info.get('product', 'Unknown')}")
            print(f"Version : {info.get('version', 'Unknown')}")
            print("-" * 30)

        # Optional full JSON output
        print("\nJSON Output :\n")

        print(json.dumps(ports, indent=4))

    except Exception as e:

        print("Display Error :", e)
