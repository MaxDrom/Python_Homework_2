class SuperList(list):
    def save(self, filename):
        types = {}
        types[float] = "float"
        types[int] = "int"
        file = open(filename, 'w')
        file.writelines([f'{types[type(element)]} {element}\n' for element in self])
        file.close()
    
    @classmethod
    def load(self, filename):
        casts = {}
        casts["float"] = lambda x: float(x)
        casts["int"] = lambda x: int(x)
        file = open(filename, 'r')
        res = []
        for line in file:
            (t, value) = line.split(" ")
            res.append(casts[t](value))
        file.close()
        return SuperList(res)

a = SuperList([5,4,3, 10.0, 20.0])
a.save("test1.txt")
b = SuperList.load("test2.txt")
print(*b)
