import pandas
import requests

class VPNGateManager:
    def __init__(self):
        self.server_api = "https://www.vpngate.net/api/iphone/"
        self.file_name = "vpnGate_servers.csv"
        self.get_csv_list()
        self.servers_dict = self.create_server_dictionary()

    def get_csv_list(self):

        try:
            print("Getting csv list from api...")
            response = requests.get(self.server_api)

            response = response.text[15:]
            with open(self.file_name, "w") as f:
                f.write(response)
        except Exception as e:
            print(f"Error while downloading csv --- {e}")

    def create_server_dictionary(self):

        try:

            print("Creating servers dictionary...")

            servers_df = pandas.read_csv(self.file_name)

            return servers_df[["HostName", "IP", "OpenVPN_ConfigData_Base64", "CountryLong", "Message"]].to_dict(orient="records")

        except Exception as e:
            print(f"Error while reading {self.file_name} --- {e}")

            return {}
