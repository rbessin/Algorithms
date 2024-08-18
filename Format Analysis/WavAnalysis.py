import struct
import matplotlib.pyplot as plt
import numpy as np

def parse_wav(file_path):
    with open(file_path, 'rb') as f:
        riff = f.read(12)
        riff_id, file_size, wave_id = struct.unpack('<4sI4s', riff)
        
        if riff_id != b'RIFF' or wave_id != b'WAVE':
            raise ValueError("This is not a valid WAV file")
        
        fmt_header = f.read(8)
        fmt_id, fmt_size = struct.unpack('<4sI', fmt_header)
        
        if fmt_id != b'fmt ':
            raise ValueError("fmt chunk not found")
        
        fmt_chunk = f.read(fmt_size)
        audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack('<HHIIHH', fmt_chunk[:16])
        
        print(f"Audio Format: {audio_format}")
        print(f"Number of Channels: {num_channels}")
        print(f"Sample Rate: {sample_rate} Hz")
        print(f"Byte Rate: {byte_rate} bytes/sec")
        print(f"Block Align: {block_align} bytes")
        print(f"Bits per Sample: {bits_per_sample} bits")

        while True:
            data_header = f.read(8)
            data_id, data_size = struct.unpack('<4sI', data_header)
            
            if data_id == b'data':
                print(f"Data Chunk Found: Size = {data_size} bytes")
                break
            else:
                f.seek(data_size, 1)

        audio_data = f.read(data_size)
        print(f"Read {len(audio_data)} bytes of audio data")
        
        # 2. Display Sample Values
        display_sample_values(audio_data, bits_per_sample, num_channels)
        
        # 3. Plot Waveform
        plot_waveform(audio_data, bits_per_sample, num_channels, sample_rate)

def display_sample_values(audio_data, bits_per_sample, num_channels):
    if bits_per_sample == 8:
        fmt = 'B'  # Unsigned 8-bit
    elif bits_per_sample == 16:
        fmt = 'h'  # Signed 16-bit
    else:
        raise ValueError(f"Unsupported bit depth: {bits_per_sample}")

    sample_count = 10  # Display the first 10 samples for simplicity
    samples = struct.unpack(f'<{sample_count * num_channels}{fmt}', audio_data[:sample_count * num_channels * (bits_per_sample // 8)])

    print(f"First {sample_count} audio samples: {samples}")

def plot_waveform(audio_data, bits_per_sample, num_channels, sample_rate):
    if bits_per_sample == 16:
        dtype = np.int16
    elif bits_per_sample == 8:
        dtype = np.uint8
    else:
        raise ValueError("Unsupported bit depth")

    audio_samples = np.frombuffer(audio_data, dtype=dtype)
    
    if num_channels > 1:
        audio_samples = audio_samples.reshape(-1, num_channels)

    time_axis = np.linspace(0, len(audio_samples) / sample_rate, num=len(audio_samples))

    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_samples)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

def get_file_path():
    file_path = r"C:\Users\rapha\Downloads\CantinaBand3.wav"
    return file_path

file_path = get_file_path()
print(f"Selected File Path: {file_path}")
parse_wav(file_path)
