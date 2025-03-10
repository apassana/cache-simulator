from WriteBackCache import WriteBackCache
from WriteThruCache import WriteThruCache
import pandas as pd

DEFAULT_PATH = "SimData.html"

L1_size = 1024
L1_block = 32
L1_set_list = [
    1,
    2,
    4,
    8,
    16,
    32,
]
L2_size = 2048
L2_block = 64
L2_set_list = [
    1,
    4,
    16,
    64,
]

H = 1
M = 100
L2H = 10
L2M = 100


def write_thru_cache_test(instructions: list):
    for i in L1_set_list:
        L1_data = WriteThruCache(L1_size, L1_block, i)
        L1_instructions = WriteThruCache(L1_size, L1_block, i)
        cache_instructions = [
            L1_data.read,
            L1_data.write,
            L1_instructions.read
        ]
        for instruction in instructions:
            cache_instructions[int(instruction[0])](instruction[1])
        L1_total_miss = L1_data.miss_count + L1_instructions.miss_count
        L1_total_access = L1_data.total_accesses + L1_instructions.total_accesses
        L1_miss_rate = L1_total_miss/L1_total_access
        L1_data_miss_rate = L1_data.miss_count / L1_data.total_accesses
        L1_inst_miss_rate = L1_instructions.miss_count / L1_instructions.total_accesses
        results = {
            "L1DMiss": L1_data.miss_count,
            "L1DTotalAccesses": L1_data.total_accesses,
            "L1DMissRate": L1_data_miss_rate,
            "L1IMiss": L1_instructions.miss_count,
            "L1ITotalAccesses": L1_instructions.total_accesses,
            "L1IMissRate": L1_inst_miss_rate,
            "L1MissCount": L1_total_miss,
            "L1TotalAccesses": L1_total_access,
            "L1MissRate": L1_miss_rate,
            "AMAT": H + (L1_miss_rate * M)
        }
        print(f"Data for {i}-set-associative L1 Cache:")
        print("L1 Data Miss count: ", L1_data.miss_count)
        print("L1 Data Total accesses: ", L1_data.total_accesses)
        print("L1 Data Miss rate: ", L1_data_miss_rate)
        print("L1 Instruction Miss count: ", L1_instructions.miss_count)
        print("L1 Instruction Total accesses: ", L1_instructions.total_accesses)
        print("L1 Instruction Miss rate: ", L1_inst_miss_rate)
        print("L1 Miss count: ", L1_total_miss)
        print("L1 Total accesses: ", L1_total_access)
        print("L1 Miss rate: ", L1_miss_rate)
        print("AMAT = ", H + (L1_miss_rate * M))
        print("")
        return results


def write_back_cache_test(instructions: list):
    for i in L1_set_list:
        L1_data = WriteBackCache(L1_size, L1_block, i)
        L1_instructions = WriteBackCache(L1_size, L1_block, i)
        cache_instructions = [
            L1_data.read,
            L1_data.write,
            L1_instructions.read
        ]
        for instruction in instructions:
            cache_instructions[int(instruction[0])](instruction[1])
        L1_total_miss = L1_data.miss_count + L1_instructions.miss_count
        L1_total_access = L1_data.total_accesses + L1_instructions.total_accesses
        L1_miss_rate = L1_total_miss / L1_total_access
        L1_data_miss_rate = L1_data.miss_count / L1_data.total_accesses
        L1_inst_miss_rate = L1_instructions.miss_count / L1_instructions.total_accesses
        results = {
            "L1DMiss": L1_data.miss_count,
            "L1DTotalAccesses": L1_data.total_accesses,
            "L1DMissRate": L1_data_miss_rate,
            "L1IMiss": L1_instructions.miss_count,
            "L1ITotalAccesses": L1_instructions.total_accesses,
            "L1IMissRate": L1_inst_miss_rate,
            "L1MissCount": L1_total_miss,
            "L1TotalAccesses": L1_total_access,
            "L1MissRate": L1_miss_rate,
            "AMAT": H + (L1_miss_rate * M)
        }
        print(f"Data for {i}-set-associative L1 Cache:")
        print("L1 Data Miss count: ", L1_data.miss_count)
        print("L1 Data Total accesses: ", L1_data.total_accesses)
        print("L1 Data Miss rate: ", L1_data_miss_rate)
        print("L1 Instruction Miss count: ", L1_instructions.miss_count)
        print("L1 Instruction Total accesses: ", L1_instructions.total_accesses)
        print("L1 Instruction Miss rate: ", L1_inst_miss_rate)
        print("L1 Miss count: ", L1_total_miss)
        print("L1 Total accesses: ", L1_total_access)
        print("L1 Miss rate: ", L1_miss_rate)
        print("AMAT = ", H + (L1_miss_rate * M))
        print("")
        return results


