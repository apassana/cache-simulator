from SetAssCache import *


class WriteBackCache(SetAssCache):
    def replace(self, new_address: Address.Address, is_dirty=False):
        new_address.is_dirty = is_dirty
        cache_set = self.cache[new_address.set_bits]  # Retrieves set of new address
        replaced_address = cache_set.pop(0)  # Removes from the end of the queue
        if replaced_address.is_dirty:
            self.miss_count += 1  # Represents the writing of the data
        cache_set.append(new_address)  # Places new address at the start of the queue

    def write(self, to_address: Address.Address):
        new_address = Address.Address(self.block_size, self.set_bits, self.word_bits, self.tag_bits)
        self.total_accesses += 1
        if new_address.tag_bits in self.cache[new_address.set_bits]:
            self.write_hit += 1  # Debug
            self.cache[new_address.set_bits][new_address.tag_bits].is_dirty = True  # Sets the block that gets written to dirty
        else:
            self.write_miss += 1  # Debug
            self.replace(new_address, True)
        if self.next_level is not None:
            self.next_level.write(to_address)
