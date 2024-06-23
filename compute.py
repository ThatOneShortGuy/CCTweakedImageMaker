from PIL import Image
from Pixel import Pixel

MONITOR_WIDTH = 21.25
MONITOR_HEIGHT = 14.5

def get_code_from_file(file_path: str, num_monitors_wide: int, num_monitors_tall: int) -> str:
    w, h = int(MONITOR_WIDTH * num_monitors_wide)-6, int(MONITOR_HEIGHT * num_monitors_tall)-6

    img = Image.open(file_path)
    img = img.resize((w, h))

    data = ''.join(Pixel(*pix).to_blit() for pix in img.convert('RGB').getdata()) # type: ignore

    code = f"""local monitor = peripheral.find("monitor")
monitor.setTextScale(0.5)
local letters = string.rep(" ", {w})
local letterColors = string.rep("0", {w})
"""

    for i in range(0, len(data), w):
        row = data[i:i+w]
        code += f'monitor.setCursorPos(1, {i//w+1})\n'
        code += f'monitor.blit(letters, letterColors,"{row}")\n'

    return code