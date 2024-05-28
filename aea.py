class AdvancedEuclideanAlgorithm:
    def __init__(self, pA, pB):
        if(pA < pB):
            print("pA muss größer sein!")
        else:
            self.r = [pA, pB]
            self.x = [1, 0]
            self.y = [0, 1]
            self.i = 1
            self.q = [0]

    def run(self):
        while self.r[self.i] != 0:
            self.q.insert(self.i, int(str(self.r[self.i - 1] / self.r[self.i]).split(".")[0]))
            self.r.insert(self.i+1, self.r[self.i-1] - self.q[self.i] * self.r[self.i])
            self.x.insert(self.i+1, self.x[self.i-1] - self.q[self.i] * self.x[self.i])
            self.y.insert(self.i+1, self.y[self.i-1] - self.q[self.i] * self.y[self.i])
            self.i += 1
    
    def output(self):
        print(f'Output for: ggt({self.r[0]}, {self.r[1]})') 
        print(f'| index | q | r | x | y |')
        for index in range(self.i):
                print(f'| {index} | {self.q[index]} | {self.r[index]} | {self.x[index]} | {self.y[index]} |')

if __name__ == "__main__":
     aea = AdvancedEuclideanAlgorithm(1386, 637)
     aea.run()
     aea.output()