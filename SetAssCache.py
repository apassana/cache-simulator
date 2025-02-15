import math
import CacheAddress as Address


class SetAssCache:
    def __init__(self, total_size: int, block_size: int, set_associativity: int, next_level=None):
        self.next_level = next_level

        self.total_size = total_size  # Total size of the cache
        self.block_size = block_size  # size of the address
        self.set_associativity = set_associativity  # how many blocks per set

        self.total_blocks = math.ceil(total_size/block_size)  # how many blocks in total in cache
        self.set_count = math.ceil(self.total_blocks/set_associativity)  # How many sets in total
        self.set_bits = int(math.log(self.set_count, 2))  # The number of bits required to represent every set.
        self.word_bits = int(math.log(block_size, 2))  # The number of bits to address block_size many bytes.
        self.tag_bits = block_size - (self.word_bits + self.set_bits)  # Whats left after the word bits and set bits are taken

        self.cache = dict()

        self.write_count = 0
        self.write_hit = 0
        self.write_miss = 0
        self.miss_count = 0
        self.total_accesses = 0
        for i in range(self.set_count):
            self.cache[i] = []
            for j in range(set_associativity):
                self.cache[i].append(Address.Address(block_size, self.set_bits, self.word_bits, self.tag_bits))

    def read(self, mem_address: str):
        self.total_accesses += 1
        target_address = Address.Address(self.block_size, self.set_bits, self.word_bits, self.tag_bits)
        target_address.set_address(mem_address)
        cache_set = self.cache[target_address.set_bits]
        if target_address.tag_bits in cache_set:
            cache_set_size = len(cache_set)
            i = cache_set.index(target_address.tag_bits)  # Gets index of the read address
            cache_set.append(cache_set.pop(i))  # Places most recently accessed address at the start of the queue
            assert cache_set_size == len(cache_set)
            return  # This counts as a hit and does nothing as the sim doesn't need to return a value
        self.miss_count += 1  # If it doesn't hit it counts as a miss and needs to read and write to the cache.
        if self.next_level is not None:  # If it is a multi-level cache it will run a read on the next-level
            self.next_level.read(mem_address)
        self.replace(target_address)  # Assumes that it gets the required address and replaces a value in the set.

    def replace(self, new_address: Address.Address):
        cache_set = self.cache[new_address.set_bits]  # Retrieves set of new address
        cache_set.pop(0)  # Removes from the end of the queue
        cache_set.append(new_address)  # Places new address at the start of the queue

    def write(self, to_address: Address.Address):
        print("Super method not defined")
        pass
