import socket

# تنظیمات اتصال کلاینت
server_host = '127.0.0.1'  # باید با آدرس IP سرور همخوانی داشته باشد
server_port = 12345        # باید با پورت سرور همخوانی داشته باشد

# ایجاد سوکت TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

print("Connected to the server.")

# حلقه برای ارسال و دریافت پیام‌ها
try:
    while True:
        # ارسال پیام به سرور
        message = input("You: ")
        client_socket.sendall(message.encode())
        
        # دریافت پاسخ از سرور
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server: {data}")
finally:
    client_socket.close()
