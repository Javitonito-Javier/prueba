from kivy.app import App
from kivy.clock import Clock


import kivy
kivy.require('2.0.0')

class Popp(App)
    def funcname(dt):
        print("Hello")
    event=Clock.schedule_internal(funcname,1/30.)
    return event
if if __name__ == "__main__":
    clockk=Popp()
    clockk.run()