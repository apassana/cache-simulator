from SetAssCache import *


class WriteThruCache(SetAssCache):
    def write(self, to_address: str):
        new_address = Address.Address(self.block_size, self.set_bits, self.word_bits, self.tag_bits)
        self.miss_count += 1
        self.total_accesses += 1
        if new_address.tag_bits in self.cache[new_address.set_bits]:
            self.write_hit += 1
        else:
            self.write_miss += 1
            self.replace(new_address)
        if self.next_level is not None:
            self.next_level.write(to_address)
