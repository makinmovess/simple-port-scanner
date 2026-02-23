import socket
import time
import sys


GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'


print(f"{CYAN}=================================================={RESET}")
print(f"{CYAN}       WŁASNY SKANER PORTÓW (BY IMMORTAL)       {RESET}")
print(f"{CYAN}=================================================={RESET}")


target_ip = input(f"{YELLOW}[?] Podaj adres IP lub domenę do skanowania (np. 8.8.8.8): {RESET}")
print(f"{CYAN}=================================================={RESET}")

ports_to_scan = [21, 22, 53, 80, 443, 3389]

start_time = time.time()
total_ports = len(ports_to_scan)

for index, port in enumerate(ports_to_scan):
    sys.stdout.write(f"\r{YELLOW}[~] Skanowanie w toku... sprawdzam port {port} ({index+1}/{total_ports}){RESET}")
    sys.stdout.flush()
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        
        sys.stdout.write("\r" + " " * 60 + "\r")
        
        if result == 0:
            print(f"{GREEN}[+] Port {port} jest OTWARTY{RESET}")
        else:
            print(f"{RED}[-] Port {port} jest ZAMKNIĘTY{RESET}")
            
        sock.close()
        
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Skanowanie przerwane przez użytkownika.{RESET}")
        break
    except socket.gaierror:
        
        print(f"\n{RED}[!] Błąd: Nie można rozpoznać adresu hosta.{RESET}")
        break
    except Exception as e:
        print(f"\n{RED}[!] Wystąpił błąd: {e}{RESET}")

end_time = time.time()
print(f"{CYAN}=================================================={RESET}")
print(f"{GREEN}[*] Skanowanie zakończone w: {round(end_time - start_time, 2)} sekund{RESET}")


print(f"{CYAN}=================================================={RESET}")
input(f"{YELLOW}Wciśnij ENTER, aby zamknąć program...{RESET}")