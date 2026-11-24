import socket as s

atteckedIp = input("Podaj ip: ")
port = 80

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect((atteckedIp, port))