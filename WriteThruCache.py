import math


class Address:
    def __init__(self, block_size: int, set_bits: int, word_bits: int, tag_bits: int):
        self.block_size = block_size

        self.set_size = set_bits
        self.word_size = word_bits
        self.tag_size = tag_bits

        self.is_valid = False
        self.is_dirty = False
        self.is_data = True

        self.tag_bits = 0
        self.set_bits = 0
        self.word_bits = 0

    def reset(self):
        self.tag_bits = 0
        self.set_bits = 0
        self.word_bits = 0

    def set_address(self, mem_address: str):
        bin_mem_address = str(bin(int(mem_address, 16)))[2:]  # bruh
        adjusted_tag_size = self.tag_size
        if len(bin_mem_address) != self.block_size:
            diff = self.block_size - len(bin_mem_address)
            adjusted_tag_size = self.tag_size - diff
            self.is_data = False
        self.tag_bits = int(bin_mem_address[:adjusted_tag_size], 2)
        self.set_bits = int(bin_mem_address[adjusted_tag_size:adjusted_tag_size + self.set_size], 2)
        self.word_bits = int(bin_mem_address[adjusted_tag_size + self.set_size:], 2)
        self.is_valid = True

    def print_address(self):
        print(f"tag bits: {hex(self.tag_bits)}")
        print(f"set bits: {hex(self.set_bits)}")
        print(f"Word bits: {hex(self.word_bits)}")


class SetAssCache:
    def __init__(self, total_size: int, block_size: int, set_associativity: int):
        self.total_size = total_size  # Total size of the cache
        self.block_size = block_size  # size of the address
        self.set_associativity = set_associativity  # how many blocks per set
        self.total_blocks = math.ceil(total_size/block_size)  # how many blocks in total in cache
        self.set_count = math.ceil(self.total_blocks/set_associativity)  # How many sets in total
        self.set_bits = int(math.log(self.set_count, 2))  # The number of bits required to represent every set.
        self.word_bits = 2  # 2 bits for a word seems standard
        self.tag_bits = block_size - (self.word_bits + self.set_bits)  # Whats left after the word bits and set bits are taken
        self.cache = dict()
        for i in range(self.set_count):
            self.cache[i] = []
            for j in range(set_associativity):
                self.cache[i].append(Address(block_size, self.set_bits, self.word_bits))
