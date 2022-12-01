# Helpers from Professor Lundeen

    def to_byte_array_string(self):
        """
        Print version.
        """
        message = self._version + self._services + self._timestamp + self._addr_recv_services + self._addr_recv_ip_address + self._addr_recv_port + self._addr_trans_services + self._addr_trans_ip_address + self._addr_trans_port + self._nonce + self._user_agent_bytes + self._user_agent_string + self._start_height + self._relay
        return message

    def version(self):
        """
        Returns the version in ascii.
        """
        number = self.unmarshal_int(self._version)
        return number

    def set_version(self, version):
        """
        Converts the version integer to an usigned array of bytes, then stores the array of bytes.
        """
        int_version = int(version)
        self._version = self.uint8_t(int_version)

    def services(self):
        """
        Returns the services in ascii.
        """
        return self.unmarshal_uint(self._services)

    def set_services(self, services):
        """
        Converts the services integer to an array of bytes, then stores the array of bytes.
        """
        self._services = self.uint8_t(services)

    def timestamp(self):
        """
        Returns the timestamp in ascii.
        """
        return self.unmarshal_uint(self._timestamp)

    def set_timestamp(self, timestamp):
        """
        Converts the timestamp integer to an array of bytes, then stores the array of bytes.
        """
        self._timestamp = self.uint8_t(timestamp)

    def addr_recv_services(self):
        """
        Returns the addr_recv_services in ascii.
        """
        return self.unmarshal_uint(self._addr_recv_services)

    def set_addr_recv_services(self, addr_recv_services):
        """
        Converts the addr_recv_services integer to an array of bytes, then stores the array of bytes.
        """
        self._addr_recv_services = self.uint8_t(addr_recv_services)

    def addr_trans_services(self):
        """
        Returns the addr_trans_services in ascii.
        """
        return self.unmarshal_uint(self._addr_trans_services)

    def set_addr_trans_services(self, addr_trans_services):
        """
        Converts the addr_trans_services integer to an array of bytes, then stores the array of bytes.
        """
        self._addr_trans_services = self.uint8_t(addr_trans_services)

    def nonce(self):
        """
        Returns the nonce in ascii.
        """
        return self.unmarshal_uint(self._nonce)

    def set_nonce(self, nonce):
        """
        Converts the nonces integer to an array of bytes, then stores the array of bytes.
        """
        self._nonce = self.uint8_t(nonce)

    def addr_recv_ip_address(self):
        """
        Returns the addr_recv_ip_address in ascii.
        """
        # return self.unmarshal_uint(self._addr_recv_ip_address)
        return ipaddress.IPv4Address(self._addr_recv_ip_address)

    def set_addr_recv_ip_address(self, addr_recv_ip_address):
        """
        Converts the addr_recv_ip_address integer to an array of
        bytes, then stores the array of bytes.
        """
        receive_ip_in_bytes = ipaddress.IPv4Address(addr_recv_ip_address).packed
        # my_bytes = self.uint16_t(addr_recv_ip_address)
        self._addr_recv_ip_address = receive_ip_in_bytes

    def addr_trans_ip_address(self):
        """
        Returns the addr_trans_ip_address in ascii.
        """
        return self.unmarshal_uint(self._addr_trans_ip_address)

    def set_addr_trans_ip_address(self, addr_trans_ip_address):
        """
        Converts the addr_trans_ip_address integer to an array
        of bytes, then stores the array of bytes.
        """
        self._addr_trans_ip_address = self.uint16_t(addr_trans_ip_address)

    def addr_recv_port(self):
        """
        Returns the addr_recv_port in ascii.
        """
        return self.unmarshal_uint(self._addr_recv_port)

    def set_addr_recv_port(self, addr_recv_port):
        """
        Converts the addr_recv_port integer to an array of bytes, then stores the array of bytes.
        """
        self._addr_recv_port = self.uint8_t(addr_recv_port)

    def addr_trans_port(self):
        """
        Returns the addr_trans_port in ascii.
        """
        return self.unmarshal_uint(self._addr_trans_port)

    def set_addr_trans_port(self, addr_trans_port):
        """
        Converts the addr_trans_port integer to an array of bytes, then stores the array of bytes.
        """
        self._addr_trans_port = self.uint8_t(addr_trans_port)

    def start_height(self):
        """
        Returns the start_height in ascii.
        """
        return self.unmarshal_uint(self._start_height)

    def set_start_height(self, start_height):
        """
        Converts the start_height integer to an array of bytes, then stores the array of bytes.
        """
        self._start_height = self.uint8_t(start_height)

    def relay(self):
        """
        Returns the relay in ascii.
        """
        return self.unmarshal_uint(self._relay)

    def set_relay(self, relay):
        """
        Converts the relay integer to an array of bytes, then stores the array of bytes.
        """
        self._relay = self.uint8_t(relay)

    def user_agent_bytes(self):
        """
        Returns the user_agent_bytes in ascii.
        """
        return self.unmarshal_uint(self._user_agent_bytes)

    def set_user_agent_bytes(self, user_agent_bytes):
        """
        Converts the user_agent_bytes integer to an array of bytes, then stores the array of bytes.
        """
        self._user_agent_bytes = self.uint8_t(user_agent_bytes)

    def user_agent_string(self):
        """
        Returns the user_agent_string in ascii.
        """
        return self.unmarshal_uint(self._user_agent_string)

    def set_user_agent_string(self, user_agent_string):
        """
        Converts the user_agent_string integer to an array of bytes, then stores the array of bytes.
        """
        # TODO Make sure we are using appropriate size.
        self._user_agent_string = self.uint8_t(user_agent_string)

    # def replaceme(self):
    #     """
    #     Returns the replaceme in ascii.
    #     """
    #     return self.replaceme

    # def set_replaceme(self, replaceme):
    #     """
    #     Converts the replaceme integer to an array of bytes, then stores the array of bytes.
    #     """
    #     self.replaceme = self.uint8_t(replaceme)

    def compactsize_t(self, n):
        """
        placeholder
        """
        if n < 252:
            return self.uint8_t(n)
        if n < 0xffff:
            return self.uint8_t(0xfd) + self.uint16_t(n)
        if n < 0xffffffff:
            return self.uint8_t(0xfe) + self.uint32_t(n)
        return self.uint8_t(0xff) + self.uint64_t(n)

    def unmarshal_compactsize(self, b):
        """
        placeholder
        """
        key = b[0]
        if key == 0xff:
            return b[0:9], self.unmarshal_uint(b[1:9])
        if key == 0xfe:
            return b[0:5], self.unmarshal_uint(b[1:5])
        if key == 0xfd:
            return b[0:3], self.unmarshal_uint(b[1:3])
        return b[0:1], self.unmarshal_uint(b[0:1])

    def bool_t(self, flag):
        """
        Returns an 8-bit unsigned integer of the boolean.
        """
        return self.uint8_t(1 if flag else 0)

    def ipv6_from_ipv4(self, ipv4_str):
        """
        Converts an IPv4 address to IPv6.
        """
        pchIPv4 = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xff, 0xff])
        return pchIPv4 + bytearray((int(x) for x in ipv4_str.split('.')))

    def ipv6_to_ipv4(self, ipv6):
        """
        Converts an IPv6 address to IPv4.
        """
        return '.'.join([str(b) for b in ipv6[12:]])

    def uint8_t(self, n):
        """
        Returns an array of bytes representing the integer. The
        array of bytes is unsigned and the order is in little
        endian, the most significant byte is at the end.
        """
        return int(n).to_bytes(1, byteorder='little', signed=False)

    def uint16_t(self, n):
        """
        Returns an array of bytes representing the integer. The
        array of bytes is unsigned and the order is in little
        endian, the most significant byte is at the end.
        """
        return int(n).to_bytes(2, byteorder='little', signed=False)

    def int32_t(self, n):
        """
        Returns an array of bytes representing the integer. The 
        array of bytes is signed and the order is in little endian,
        the most significant byte is at the end.
        """
        return int(n).to_bytes(4, byteorder='little', signed=True)

    def uint32_t(self, n):
        """
        Returns an array of bytes representing the integer. The
        array of bytes is unsigned and the order is in little
        endian, the most significant byte is at the end.
        """
        return int(n).to_bytes(4, byteorder='little', signed=False)

    def int64_t(self, n):
        """
        Returns an array of bytes representing the integer. The 
        array of bytes is signed and the order is in little endian,
        the most significant byte is at the end.
        """
        return int(n).to_bytes(8, byteorder='little', signed=True)

    def uint64_t(self, n):
        """
        Returns an array of bytes representing the integer. The
        array of bytes is unsigned and the order is in little
        endian, the most significant byte is at the end.
        """
        return int(n).to_bytes(8, byteorder='little', signed=False)

    def unmarshal_int(self, b):
        """
        Returns the integer version of the byte array. The byte array
        is signed and the order is in little endian, the most
        significant byte is at the end.
        """
        return int.from_bytes(b, byteorder='little', signed=True)

    def unmarshal_uint(self, b):
        """
        Returns the integer version of an array of bytes. The byte array
        is unsigned and the order is in little endian, the most
        significant byte is at the end.
        """
        return int.from_bytes(b, byteorder='little', signed=False)
