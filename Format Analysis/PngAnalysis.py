import struct

def parse_png(file_path):
    with open(file_path, 'rb') as f:
        signature = f.read(8)
        expected_signature = b'\x89PNG\r\n\x1a\n'
        if signature != expected_signature:
            raise ValueError("This is not a valid PNG file")
        print("PNG Signature Verified")

        while True:
            chunk_len_bytes = f.read(4)
            if len(chunk_len_bytes) == 0:
                break
            chunk_length = struct.unpack('>I', chunk_len_bytes)[0]

            chunk_type = f.read(4).decode('ascii')
            print(f"Chunk Type: {chunk_type}")

            chunk_data = f.read(chunk_length)
            crc = struct.unpack('>I', f.read(4))[0]

            print(f"Chunk Length: {chunk_length} bytes, CRC: {crc}")

            if chunk_type == 'IHDR':
                width, height, bit_depth, color_type, compression, filter_method, interlace_method = struct.unpack('>IIBBBBB', chunk_data)
                print(f"  Width: {width}, Height: {height}")
                print(f"  Bit Depth: {bit_depth}, Color Type: {color_type}")
                print(f"  Compression: {compression}, Filter Method: {filter_method}, Interlace: {interlace_method}")
            
            if chunk_type == 'IEND':
                print("End of PNG file reached.")
                break

def get_file_path():
    file_path = r"C:\Users\rapha\Art\Pixel Art\Pictures\Avatar.png"
    return file_path

file_path = get_file_path()
print(f"Selected File Path: {file_path}")
parse_png(file_path)
