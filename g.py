imoprt pgzrun

aliend = Actor('character_0002',pos =(200,200))
aliend = Actor('character_0002',topleft =(50,50))

def draw():
    screen.fill('white')
    aliend.draw()
    aliend.draw()

def update():
    aliend.y += 1
    if aliend.y > HEIGHT:
        aliend.y = 0
    
pgzrun.go()
