import asyncio

class ServerController:
    def __init__(self, servers):
        self.servers = servers
        self.tcp_port = 443
        self.udp_port = 443
        self.available_servers = []


    async def server_connect(self, server):

        try:
            reader, writer = await asyncio.open_connection(server['IP'], self.tcp_port)
            print(f"Successfully connected to {server['IP']} --- {server['CountryLong']}")
            writer.close()
            await writer.wait_closed()
            self.available_servers.append(server)
            return True
        except Exception as e:
            print(f"Error while connecting to {server['IP']} {server['CountryLong']} --- {e}")
            return False

    async def check_servers(self):
        await asyncio.gather(*(self.server_connect(server) for server in self.servers))


    def run_check(self):
        print("Running server checks...")
        asyncio.run(self.check_servers())
        return self.available_servers
