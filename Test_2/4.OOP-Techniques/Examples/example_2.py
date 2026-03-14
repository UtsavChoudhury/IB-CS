class WirelessDevice:
    def __init__(self, mac_address):
        self.__mac_address = mac_address

    def get_mac_address(self): return self.__mac_address

class Laptop(WirelessDevice):
    def __init__(self,
                 mac_address,
                 has_wired_connection):
        # call superclass constructor
        super().__init__(mac_address) # This passes the mac_address into the base class WirelessDevice which leads to initialisation in the base class.
        self.has_wired_connection = has_wired_connection

lenovo = Laptop('nfsdnfbdsn', False) # This creates a laptop with this mac_address. It is passed into the WirelessDevice superclass and stored as a private variable.
print(lenovo.get_mac_address()) # Now we can access it from the superclass.
print(lenovo.__mac_address) # THIS WILL FAIL BECAUSE IT IS PRIVATE