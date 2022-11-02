from collections import deque
from memory_cs104 import Memory

Cache_Space = 4

class Cache:
  def __init__(self):
    self.cache = deque(maxlen=Cache_Space)
    self.flush()
  
  def flush(self):
    for i in range(Cache_Space):
      self.cache.append(("", ""))

  def write(self, tag, value):
    self.cache.append(tuple((tag, value)))

  def read(self, tag):
    for i in range(Cache_Space):
      if self.cache[i][0] == tag:
        return self.cache[i][1]
    print("That's not a valid cache tag!")

  def get_value_tag(self, value):
    for tag, cache_value in self.cache:
      if cache_value == value:
        return tag
    print("That value isn't in cache. Getting value from memory!")