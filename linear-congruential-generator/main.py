from time import time_ns

class LCG:

    def __init__(self, seed= None) -> None:
        self.__seed       = seed if seed != None else time_ns()
        self.__modulus    = 0x100000000 # m
        self.__multiplier = 0x19660d    # a
        self.__increment  = 0x3c6ef35f  # c

        # NOTE: values of m, a, and c are taken from section 
        # named "parameters in common use" of a wikipedia page 
        # for "linear congruential generator" 
        # https://en.wikipedia.org/wiki/Linear_congruential_generator

    def __nextint(self):
        self.__seed = (self.__multiplier * self.__seed + self.__increment) % self.__modulus
        return self.__seed

    def randint(self, start, stop):
        """return random integer in range [start, stop)"""
        _range = (stop - start)
        return start + (self.__nextint() % _range)

    def choice(self, seq): 
        """return random element from given sequence"""
        index = self.randint(0, len(seq))
        return seq[index]

    def choices(self, seq, k):
        """return randomly selected k elements from sequence"""
        indices = set()
        while len(indices) < k:
            indices.add(self.randint(0, len(seq)))

        return [seq[i] for i in indices]

    def shuffle(self, seq): 
        """return sequence with its elements shuffled randomly"""
        for i in range(len(seq)):
            j = self.randint(i, len(seq))
            seq[i], seq[j] = seq[j], seq[i]
        
        return seq

if __name__ == "__main__":

    # initialize generator with seed 31
    lcg = LCG(seed=31)

    # random integer in range [0, 5)
    print(lcg.randint(0, 5)) # 3

    # random element from given sequence
    print(lcg.choice([1, 2, 3, 4, 5])) # 5
 
    # random 2 elements from given sequence
    print(lcg.choices([1, 2, 3, 4, 5], k=2)) # [3, 5]

    # reorder elements of sequence randomly
    print(lcg.shuffle([1, 2, 3, 4, 5])) # [3, 1, 5, 2, 4]
