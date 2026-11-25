import socket as s
import threading 

attacekd_ip = input("Podaj ip: ")
threads =[]
show = input("Shwo closed ports(Y/n): ")

open_ports=[]

def connect(Ip, port):
    try:
        with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:
            sock.settimeout(2.0)  # Wait at most 2 seconds per port
            sock.connect((Ip, port))
            print(f"Port {port} on {Ip} is OPEN")
            open_ports.append(port)
    except ConnectionRefusedError:
        if show == "Y" or show == "y":
            print(f"Port {port} on {Ip} is CLOSED (connection refused)")
    except TimeoutError:
        if show == "Y" or show == "y":
            print(f"Port {port} on {Ip} TIMED OUT (filtered or unreachable)")
    except s.gaierror:
        print(f"Invalid IP address or hostname: {Ip}")
    except OSError as e:
        print(f"Connection failed: {e}")

for i in range(24000):
    t = threading.Thread(target=connect, args=(attacekd_ip, i))
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()

print("""

==========

""")

for port in open_ports:
    print(f"Port {port} is open")