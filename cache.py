class Cache:
    def __init__(self, total_size: int, block_size: int):
        self.total_size = total_size
        self.block_size = block_size
        self.cache = []
        self.m = total_size/block_size

