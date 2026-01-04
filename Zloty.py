class Zloty(float):
    def __add__(self, other):
        return Zloty(super().__add__(other))

    def zmien_na_euro(self):
        return self / 4.21

a = Zloty(4)
b = Zloty(7)

c = a + b
print(c)
print(c.zmien_na_euro())