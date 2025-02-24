import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(10000000))  # Read only the first 1024 bytes
        return result['encoding']

file_path = 'data/data.csv'
encoding = detect_encoding(file_path)
print(f'The detected encoding is: {encoding}')