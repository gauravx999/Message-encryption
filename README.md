# Message-encryption
A simple encrypted chat application using RSA + AES + SHA-256, built with Python. This project demonstrates secure communication between a client and a server with end-to-end encryption.


Perfect 👍
Let’s build a **proper, professional README.md** for your GitHub repo, with everything clearly explained: structure, badges, setup guide, screenshots, and working details.

Here’s the polished version you can directly use in your repo:

---

# 🔐 Network Secure Chat (Python + Tkinter)

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python\&logoColor=white)
![Cryptography](https://img.shields.io/badge/Security-Cryptography-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A simple **encrypted chat application** using **RSA + AES + SHA-256**, built with Python.
This project demonstrates **secure communication** between a client and a server with **end-to-end encryption** and a Tkinter-based UI.

---

## 📌 Features

* 🔑 **RSA** for secure key exchange
* ⚡ **AES-256 (CBC mode)** for fast message encryption
* 🛡️ **SHA-256** for integrity verification
* 🎨 Tkinter **chat UI**
* 🔄 Works as **Server or Client** (select on start)
* 📡 Messages can be viewed in both **encrypted** and **decrypted** form

---

## 📂 Project Structure

```
Network-Secure-Chat/
│
├── client_ui.py          # Main Tkinter app (choose Server or Client on start)
├── crypto_utils.py       # Cryptography helper functions
│
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
│
└── assets/               # Project images (logo, screenshots)
    ├── logo.png
    ├── screenshot_client.png
    ├── screenshot_server.png
```

---

## 🚀 Getting Started

### 1️⃣ Clone this repository

```bash
git clone https://github.com/yourusername/Network-Secure-Chat.git
cd Network-Secure-Chat
```

### 2️⃣ Install dependencies

Make sure you have **Python 3.8+** installed.
Install dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pycryptodome
```

### 3️⃣ Run the application

```bash
python client_ui.py
```

A **popup window** will appear asking:

➡️ Start as **Server** or **Client**

* 🚀 **Server** → waits for a client to connect
* 💻 **Client** → connects to the server and starts encrypted messaging

---

## 🖼️ Screenshots

### 🔹 Client Window

![Client Screenshot](assets/screenshot_client.png)

### 🔹 Server Window

![Server Screenshot](assets/screenshot_server.png)

---

## 🔐 How It Works

1. **RSA Key Exchange**

   * Server generates an RSA key pair
   * Client encrypts an AES session key with server’s RSA public key

2. **AES-256 for Messages**

   * Once the AES key is shared, all chat messages are encrypted with AES in **CBC mode**

3. **SHA-256 Integrity Check**

   * Each message is hashed with SHA-256
   * The receiver verifies the hash before accepting the message

---

## 🛠️ Requirements

* Python **3.8+**
* **Tkinter** (comes pre-installed with Python)
* **PyCryptodome**

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to fork, use, and improve! 🚀

---

👉 Do you also want me to **generate a `requirements.txt` file** for you automatically, so users can install dependencies in one command?

