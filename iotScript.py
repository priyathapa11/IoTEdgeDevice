import sys
sys.path.append('/home/thapa/gem5/configs')  # ensures gem5 c>

from m5.objects import *
from common.Caches import L1_ICache, L1_DCache, L2Cache
import m5

# System Configuration
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'  # timing simulation
system.mem_ranges = [AddrRange('512MB')]

# Simple in-order CPU
system.cpu = TimingSimpleCPU()

# Cache Hierarchy
icache = L1_ICache(size='16kB', assoc=2)
dcache = L1_DCache(size='16kB', assoc=2)
l2cache = L2Cache(size='128kB', assoc=4)

# L2 bus
system.l2bus = L2XBar()

# Connect caches using 25.x ports
system.cpu.icache_port = icache.cpu_side
system.cpu.dcache_port = dcache.cpu_side

icache.mem_side = system.l2bus.cpu_side_ports
dcache.mem_side = system.l2bus.cpu_side_ports

l2cache.cpu_side = system.l2bus.cpu_side_ports
system.membus = SystemXBar()
l2cache.mem_side = system.membus.mem_side_ports

# Memory Controller
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8(range=system.mem_ranges[>
system.mem_ctrl.port = system.membus.mem_side_ports

# Workload / Application
process = Process()
process.executable = 'iot_sensors_sim'   # your compiled C pr>
process.cmd = ['iot_sensors_sim', '1000']  # program + argume>
system.cpu.workload = process
system.cpu.createThreads()

# Root and Simulation
root = Root(full_system=False, system=system)
m5.instantiate()

print("===== Starting IoT Low-Power Microprocessor Simulation>
exit_event = m5.simulate()
print(f"Simulation ended at tick {m5.curTick()} because {exit>
