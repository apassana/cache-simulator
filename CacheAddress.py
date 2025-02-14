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

    def __eq__(self, other):
        if isinstance(other, Address):
            return self.tag_bits == other.tag_bits
        if isinstance(other, int):
            return self.tag_bits == other
        else:
            raise ValueError(f"Cannot compare with {type(other)}")

    def reset(self):
        self.tag_bits = 0
        self.set_bits = 0
        self.word_bits = 0
        self.is_valid = False

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
