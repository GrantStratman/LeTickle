from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation
from kivy.uix.button import Button
import random
from kivy.config import Config
<<<<<<< HEAD
from kivy.uix.progressbar import ProgressBar
=======
import time
>>>>>>> 143935aebd58e797781adc7ad85ebb65e6e56cde

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
Config.write()

tickles = 0
        
class LeTickleApp(App): 
    def build(self): 
        btn = Button(text ="",
                     color =(1, 0, .65, 1),
                     background_normal = 'lebron.png',
                     background_down ='lebronBlush4.png',
                     size_hint = (.3, .3),
                     pos = (0,0),
                   ) 
        btn.bind(on_press = lambda x: self.callback(btn))
        return btn 
    def callback(self,btn):
        animation = Animation(pos=(random.randint(0,960),random.randint(0,540)), t='in_out_back')
        animation.start(btn)
        global tickles
        tickles += 1
        if tickles > 5 and tickles <= 10:
            btn.background_normal = 'lebronBlush1.png'
        elif tickles > 10 and tickles <= 15:
            btn.background_normal = 'lebronBlush2.png'
        elif tickles > 15 and tickles <= 20:
            btn.background_normal = 'lebronBlush3.png'
        elif tickles > 20:
            btn.background_normal = 'lebronBlush4.png'
            
class progressBar(ProgressBar):
    pb = ProgressBar(max=100, value = 0,
                     pos_hint = {'center_x': .5, 'center_y': .5},
                     size_hint_x = .8,
                     size_hint = (.3, .3),
                     pos = (0,0)
                   )

    
root = LeTickleApp() 
    
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()
