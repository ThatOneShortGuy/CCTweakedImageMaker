import cv2 as cv
from typing import Optional
from Video import Frame, Header
from Video import Video

class VideoReader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._cap: Optional[cv.VideoCapture] = None

    def __iter__(self):
        return self
    
    def __next__(self) -> Frame:
        if self._cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        ret, frame = self._cap.read()
        if not ret:
            raise StopIteration
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
    
    def get_header(self) -> Header:
        w, h = self.get_dimensions()
        fps = self.get_framerate()
        return Header(0, w, h, fps)
    
    def get_video(self) -> Video:
        return Video(self.get_header(), self)