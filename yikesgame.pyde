global x
global y
global screen
x = 60
y = 60
screen = 0

def setup():
    size(1200, 800)
    background(0)
    global img_floor
    global img_door
    global img_croppedfloor
    img_floor = loadImage("FloorPixel.png")
    img_door = loadImage("door.png")
    img_croppedfloor = loadImage("FloorPixelCropped.png")
    
def draw():
    global screen
    global img_floor
    global img_door
    if screen == 0:
        background(0)
        fill(255)
        play_button()
    
    if screen == 1:
        background(0)
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
            img_door.resize(160, 50)
            fill(255)
            rect(x, y, 60, 60)
        def screen_change():
            global x
            global y
            global screen
            if (x >= 510 and x <= 610 and y >= 50 and
            y <= 150):
                textSize(15)
                text("press i to go outside", 560, 150)
                if keyPressed:
                    if (key == "i"):
                        screen += 1
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
            
        character_movement()
        graphics()
        screen_change()
        display_location()

    if screen == 2:
        background(139,0,139)
        rect(50, 50, 1100, 700)
        rect(x, y, 60, 60)
        def screen_change():
            global screen
            if (keyPressed):
                if (key == 'x'):
                    screen = 3
        character_movement()
        screen_change()
    if screen == 3:
        background(0)
        if keyPressed:
            if (key == 'q'):
                screen = 1
        if keyPressed:
            if (key == 'w'):
                screen = 2
              
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
                
def play_button():
    global screen
    text("Play", 600, 400)
    textSize(50)
    if (mouseX >= 450 and mouseX <= 750 and mouseY >= 200 and
    mouseY <= 600 and mousePressed):
        screen = 1
        

