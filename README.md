OSINT & Web Security Toolkit

TELE-OSINT-11 is a Python-based cybersecurity toolkit developed as an academic/internship project for exploring Open-Source Intelligence (OSINT), network reconnaissance, web security testing, and information gathering.

The project brings multiple security and reconnaissance utilities together under a single command-line interface.

🚀 Features
OSINT
Phone number information lookup
Email information and breach checking
MAC address vendor lookup
IP geolocation
Multiple IP analysis and heatmap generation
Image metadata / EXIF analysis
Username-based information gathering
Web Reconnaissance
Reverse IP lookup
DNS lookup
Subdomain enumeration
CMS detection
Port scanning
Host availability checking
Web Security Testing
Clickjacking header checks
CORS configuration testing
Host Header Injection checks
SSH/FTP security testing
🛠️ Technologies Used
Python
Requests
BeautifulSoup
Pillow
Paramiko
Python-Nmap
Pyrogram
TextBlob
Tweepy
GMPlot
Various OSINT and security APIs
📂 Project Structure
JP2K26/
│
├── cosint.py
├── EmailScan.py
├── maclookup.py
├── metadata.py
├── multipleip.py
├── phonenum.py
├── reverseimg.py
├── sentinment.py
├── username.py
├── web.py
├── requirements.txt
│
├── src/
│   └── api.py
│
├── webosint/
│   ├── cmsdetect.py
│   ├── nslookup.py
│   ├── portscan.py
│   ├── reverseip.py
│   └── subdomain.py
│
└── webvuln/
    ├── bruteforce.py
    ├── clickjacking.py
    ├── cors.py
    └── hostheader.py
⚙️ Installation

Clone the repository:

git clone <YOUR-GITHUB-REPOSITORY-URL>
cd JP2K26

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Activate it on Linux/macOS:

source venv/bin/activate

Install the dependencies:

pip install -r requirements.txt
🔑 API Configuration

Some features require third-party API credentials.

Do not place API keys directly inside Python source files.

Configure credentials through environment variables or a local .env file that is excluded from Git.

Example:

IPSTACK_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
RAPIDAPI_KEY=your_key_here
MACVENDORS_API_KEY=your_key_here

Refer to the source code for the environment variables required by each module.

▶️ Usage

Run the main program:

python cosint.py

The interactive menu provides access to the available OSINT and web-security modules.

⚠️ Disclaimer

This project is intended for educational, research, and authorized security-testing purposes only.

Only use the reconnaissance and security-testing functionality against systems, domains, accounts, or data that you own or have explicit permission to assess.

The author is not responsible for misuse of this software or for any damage caused by unauthorized testing.

📌 Project Status

This project was developed as a learning-focused cybersecurity toolkit. Some modules depend on external APIs and third-party services, and their availability or behavior may change over time.

Future improvements may include:

Better error handling
Modern API integrations
Environment-based configuration
Improved CLI design
Modular configuration management
Automated testing
Better documentation
Additional reconnaissance modules
👨‍💻 Author

Sohail Siddiqui

Cybersecurity | SOC | DFIR | OSINT | Python
