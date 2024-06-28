import cv2 as cv
from typing import Optional
from Video import Frame

class VideoReader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cap: Optional[cv.VideoCapture] = None

    def __iter__(self):
        return self
    
    def __next__(self) -> Frame:
        if self.cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        ret, frame = self.cap.read()
        if not ret:
            raise StopIteration
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        return Frame.from_ndarray(frame) # type: ignore
    
    def __enter__(self):
        self.cap = cv.VideoCapture(self.filepath)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.cap:
            self.cap.release()
    
    def get_dimensions(self):
        if self.cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        return width, height
    
    def get_framerate(self):
        if self.cap is None:
            raise Exception("VideoReader is not opened. Use 'with' statement to open the video file.")
        return self.cap.get(cv.CAP_PROP_FPS)