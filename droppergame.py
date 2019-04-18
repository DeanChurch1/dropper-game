#Dropper Game
#Dean Church
#4/18/19

#imports
from superwires import games, color
import random



#screen creation

games.init(screen_width = 640, screen_height = 480,fps=60)







#Classes
class Present(games.Sprite):
    pass

class Bag(games.Sprite):
    image = games.load_image("sprites/bag.png")
    def __init__(self):
        super(Bag,self).__init__(image = Bag.image,x=games.mouse.x, bottom = games.screen.height)
    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()
    def check_catch(self):
        pass
    

class Santa(games.Sprite):
    image = games.load_image("sprites/character.png")
    def __init__(self, y=55, speed = 5, odds_change = 100):
        super(Santa,self).__init__(image = Santa.image, x = games.screen.width / 2, y = y, dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
                              

            
    def check_drop(self):
        pass
    

class ScText(games.Text):
    #def update(self):
        #self.value = SCORE
    pass










#Main
def main():

    #load img's
    wall_image = games.load_image("sprites/background.JPG",transparent = False)
    



    #create game objs
    the_bag = Bag()
    the_santa = Santa()



    #draw objs to screen
    games.screen.background = wall_image
    games.screen.add(the_bag)
    games.screen.add(the_santa)




    #set up mouse
    games.mouse.is_visible = False
    games.mouse.event_grab = False




    #start game loop
    games.screen.mainloop()









#Startup
main()








