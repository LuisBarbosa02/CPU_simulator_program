from memory_cs104 import Memory
from cache_cs104 import Cache

Number_Registers = 12

class CPU:
  def __init__(self):
    self.memory = Memory()
    self.cache = Cache()
    self.registers = [0] * Number_Registers
    self.cache_use = True


  # Memory
  def write_to_memory(self, address, value):
    self.memory.write(address, value)

  def read_from_memory(self, address):
    return self.memory.read(address)
  
  def get_value_memory_address(self, value):
    return self.memory.get_value_address(value)
  # --- #


  # Cache
  def write_to_cache(self, tag, value):
    self.cache.write(tag, value)
  
  def read_from_cache(self, tag):
    return self.cache.read(tag)
  
  def get_value_cache_tag(self, value):
    return self.cache.get_value_tag(value)
  # --- #


  # Registers
  def reset_registers(self):
    for i in range(len(self.registers)):
      self.registers[i] = 0

  def write_to_register(self, register, value):
    if int(register[1]) == 0:
      print("\n" + "That register it's only for number 0!", end='\n\n')
      return

    ## If cache_use is False
    if self.cache_use is False:
      address = self.get_value_memory_address(value)
      if not address:
        print("Can't write that value to register!", end='\n\n')
        return
      self.registers[int(register[1])] = self.memory.memory_dict[address]
    
    ## If cache_use is True
    tag = self.get_value_cache_tag(value)
    if tag:
      self.registers[int(register[1])] = self.read_from_cache(tag)
    else:
      address = self.get_value_memory_address(value)
      if not address:
        print("Can't write that value to register!", end='\n\n')
        return
      self.registers[int(register[1])] = self.memory.memory_dict[address]
      self.write_to_cache(address, value)
  # --- #


  # CPU functions (need to write into the register before doing the instruction)
  def add_instruction(self, destination, source_s, source_t):
    if int(destination[1]) == 0:
      print("That register it's only for number 0!")
      return
    self.registers[int(destination[1])] = self.registers[int(source_s[1])] + self.registers[int(source_t[1])]
  
  def addi_instruction(self, destination, source_s, immediate):
    if int(destination[1]) == 0:
      print("That register it's only for number 0!")
      return
    self.registers[int(destination[1])] = self.registers[int(source_s[1])] + int(immediate)
  
  def cache_instruction(self, number):
    if number == 0:
      self.cache_use = False
    if number == 1:
      self.cache_use = True
    if number == 2:
      self.cache.flush()

  def parse_instruction(self, instruction):
    splited_instruction = instruction.split(',')
    
    if splited_instruction[0] == 'ADD':
      print("Adding...")
      self.write_to_register(splited_instruction[2], int(input('Choose the number: ')))
      self.write_to_register(splited_instruction[3], int(input('Choose the number: ')))
      self.add_instruction(splited_instruction[1], splited_instruction[2], splited_instruction[3])
      print(f"Result: {self.registers[int(splited_instruction[1][1])]}", end='\n\n')
    
    if splited_instruction[0] == 'ADDI':
      print("Adding with an immediate...")
      self.write_to_register(splited_instruction[2], int(input('Choose the number: ')))
      self.addi_instruction(splited_instruction[1], splited_instruction[2], splited_instruction[3])
      print(f"Result: {self.registers[int(splited_instruction[1][1])]}", end='\n\n')
    
    if splited_instruction[0] == 'CACHE':
      self.cache_instruction(splited_instruction[1])