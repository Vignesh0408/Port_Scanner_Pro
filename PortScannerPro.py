import socket
import ssl
import colorama
from colorama import *
from datetime import datetime

colorama.init()

print (Fore.GREEN +"""8888888b.                   888     .d8888b.                                                       8888888b.                   
888   Y88b                  888    d88P  Y88b                                                      888   Y88b                  
888    888                  888    Y88b.                                                           888    888                  
888   d88P  .d88b.  888d888 888888  "Y888b.    .d8888b  8888b.  88888b.  88888b.   .d88b.  888d888 888   d88P 888d888  .d88b.  
8888888P"  d88""88b 888P"   888        "Y88b. d88P"        "88b 888 "88b 888 "88b d8P  Y8b 888P"   8888888P"  888P"   d88""88b 
888        888  888 888     888          "888 888      .d888888 888  888 888  888 88888888 888     888        888     888  888 
888        Y88..88P 888     Y88b.  Y88b  d88P Y88b.    888  888 888  888 888  888 Y8b.     888     888        888     Y88..88P 
888         "Y88P"  888      "Y888  "Y8888P"   "Y8888P "Y888888 888  888 888  888  "Y8888  888     888        888      "Y88P"  
                                                                                                                               
                                                                                                                               
                                                                                                                               """ + Style.RESET_ALL)

target = input("Enter the host name: ")
ip = socket.gethostbyname(target)

context = ssl.create_default_context()

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((target, 443))
        with context.wrap_socket(sock, server_hostname=target) as ssock:
            tls_version = ssock.version()
            cipher_suite = ssock.cipher()
except:
    print("error")

print("Enter the range of ports to scan the Target")
startport = int(input("Enter the Start Port: "))
endport = int(input("Enter the End Port: "))

print("Given Target", ip , "is scanning")
time_init = datetime.now()

open_ports = []

try:
    for port in range(startport, endport):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.settimeout(0.2)
        result = server_sock.connect_ex((ip, port))
        if result == 0:
            print(f"port {port}: Open")
            open_ports.append(port)
        else:
            pass
        
except socket.error as err:
    print("couldn't connect to server:", err)

time_finish = datetime.now()
total_time = time_finish - time_init

print("TLS Version of the hostname:", tls_version)
print("Cipher Suite used by the hostname:", cipher_suite)
print("Open ports:", open_ports)
print("Total time to Scan the process is:", total_time)
