class Mynumbers:
    def __iter__(self):
      self= 1
      return self
    def __iter__(self):
      x = self
      self +=1
      return x

myclass= Mynumbers()
myiter= iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))