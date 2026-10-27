import random
import pyfiglet

name = "JANGOTRA"
print ("=" * 60)

ban = pyfiglet.figlet_format(
    name,
    font="slant"
)

print("\033[96m" + ban + "\033[0m")
print("=" * 60)
print("       Block IP Addresees")
print("=" * 60)
print("Date : 27/10/2026\n")

def check_rule(ip_address, block_ip):

    for rule_ip,count in block_ip.items():
        if ip_address == rule_ip:
            return count
    return "allow"

def generate_ip():
    return f"192.168.1.{random.randint(1,25)}"

def main():

    block_ip = {
        "192.168.1.1" : "block",
        "192.168.1.2" : "block",
        "192.168.1.3" : "block",
        "192.168.1.4" : "block",
        "192.168.1.5" : "block",
        "192.168.1.6" : "block",
        "192.168.1.7" : "block",
        "192.168.1.8" : "block",
    }

    for _ in range(12):
        ip_address = generate_ip()
        firewall = check_rule(ip_address,block_ip)
        randon_number = random.randint(1,9999)

        print(f"IP: {ip_address}, Action: {firewall}, Randon Number: {randon_number}")



if __name__ == "__main__":
    main()
