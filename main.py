# from parsers.fcc_file_parser import FccFileParser
# from parsers.crtc_reader import CrtcFileParser
from parsers.text_file_parser import TextFileParser
from parsers.dtb import DTB

if __name__ == '__main__':
    # fcc_parser = FccFileParser(r'D:\DPR\DTBCreate\2021\ARRL\Full\EN.dat')
    # crtc_parser = CrtcFileParser(r'D:\DPR\DTBCreate\2021\ARRL\Full\amateur.txt')
    # writer = DTB()
    # writer.add_list(fcc_parser.dtb)
    # writer.add_list(crtc_parser.dtb)
    # writer.write_dtb(r'D:\DPR\DTBCreate\2021\ARRL\Full\ARRL-USVE.dtb')
    # writer.write_scp(r'D:\DPR\DTBCreate\2021\ARRL\Full\MASTER.scp')
    text_parser = TextFileParser(r'V:\FRANK\DPR\DTBCreate\2021\ARRL\Trimmed\CQ-160-CW_STN1@P40AA.prn')
    writer = DTB()
    writer.add_list(text_parser.dtb)
    writer.write_dtb(r'V:\FRANK\temp\ARRL-USVE.dtb')
