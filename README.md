IoT Edge Microprocessor Simulation using gem5
Project Overview

This project demonstrates the design and simulation of a low-power x86 microprocessor for IoT edge devices using gem5, a computer architecture simulator. The system simulates a CPU aggregating data from multiple sensors, performing lightweight computations, and analyzing performance and energy efficiency.

The main goal is to explore low-power design techniques, including small cache sizes, simple in-order cores, and efficient memory access, while running a realistic IoT workload.

Features

Single in-order CPU core for low-power operation

Custom L1 instruction and data caches

System memory configuration using DDR3

Simulation of an IoT sensor workload (iot_sensors_sim)

Collection of performance metrics such as IPC, cache hits/misses, and simulation runtime

Prerequisites

gem5 version 25.x, compiled for x86

Python 3 and required gem5 modules

GCC or compatible compiler to build the IoT workload

Linux or WSL environment (Ubuntu recommended)

Setup and Installation

Clone or download the gem5 repository.

Build gem5 for x86:

scons build/X86/gem5.opt -j$(nproc)


Compile the IoT workload C program:

gcc -O2 -static -o iot_sensors_sim iot_sensors_sim.c


Place iotScript.py in the gem5 root directory along with the compiled workload.

Running the Simulation

Execute the simulation using:

build/X86/gem5.opt iotScript.py


During the simulation, the CPU will process the IoT workload, aggregating sensor data and computing averages at each step. Results and performance metrics will be saved in the m5out/ directory.
