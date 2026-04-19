import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("--- SERVIDOR TCP  ---")
print("Se esta esperando una conexion...")

conexion, direccion = server.accept()
print(f"Conectado con {direccion}. Listo para recibir mensajes.")

while True:
    mensaje = conexion.recv(1024).decode()
    if not mensaje or mensaje.lower() == 'salir':
        break
    print(f"Cliente dice: {mensaje}")
    conexion.send("Mensaje TCP recibido".encode())

print("Cerrando servidor...")
conexion.close()
server.close()