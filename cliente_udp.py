import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.settimeout(3) # Si en 3 segundos no hay respuesta, se asume  que se perdió
servidor_dir = ('localhost', 6000)

print("--- CLIENTE UDP ---")

while True:
    msg = input("\nEscribe tu mensaje: ")
    if msg.lower() == 'salir': break
    
    cliente.sendto(msg.encode(), servidor_dir)
    
    try:
        # Intentamos recibir respuesta
        respuesta, addr = cliente.recvfrom(1024)
        print(f"Servidor respondio: {respuesta.decode()}")
    except socket.timeout:
        # Aquí es donde se cumple la teoría de UDP
        print("El paquete se  a perdio en la red (No hubo respuesta por parte del servidor ).")

cliente.close()