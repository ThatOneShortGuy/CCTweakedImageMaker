# Codec Specification
It will be broken up into 2 main sections: the [header](#header) and the [body](#body). The [header](#header) will contain the metadata about the video, such as the version, dimensions, and frame rate. The [body](#body) will contain the actual video data.

# Header
The header will first contain a magic string to identify the file as a video file. This will be the string `ccvid`. Immediately following the magic string will be the version number of the codec. The version will be human readable in the format `ab`, where `a` is the major version and `b` is the minor version (ex. 12). It will be followed by the dimensions of the video `wh` where `w` is the width as a 2 byte unsigned integer and `h` is the height as a 2 byte unsigned integer. The frame rate will be the next field, as a 4 byte float.

`ccvid{version}{width}{height}{frame rate}`

# Body
The body contains a series of [frames](#frame). The frames will be concatenated together in the order they appear in the video:
`{frame1}{frame2}...{frameN}`

# Frame
A frame consists of 2 parts: the [color information](#color-information) and the [frame data](#frame-data).

## Color Information
The frame will first contain color information. It will be compressed by this codec's [standard compression](#standard-compression). There are always 16 different colors that can be used. The colors will be stored in the following format:
`{color1}{color2}...{color16}`

Where each color is a 3 byte RGB value.

## Frame Data
The frame's data is to be compressed by this codec's [standard compression](#standard-compression). Each pixel is half a byte, so 2 pixels are stored in a single byte. The pixels are stored in [row major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order). Example of a 3x3 image with [initial colors](#initial-frame):
```
433303ddd
```

# Standard Compression
It will be the XOR diff from the previous frame compressed with [Run Length Encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE). This implementation of RLE is simple: `{count}{char}` where count is 4 bits and char is the other 4 bits  .

# Initial Frame
The first frame will be an imaginary black frame where the colors are:
```
white    (0): #F0F0F0
orange   (1): #F2B233
magenta  (2): #E57FD8
lightBlue(3): #99B2F2
yellow   (4): #DEDE6C
lime     (5): #7FCC19
pink     (6): #F2B2CC
gray     (7): #4C4C4C
lightGray(8): #999999
cyan     (9): #4C99B2
purple   (a): #B266E5
blue     (b): #3366CC
brown    (c): #7F664C
green    (d): #57A64E
red      (e): #CC4C4C
black    (f): #111111
```