import base64
import subprocess
import os

class OpenVPNManager:
    def __init__(self, servers):
        self.servers = servers
        self.decode_openvpn_config()

    def decode_openvpn_config(self):
        if not os.path.isdir("open_vpn_configs"):
            os.mkdir("open_vpn_configs")
        print("Decoding OpenVPN Config Data...")
        for server in self.servers:
            decoded = base64.b64decode(server['OpenVPN_ConfigData_Base64']).decode('utf-8')
            server['OpenVPN_ConfigData_Base64'] = decoded
            with open(f"open_vpn_configs/{server['IP']}.ovpn", "w") as f:
                f.write(decoded)

    def connect(self):
        do_connect = True
        index = 0

        while do_connect and index < len(self.servers):
            current_server = self.servers[index]
            config_path = os.path.abspath(f"open_vpn_configs/{current_server['IP']}.ovpn")
            print(f"\nConnecting to {current_server['IP']}...")

            try:
                proc = subprocess.Popen(
                    ["sudo", "openvpn", "--config", config_path, "--data-ciphers", "AES-128-CBC"]
                )

                print("VPN started. Press Ctrl+C to disconnect.")

                proc.wait()

            except KeyboardInterrupt:
                print("\nVPN disconnected by user (Ctrl+C).")
                proc.terminate()
                proc.wait()
            except Exception as e:
                print(f"Unexpected error: {e}")

            user_input = input("\nDo you want to try a different server? (y/n): ").strip().lower()
            if user_input == "y":
                index += 1
            else:
                do_connect = False