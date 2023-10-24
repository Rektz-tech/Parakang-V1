import time
import socket
import ssl

def print_message(message, color="red", bold=True):
    color_code = {"red": "\033[91m", "default": ""}
    bold_code = "\033[1m" if bold else ""
    reset_code = "\033[0m"
    print(f"{color_code[color]}{bold_code}{message}{reset_code}")

def main_menu():
    print_message("HALO, I AM REKTZ AI FROM MHAMINN", color="red", bold=True)
    time.sleep(3)
    return True

def submenu():
    print("\n>> Tekan 1 untuk scan domain")
    print(">> Tekan 2 untuk scan SSL")
    print(">> Tekan 3 untuk scan Host dan port")
    choice = input("$Jawab = ")

    if choice == '1':
        domain = input("\n$HOST/IP = ")
        scan_domain(domain)
    elif choice == '2':
        domain = input("\n$HOST/IP = ")
        scan_ssl(domain)
    elif choice == '3':
        host = input("\n>> Masukan Host/IP\n")
        port = int(input(">> Masukan Port\n"))
        scan_host_port(host, port)

def scan_domain(domain):
    print_message("\nTUNGGU TELASO!!....", color="red", bold=True)
    time.sleep(8)
    print_message("SABAR YA TOD!!...", color="red", bold=True)
    time.sleep(5)

    # Contoh pemindaian
    try:
        result = socket.getaddrinfo(domain, 443, socket.AF_UNSPEC, socket.SOCK_STREAM)
        hosts = [info[4][0] for info in result]
        print(f"\nDaftar host yang mendukung SSL untuk {domain}:\n")
        for host in hosts:
            print(host)
    except Exception as e:
        print(f"Error: {e}")

def scan_ssl(domain):
    print_message("\nTUNGGU TELASO!!....", color="red", bold=True)
    time.sleep(8)
    print_message("SABAR YA TOD!!...", color="red", bold=True)
    time.sleep(5)

    # Contoh pemindaian
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                print(f"\nInformasi sertifikat SSL:\n{cert}\n")
    except Exception as e:
        print(f"Error: {e}")

def scan_host_port(host, port):
    print_message("\nTUNGGU TELASO!!....", color="red", bold=True)
    time.sleep(8)
    print_message("SABAR YA TOD!!...", color="red", bold=True)
    time.sleep(5)

    # Contoh pemindaian
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, port))
        print_message(f"\ntersambung ke {host}:{port}")
        sock.close()
    except socket.error as e:
        print_message(f"Gagal tersambung ke {host}:{port} - {e}")

def goodbye():
    print_message("\nTERIMA KASIH", color="red", bold=True)

def main():
    if not main_menu():
        return

    while True:
        submenu()
        choice = input("\nKembali ke halaman utama? (Y/N): ")
        if choice.lower() != 'y':
            break

    goodbye()

if __name__ == "__main__":
    main()
