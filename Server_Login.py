import socket
from shutil import which
MEU_IP = "10.15.2.98"
def init():
    print()
    print("SERVER  Online |/_")
    print()
def envio_login(ddd): 
                print("6")
                PORTA_Servidor = 5100
                print("7")
                udp4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                DESTINO = (MEU_IP, PORTA_Servidor)
                print("8")
                udp4.sendto (bytes( str(ddd) ,"utf8"), DESTINO) 
                print("9")
                udp4.close()
while True:
                print("1")
                MINHA_PORT = 5007
                MEU_SERVIDOR_3 = (MEU_IP, MINHA_PORT)
                print("2")
                udp3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                udp3.bind(MEU_SERVIDOR_3)
                print("3")
                matricula, END_cliente_5 = udp3.recvfrom(1024) 
                matricula = matricula.decode()
                print("4")
                with open(f'C:\\Users\\Robótica-LaISER\\Desktop\\Interface\\Mensagens\\{matricula}.txt','r') as l:
                    ddd = l.read()
                    envio_login(ddd)
                print("5")
                udp3.close()
