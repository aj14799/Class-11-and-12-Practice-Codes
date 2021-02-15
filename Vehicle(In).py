# Vehicle Class(Inheritance)
class vehicle(object):
    def __init__(self, l=0, w=0):
        self.l= l
        self.w = w

    def define(self):
        print('Vechile with length', self.l, '\n and width', self.w,'in.')
class Car(vehicle):
    def __init__(self, clr, seats, l, w):
        vehicle.__init__(self, l, w)
        self.colour = clr
        self.seat = seats

    def chgear(self, gr):
        print('Changed to gear', gr)

    def turn(self, dr):
        print('Turned to direction', dr)

class RacingCar(Car):
    def __init__(self, clr, seats, l, w, tr, spd):
        Car.__init__(self, clr, seats, l, w)
        self.tr = tr
        self.spd= spd
        print ('racing car instance created')

    def start(self):
        self.define()
        self.chgear(2)
        print('Racing car starts - ready to droom!')

#-----Main-----
r=RacingCar("Blue",2, 204, 360, 6, 350)
r.start()
r.turn('left')
