from pathlib import Path
import gzip


def run_length_encode(data):
    encoded_data = ""
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_data += data[i - 1] + str(count)
            count = 1

    # Handle the last run
    encoded_data += data[-1] + str(count)

    return encoded_data


def run_length_decode(encoded_data):
    decoded_data = ""

    i = 0
    while i < len(encoded_data):
        char = encoded_data[i]
        count_str = ""

        i += 1
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count_str += encoded_data[i]
            i += 1

        count = int(count_str)
        decoded_data += char * count

    return decoded_data


file_path = input("Path to text file: ")
path = Path(file_path)

if path.exists():
    data = path.read_text()
    encoded_data = run_length_encode(data)
    decoded_data = run_length_decode(encoded_data)

    with gzip.open("./compressed.gz", 'wt') as gzfile:
        gzfile.write(encoded_data)
    # destination = Path("./compressed.zip")

    # destination.write_text(encoded_data)
    # destination.write_text(decoded_data)

else:
    print("We can't find this file.")
