from collections import OrderedDict

class Cache:
    def __init__(self, size):
        self.size = size
        self.memory = OrderedDict()
        self.hit = 0
        self.miss = 0
    
    def lru(self, element):
        element = element.lower()
        if element in self.memory:
            self.hit += 1
            self.memory.move_to_end(element, last=True)
        else:
            self.miss += 1
            if self.memory and (len(self.memory) == self.size):
                self.memory.popitem(last=False)
            if self.size > 0:
                self.memory[element] = 0
        
def solution(cacheSize, cities):
    answer = 0
    cache = Cache(cacheSize)
    for city in cities:
        cache.lru(city)
    
    answer += cache.hit + cache.miss * 5
    return answer