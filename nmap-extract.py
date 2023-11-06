import re
import argparse
import socket
import pyperclip

def extract_ipv4_addresses(file_path):
    ip_addresses = []
    with open(file_path, 'r') as file:
        data = file.read()
        ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        ip_addresses = re.findall(ipv4_pattern, data)

    ip_addresses = list(dict.fromkeys(ip_addresses))  # Remove duplicates and maintain order

    return ip_addresses

def get_domains(ip_addresses):
    domains = {}
    for ip in ip_addresses:
        try:
            domain = socket.gethostbyaddr(ip)[0]
            domains[ip] = domain
        except socket.herror:
            domains[ip] = "Domain not found"

    return domains

def main():
    parser = argparse.ArgumentParser(description="Extract IPv4 addresses and associated domains from an NMAP output file")
    parser.add_argument('file_path', help='Path to the NMAP output file')
    parser.add_argument('-o', '--output', help='Output file to save the results')
    parser.add_argument('-c', '--clipboard', action='store_true', help='Copy results to clipboard')
    parser.add_argument('-d', '--dns', action='store_true', help='Show associated domains')
    args = parser.parse_args()

    ip_list = extract_ipv4_addresses(args.file_path)

    domains = None
    if args.dns:
        domains = get_domains(ip_list)

    if ip_list:
        print("List of unique IPv4 addresses found in the NMAP file:")
        for ip in ip_list:
            if args.dns:
                print(f"{ip}: {domains[ip]}")
            else:
                print(ip)

        if args.output:
            with open(args.output, 'w') as output_file:
                for ip in ip_list:
                    if args.dns:
                        output_file.write(f"{ip}: {domains[ip]}\n")
                    else:
                        output_file.write(ip + '\n')
            print(f"Results saved to {args.output}")

        if args.clipboard:
            if args.dns:
                ip_addresses_text = '\n'.join([f"{ip}: {domains[ip]}" for ip in ip_list])
            else:
                ip_addresses_text = '\n'.join(ip_list)
            pyperclip.copy(ip_addresses_text)
            print("Results copied to clipboard")

    else:
        print("No IPv4 addresses found in the NMAP file.")

if __name__ == "__main__":
    main()

