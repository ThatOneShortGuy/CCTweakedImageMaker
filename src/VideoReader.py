from typing import Optional

import cv2 as cv

from .Video import Frame, Header, Video


class VideoReader:
    def __init__(self, filepath: str, output_width: int, output_height: int):
        self.filepath = filepath
        self.output_width = output_width
        self.output_height = output_height
        self._cap: Optional[cv.VideoCapture] = None

    def __iter__(self):
        return self
    
    def __next__(self) -> Frame:
        if self._cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        ret, frame = self._cap.read()
        if not ret:
            raise StopIteration
        frame = cv.resize(frame, (self.output_width, self.output_height))
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        return Frame.from_ndarray(frame) # type: ignore
    
    def __enter__(self):
        self._cap = cv.VideoCapture(self.filepath)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self._cap:
            self._cap.release()
    
    def get_dimensions(self):
        if self._cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        width = int(self._cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(self._cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        return width, height
    
    def get_framerate(self):
        if self._cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        return self._cap.get(cv.CAP_PROP_FPS)
    
    def get_num_frames(self):
        if self._cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        return int(self._cap.get(cv.CAP_PROP_FRAME_COUNT))
    
    def get_video_from_header(self, header: Header) -> Video:
        return Video(header, self)