#Dean Church

#all objects
#event_grab
#add(sprite)
#clear()
#mainloop()
#quit()

import random
from superwires import games,color

SCORE = 0



class Bag(games.Sprite):
    """ A pan controlled by the mouse. """
    def update(self):
        """Move to mouse coordinates"""
        self.x = games.mouse.x
        #self.y = games.mouse.y
        self.check_collide()
    def check_collide(self):
        """Check for collision with pizzas"""
        for present in self.overlapping_sprites:
            present.handle_collide()

class Present(games.Sprite):

    def update(self):
        global SCORE

#Bouncing       
##        if self.right > games.screen.width or self.left< 0:
##            self.dx = -self.dx
##            SCORE += 1
##        
##        if self.bottom > games.screen.height or self.top < 0:
##            self.dy = -self.dy
##            SCORE += 1
    
#teleporting        
        if self.left > games.screen.width:
            self.right = 0
            SCORE += 1
        if self.right < 0:
            self.left = games.screen.width
            SCORE += 1
        if self.top > games.screen.height:
            self.top = 0
            SCORE += 1
        if self.bottom < 0:
            self.bottom = games.screen.height+1
            SCORE += 1

    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)
        


class ScText(games.Text):
    def update(self):
        self.value = SCORE
        
        

def main():
    
    SW=640
    SH=480
  
    games.init(screen_width = SW, screen_height = SH, fps=60)

    #background
    bg_img = games.load_image("sprites/background.jpg",transparent=False)
    games.screen.background = bg_img
    #character
    ch_img = games.load_image("sprites/character.png",transparent=True)
    character = games.Sprite(image=ch_img, x=SW/3, y=SH/3)
    games.screen.add(character)
    

    #present
    present_img = games.load_image("sprites/present.png", transparent=True)

    present = Present(image = present_img,
                    x=SW/2,
                    y=SH/2,
                    dx= random.randint(-10,10),
                    dy= random.randint(-10,10))
    present2 = Present(image = present_img,
                    x=SW/2,
                    y=SH/2,
                    dx= random.randint(-10,10),
                    dy= random.randint(-10,10))
    present3 = Present(image = present_img,
                    x=SW/2,
                    y=SH/2,
                    dx= random.randint(-10,10),
                    dy= random.randint(-10,10))
    
    #bag
    bag_img = games.load_image("sprites/bag.png",transparent=True)
    bag = Bag(image = bag_img,
              x = games.mouse.x,
              y = 420)
                
    #Creating txt object
    score = ScText(value=SCORE,
                   size = 60,
                   is_collideable = False,
                   color = color.black,
                   x = 550,
                   y = 30
                   )

    #Putting objects on screen
    games.screen.add(score)
    games.screen.add(present)
    games.screen.add(present2)
    games.screen.add(present3)
    games.screen.add(bag)

    #makes mouse invisible
    games.mouse.is_visible = False
    #locks screen
    games.screen.event_grab = False
    
    #starts mainloop
    games.screen.mainloop()

main()
