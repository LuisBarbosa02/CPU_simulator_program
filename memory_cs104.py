Memory_Space = 256

class Memory():
  def __init__(self):
    self.memory_dict = {}
    self.init_memory_addresses()

  def init_memory_addresses(self):
    for i in range(Memory_Space):
      self.memory_dict[f"{i:08b}"] = 0

  def write(self, address, value):
    if address in self.memory_dict:
      self.memory_dict[address] = value
      return
    print("That's not a valid memory address!")
  
  def read(self, address):
    if address in self.memory_dict:
      return self.memory_dict[address]
    print("That's not a valid memory address!")

  def get_value_address(self, value):
    for address, memory_value in self.memory_dict.items():
      if memory_value == value:
        return address