def two_level_cache_test(instructions: list):
    for i in L2_set_list:
        L1_data = WriteBackCache(L1_size, L1_block, 2)
        L1_instructions = WriteBackCache(L1_size, L1_block, 2)
        L2 = WriteBackCache(L2_size, L2_block, i)
        L1_data.next_level = L2
        L1_instructions.next_level = L2
        cache_instructions = [
            L1_data.read,
            L1_data.write,
            L1_instructions.read
        ]
        for instruction in instructions:
            cache_instructions[int(instruction[0])](instruction[1])
        L1_total_miss = L1_data.miss_count + L1_instructions.miss_count
        L1_total_access = L1_data.total_accesses + L1_instructions.total_accesses
        L1_data_miss_rate = L1_data.miss_count/L1_data.total_accesses
        L1_inst_miss_rate = L1_instructions.miss_count / L1_instructions.total_accesses
        L1_miss_rate = L1_total_miss/L1_total_access
        L2_miss_rate = L2.miss_count/L2.total_accesses
        results = {
            "L1DMiss": L1_data.miss_count,
            "L1DTotalAccesses": L1_data.total_accesses,
            "L1DMissRate": L1_data_miss_rate,
            "L1IMiss": L1_instructions.miss_count,
            "L1ITotalAccesses": L1_instructions.total_accesses,
            "L1IMissRate": L1_inst_miss_rate,
            "L1MissCount": L1_total_miss,
            "L1TotalAccesses": L1_total_access,
            "L1MissRate": L1_miss_rate,
            "L2MissCount": L2.miss_count,
            "L2TotalAccesses": L2.total_accesses,
            "L2MissRate": L2.miss_count/L2.total_accesses,
            "AMAT": H + L1_miss_rate * (L2H + L2_miss_rate * L2M)
        }
        print(f"Data for {i}-set-associative L2 Cache:")
        print("L1 Data Miss count: ", L1_data.miss_count)
        print("L1 Data Total accesses: ", L1_data.total_accesses)
        print("L1 Data Miss rate: ", L1_data_miss_rate)
        print("L1 Instruction Miss count: ", L1_instructions.miss_count)
        print("L1 Instruction Total accesses: ", L1_instructions.total_accesses)
        print("L1 Instruction Miss rate: ", L1_inst_miss_rate)
        print("L1 Miss count: ", L1_total_miss)
        print("L1 Total accesses: ", L1_total_access)
        print("L1 Miss rate: ", L1_miss_rate)
        print("L2 Miss count: ", L2.miss_count)
        print("L2 Total accesses: ", L2.total_accesses)
        print("L2 Miss rate: ", L2.miss_count/L2.total_accesses)
        print("AMAT: ", H + L1_miss_rate * (L2H + L2_miss_rate * L2M))
        print("")
        return results


def run_all_and_save():
    results = {}
    trace_list = [
        "spice.trace",
        "cc.trace",
        "tex.trace"
    ]
    test_list = [
        write_thru_cache_test,
        write_back_cache_test,
        two_level_cache_test
    ]
    test_list_name = [
        "Write-through Cache test",
        "Write-back Cache test",
        "Two Cache test"
    ]
    for test_i in range(len(test_list_name)):
        for trace_i in range(len(trace_list)):
            trace = open(trace_list[trace_i], 'r')
            trace_lines = trace.readlines()
            instructions = []
            for i in trace_lines:
                instructions.append(i.split())
            trace.close()
            results[f"{test_list_name[test_i]} with {trace_list[trace_i]}"] = test_list[test_i](instructions)
    data = pd.DataFrame(results)
    data.to_html(DEFAULT_PATH)
    print("data exported...")


def main():
    if input("Run all tests (y/n): ") == 'y':
        run_all_and_save()
        return 0
    trace_list = [
        "spice.trace",
        "cc.trace",
        "tex.trace"
    ]
    while True:
        print("Trace List:")
        for i in range(len(trace_list)):
            print(f"{i} - {trace_list[i]}")
        trace_index = int(input("Select index: "))
        if trace_index in range(len(trace_list)):
            break
        print(f"{trace_index} not in list")
    print("")

    trace = open(trace_list[trace_index], 'r')
    trace_lines = trace.readlines()
    instructions = []
    for i in trace_lines:
        instructions.append(i.split())
    trace.close()

    test_list = [
        write_thru_cache_test,
        write_back_cache_test,
        two_level_cache_test
    ]
    test_list_name = [
        "Write-through Cache test",
        "Write-back Cache test",
        "Two Cache test"
    ]
    while True:
        print("Test List:")
        for i in range(len(test_list)):
            print(f"{i} - {test_list_name[i]}")
        test_index = int(input("Select index: "))
        if test_index in range(len(test_list)):
            break
        print(f"{test_index} not in list")
    print("")
    test_list[test_index](instructions)


if __name__ == "__main__":
    main()
