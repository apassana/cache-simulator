import WriteBackCache
from WriteThruCache import WriteThruCache


def main(trace_index: int):
    trace_list = [
        "spice.trace",
        "cc.trace",
        "tex.trace"
    ]
    trace = open(trace_list[trace_index], 'r')
    trace_lines = trace.readlines()
    instructions = []
    for i in trace_lines:
        instructions.append(i.split())
    c = WriteThruCache(1024, 32, 4)
    cache_instructions = [
        c.read,
        c.write,
        c.read
    ]
    for instruction in instructions:
        cache_instructions[int(instruction[0])](instruction[1])
    print("Miss count: ", c.miss_count)
    print("Total accesses: ", c.total_accesses)


if __name__ == "__main__":
    main(0)
