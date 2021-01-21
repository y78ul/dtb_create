from parsers.file_parser import FileParser


class TextFileParser(FileParser):
    def _parse(self):
        CALLSIGN_INDEX = 0
        LOCATION_INDEX = 1
        with open(self._file_name) as f:
            for line in f:
                lst = line.split()
                self.dtb.add_item(lst[CALLSIGN_INDEX].strip(), lst[LOCATION_INDEX].strip())
        return True
