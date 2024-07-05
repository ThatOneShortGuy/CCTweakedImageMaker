from typing import BinaryIO

import numpy as np
from numba import njit, uint8, vectorize
from numba.experimental import jitclass
from numpy.typing import NDArray

@vectorize(['u1(u1, u1)'], target='cpu')
def xor(a: NDArray[np.uint8], b: NDArray[np.uint8]) -> NDArray[np.uint8]:
    return a ^ b

@njit('u1[:](u8, u8)')
def default(width: int, height: int):
    return np.zeros(height * width, dtype=np.uint8)+np.uint8(15)

@njit('u8(u8, u1[:], u8)')
def read_byte(num: int, buffer: NDArray[np.uint8], buffer_pos: int) -> int:
    count = num // 16 + 1
    c = num % 16
    buffer[buffer_pos:buffer_pos+count] = c
    return buffer_pos + count

@jitclass([('pixels', uint8[:])]) # type: ignore
class FrameData:
    def __init__(self, pixels: NDArray[np.uint8]):
        self.pixels = pixels

@njit
def default_from_size(width: int, height: int) -> 'FrameData':
    return FrameData(default(width, height))

def read_from(file: BinaryIO, width: int, height: int, previous_frame_data: bytes) -> 'FrameData':
    data = np.frombuffer(file.read(width * height), dtype=np.uint8)
    previous_frame_data_arr = np.frombuffer(previous_frame_data, dtype=np.uint8)
    buffer = np.empty_like(previous_frame_data_arr)
    data_pos = 0
    buffer_pos = 0
    while True:
        buffer_pos = read_byte(data[data_pos], buffer, buffer_pos)
        data_pos += 1
        if buffer_pos == width * height:
            break
        elif buffer_pos > width * height:
            raise ValueError('Too many pixels')
    
    file.seek(data_pos - width * height, 1)
    res = xor(previous_frame_data_arr, buffer[:buffer_pos])
    return FrameData(np.frombuffer(res, dtype=np.uint8))

if __name__ == '__main__':
    a = default_from_size(42,42)
    b = default_from_size(42,42)

    xor(a.pixels, b.pixels)