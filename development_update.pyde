global x
global y
global screen
global obstacles
timeElapsed = None
room_obstacles = [[50, 50, 410, 195], [900, 50, 250, 165], [50, 580, 480, 170], [110, 320, 280, 90], [940, 545, 5, 200]]
outdoor_obstacles = [[220, 150, 256, 256], [800, 120, 256, 256], [95, 450, 198, 170], [835, 435, 100, 180]]
upstairs_obstacles = []
x = 600
y = 600
y2 = 610
screen = 0

def setup():
    global img_floor
    global img_door
    global img_croppedfloor
    global img_couch
    global img_chest
    global img_desk
    global img_carpet
    global img_stairs
    global img_table
    global img_grass
    global img_tree
    global img_berry
    global img_grassCropped
    global img_grassCropped2
    global img_grassCropped3
    global img_ted_down
    global img_ted_left
    size(1200, 800)
    background(0)
    img_floor = loadImage("FloorPixel.png")
    img_door = loadImage("door.png")
    img_croppedfloor = loadImage("FloorPixelCropped.png")
    img_couch =loadImage("couch.png")
    img_chest = loadImage("chest.png")
    img_desk = loadImage("desk.png")
    img_carpet = loadImage("carpet.png")
    img_stairs = loadImage("stairs.png")
    img_table = loadImage("table.png")
    img_grass = loadImage("grass.png")
    img_tree = loadImage("tree.png")
    img_berry = loadImage("berry.png")
    img_grassCropped = loadImage("grassCropped.png")
    img_grassCropped2 = loadImage("grassCropped2.png")
    img_grassCropped3 = loadImage("grassCropped3.png") 
    img_ted_down = loadImage("tedDown.png")
    img_ted_left = loadImage("tedLeft.png")


def draw():
    global screen
    noFill()
    #character
    rect(x, y + 80, 60, 60)
    
    if screen == 0:
        background(0, 0, 205)
        fill(255)
        main_menu()
    
    if screen == 1:
        background(0)
        character_movement()
        room_graphics()
        room_screen_change()
        display_location()

    if screen == 2:
        outdoor_scene()
        
    if screen == 3:
        upstairs()
        
    if screen == 4:
        background(0)
        fill(255)
        text("I can only live where there is light, but I die if the light shines on me. What I am I?", 50, 50)
        if keyPressed:
            if (key =='q'):
                screen = 1
        if keyPressed:
            if (key == 'w'):
                screen = 2
                
    if screen == 5:
        background(0, 0, 205)
        textSize(30)
        text("You check the funiture for pieces of a riddle,", 30, 50)
        text("once you obtain the anwser you must input the answer in to the treasure chest to win", 30, 90)
        text("answer in to the treasure chest to win", 30, 130)
        textSize(30)
        text("Back", 1000, 600)
        if (mouseX >= 1000 and mouseX <= 1050 and mouseY >= 590 and mouseY <= 615 
            and mousePressed):
            screen = 0
              
    if screen == 6:
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
    if screen == 7:
        background(0)
        textSize(50)
        text("WINNER, WINNER!", 500, 550)
        
    if screen == 8:
        import time
        global timeElapsed
        
        timeElapsed = timeElapsed or millis()
        
        background(0)
        
        fill(255)
        textSize(20)
        text("What's your name?", 300, 400)
        
        if millis() > timeElapsed + 2500:
            fill(255)
            textSize(20)
            text("Just kidding. We don't care.", 300, 500)
             
        if millis() > timeElapsed + 5000:
            fill(255)
            textSize(20)
            text("Your new name is Ted Bundy.", 300, 600)
        
        if millis() > timeElapsed + 8000:
            timeElapsed = None
            screen = 1
   
        
def room_graphics():
    global obstacles
    global x
    global y
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
    image(img_stairs, 945, 540)
    image(img_stairs, 945, 640)
    image(img_table, 110, 320)
    image(img_ted_down, x, y)
    noFill()
    #couch
    rect(*room_obstacles[0])
    #treasure chest
    rect(*room_obstacles[1])
    #goldfish
    rect(*room_obstacles[2])
    #table
    rect(*room_obstacles[3])
    #stairs
    rect(*room_obstacles[4])

def bedroom_graphics():
    global obstacles
    image(img_floor, 50, 50)
    image(img_floor, 50, 145)
    image(img_floor, 50, 240)
    image(img_floor, 50, 335)
    image(img_floor, 50, 430)
    image(img_floor, 50, 525)
    image(img_floor, 50, 620)
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
    
def room_screen_change():
    global x
    global y
    global screen
    if (x >= 510 and x <= 610 and y >= 45 and y <= 100):
        textSize(15)
        text("press i to go outside", 520, 150)
        if keyPressed:
            if (key == "i"):
                screen = 2
    #stairs
    if (x >= 800 and x <= 900 and y >= 600 and y <= 750):
        textSize(15)
        text("press x to inspect", 760, 550)
        if keyPressed:
            if (key == "x"):
                screen = 3
    #chest
    if (x >= 900 and x <= 1050 and y >= 50 and y <= 280):
        textSize(15)
        text("press o to open chest", 700, 250)
        if (keyPressed):
            if (key == 'o'):
                screen = 5
    #couch
    if (x >= 100 and x <= 350 and y >= 50 and y <= 280):
        textSize(15)
        text("press x to inspect", 200, 250)
        if (keyPressed):
            if (key == 'x'):
                screen = 5
    #goldfish
    if (x >= 100 and x <= 350 and y >= 500 and y <= 1050):
        textSize(15)
        text("press x to inspect", 300, 550)
        if (keyPressed):
            if (key == 'x'):
                screen = 5
    #upstairs
    if (keyPressed):
        if (x >= 950 and x <= 1050 and y >= 680 and y <= 750):
            textSize(15)
            text("press i to go upstairs", 770, 600)
            if keyPressed:
                if (key == "i"):
                    screen = 3
            
