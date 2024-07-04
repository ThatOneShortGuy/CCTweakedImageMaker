import sys
from src.VideoReader import VideoReader
from typing import Optional
from src.Video import Header

from src.compute import get_output_width, get_output_height

DEBUG = bool(sys.gettrace())

HELP_MESSAGE = """
Usage: python encode.py -i <input_file> [-w <width>] [-h <height>] [-f <fps>] output_file

Options:
    -i <input_file>     Input video file path
    -w <width>          Number of ComputerCraft monitors in width (default: 1)
    -h <height>         Number of ComputerCraft monitors in height (default: 1)
    -f <fps>            Output video frame rate (default: match input)
    output_file         Output file path
"""

def main(filename: str, monitor_width: int, monitor_height: int, output_file: str, framerate: Optional[float] = None):
    output_width = get_output_width(monitor_width)
    output_height = get_output_height(monitor_height)

    with VideoReader(filename, output_width, output_height) as reader, open(output_file, 'wb') as output:
        if framerate is None:
            framerate = reader.get_framerate()
        header = Header(1, output_width, output_height, framerate)
        reader.get_video_from_header(header).write_to(output, reader.get_num_frames())

if __name__ == '__main__':
    if DEBUG:
        sys.argv.extend(["-i", "sample.mp4", "sample.ccv"])
    args = sys.argv[1:]
    filename = ''
    width = 1
    height = 1
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
                print(HELP_MESSAGE, file=sys.stderr)
                sys.exit(1)
    
    if not filename:
        print(f"Error: Input file is not specified.\n{HELP_MESSAGE}", file=sys.stderr)
        sys.exit(1)
    
    if not output_file:
        print(f"Error: Output file is not specified.\n{HELP_MESSAGE}", file=sys.stderr)
        sys.exit(1)

    main(filename, width, height, output_file, fps)
