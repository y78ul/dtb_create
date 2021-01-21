class DtbItem:
    def __init__(self, callsign, location):
        self.callsign = callsign
        self.location = location

    def __repr__(self):
        return 'callsign={}, location={}'.format(self.callsign, self.location)


class DTB:
    def __init__(self):
        self.items = []

    def add_item(self, callsign, location):
        self.items.append(DtbItem(callsign, location))

    def add_list(self, dtb_items):
        self.items.extend(dtb_items.items)

    def write_dtb(self, file_name):
        with open(file_name, 'wb') as f:
            for item in self.items:
                s = bytearray(26)
                for i, c in enumerate(item.callsign):
                    s[i] = ord(c)
                for i, c in enumerate(item.location):
                    s[i+14] = ord(c)
                f.write(s)

    def write_scp(self, file_name):
        with open(file_name, 'wt') as f:
            for item in self.items:
                f.write('{}\n'.format(item.callsign))
