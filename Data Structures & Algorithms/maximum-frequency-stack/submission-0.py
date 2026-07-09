class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        
        if self.freq[val] not in self.group:
            self.group[self.freq[val]] = []
        self.group[self.freq[val]].append(val)
        
        self.max_freq = max(self.max_freq, self.freq[val])


    def pop(self) -> int:
        curr_pop = self.group[self.max_freq].pop()
        if len(self.group[self.max_freq]) == 0:
            self.group.pop(self.max_freq)
            self.max_freq -= 1
        self.freq[curr_pop] -=1
        return curr_pop
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()