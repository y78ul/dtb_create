import sys
import getopt

from parsers.fcc_file_parser import FccFileParser
from parsers.crtc_reader import CrtcFileParser
from parsers.text_file_parser import TextFileParser
from parsers.dtb import DTB


def lets_rumble(argv):
    USAGE = 'main.py -f <input fcc-file> -c <input crtc-file> -t <input text-file> -d <DTB output file> ' \
            '-s <SCP output file>'
    fcc_file = ''
    crtc_file = ''
    text_file = ''
    dtb_output_file = ''
    scp_output_file = ''
    opts = None
    try:
        opts, args = getopt.getopt(argv, 'f:c:t:d:s:', ['fcc=', 'crtc=', 'text=', 'dtb=', 'scp='])
    except getopt.GetoptError:
        pass
    if not opts:
        print(USAGE)
        sys.exit(2)

    for opt, arg in opts:
        match opt:
            case '-f' | '--fcc': fcc_file = arg
            case '-c' | '--crtc': crtc_file = arg
            case '-t' | '--text': text_file = arg
            case '-d' | '--dtb': dtb_output_file = arg
            case '-s' | '--scp': scp_output_file = arg

    print(f'FCC input file = {fcc_file}')
    print(f'CRTC input file = {crtc_file}')
    print(f'Text input file = {text_file}')
    print(f'DTB output file = {dtb_output_file}')
    print(f'SCP output file = {scp_output_file}')

    dtb = DTB()
    # Read the input files
    if fcc_file:
        dtb.add_list(FccFileParser(fcc_file).dtb)
    if crtc_file:
        dtb.add_list(CrtcFileParser(crtc_file).dtb)
    if text_file:
        dtb.add_list(TextFileParser(text_file).dtb)

    # Write the output files
    if len(dtb.items) == 0:
        print('Nothing to write...')
    else:
        if dtb_output_file:
            dtb.write_dtb(dtb_output_file)
        if scp_output_file:
            dtb.write_scp(scp_output_file)


if __name__ == '__main__':
    # Args example: --fcc C:\EN.dat --crtc C:\amateur.txt --dtb C:\ARRL-USVE.dtb --scp C:\Master.scp
    lets_rumble(sys.argv[1:])
