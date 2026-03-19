🔐 get_jwt_secret.py

A fast, multi-threaded JWT secret brute-force tool designed for penetration testers, red teamers, and bug bounty hunters.

This tool attempts to recover the secret used to sign HMAC-based JWT tokens (HS256, HS384, HS512) using a wordlist attack.

⚡ Features

🚀 Multi-threaded brute forcing

🧠 Automatic JWT algorithm detection

📂 Custom wordlist support

🔇 Clean output (warnings suppressed)

🎯 Early stop on success (optimized performance)

🛠️ Simple and easy CLI usage

🧪 Use Cases

JWT security testing

Weak secret detection

Bug bounty assessments

Red team engagements

CTF challenges

📦 Installation
git clone https://github.com/yourusername/get_jwt_secret.git
cd get_jwt_secret
pip install pyjwt
🚀 Usage
python3 get_jwt_secret.py <JWT_TOKEN> <WORDLIST> -t <THREADS>
Example
python3 get_jwt_secret.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... jwt.secrets.list -t 20
⚙️ Arguments
Argument	Description
token	Target JWT token
wordlist	Path to wordlist file
-t, --threads	Number of threads (default: 10)
-v, --verbose	Show failed attempts
📂 Default Wordlist

The default wordlist included:

jwt.secrets.list

You can replace it with any custom wordlist (e.g., from SecLists or Metasploit).

🧠 How It Works

Extracts JWT header and detects algorithm

Loads secrets from wordlist

Attempts decoding using each secret

Stops immediately when a valid secret is found

⚠️ Disclaimer

This tool is intended for:

Authorized penetration testing

Educational purposes

Security research

Do not use this tool against systems you do not own or have explicit permission to test.

👨‍💻 Author

Maimo Harris

🔗 LinkedIn: https://linkedin.com/in/maimoharris

📱 WhatsApp: +237680226898

⭐ Support

If you find this tool useful:

⭐ Star the repository

🍴 Fork it

🧠 Contribute improvements

🚀 Future Improvements

Multiprocessing support (true CPU scaling)

Progress bar & performance metrics

Wordlist mutation engine

Output logging

GPU acceleration integration

🏁 Final Note

Weak JWT secrets are still one of the most common and dangerous misconfigurations in modern applications.

Test responsibly. Hack ethically.
