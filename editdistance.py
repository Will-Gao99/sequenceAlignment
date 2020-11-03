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
        self.result1 = []
        self.result2 = []
        self.alignment = []
        self.opt = {}

        #initializing opt table
        for i in range(len(self.based)+1):
            self.opt[(i,0)] = i*gapPenalty
        for j in range(len(self.subject)+1):
            self.opt[(0,j)] = j*gapPenalty

    def editDistance(self):
        subLen = len(self.subject)
        baseLen = len(self.based)
        for j in range(1,subLen+1):
            for i in range(1,baseLen+1):
                #print((i,j))
                self.opt[(i,j)] = min(alpha(self.based[i-1],self.subject[j-1])+self.opt[(i-1,j-1)],gapPenalty+self.opt[(i-1,j)],gapPenalty+self.opt[(i,j-1)])
        return self.opt[(baseLen,subLen)]

    def backtrace(self, i, j):
        if (i==0 or j==0):
            pass
        elif self.opt[(i,j)] == alpha(self.based[i-1],self.subject[j-1])+self.opt[(i-1,j-1)]:
            self.result1.insert(0,i)
            self.result2.insert(0,j)
            self.alignment.insert(0,(i,j))
            self.backtrace(i-1,j-1)
        else:
            if gapPenalty+self.opt[(i-1,j)] < gapPenalty+self.opt[(i,j-1)]:
                self.result1.insert(0,i)
                self.result2.insert(0,0)
                self.backtrace(i-1,j)
            else:
                self.result1.insert(0,0)
                self.result2.insert(0,j)
                self.backtrace(i,j-1)

    def stringBuild(self):
        if self.result1[0] != 1:
            counter = self.result1[0]
            while counter != 1:
                self.result1.insert(0,counter-1)
                self.result2.insert(0,0)
                counter -= 1
        elif self.result2[0] != 1:
            counter = self.result2[0]
            while counter != 1:
                self.result1.insert(0,0)
                self.result2.insert(0,counter-1)
                counter -= 1


    def solve(self):
        editDist = self.editDistance()
        self.backtrace(len(self.based),len(self.subject))
        #(self.alignment)
        self.stringBuild()
        out = str(editDist) + "\n"
        for i in self.result1:
            if i == 0:
                out += " "
            else:
                out += self.based[i-1]
        out += "\n"
        for i in self.result2:
            if i == 0:
                out += " "
            else:
                out += self.subject[i-1]
        out += "\n"
        print(out)

    def debug(self):
        out = ""
        for i in range(len(self.based)+1):
            for j in range(len(self.subject)+1):
                out += (str((i,j))+"="+str(self.opt[(i,j)]))
            out += "\n"
        print(self.opt.keys())
        print(out)

if __name__ == "__main__":
    inp=sys.stdin.readlines()
    idx = 0
    based = ""
    subject= ""
    for line in inp:
        if i == 0:
            inp1 = line.rstrip()
            i += 1
        else:
            inp2 = line.rstrip()

    # inp1 = "abracadabra"
    # inp2 = "candelabra"
    seq = SequenceAlign(inp1,inp2)
    seq.solve()
    #seq.debug()
