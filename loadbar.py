class LoadBar():
    def __init__(self, len):
        self.char = '#'
        self.len = len
        self.loaderlen = 50

    def printbar(self, prog):
        per = prog / self.len
        print('|',end='')
        black = self.loaderlen * per
        b = []
        for i in range(int(black)):
            b.append(self.char)
        print(''.join(b), end='')
        w = []
        for i in range(self.loaderlen - int(black)):
            w.append(' ')
        print(''.join(w), end='|')
        print('Progress: ' + str(round(per * 100.0, 2)) + '%', end='\r')