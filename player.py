import sys

from src.Video import Frame, Header
from src.Video.FrameData import default_from_size

filename = "sample.ccv"

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, 'rb') as f:
    header = Header.read_from(f)
    previous_frame_data = default_from_size(header.width, header.height)
    while True:
        if f.peek(1) == b'':
            break
        frame = Frame.read_from(f, header.width, header.height, previous_frame_data.pixels.tobytes())
        frame.display('Video', header.width, header.height)
        previous_frame_data = frame.frame_data
    Frame.close_display()