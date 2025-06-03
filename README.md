# VPNGate CLI

> A lightweight Python command-line client to connect to free VPN servers from [VPNGate.net](https://www.vpngate.net) using OpenVPN.

---

## 🚀 Features

- Fetch the latest VPN server list directly from the official VPNGate API  
- Asynchronously check server availability for faster results  
- Automatically decode and save OpenVPN configuration files  
- Connect to VPN servers using OpenVPN with an interactive prompt  
- Easily switch between multiple VPN servers  

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:Guwanch1/VPNGate_CLI.git
   cd VPNGate_CLI

2. **(Optional) Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
   
## ⚙️ Usage

1. **Run the main script**
    ```bash
    python main.py
   
**Note: Make sure you have OpenVPN installed on your system and that the openvpn command is available in your PATH. This is required for the client to connect to VPN servers.**

