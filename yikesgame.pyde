global x, y, y2
global screen
global obstacles
timeElapsed = None
room_obstacles = [[50, 50, 410, 195], [900, 50, 250, 165], [50, 580, 480, 170], [110, 320, 280, 90], [940, 545, 5, 200]]
x = 650
y = 650
outdoor_obstacles = [[170, 110, 256, 256], [800, 120, 256, 256], [230, 475, 198, 170], [785, 510, 178, 126]]
upstairs_obstacles = [[50, 285, 290,200], [300, 50, 505, 150]]
y2 = 610
screen = 0

def setup():
    #all images for main room
    global img_floor, img_door, img_croppedfloor, img_couch, img_chest, img_desk, img_carpet, img_stairs, img_table
    #all images for outside
    global img_grass, img_tree, img_berry, img_grassCropped, img_grassCropped2, img_grassCropped3, img_picnic
    #characters
    global img_ted_down, img_ted_left, img_ted_down, img_ted_right, img_ted_up
    #all images for bedroom
    global img_bed, img_bookshelf

  
   
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
    img_picnic = loadImage("picnic.png")
    img_ted_down = loadImage("tedDown.png")
    img_ted_left = loadImage("tedLeft.png")
    img_ted_right = loadImage("tedRight.png")
    img_ted_up = loadImage("tedUp.png")
    img_bed = loadImage("bed.png")
    img_bookshelf = loadImage("bookshelf.png")


