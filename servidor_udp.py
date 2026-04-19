import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 6000))

print("--- SERVIDOR UDP   ---")

while True:
    try:
        mensaje, direccion = server.recvfrom(1024)
        
        # Simulacion de no recibir el mensaje
        suerte = random.randint(1, 10)
        
        if suerte <= 3:  # 30% de probabilidad de falla
            print(f"Paquete de {direccion} perdido.")
            # el servidor lo ignora y no responde
        else:
            print(f"Paquete recibido de {direccion}: {mensaje.decode()}")
            server.sendto("Respuesta: Confirmado.".encode(), direccion)
            
    except KeyboardInterrupt:
        break

server.close()