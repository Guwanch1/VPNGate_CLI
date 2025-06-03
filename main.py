from base.vpngateManager import VPNGateManager
from base.serverController import ServerController
from base.openVPNManager import OpenVPNManager

vpnGate_manager = VPNGateManager()
server_controller = ServerController(vpnGate_manager.servers_dict)
openVPN_manager = OpenVPNManager(server_controller.run_check())

openVPN_manager.connect()
