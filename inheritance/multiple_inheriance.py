# multiple inheritance should be used sparingly
# it can complicate things very quickly

class Flyer:
    def fly(self):
        print("me fly")

    def sleep(self):
        print("me land and sleep")


class Swimmer:
    def swim(self):
        print("me swim")

    def sleep(self):
        print("me swim and sleep")


class FlyingFish(Flyer, Swimmer):
    pass


f = FlyingFish()

f.fly()
f.swim()

f.sleep()
