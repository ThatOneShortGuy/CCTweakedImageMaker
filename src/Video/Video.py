from typing import BinaryIO, Iterable, Optional

from tqdm import tqdm

from .ColorInformation import ColorInformation
from .Compression import compress
from .Frame import Frame
from .FrameData import FrameData
from .Header import Header


class Video:
    def __init__(self, header: Header, frames: Iterable[Frame]):
        self.header = header
        self.frames = frames
        self._previous_frame = Frame(ColorInformation.default(), FrameData.default_from_size(header.width, header.height))

    def write_to(self, file: BinaryIO, num_frames: Optional[int] = None):
        file.write(self.header.serialize())
        for frame in tqdm(self.frames, unit='frames', total=num_frames):
            file.write(frame.color_information.serialize())
            data = compress(self._previous_frame.frame_data.serialize(), frame.frame_data.serialize())
            file.write(data)
            self._previous_frame = frame