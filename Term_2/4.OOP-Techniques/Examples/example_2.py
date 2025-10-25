class WirelessDevice:
    def __init__(self, mac_address):
        self.__mac_address = mac_address

    def get_mac_address(self): return self.__mac_address

class Laptop(WirelessDevice):
    def __init__(self,
                 mac_address,
                 has_wired_connection):
        # call superclass constructor
        super().__init__(mac_address)
        self.has_wired_connection = has_wired_connection;

lenovo = Laptop('nfsdnfbdsn', False)
print(lenovo.get_mac_address())