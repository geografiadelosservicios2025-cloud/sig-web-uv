import socket

def get_local_ip():
    try:
        # Crea un socket temporal para determinar la IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    print(f"\n--- CONFIGURACIÓN DE ACCESO ---")
    print(f"Tu IP local es: {get_local_ip()}")
    print(f"Para que otros accedan, diles que entren a: http://{get_local_ip()}:8000")
    print(f"-------------------------------\n")
