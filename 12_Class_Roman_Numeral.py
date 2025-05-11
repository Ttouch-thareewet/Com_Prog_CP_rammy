class roman :
    def __init__(self, r):
        self.rmn = r

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return self.rmn

    def __int__(self):
        self.n = 0
        prev = 0
        value = {'I': 1, 'V': 5, 
                 'X': 10, 'L': 50, 
                 'C': 100, 'D': 500, 
                 'M': 1000}
        
        for char in self.rmn[::-1]:
            current = value[char]
            if current < prev:
                self.n -= current
            else:
                self.n += current
            prev = current
        return self.n

    def __add__(self, rhs):
        x = int(self) + int(rhs)
        base = [1000, 500, 100, 50, 10, 5, 1]
        out = ""

        a = x // 1000
        out += 'M' * a
        x %= 1000

        a = x // 100
        if a == 9:
            out += 'CM'
        elif a in [5,6,7,8]:
            out += 'D' + 'C' * (a%5)
        elif a == 4:
            out += 'CD'
        elif a in [3,2,1,0]:
            out += 'C' * a
        x %= 100

        a = x // 10
        if a == 9:
            out += 'XC'
        elif a in [5,6,7,8]:
            out += 'L' + 'X' * (a%5)
        elif a == 4:
            out += 'XL'
        elif a in [3,2,1,0]:
            out += 'X' * a
        x %= 10

        if x == 9:
            out += 'IX'
        elif x in [5,6,7,8]:
            out += 'V' + 'I' * (x%5)
        elif x == 4:
            out += 'IV'
        elif x in [3,2,1,0]:
            out += 'I' * x
        
        self.rmn = out
        return self

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))