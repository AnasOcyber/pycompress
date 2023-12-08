import heapq
from collections import defaultdict
from pathlib import Path


class Node:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(data):
    char_freq = defaultdict(int)
    for char in data:
        char_freq[char] += 1

    priority_queue = [Node(char=char, freq=freq)
                      for char, freq in char_freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged_node = Node(freq=node1.freq + node2.freq,
                           left=node1, right=node2)
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def huffman_encode(data, root, encoding_map=None, current_encoding=""):
    if encoding_map is None:
        encoding_map = {}

    if root is not None:
        if root.char is not None:
            encoding_map[root.char] = current_encoding
        huffman_encode(data, root.left, encoding_map, current_encoding + "0")
        huffman_encode(data, root.right, encoding_map, current_encoding + "1")

    return encoding_map


def huffman_decode(encoded_data, root):
    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data


file_path = input("Path to uncompressed file: ")
path = Path(file_path)

if path.exists():
    data = path.read_text()
    root = build_huffman_tree(data)
    encoding_map = huffman_encode(data, root)
    encoded_data = "".join(encoding_map[char] for char in data)
    decoded_data = huffman_decode(encoded_data, root)

    print(f"Original data: {data}")
    print(f"Encoded data: {encoded_data}")
    print(f"Decoded data: {decoded_data}")
else:
    print("We can't find this file.")
