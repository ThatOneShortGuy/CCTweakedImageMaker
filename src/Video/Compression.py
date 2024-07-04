def xor(a: bytes, b: bytes) -> bytes:
    return b''.join(map(lambda x: (x[0] ^ x[1]).to_bytes(1, 'little'), zip(*(a, b))))

def RLE(s: bytes) -> bytes:
    res = b''
    count = -1
    c = s[0]
    for char in s:
        if char != c or count >= 15:
            res += (count * 16 + c).to_bytes(1, 'little')
            count = 0
            c = char
        else:
            count += 1
    
    res += (count * 16 + c).to_bytes(1, 'little')
    return res

def compress(existing_frame: bytes, new_frame: bytes) -> bytes:
    return RLE(xor(existing_frame, new_frame))

def unRLE(s: bytes) -> bytes:
    res = b''
    i = 0
    while i < len(s):
        count = s[i] // 16
        c = s[i] % 16
        res += bytes([c] * (count + 1))
        i += 1
    return res

def uncompress(existing_frame: bytes, compressed_frame: bytes) -> bytes:
    return xor(existing_frame, unRLE(compressed_frame))