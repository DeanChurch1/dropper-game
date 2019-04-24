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
    #load img
    image = games.load_image("sprites/present.png")
    speed = 5
    def __init__(self,x ,y = 90):
        super(Present,self).__init__(image = Present.image, x = x, y = y, dy = Present.speed)

    def update(self):
        self.start_game()
        if self.top > games.screen.height:
            self.destroy()
            self.end_game()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 120,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 2*games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

    def start_game(self):
        start_message = games.Message(value = "Santa is on a rampage. He's dropping all the \nchildrens presents and it's up to you to stop him.",
                                      size = 30,
                                      color = color.purple,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 2*games.screen.fps)
        games.screen.add(start_message)
                                      
        


        

class Bag(games.Sprite):
    image = games.load_image("sprites/bag.png")
    def __init__(self):
        super(Bag,self).__init__(image = Bag.image,x=games.mouse.x, bottom = games.screen.height)

        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        
    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

        
    def check_catch(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_caught()
            self.score.value += 10
            self.score.right = games.screen.width - 10
            
    

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
        self.check_drop()                

            
    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_present = Present(x = self.x)
            games.screen.add(new_present)
            self.time_til_drop = random.randrange(10,200)
    

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
    #the_present = Present(200)



    #draw objs to screen
    games.screen.background = wall_image
    games.screen.add(the_bag)
    games.screen.add(the_santa)
    #games.screen.add(the_present)



    #set up mouse
    games.mouse.is_visible = False
    games.mouse.event_grab = False




    #start game loop
    games.screen.mainloop()









#Startup
main()