def display_location():
    global x, y
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
            image(img_ted_down, x, y)
            if point_collide(x,y) == True:
                y -= 5 

        if (keyCode == LEFT and x >= 50):
            x -= 5
            image(img_ted_left, x, y)
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
    
    
    
    for furniture in room_obstacles:
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

        
        
def outdoor_scene():
    outdoor_graphics()
    outdoor_screenchange()
    outdoor_displaylocation()
    outdoor_movement()
    
def outdoor_screenchange():
    global screen
    if (keyPressed):
        if (key == 'x'):
            screen = 3
    if (x >= 510 and x <= 618 and y2 >= 633 and y2 <= 690):
        textSize(15)
        text("press O to go inside", 510, 650)
        if (keyPressed):
            if (key == 'o'):
                screen = 1
                
def outdoor_graphics():
    background(135,206,250)
    rect(50, 50, 1100, 700)
    image(img_grass, 50, 50)
    image(img_grass, 519, 50)
    image(img_grass, 50, 355)
    image(img_grass, 519, 355)
    image(img_grassCropped, 50, 450)
    image(img_grassCropped, 519, 450)
    image(img_grassCropped2, 989, 50)
    image(img_grassCropped2, 989, 350)
    image(img_grassCropped3, 989, 655)
    image(img_door, 510, 690)
    image(img_tree, 220, 150)
    image(img_tree, 800, 120)
    image(img_berry, 95,450)
    fill(255)
    rect(x, y2, 60, 60)    

def outdoor_displaylocation():
    global x
    textSize(15)
    text(str(x), 10, 20)
    text(str(y2), 10, 40)
    
def outdoor_pc(playerx, playery2):
    global outdoor_obstacles
    
    player_x1 = x
    player_x2 = x + 60
    player_y1 = y2
    player_y2 = y2 + 60
    
    
    
    for nature in outdoor_obstacles:
        x_coll = False
        y_coll = False
        
        obstical_x1 = nature[0]
        obstical_y1 = nature[1]
        obstical_x2 = nature[0] + nature[2]
        obstical_y2 = nature[1] + nature[3]
        

        noFill()
        stroke(0, 255, 0)
        rect(*nature)
        
        if (player_x2 >= obstical_x1) and (player_x1 <= obstical_x2):
            x_coll = True
            
        if (player_y2 >= obstical_y1) and (player_y1 <= obstical_y2):
            y_coll = True
        
        if x_coll == True and y_coll == True:
            return True
        
    return False    

def outdoor_movement():
    global x, y2
    
    if keyPressed and key == CODED:
        if keyCode == UP and y2 >= 50:
            y2 -= 5
            if outdoor_pc(x,y2) == True:
                y2 += 5
        
        if (keyCode == DOWN and y2 <= 690):
            y2 += 5
            if outdoor_pc(x,y2) == True:
                y2 -= 5 

        if (keyCode == LEFT and x >= 50):
            x -= 5
            if outdoor_pc(x,y2) == True:
                x += 5

        if (keyCode == RIGHT and x <= 1090):
            x += 5
            if outdoor_pc(x,y2) == True:
                x -= 5
def upstairs():
    background(0)
    upstairs_movement()
    bedroom_graphics()
    display_location()
    bedroom_screen_change()
    #bedroom_screen_change()
    if keyPressed:
        if key == 'e':
            screen = 1
            
def upstairs_pc(playerx, playery):
    global obstacles
    
    player_x1 = x
    player_x2 = x + 60
    player_y1 = y
    player_y2 = y + 60
    
    
    
    for upstairs in upstairs_obstacles:
        x_coll = False
        y_coll = False
        
        obstical_x1 = upstairs[0]
        obstical_y1 = upstairs[1]
        obstical_x2 = upstairs[0] + upstairs[2]
        obstical_y2 = upstairs[1] + upstairs[3]
        

        noFill()
        stroke(0, 255, 0)
        rect(*upstairs)
        
        if (player_x2 >= obstical_x1) and (player_x1 <= obstical_x2):
            x_coll = True
            
        if (player_y2 >= obstical_y1) and (player_y1 <= obstical_y2):
            y_coll = True
        
        if x_coll is True and y_coll is True:
            return True
        
    return False
            
def upstairs_movement():
    global x, y

    if keyPressed and key == CODED:
        if keyCode == UP and y >= 50:
            y -= 5
            if upstairs_pc(x,y) == True:
                y += 5
        
        if (keyCode == DOWN and y <= 690):
            y += 5
            if upstairs_pc(x,y) == True:
                y -= 5 

        if (keyCode == LEFT and x >= 50):
            x -= 5
            if upstairs_pc(x,y) == True:
                x += 5

        if (keyCode == RIGHT and x <= 1090):
            x += 5
            if upstairs_pc(x,y) == True:
                x -= 5
    
        
