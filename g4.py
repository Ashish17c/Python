import pgzrun

HEIGHT = 500
WIDTH = 500

alienb = Actor('character_0012',topleft=(500,500))
alieng = Actor('character_0002',topleft=(300,50))

def draw():
    Screen.fill('black')
    alienb.drow()
    alieng.draw()

def update():
    alieng.x += 1
    if alieng.x > WIDTH:
        alienb.x = 0
    if Keyboard.left:
        alienb.x -= speed
    if Keyboard.right:
        alienb.x += speed
    if Keyboard.up:
        alienb.y -= speed
    if keyboard.down:
        alienb.y += speed
    if alienb.colliderect(alieng):
        sounds.sound1.play()
pgzrun.go()