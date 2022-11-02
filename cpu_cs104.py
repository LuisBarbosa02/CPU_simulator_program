from memory_cs104 import Memory
from cache_cs104 import Cache

Number_Registers = 12

class CPU:
  def __init__(self):
    self.memory = Memory()
    self.cache = Cache()
    self.registers = [0] * Number_Registers

  # Memory
  def write_to_memory(self, address, value):
    self.memory.write(address, value)

  def read_from_memory(self, address):
    return self.memory.read(address)
  # --- #

  # Cache
  def write_to_cache(self, value):
    self.cache.write(value)
  
  def read_from_cache(self, tag):
    return self.cache.read(tag)
  # --- #

  # Registers
  def reset_registers(self):
    for i in range(len(self.registers)):
      self.registers[i] = 0
  # --- #

  # CPU functions
  def add_instruction(self, destination, source_s, source_t):
    if destination[1] == 0:
      print("That register it's only for number 0!")
      return
    