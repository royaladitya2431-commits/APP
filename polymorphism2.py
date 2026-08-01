class Bird:
    def sound(self):
        print("Chirp")

class Lion:
    def sound(self):
        print("Roar")

for obj in [Bird(), Lion()]:
    obj.sound()