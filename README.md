# Cache Simulator

A Python-based simulator for modeling various cache architectures and analyzing their performance using memory access trace files.

---

## Problem Statement

The goal of this project is to simulate different cache configurations and policies to better understand their impact on system performance. The simulator provides metrics such as cache hit/miss rates and average memory access time.

---

## Features

- Supports multiple cache levels and policies
- Simulates:
  - **Write-through** and **write-back** policies
  - **Set-associative** caches
- Parses memory trace files in plain-text format
- Provides detailed statistics on cache performance

---

## System Architecture

- `main.py`: The simulation driver. Allows users to run trace files through configured cache simulations.
- `CacheAddress.py`: Defines a class to represent memory addresses accessed by the simulator.
- `SetAssCache.py`: Base class for all cache implementations; supports set-associative behavior.
- `WriteThruCache.py`: Subclass of `SetAssCache.py`. Implements a write-through cache policy.
- `WriteBackCache.py`: Subclass of `SetAssCache.py`. Implements a write-back cache policy.

---

## Getting Started

### Prerequisites

- Python 3.9+
- pandas

### To Run

Run the following command from the terminal:
```bash
python main.py
```

This will execute the simulation using the default settings or the trace file specified within `main.py`.

> trace files will be automatically loaded by the driver if they are placed in the `traces` folder and end in `.trace`

---

## Example Trace File Format

Each line in the trace file should represent a memory access, such as:

```
2 408ed4  
1 10019d88 
0 10019d94 
```
- `0` denotes a data read operation  
- `1` denotes a data write operation
- `2` denotes an instruction read operation  
- Followed by a hexadecimal address

---

## Output

The simulator reports:

- Total cache accesses
- Number of hits and misses
- Hit/miss ratios
- Average memory access time (based on configurable latency settings)

---


## Author

Alexander Passanante
