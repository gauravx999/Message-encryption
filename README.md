

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

<img width="904" height="383" alt="image" src="https://github.com/user-attachments/assets/9c693f87-ce85-4f70-92d1-c1f290c0379d" />


## 📂 Project Structure

```
Network-Secure-Chat/
│
├── client_ui.py          # Main Tkinter app (choose Server or Client on start)
├── crypto_utils.py       # Cryptography helper functions
│
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
            
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

### 🔹 Server Window  &  ### 🔹 Client Window 

<img width="1866" height="922" alt="Screenshot 2025-10-01 222220" src="https://github.com/user-attachments/assets/d09faaeb-9dca-42de-9814-04cedc029cea" />




---


## 🛠️ Requirements

* Python **3.8+**
* **Tkinter** (comes pre-installed with Python)
* **PyCryptodome**

---

---


