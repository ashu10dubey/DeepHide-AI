# 🔐 DeepHide AI – Secure Communication via AI-Powered Multilayered Steganography

Welcome to **DeepHide AI**, a secure, AI-driven encryption system that embeds confidential messages within images using cutting-edge **steganography** combined with **hybrid cryptography (AES + ECC)**. 


---

##  Overview

**DeepHide AI** is a desktop application that enhances data confidentiality by:
- Hiding encrypted text within AI-selected images.
- Leveraging **AES (Advanced Encryption Standard)** for payload encryption.
- Securing the AES key using **ECC (Elliptic Curve Cryptography)**.
- Using **LSB (Least Significant Bit)** steganography for invisible embedding.

---

##  Features

- 🧠 **AI-driven image selection** for embedding (based on message length).
- 🔐 **Dual-layered encryption** using AES (symmetric) and ECC (asymmetric).
- 🖼️ **Steganography** via LSB pixel modification.
- 🔄 **Encrypt/Decrypt flow** with secure temporary file handling.
- 🧹 **Automatic deletion** of sensitive assets post-operation.

---

## 🗂 Project Structure

```bash
DeepHide-AI/
│
├── .vscode/
│   └── settings.json               # Live server config (e.g., port 5500)
│
├── AEScipher.py                   # AES encryption using CBC and PKCS padding
├── Decrypter.py                   # AES decryption with ECC key extraction
├── Encrypter.py                   # Encrypts input using AES, saves as PNG
├── Hybrid.py                      # Manages both AES and ECC hybrid flow
├── decryptonce.py                 # Decrypts once using ECC + AES
│
├── static/
│   ├── cipher/
│   │   ├── cipher.txt             # Encrypted text (AES)
│   │   ├── cipherImage.png        # Image with embedded ciphertext
│   │   ├── decryptedImage.jpg     # Output image after decryption
│   │
│   ├── css/
│   │   ├── style.css              # Base styling
│   │   └── index.css              # Styling for main page
│   │
│   ├── js/
│   │   └── functions.js           # JS actions for encryption, decryption, UI
│
├── templates/
│   ├── encrypt.html               # UI page for encryption
│   ├── decrypt.html               # UI page for decryption
│   ├── index.html                 # Home interface
│   └── success.html               # Results after operation
│
├── app.py                         # Flask app entry point
├── deletesecret.py                # Auto-deletes temporary/generated files

```

##  Tech Stack

| Component        | Tools / Libraries                        |
|------------------|------------------------------------------|
| Language         | Python                                   |
| UI               | Tkinter                                  |
| Encryption       | PyCryptodome (AES), ECC (custom logic)   |
| Steganography    | PIL, Stegano                             |
| AI Integration   | Text-length based image selector         |

---

## 🔐 Cryptography Model

**Hybrid Encryption Workflow:**
1. **AES** encrypts the plaintext message.
2. **ECC** secures the AES key during transmission.
3. The encrypted data is embedded in an image using **LSB** steganography.

**Decryption Workflow:**
- Retrieve the AES key via ECC.
- Decrypt the ciphertext.
- Extract hidden text from the image.

---

##  Use Cases

- 🪖 **Military communications**
- 🏥 **Confidential medical data transmission**
- 💼 **Enterprise secure messaging**
- 👤 **Personal data protection in public media**

---

##  Demonstration

> Encrypt → Embed → Transmit → Decrypt → Retrieve  
> *All in a user-friendly, AI-powered interface.*

Images and data are **auto-deleted** from memory after processing to maintain zero data exposure.

---

##  License

**© 2025 Ashutosh Dubey. All rights reserved.**

This repository is **proprietary**. Use, distribution, or modification without express permission is strictly prohibited.

---

## 🤝 Contact

- 📧 [ashutoshdubey9794@gmail.com](mailto:ashutoshdubey9794@gmail.com)  
- 🌐 [Portfolio](https://oneashutoshdubey.co/)  
- 🔗 [LinkedIn](https://linkedin.com/in/ashutoshdubey10)

