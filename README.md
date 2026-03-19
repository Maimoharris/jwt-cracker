# 🔐 JWT-Secret Cracker

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Purpose](https://img.shields.io/badge/purpose-Penetration%20Testing-red.svg)

A high-performance, multi-threaded JWT secret brute-force tool designed for **penetration testers**, **red teamers**, and **bug bounty hunters**. 

This tool attempts to recover the secret key used to sign HMAC-based JWT tokens (**HS256, HS384, HS512**) using an optimized wordlist attack.

---

## ⚡ Features

* 🚀 **Multi-threaded:** Fast execution with customizable thread counts.
* 🧠 **Auto-Detection:** Automatically identifies the JWT algorithm from the header.
* 📂 **Custom Wordlists:** Support for any external dictionary (SecLists, RockYou, etc.).
* 🔇 **Clean UI:** Suppresses unnecessary warnings for a focused output.
* 🎯 **Optimized:** Implements early-exit logic—stops immediately upon discovery.
* 🛠️ **CLI Friendly:** Simple syntax for quick integration into your workflow.

---

## 🧪 Use Cases

* **Security Audits:** Identifying weak or default signing keys.
* **Bug Bounties:** Testing for JWT misconfigurations in web apps.
* **CTF Challenges:** Quickly cracking HMAC tokens in competitive environments.
* **Red Teaming:** Escalating privileges via token manipulation.

---

## 📦 Installation

```bash
# Clone the repository
git clone [https://github.com/yourusername/get_jwt_secret.git](https://github.com/yourusername/get_jwt_secret.git)

# Navigate to the directory
cd get_jwt_secret

# Install dependencies
pip install pyjwt

🚀 Usage
Bash

python3 get_jwt_secret.py <JWT_TOKEN> <WORDLIST> -t <THREADS>

Example
Bash

python3 get_jwt_secret.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... jwt.secrets.list -t 20

⚙️ Arguments
Argument	Description
token	The target JWT token string
wordlist	Path to your secret wordlist file
-t, --threads	Number of concurrent threads (Default: 10)
-v, --verbose	Enable to show failed attempts (useful for debugging)
🧠 How It Works

    Parsing: Extracts the JWT header to determine the hashing algorithm (HS256, HS384, or HS512).

    Loading: Efficiently streams the wordlist into the threading engine to minimize memory overhead.

    Validation: Attempts to decode the token using each secret from the wordlist.

    Success: If a secret matches, it is printed to the console and the process terminates immediately.

🚀 Future Roadmap

    [ ] Multiprocessing Support: Utilizing true CPU scaling for massive wordlists.

    [ ] Progress Bar: Real-time ETA and performance metrics.

    [ ] Mutation Engine: On-the-fly wordlist variations (e.g., adding numbers/years).

    [ ] GPU Acceleration: Integration for high-speed cracking.

👨‍💻 Author

Maimo Harris

    LinkedIn: maimoharris

    WhatsApp: +237 680 226 898

⚠️ Disclaimer

This tool is intended for authorized penetration testing and educational purposes only. Do not use this tool against systems you do not own or have explicit, written permission to test. The author is not responsible for any misuse or damage caused by this tool.
⭐ Support

If this tool helped you find a bug or win a CTF, please consider giving it a Star and forking the repo!
