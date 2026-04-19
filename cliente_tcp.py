import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))

print("--- CLIENTE TCP ACTIVO ---")
print("Si quieres cerrar, escribe 'salir' para terminar.\n")

while True:
    msg = input("Cliente (TCP): ")
    cliente.send(msg.encode())
    
    if msg.lower() == 'salir':
        break
        
    respuesta = cliente.recv(1024).decode()
    print(f"Servidor: {respuesta}")

cliente.close()