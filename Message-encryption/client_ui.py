import tkinter as tk
from tkinter import messagebox
import socket, threading, json, base64
from crypto_utils import generate_rsa_keypair, rsa_encrypt, rsa_decrypt, generate_aes_key, aes_encrypt, aes_decrypt, sha256_hash

HOST = 'localhost'
PORT = 5000

class ChatUI:
    def __init__(self, root, mode="server"):
        self.root = root
        self.mode = mode
        self.root.title(f"🔐 Secure {mode.capitalize()}")

        # Output box
        self.output_text = tk.Text(root, width=60, height=15)
        self.output_text.pack(pady=10)
        
        # Entry and buttons
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        tk.Button(root, text="Send", command=self.send_msg).pack(pady=5)
        tk.Button(root, text="Toggle View", command=self.toggle_view).pack(pady=5)

        self.show_encrypted = False

        # Keys
        if mode=="server":
            self.private_key, self.public_key = generate_rsa_keypair()
            with open("server_public.pem", "wb") as f:
                f.write(self.public_key)
            self.aes_key = None
            threading.Thread(target=self.start_server, daemon=True).start()
        else:
            self.s = socket.create_connection((HOST, PORT))
            with open("server_public.pem", "rb") as f:
                self.server_pub = f.read()
            self.aes_key = generate_aes_key()
            self.send_handshake()
            threading.Thread(target=self.listen, daemon=True).start()

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1)
        self.conn, addr = server.accept()
        self.output_text.insert(tk.END, f"✅ Connected: {addr}\n")
        while True:
            try:
                data = self.conn.recv(4096)
                if not data:
                    break
                payload = json.loads(data.decode())
                # Extract AES key if present
                if 'encrypted_aes_key' in payload:
                    enc_aes = base64.b64decode(payload['encrypted_aes_key'])
                    self.aes_key = rsa_decrypt(enc_aes, self.private_key)
                iv = base64.b64decode(payload['iv'])
                enc = base64.b64decode(payload['encrypted_message'])
                h = base64.b64decode(payload['sha256_hash'])
                msg = aes_decrypt(enc, self.aes_key, iv)
                valid = sha256_hash(msg)==h
                self.display(msg.decode(), valid, "Client", iv, enc)
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {e}\n")
                break

    def send_handshake(self):
        iv, enc = aes_encrypt(b"Handshake", self.aes_key)
        enc_aes = rsa_encrypt(self.aes_key, self.server_pub)
        h = sha256_hash(b"Handshake")
        payload = {
            "encrypted_aes_key": base64.b64encode(enc_aes).decode(),
            "iv": base64.b64encode(iv).decode(),
            "encrypted_message": base64.b64encode(enc).decode(),
            "sha256_hash": base64.b64encode(h).decode()
        }
        self.s.sendall(json.dumps(payload).encode())
        self.output_text.insert(tk.END, "Handshake sent\n")

    def send_msg(self):
        msg = self.entry.get().encode()
        if self.mode=="server":
            if not self.aes_key:
                messagebox.showerror("Error", "No AES key established yet!")
                return
            iv, enc = aes_encrypt(msg, self.aes_key)
            h = sha256_hash(msg)
            payload = {
                "iv": base64.b64encode(iv).decode(),
                "encrypted_message": base64.b64encode(enc).decode(),
                "sha256_hash": base64.b64encode(h).decode()
            }
            self.conn.sendall(json.dumps(payload).encode())
        else:
            iv, enc = aes_encrypt(msg, self.aes_key)
            h = sha256_hash(msg)
            payload = {
                "iv": base64.b64encode(iv).decode(),
                "encrypted_message": base64.b64encode(enc).decode(),
                "sha256_hash": base64.b64encode(h).decode()
            }
            self.s.sendall(json.dumps(payload).encode())
        self.display(msg.decode(), True, self.mode.capitalize(), iv, enc)
        self.entry.delete(0, tk.END)

    def listen(self):
        while True:
            try:
                data = self.s.recv(4096)
                if not data:
                    break
                payload = json.loads(data.decode())
                iv = base64.b64decode(payload['iv'])
                enc = base64.b64decode(payload['encrypted_message'])
                h = base64.b64decode(payload['sha256_hash'])
                msg = aes_decrypt(enc, self.aes_key, iv)
                valid = sha256_hash(msg)==h
                self.display(msg.decode(), valid, "Server", iv, enc)
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {e}\n")
                break

    def display(self, msg, valid, sender, iv, enc):
        if self.show_encrypted:
            text = f"[{sender}] Encrypted: {base64.b64encode(enc).decode()}\n"
        else:
            text = f"[{sender}] {msg} {'✅' if valid else '❌'}\n"
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)

    def toggle_view(self):
        self.show_encrypted = not self.show_encrypted

if __name__=="__main__":
    root = tk.Tk()
    mode = input("Start as server or client? (s/c): ").lower()
    app = ChatUI(root, "server" if mode=="s" else "client")
    root.mainloop()
