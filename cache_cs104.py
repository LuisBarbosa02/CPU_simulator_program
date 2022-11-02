from collections import deque

Cache_Space = 4

class Cache:
  def __init__(self):
    self.cache = deque(maxlen=Cache_Space)
    self.flush()
    self.tag = 0
  
  def flush(self):
    for i in range(Cache_Space):
      self.cache.append(("", ""))

  def write(self, value):
    self.tag += 1
    if self.tag > 4:
      self.tag = 1
    self.cache.append(tuple((self.tag, value)))

  def read(self, tag):
    for i in range(Cache_Space):
      if self.cache[i][0] == tag:
        return self.cache[i][1]
    print("That's not a valid cache tag!")