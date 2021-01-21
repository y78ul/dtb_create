from parsers.file_parser import FileParser


class CrtcFileParser(FileParser):
    def _parse(self):
        CALLSIGN_START_POS = 0
        CALLSIGN_END_POS = 6
        LOCATION_START_POS = 186
        LOCATION_END_POS = 188
        ALTERNATIVE_LOCATION_START_POS = 459
        ALTERNATIVE_LOCATION_END_POS = 461

        with open(self._file_name, 'rt', encoding='latin1') as f:
            for line in f:
                if len(line) < (LOCATION_END_POS + 1):
                    continue

                callsign = line[CALLSIGN_START_POS:CALLSIGN_END_POS].strip()
                location = line[LOCATION_START_POS:LOCATION_END_POS].strip()
                if not location and len(line) >= ALTERNATIVE_LOCATION_END_POS+1:
                    location = line[ALTERNATIVE_LOCATION_START_POS:ALTERNATIVE_LOCATION_END_POS].strip()

                # Special treatment for NL and VO1/VO2:
                # 	Treat VO1 in NL as NF
                # 	Treat VO2 in NL as LB"""
                if location == 'NL':
                    if callsign.startswith('VO1'):
                        location = 'NF'
                    elif callsign.startswith('VO2'):
                        location = 'LB'

                self.dtb.add_item(callsign, location)
        return True