def draw():
    global screen
    global x
    global y
    noFill()
    #character
    rect(x, y + 80, 60, 60)
    
    if screen == 0:
        background(0, 0, 205)
        fill(255)
        main_menu()
    
    if screen == 1:
        background(0)
        character_movement(x, y, room_obstacles)
        room_graphics()
        room_screenchange()
        display_location(x, y)
        character_animation(x, y)
        if keyPressed and key == "e":
            screen = 6

    if screen == 2:
        character_movement(x, y2, outdoor_obstacles)
        outdoor_graphics()
        outdoor_screenchange()
        display_location(x, y2)
        character_animation(x, y2)
        
    if screen == 3:
        background(0)
        character_movement(x, y, upstairs_obstacles)
        bedroom_graphics()
        display_location(x,y)
        bedroom_screenchange()
        character_animation(x, y)
        


        
    if screen == 4:
        background(0)
        fill(255)
        text("I can only live where there is light, but I die if the light shines on me. What am I?", 50, 50)

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

        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150 and mousePressed):
            screen = 1
        guess = ''
        guess += key 
        if guess == answer:
            screen = 7
        #else:
            #continue

    

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
   
    if screen == 17:
        background(0)
        textSize(50)
        text("is light", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
    
    if screen == 18:
        background(255,0,0)
        textSize(50)
        text("the light", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
            
    if screen == 19:
        background(0,0,255)
        textSize(50)
        text("I can", 500, 550)
        text("back", 50, 50)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
            
    if screen == 20:
        background(255)
        textSize(50)
        fill(0)
        text("am I?", 500, 550)
        text("back", 50, 50)
        fill(255)
        if (mouseX >= 0 and mouseX <= 150 and mouseY >= 0 and mouseY <= 150
        and mousePressed):
            screen = 2
        
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
    noFill()
    for furniture in room_obstacles:
        rect(*furniture)
    noFill()
    #character
    rect(x, y, 60, 0)

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
    
def room_screenchange():
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
                screen = 6
    #chest
    if (x >= 900 and x <= 1050 and y >= 50 and y <= 280):
        textSize(15)
        text("press o to open chest", 700, 250)
        if (keyPressed):
            if (key == 'o'):
                screen = 6
    #couch
    if (x >= 100 and x <= 350 and y >= 50 and y <= 280):
        textSize(15)
        text("press x to inspect", 200, 250)
        if (keyPressed):
            if (key == 'x'):
                screen = 6
    #goldfish
    if (x >= 100 and x <= 350 and y >= 500 and y <= 1050):
        textSize(15)
        text("press x to inspect", 300, 550)
        if (keyPressed):
            if (key == 'x'):
                screen = 6
    #upstairs
    if (x >= 950 and x <= 1050 and y >= 680 and y <= 750):
        textSize(15)
        text("press i to go upstairs", 770, 600)
        if keyPressed:
            if (key == "i"):
              screen = 3 
                
def display_location(x, y):
    textSize(15)
    text(str(x), 10, 20)
    text(str(y), 10, 40)


        
def character_movement(playerx, playery, obstacles_ar):
    global x
    global y
    global y2

    if keyPressed and key == CODED:
        if keyCode == UP and y >= 50:
            y -= 5
            print("up")
            if point_collide(playerx, playery, obstacles_ar) == True:
                y += 5
        if (keyCode == DOWN and y <= 690):
            y += 5
            print("down")
            if point_collide(playerx, playery, obstacles_ar) == True:
                y -= 5
        if screen == 2 and keyPressed and key == CODED:
            if keyCode == UP and y2 >= 50:
                y2 -= 5
                print("up")
            if point_collide(playerx, playery, obstacles_ar) == True:
                y2 += 5
            if (keyCode == DOWN and y <= 690):
                y2 += 5
                print("down")
            if point_collide(playerx, playery, obstacles_ar) == True:
                y2 -= 5

        if (keyCode == LEFT and x >= 50):
            x -= 5
            print("left")
            if point_collide(playerx, playery, obstacles_ar) == True:
                x += 5

        if (keyCode == RIGHT and x <= 1090):
            x += 5
            print("right")
            if point_collide(playerx, playery, obstacles_ar) == True:
                x -= 5
    

                
def character_animation(x , y2):
            if keyCode == LEFT:
                image(img_ted_left, x, y)
            elif keyCode == DOWN:
                image(img_ted_down, x, y)
            elif keyCode == UP:
                image(img_ted_up, x, y)
            elif keyCode == RIGHT:
                image(img_ted_right, x, y)
            else:
                image(img_ted_down, x, y)
    
def point_collide(playerx, playery, obstacles_ar):
    global x, y, y2
        
    player_x1 = x
    player_x2 = x + 60
    player_y1 = y
    player_y2 = y + 60
    
    

    for furniture in obstacles_ar:

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

        
        
    
def outdoor_screenchange():
    global screen
    # tree 
    if (x >= 105 and x <= 430 and y2 >= 45 and y2 <= 375):
        textSize(15)
        text("press x to inspect", 430, 205)
        text("the tree", 430, 225)
        if (keyPressed):
            if (key == 'x'):
                screen = 17
    #tree on right     
    if (x >= 730 and x <= 1060 and y2 >= 55 and y2 <= 385):
        textSize(15)
        text("press x to inspect", 625, 190)
        text("the tree", 660, 210)
        if (keyPressed):
            if (key == 'x'):
                screen = 18
    #berry farm
    if (x >= 165 and x <= 430 and y2 >= 410 and y2 <= 645):
        textSize(15)
        text("press x to inspect", 255, 450)
        text("the berry farm", 255, 470)
        if (keyPressed):
            if (key == 'x'):
                screen = 19
    #picnic table        
    if (x >= 720 and x <= 975 and y2 >= 445 and y2 <= 645):
        textSize(15)
        text("press x to inspect picnic table", 790, 650)
        if (keyPressed):
            if (key == 'x'):
                screen = 20
    #going inside
    if (x >= 505 and x <= 685 and y2 >= 660 and y2 <= 700):
        textSize(15)
        text("press o to go inside", 510, 675)
        if (keyPressed):
            if (key == 'o'):
                screen = 1
                

def bedroom_screenchange():
    if (x >= 950 and x <= 1050 and y >= 680 and y <= 750):
        textSize(15)
        text("press r to go downstairs", 770, 600)
        if (keyPressed):
            if (key == "r"):
                screen = 1 
      
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
    image(img_bed, 45, 285)
    image(img_bookshelf, 300, 50)
