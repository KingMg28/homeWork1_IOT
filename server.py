import socket

# تنظیمات سرور
server_host = '127.0.0.1'  # آدرس IP لوپ‌بک برای تست لوکال
server_port = 12345        # پورتی که سرور به آن گوش می‌دهد

# ایجاد سوکت TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)  # تعداد کلاینت‌هایی که سرور می‌تواند همزمان بپذیرد

print(f"Server listening on {server_host}:{server_port}...")

# انتظار برای اتصال کلاینت
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# حلقه برای ارسال و دریافت پیام‌ها
try:
    while True:
        # دریافت پیام از کلاینت
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")
        
        # ارسال پاسخ به کلاینت
        message = input("You: ")
        conn.sendall(message.encode())
finally:
    conn.close()
    server_socket.close()
