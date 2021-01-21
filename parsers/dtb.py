class DtbItem:
    def __init__(self, callsign, location):
        self.__callsign = callsign
        self.__location = location

    def __repr__(self):
        return 'callsign={}, location={}'.format(self.__callsign, self.__location)

    def __get_callsign(self):
        return self.__callsign

    def __get_location(self):
        return self.__location

    callsign = property(__get_callsign)
    location = property(__get_location)


class DTB:
    """ Container for DtbItems list and write methods to save it to DTB and SCP files. """
    def __init__(self):
        self.__items = []

    def add_item(self, callsign, location):
        self.__items.append(DtbItem(callsign, location))

    def add_list(self, dtb):
        self.__items.extend(dtb.items)

    def write_dtb(self, file_name):
        with open(file_name, 'wb') as f:
            for item in self.__items:
                s = bytearray(26)
                for i, c in enumerate(item.callsign):
                    s[i] = ord(c)
                for i, c in enumerate(item.location):
                    s[i+14] = ord(c)
                f.write(s)

    def write_scp(self, file_name):
        with open(file_name, 'wt') as f:
            for item in self.__items:
                f.write('{}\n'.format(item.callsign))

    def __get_items(self):
        return self.__items

    items = property(__get_items)
