from parsers.dtb import DTB
from parsers.file_parser import FileParser


class DtbFileParser(FileParser):
    def _parse(self):
        CALLSIGN_INDEX = 0
        LOCATION_INDEX = 14
        with open(self._file_name) as f:
            while True:
                s = f.read(26)
                if not s:
                    break
                callsign = s[CALLSIGN_INDEX:LOCATION_INDEX-1].strip('\x00')
                location = s[LOCATION_INDEX:25].strip('\x00')
                self.dtb.add_item(callsign, location)

        # print(f'first item: {self.dtb.items[0]}')
        # print(f'last item: {self.dtb.items[len(self.dtb.items)-1]}')
        return True


def merge_dtb_files(filename_x, filename_y):
    merged_dtb = DTB()
    file_x = DtbFileParser(filename_x)
    file_y = DtbFileParser(filename_y)

    # Step 1: Check all items from file x for availability in file y. If available, use the location from file y.
    # If not, use the location from file x.
    for x_item in file_x.dtb.items:
        y_found = False
        for y_item in file_y.dtb.items:
            if x_item.callsign == y_item.callsign:
                # debug
                if x_item.location != y_item.location:
                    print(f'{x_item.callsign} old DOK: {x_item.location}, new DOK: {y_item.location}')
                # end debug
                merged_dtb.add_item(y_item.callsign, y_item.location)
                y_found = True
                break
        if not y_found:
            merged_dtb.add_item(x_item.callsign, x_item.location)

    # Step 2: Check if all callsigns from file y are available in the merged DTB, add new ones.
    for y_item in file_y.dtb.items:
        merged_found = False
        for merged_item in merged_dtb.items:
            if y_item.callsign == merged_item.callsign:
                merged_found = True
                break
        if not merged_found:
            # debug
            print(f'New y item: {y_item.callsign} {y_item.location}')
            # end debug
            merged_dtb.add_item(y_item.callsign, y_item.location)

    return merged_dtb