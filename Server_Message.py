from shutil import which
import socket
MEU_IP = "10.15.2.98"
def init():
    print()
    print("SERVER  Online |/_")
    print()
while True:
        MINHA_PORTA = 5000
        MINHA_PORTA2 = 5001
        MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)
        MEU_SERVIDOR2 = (MEU_IP, MINHA_PORTA2)
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        udp1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        udp.bind(MEU_SERVIDOR)
        udp1.bind(MEU_SERVIDOR2)
        matricula, END_cliente_1 = udp.recvfrom(1024)
        msg, END_cliente_2 = udp1.recvfrom(1024)
        print()       
        print("Matricula  { ", matricula , " } .") #, END_cliente_1) 
        print("Mensagem recebida  | ", msg , " | .") #, END_cliente_2)
        print()
        msg = msg.decode()
        matricula = matricula.decode()
        with open(f'C:\\Users\\Robótica-LaISER\\Desktop\\Interface\\Mensagens\\{matricula}.txt' , 'a+') as k:
            k.write(" | ")
            k.write(str(msg))
        udp.close() 
        udp1.close()

