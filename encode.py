import sys
from VideoReader import VideoReader
from typing import Optional

HELP_MESSAGE = """
Usage: python encode.py -i <input_file> [-w <width>] [-h <height>] [-f <fps>] output_file

Options:
    -i <input_file>     Input video file path
    -w <width>          Number of ComputerCraft monitors in width (default: 8)
    -h <height>         Number of ComputerCraft monitors in height (default: 6)
    -f <fps>            Output video frame rate (default: match input)
    output_file         Output file path
"""

def main(filename: str, output_width: int, output_height: int, output_file: str, framerate: Optional[float] = None):
    with VideoReader(filename)as reader, open(output_file, 'wb') as output:
        output.write(reader.get_video().serialize())

if __name__ == '__main__':
    args = sys.argv[1:]
    filename = ''
    width = 8
    height = 6
    fps: Optional[float] = None
    output_file = ""

    while args:
        arg = args.pop(0)
        if arg == '-i':
            filename = args.pop(0)
        elif arg == '-w':
            width = int(args.pop(0))
        elif arg == '-h':
            height = int(args.pop(0))
        elif arg == '-f':
            fps = float(args.pop(0))
        elif arg in ('-h', '--help'):
            print(HELP_MESSAGE)
            sys.exit(0)
        else:
            if not output_file:
                output_file = arg
            else:
                print(HELP_MESSAGE)
                sys.exit(1)
    
    if not filename:
        print(f"Error: Input file is not specified.\n{HELP_MESSAGE}")
        sys.exit(1)

    main(filename, width, height, output_file, fps)
