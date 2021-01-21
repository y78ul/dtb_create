import sys
import getopt
from parsers.fcc_file_parser import FccFileParser
from parsers.crtc_reader import CrtcFileParser
from parsers.text_file_parser import TextFileParser
from parsers.dtb import DTB


def lets_rumble(argv):
    USAGE = 'main.py -f <input fcc-file> -c <input crtc-file> -t <input text-file> -d <output file>'
    fcc_file = ''
    crtc_file = ''
    text_file = ''
    dtb_output_file = ''
    scp_output_file = ''
    try:
        opts, args = getopt.getopt(argv, 'f:c:t:d:s:', ['fcc=', 'crtc=', 'text=', 'dtb=', 'scp='])
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-f', '--fcc'):
            fcc_file = arg
        elif opt in ('-c', '--crtc'):
            crtc_file = arg
        elif opt in ('-t', '--text'):
            text_file = arg
        elif opt in ('-d', '--dtb'):
            dtb_output_file = arg
        elif opt in ('-s', '--scp'):
            scp_output_file = arg

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
    lets_rumble(sys.argv[1:])
