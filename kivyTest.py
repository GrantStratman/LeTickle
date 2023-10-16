from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation
from kivy.uix.button import Button
import random
from kivy.config import Config
from kivy.uix.progressbar import ProgressBar

Config.set('graphics', 'width', '960')
Config.set('graphics', 'height', '540')
Config.write()
        
class ButtonApp(App): 
    def build(self): 
        btn = Button(text ="",
                     color =(1, 0, .65, 1),
                     background_normal = 'lebron.png',
                     background_down ='lebron2.png',
                     size_hint = (.3, .3),
                     pos = (0,0)
                   ) 
        btn.bind(on_press =lambda x:self.callback(btn))
        return btn 
    def callback(self,btn):
        animation = Animation(pos=(random.randint(0,960),random.randint(0,540)), t='in_out_back')
        animation.start(btn)
        print("tickle")
            
class progressBar(ProgressBar):
    pb = ProgressBar(max=100, value = 0,
                     pos_hint = {'center_x': .5, 'center_y': .5},
                     size_hint_x = .8,
                     size_hint = (.3, .3),
                     pos = (0,0)
                   )

    
root = ButtonApp() 
    
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run()
