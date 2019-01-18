global x
global y
global screen
global obstacles
obstacles = [[900, 50, 250, 400], [50, 50, 350, 200], [900, 590, 250, 160], [50, 550, 400, 200]]
x = 600
y = 600
screen = 0

def setup():
    global img_floor
    global img_door
    global img_croppedfloor
    global img_grass
    size(1200, 800)
    background(0)
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
        character_movement()
        graphics()
        screen_change()
        display_location()

    if screen == 2:
        background(135,206,250)
        character_movement()
        screen_change()
        graphics()
        
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
        
def graphics():
    rect(50, 50, 1100, 700)
    image(img_floor, 50, 50)
    image(img_floor, 50, 145)
    image(img_floor, 50, 240)
    image(img_floor, 50, 335)
    image(img_floor, 50, 430)
    image(img_floor, 50, 525)
    image(img_floor, 50, 620)
    image(img_door, 510, 40)
    image(img_croppedfloor, 780, 50)
    image(img_floor, 355, 145)
    image(img_croppedfloor, 780, 240)
    image(img_floor, 355, 335)
    image(img_croppedfloor, 780, 430)
    image(img_floor, 355, 525)
    image(img_croppedfloor, 780, 620)
    image(img_floor, 355, 655)
    img_door.resize(160, 50)
    #display cabinet
    rect(*obstacles[0])
    #couch
    rect(*obstacles[1])
    #treasure chest
    rect(*obstacles[2])
    #T.V.
    rect(*obstacles[3])
    fill(255)
    rect(x, y, 60, 60)
    
    
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
        text("press i to open chest", 760, 550)
        if keyPressed:
            if (key == "i"):
                screen = 5
    if (x >= 800 and x <= 900 and y >= 100 and y <= 400):
        textSize(15)
        text("press x to inspect", 700, 250)
        if (keyPressed):
            if (key == 'x'):
                screen = 3
    if (keyPressed):
        if (key == 'j'):
            screen += 1
            
            
def display_location():
    global x
    global y
    textSize(15)
    text(str(x), 10, 20)
    text(str(y), 10, 40)


        
def character_movement():
    global x, y

    if keyPressed and key == CODED:
        if keyCode == UP and y >= 50:
            y -= 5
            if point_collide(x,y) == True:
                y += 5
        
        elif (keyCode == DOWN and y <= 690):
            y += 5
            if point_collide(x,y) == True:
                y -= 5 

        elif (keyCode == LEFT and x >= 50):
            x -= 5
            if point_collide(x,y) == True:
                x += 5

        elif (keyCode == RIGHT and x <= 1090):
            x += 5
            if point_collide(x,y) == True:
                x -= 5

        
def point_collide(playerx, playery):
    global obstacles
    
    player_x1 = x
    player_x2 = x + 60
    player_y1 = y
    player_y2 = y + 60
    
    
    
    for furniture in obstacles:
        x_coll = False
        y_coll = False
        
        obstical_x1 = furniture[0]
        obstical_y1 = furniture[1]
        obstical_x2 = furniture[0] + furniture[2]
        obstical_y2 = furniture[1] + furniture[3]
        
        noFill()
        stroke(0, 255, 0)
        rect(*furniture)
        
        if (player_x2 >= obstical_x1) and (player_x1 <= obstical_x2):
            print(frameCount, "x_coll")
            x_coll = True
            
        if (player_y2 >= obstical_y1) and (player_y1 <= obstical_y2):
            print(frameCount, "y_coll")
            y_coll = True
        
        if x_coll is True and y_coll is True:
            return True
        
    return False
            

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
