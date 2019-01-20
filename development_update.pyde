global x
global y
global screen
global obstacles
obstacles = [[950, 350, 200, 400], [50, 50, 410, 195], [900, 50, 250, 165], [50, 580, 480, 180]]
x = 600
y = 600
y2 = 609
screen = 0

def setup():
    global img_floor
    global img_door
    global img_croppedfloor
    global img_couch
    global img_grass
    global img_chest
    global img_desk
    global img_carpet
    global mono
    size(1200, 800)
    background(0)
    img_floor = loadImage("FloorPixel.png")
    img_door = loadImage("door.png")
    img_croppedfloor = loadImage("FloorPixelCropped.png")
    img_grass = loadImage("grass.png")
    img_couch =loadImage("couch.png")
    img_grass = loadImage("grass.png")
    img_chest = loadImage("chest.png")
    img_desk = loadImage("desk.png")
    img_carpet = loadImage("carpet.png")
    mono = loadFont("LucidaSans-Typewriter-48.vlw")

def draw():
    global screen   
    if screen == 0:
        background(0, 0, 205)
        fill(255)
        main_menu()
    
    if screen == 1:
        background(0)
        character_movement()
        living_room_graphics()
        living_room_screen_change()
        display_location()

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
        textSize(30)
        textFont(mono)
        text("You check the funiture for pieces of a riddle,", 30, 50)
        text("once you obtain the anwser you must input the answer in to the treasure chest to win", 30, 90)
        text("answer in to the treasure chest to win", 30, 130)
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
        '''
        a = ""
        guess = ""
        answer = str("shadow")
        while guess != answer:
            if keyPressed:
                a = key
            guess += a
        if guess == answer:
            screen = 7
        '''
        
    if screen == 6:
        background(0)
        character_movement()
        bedroom_graphics()
        #bedroom_screen_change()
        display_location()
        if keyPressed:
            if key == 'e':
                screen = 1
    if screen == 7:
        background(0)
        textSize(50)
        text("WINNER, WINNER!", 500, 550)
            
        
def living_room_graphics():
    global obstacles
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
    image(img_floor, 50, 655)
    image(img_carpet, 200, 100)
    image(img_couch, 50, 50)
    image(img_chest, 900, 50)
    image(img_desk, 0, 525)
    #display cabinet
    noFill()
    rect(*obstacles[0])
    #couch
    rect(*obstacles[1])
    #treasure chest
    rect(*obstacles[2])
    #T.V.
    rect(*obstacles[3])
    fill(255)
    rect(x, y, 60, 60)

def bedroom_graphics():
    global obstacles
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
    image(img_floor, 50, 655)
    fill(255)
    rect(x, y, 60, 60)
    
def living_room_screen_change():
    global x
    global y
    global screen
    if (x >= 510 and x <= 610 and y >= 48 and
    y <= 90):
        textSize(15)
        text("press i to go outside", 520, 150)
        if keyPressed:
            if (key == "i"):
                screen = 2
    #chest
    if (x >= 800 and x <= 1150 and y >= 350 and y <= 750):
        textSize(15)
        text("press x to inspect", 760, 550)
        if keyPressed:
            if (key == "x"):
                screen = 3
    if (x >= 900 and x <= 1050 and y >= 50 and y <= 280):
        textSize(15)
        text("press o to open chest", 700, 250)
        if (keyPressed):
            if (key == 'o'):
                screen = 5
    if (keyPressed):
        if (key == 'j'):
            screen += 1
    if (x >= 510 and x <= 610 and y >= 600 and y <= 750):
        textSize(15)
        text("press i to go to the bedroom", 520, 550)
        if keyPressed:
            if (key == "i"):
                screen = 6
    #couch
    if (x >= 100 and x <= 350 and y >= 50 and y <= 280):
        textSize(15)
        text("press x to inspect", 200, 250)
        if (keyPressed):
            if (key == 'x'):
                screen = 5
    #goldfish
    if (x >= 100 and x <= 350 and y >= 400 and y <= 1050):
        textSize(15)
        text("press x to inspect", 200, 500)
        if (keyPressed):
            if (key == 'x'):
                screen = 5
            
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
        
        if (keyCode == DOWN and y <= 690):
            y += 5
            if point_collide(x,y) == True:
                y -= 5 

        if (keyCode == LEFT and x >= 50):
            x -= 5
            if point_collide(x,y) == True:
                x += 5

        if (keyCode == RIGHT and x <= 1090):
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

            x_coll = True
            
        if (player_y2 >= obstical_y1) and (player_y1 <= obstical_y2):
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
        fill(255)
        rect(x, y2, 60, 60)
    if (x >= 300 and x <= 900 and y2 >= 40 and y2 <= 600):
        textSize(15)
        text("press f to go inside", 500, 650)
        if (keyPressed):
            if (key == 'i'):
                screen = 1
    if keyPressed:
        global x
        global y2
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
    outdoor_screenchange()
        
