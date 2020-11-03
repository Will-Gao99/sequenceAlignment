import sys

gapPenalty = 1

def alpha(p, q):
    if p != q:
        return 1
    else:
        return 0

class SequenceAlign:
    def __init__(self,based,subject):
        self.based = based
        self.subject = subject
        self.result1 = ""
        self.result2 = ""
        self.opt = {}

        #initializing opt table
        for i in range(len(based)+1):
            self.opt[(i,0)] = i*gapPenalty
        for j in range(len(subject)+1):
            self.opt[(0,j)] = j*gapPenalty

    def solve(self):
        for j in range(1,len(subject)+1):
            for i in range(1,len(based)+1):
                print((i,j))
                self.opt[(i,j)] = min(alpha(based[i-1],subject[j-1])+self.opt[(i-1,j-1)],gapPenalty+self.opt[(i-1,j)],gapPenalty+self.opt[(i,j-1)])
        return self.opt[(len(based),len(subject))]

    def debug(self):
        out = ""
        for i in range(len(based)+1):
            for j in range(len(subject)+1):
                out += (str((i,j))+"="+str(self.opt[(i,j)]))
            out += "\n"
        print(self.opt.keys())
        print(out)

if __name__ == "__main__":
    # inp=sys.stdin.readlines()
    # idx = 0
    # based = ""
    # subject= ""
    # for line in inp:
    #     if i == 0:
    #         based = line.rstrip()
    #         i += 1
    #     else:
    #         subject = line.rstrip()

    based = "abracadabra"
    subject = "candelabra"
    seq = SequenceAlign(based,subject)
    print(seq.solve())
    seq.debug()
