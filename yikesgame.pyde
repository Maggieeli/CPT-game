global x
global y
global screen
x = 60
y = 60
y2 = 609
screen = 0

def setup():
    size(1200, 800)
    background(0)
    global img_floor
    global img_door
    global img_croppedfloor
    global img_grass
    img_floor = loadImage("FloorPixel.png")
    img_door = loadImage("door.png")
    img_croppedfloor = loadImage("FloorPixelCropped.png")
    img_grass = loadImage("grass.png")
    
def draw():
    global screen
    global img_floor
    global img_door
    global img_grass
    if screen == 0:
        background(0, 0, 205)
        fill(255)
        main_menu()
    
    if screen == 1:
        background(0)
        def screen_change():
            global x
            global y
            global screen
            if (x >= 510 and x <= 610 and y >= 48 and
            y <= 90):
                textSize(15)
                text("press i to go outside", 510, 110)
                if keyPressed:
                    if (key == "i"):
                        screen = 2
            if (x >= 850 and x <= 1150 and y >= 540 and 
                y <= 750):
                textSize(15)
                text("press i to open chest", 760, 600)
                if keyPressed:
                    if (key == "i"):
                        screen = 5
            if (x >= 850 and x <= 900 and y >= 100 and y <= 400):
                textSize(15)
                text("press x to inspect", 700, 250)
                if (keyPressed):
                    if (key == 'x'):
                        screen = 3
            if (keyPressed):
                if (key == 'j'):
                    screen += 1
            
        character_movement()
        screen_change()
        display_location()
        point_collide(x,y)

    if screen == 2:
        screen2()
        
    if screen == 3:
        background(0)
        fill(255)
        text("I can only live where there is light, but I die if the light shines on me. What I am I?", 50, 50)
        if keyPressed:
            if (key =='q'):
                screen = 1
        if keyPressed:
            if (key == 'w'):
                screen = 2
                
    if screen == 4:
        background(0, 0, 205)
        textSize(50)
        text("You check the funiture for pieces of a riddle,", 50, 50)
        text("once you obtain the anwser you must input the answer in to the treasure chest to win", 50, 90)
        text("answer in to the treasure chest to win", 50, 130)
        textSize(30)
        text("Back", 1000, 600)
        if (mouseX >= 1000 and mouseX <= 1050 and mouseY >= 590 and mouseY <= 615 
            and mousePressed):
            screen = 0
              
    if screen == 5:
        background(0)
        textSize(50)
        text("Input Code Here", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
            and mousePressed):
            screen = 1
        
def character_movement():
    if keyPressed:
        global x
        global y
        if (key == CODED):
            if (keyCode == UP and y > 50):
                y -= 3
            elif (keyCode == DOWN and y < 690):
                y += 3
            elif (keyCode == LEFT and x > 50):
                x -= 3
            elif (keyCode == RIGHT and x < 1090):
                x += 3
                
def point_collide(playerx, playery):
    x = playerx
    y = playery
    
    player_x1 = x
    player_x2 = x + 50
    player_y1 = y
    player_y2 = y + 50
    
    x_coll = False
    y_coll = False
    x_coll1 = False
    y_coll1 = False
    

    ar = [[50, 50, 50, 50]]
    
    
    for line in ar:
        obstical_x1 = line[0]
        obstical_y1 = line[1]
        obstical_x2 = line[0] + line[2]
        obstical_y2 = line[1] + line[3]
        
        if (player_x1 < obstical_x1) or (player_x1 > obstical_x2):
            x_coll = True
        
        if (player_x2 < obstical_x1) or (player_x2 > obstical_x2):
            x_coll1 = True
            
        if (player_y1 < obstical_y1) or (player_y1 > obstical_y2):
            y_coll = True
        
        if (player_y2 < obstical_y1) or (player_y2 > obstical_y2):
            y_coll1 = True
        
        if (x_coll == True and y_coll == True) and (x_coll1 == True and y_coll1 == True):

            print('within funiture')
        
        else:
            print("outside of funiture")
            
        x_coll = False
        y_coll = False
        x_coll1 = False
        y_coll1 = False
        
def main_menu():
    global screen
    textSize(70)
    text("Welcome To Yikes", 320, 300)
    textSize(50)
    text("Play", 550, 500)
    text("How to Play", 450, 600)
    if (mouseX >= 550 and mouseX <= 650 and mouseY >= 475 and
    mouseY <= 515 and mousePressed):
        screen = 1
    if (mouseX >= 500 and mouseX <= 775 and mouseY >= 575 and mouseY <=615
        and mousePressed):
        screen = 4

def display_location():
    global x
    global y
    textSize(15)
    text(str(x), 10, 20)
    text(str(y), 10, 40)
    
def screen2():
    global y2
    global screen
    def outdoor_graphics():
        background(135,206,250)
        rect(50, 50, 1100, 700)
        image(img_grass, 50, 50)
        image(img_grass, 519, 50)
        image(img_grass, 50, 450)
        image(img_grass, 519, 450)
        image(img_door, 510, 690)
        img_door.resize(160, 50)
        fill(255)
        rect(x, y2, 60, 60)
    if (x >= 510 and x <= 618 and y2 >= 633 and y2 <= 690):
        textSize(15)
        text("press i to go inside", 510, 650)
        if (keyPressed):
            if (key == 'i'):
                screen = 1
    if keyPressed:
        global x
        if (key == CODED):
            if (keyCode == UP and y2 > 50):
                y2 -= 3
            elif (keyCode == DOWN and y2 < 690):
                y2 += 3
            elif (keyCode == LEFT and x > 50):
                x -= 3
            elif (keyCode == RIGHT and x < 1090):
                x += 3
    def outdoor_screenchange():
        global screen
        if (keyPressed):
            if (key == 'x'):
                screen = 3
    def display_location2():
        global x
        textSize(15)
        text(str(x), 10, 20)
        text(str(y2), 10, 40)
    outdoor_screenchange()
    display_location2()
    outdoor_graphics()
