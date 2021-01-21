from parsers.file_parser import FileParser


class FccFileParser(FileParser):
    def _parse(self):
        CALLSIGN_INDEX = 4
        LOCATION_INDEX = 17
        with open(self._file_name) as f:
            for line in f:
                lst = line.split('|')
                self.dtb.add_item(lst[CALLSIGN_INDEX], lst[LOCATION_INDEX])
        return True
