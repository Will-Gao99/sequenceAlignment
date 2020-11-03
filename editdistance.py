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
        for i in range(len(based)):
            self.opt[(i,0)] = i*gapPenalty
        for j in range(len(subject)):
            self.opt[(0,j)] = j*gapPenalty

    def solve(self):
        for j in range(1,len(subject)):
            for i in range(1,len(based)):
                print((i,j))
                self.opt[(i,j)] = min(alpha(based[i],subject[j])+self.opt[(i-1,j-1)],gapPenalty+self.opt[(i-1,j)],gapPenalty+self.opt[(i,j-1)])
        return self.opt[(len(based)-1,len(subject)-1)]

    def debug(self):
        out = ""
        for i in range(len(based)):
            for j in range(len(subject)):
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

    based = "stop"
    subject = "tops"
    seq = SequenceAlign(based,subject)
    print(seq.solve())
    seq.debug()
