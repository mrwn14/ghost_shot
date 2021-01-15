import pygame
import random
from pygame import mixer

pygame.init()

time_gone = 0
score_font = pygame.font.Font("freesansbold.ttf", 38)
timer_font = pygame.font.Font("freesansbold.ttf", 38)
maintext = pygame.font.Font("freesansbold.ttf", 25)
starttext = pygame.font.Font("freesansbold.ttf", 15)
starttextbig = pygame.font.Font("freesansbold.ttf", 16)
scoretext = pygame.font.Font("freesansbold.ttf", 40)
restarttextbig = pygame.font.Font("freesansbold.ttf", 30)
icon = pygame.image.load("console.png")
x = 800
y = 600
screen = pygame.display.set_mode((x,y))
num_of_enemies = 2
exvel = 1





def draw_text(what,txt,x,y,c1,c2,c3):
    text = what.render(txt, True, (c1,c2,c3))
    screen.blit(text, (x,y))

def mainmenu():
    pygame.init()
    runn = True
    mainbg = pygame.image.load("mainbg.jpg")
    while runn:
        screen.blit(mainbg, (0,0))
        draw_text(maintext,"Ghost shot", 335,35, 255,255,255)
        but1 = pygame.draw.circle(screen, (255,0,0), (200,300), 50)
        draw_text(starttextbig,"Start", 183,295,0,0,0)
        but2 = pygame.draw.circle(screen, (255,0,0), (600,300), 50)
        draw_text(starttextbig, "Options", 572, 295,0,0,0)
        

        mx,my = pygame.mouse.get_pos()

        if but1.collidepoint(mx, my):
            but1 = pygame.draw.circle(screen, (255,0,0), (200,300), 55)
            draw_text(starttextbig,"Start", 183,295,0,0,0)
        if but2.collidepoint(mx,my):
            but2 = pygame.draw.circle(screen, (255,0,0), (600,300), 55)
            draw_text(starttextbig, "Options", 572, 295,0,0,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and but1.collidepoint(mx, my):
                    game()
                if event.button == 1 and but2.collidepoint(mx, my):
                    options()
        
        pygame.display.update()


def options():
    pygame.init()
    global num_of_enemies
    global exvel
    runnn = True
    back = pygame.image.load("optionbackgrounnd.png")
    while runnn:
        mx,my = pygame.mouse.get_pos()
        screen.blit(back, (0,0))

        draw_text(starttext, "Choose the number of enemies",290,100,255,255,255)
        e1 = pygame.draw.circle(screen, (255,0,0), (80,150), 20)
        draw_text(starttextbig, "2", 77,144,0,0,0)
        e2 = pygame.draw.circle(screen, (255,0,0), (160,150), 20)
        draw_text(starttextbig, "3", 157,144,0,0,0)
        e3 = pygame.draw.circle(screen, (255,0,0), (240,150), 20)
        draw_text(starttextbig, "4", 237,144,0,0,0)
        e4 = pygame.draw.circle(screen, (255,0,0), (320,150), 20)
        draw_text(starttextbig, "5", 317,144,0,0,0)
        e5 = pygame.draw.circle(screen, (255,0,0), (400,150), 20)
        draw_text(starttextbig, "6", 397,144,0,0,0)
        e6 = pygame.draw.circle(screen, (255,0,0), (480,150), 20)
        draw_text(starttextbig, "7", 477,144,0,0,0)
        e7 = pygame.draw.circle(screen, (255,0,0), (560,150), 20)
        draw_text(starttextbig, "8", 557,144,0,0,0)
        e8 = pygame.draw.circle(screen, (255,0,0), (640,150), 20)
        draw_text(starttextbig, "9", 637,144,0,0,0)
        e9 = pygame.draw.circle(screen, (255,0,0), (720,150), 20)
        draw_text(starttextbig, "10", 712,144,0,0,0)



        if e1.collidepoint(mx, my):
            e1 = pygame.draw.circle(screen, (255,0,0), (80,150), 23)
            draw_text(starttextbig, "2", 77,144,0,0,0)
        if e2.collidepoint(mx,my):
            e2 = pygame.draw.circle(screen, (255,0,0), (160,150), 23)
            draw_text(starttextbig, "3", 157,144,0,0,0)
        if e3.collidepoint(mx,my):
            e3 = pygame.draw.circle(screen, (255,0,0), (240,150), 23)
            draw_text(starttextbig, "4", 237,144,0,0,0)
        if e4.collidepoint(mx,my):
            e4 = pygame.draw.circle(screen, (255,0,0), (320,150), 23)
            draw_text(starttextbig, "5", 317,144,0,0,0)
        if e5.collidepoint(mx,my):
            e5 = pygame.draw.circle(screen, (255,0,0), (400,150), 23)
            draw_text(starttextbig, "6", 397,144,0,0,0)
        if e6.collidepoint(mx,my):
            e6 = pygame.draw.circle(screen, (255,0,0), (480,150), 23)
            draw_text(starttextbig, "7", 477,144,0,0,0)
        if e7.collidepoint(mx,my):
            e7 = pygame.draw.circle(screen, (255,0,0), (560,150), 23)
            draw_text(starttextbig, "8", 557,144,0,0,0)
        if e8.collidepoint(mx,my):
            e8 = pygame.draw.circle(screen, (255,0,0), (640,150), 23)
            draw_text(starttextbig, "9", 637,144,0,0,0)
        if e9.collidepoint(mx,my):
            e9 = pygame.draw.circle(screen, (255,0,0), (720,150), 23)
            draw_text(starttextbig, "10", 712,144,0,0,0)


        draw_text(starttext, "Choose the difficulty", 325, 320,255,255,255)
        d1 = pygame.draw.circle(screen, (255,0,0), (200,375), 30)
        draw_text(starttext, "Easy", 184, 370,0,0,0)
        d2 = pygame.draw.circle(screen, (255,0,0), (400,375), 30)
        draw_text(starttext, "Medium", 372, 370,0,0,0)
        d3 = pygame.draw.circle(screen, (255,0,0), (600,375), 30)
        draw_text(starttext, "Hard", 583, 370,0,0,0)


        if d1.collidepoint(mx, my):
            d1 = pygame.draw.circle(screen, (255,0,0), (200,375), 32)
            draw_text(starttext, "Easy", 184, 370,0,0,0)
        if d2.collidepoint(mx, my):
            d2 = pygame.draw.circle(screen, (255,0,0), (400,375), 32)
            draw_text(starttext, "Medium", 372, 370,0,0,0)
        if d3.collidepoint(mx, my):
            d3 = pygame.draw.circle(screen, (255,0,0), (600,375), 32)
            draw_text(starttext, "Hard", 583, 370,0,0,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    runnn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and e1.collidepoint(mx, my):
                    num_of_enemies = 2
                if event.button == 1 and e2.collidepoint(mx, my):
                    num_of_enemies = 3
                if event.button == 1 and e3.collidepoint(mx, my):
                    num_of_enemies = 4
                if event.button == 1 and e4.collidepoint(mx, my):
                    num_of_enemies = 5
                if event.button == 1 and e5.collidepoint(mx, my):
                    num_of_enemies = 6
                if event.button == 1 and e6.collidepoint(mx, my):
                    num_of_enemies = 7
                if event.button == 1 and e7.collidepoint(mx, my):
                    num_of_enemies = 8
                if event.button == 1 and e8.collidepoint(mx, my):
                    num_of_enemies = 9
                if event.button == 1 and e9.collidepoint(mx, my):
                    num_of_enemies = 10
                if event.button == 1 and d1.collidepoint(mx, my):
                    exvel = 1
                if event.button == 1 and d2.collidepoint(mx, my):
                    exvel = 2
                if event.button == 1 and d3.collidepoint(mx, my):
                    exvel = 4

        if num_of_enemies == 2:
            e1 = pygame.draw.circle(screen, (255,255,0), (80,150), 23)
            draw_text(starttextbig, "2", 77,144,0,0,0)
        if num_of_enemies == 3:
            e2 = pygame.draw.circle(screen, (255,255,0), (160,150), 23)
            draw_text(starttextbig, "3", 157,144,0,0,0)
        if num_of_enemies == 4:
            e3 = pygame.draw.circle(screen, (255,255,0), (240,150), 23)
            draw_text(starttextbig, "4", 237,144,0,0,0)
        if num_of_enemies == 5:
            e4 = pygame.draw.circle(screen, (255,255,0), (320,150), 23)
            draw_text(starttextbig, "5", 317,144,0,0,0)
        if num_of_enemies == 6:
            e5 = pygame.draw.circle(screen, (255,255,0), (400,150), 23)
            draw_text(starttextbig, "6", 397,144,0,0,0)
        if num_of_enemies == 7:
            e6 = pygame.draw.circle(screen, (255,255,0), (480,150), 23)
            draw_text(starttextbig, "7", 477,144,0,0,0)
        if num_of_enemies == 8:
            e7 = pygame.draw.circle(screen, (255,255,0), (560,150), 23)
            draw_text(starttextbig, "8", 557,144,0,0,)
        if num_of_enemies == 9:
            e8 = pygame.draw.circle(screen, (255,255,0), (640,150), 23)
            draw_text(starttextbig, "9", 637,144,0,0,0)
        if num_of_enemies == 10:
            e9 = pygame.draw.circle(screen, (255,255,0), (720,150), 23)
            draw_text(starttextbig, "10", 712,144,0,0,0)

        if exvel == 1:
            d1 = pygame.draw.circle(screen, (255,255,0), (200,375), 32)
            draw_text(starttext, "Easy", 184, 370,0,0,0)
        if exvel == 2:
            d2 = pygame.draw.circle(screen, (255,255,0), (400,375), 32)
            draw_text(starttext, "Medium", 372, 370,0,0,0)
        if exvel == 4:
            d3 = pygame.draw.circle(screen, (255,255,0), (600,375), 32)
            draw_text(starttext, "Hard", 583, 370,0,0,0)



        pygame.display.update()

def game():
    end = True
    run = True
    timer_sec = 60
    global screen
    global x
    global y
    global num_of_enemies
    global exvel
    background = pygame.image.load("bg2.png")
    timer = pygame.USEREVENT + 1                                                
    pygame.time.set_timer(timer, 1000)
    clock = pygame.time.Clock()
    getick = pygame.time.get_ticks()
    spaceship = pygame.image.load("spaceship.png")
    pew = pygame.image.load("bullet.png")
    pygame.display.set_caption("first game")
    pygame.display.set_icon(icon)
    spx = 370
    spy = 480
    ex = []
    ey = []
    enem = []
    exchange = []
    eychange = []
    score_value = 0
    bstate = "not fired"


    for i in range(num_of_enemies):
        enem.append(pygame.image.load("ghost.png"))
        ex.append(random.randint(0,736))
        ey.append(random.randint(0,300))
        exchange.append(exvel)
        eychange.append(exvel)

    vel = 3
    spxchange = 0
    spychange = 0
    bx = spx
    by = spy
    bychange = 4
    bstate = "not fired"

    def player(x,y):
        screen.blit(spaceship, (x,y))

    def scorevalue(x,y):
        if end == True:
            score = score_font.render('score: ' + str(score_value), True, (255,255,255))
            screen.blit(score, (x,y))

    def enemy(x,y,i):
        screen.blit(enem[i], (x,y))

    def bullet(x,y):
        screen.blit(pew, (x,y))

    def tim(x,y,c):
        if end == True:
            seconds = (pygame.time.get_ticks()-getick)/1000
            tim = timer_font.render(str(seconds), True, (255,255,255))
            screen.blit(tim, (x,y))

    while run:
        screen.blit(background, (0,0))
        player(spx,spy)
        scorevalue(20,10)
        seconds = (pygame.time.get_ticks()-getick)/1000
        tim(650,10,0)
        if seconds > 60:
            tim(650,10,255)
            draw_text(scoretext, "You got " + str(score_value), 305,250,255,255,255)
            draw_text(restarttextbig, "Press R to restart", 265, 300,255,255,255)
            end = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()
                    if event.key == pygame.K_ESCAPE:
                        mainmenu()
            
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and end == True:
                if event.key == pygame.K_RIGHT:
                    spxchange += vel
                if event.key == pygame.K_LEFT:
                    spxchange -= vel
                if event.key == pygame.K_UP:
                    spychange -= vel
                if event.key == pygame.K_DOWN:
                    spychange += vel
                if event.key == pygame.K_SPACE:
                    if bstate == 'not fired':
                        bul = mixer.Sound("494772__alderman2k__lazer.wav")
                        bul.play()
                        bx = spx
                        by = spy
                        bullet(bx+12,by+10)
                        bstate = "fired"
                if event.key == pygame.K_ESCAPE:
                    mainmenu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    spxchange = 0
                if event.key == pygame.K_LEFT:
                    spxchange = 0
                if event.key == pygame.K_UP:
                    spychange = 0
                if event.key == pygame.K_DOWN:
                    spychange = 0
                if event.key == pygame.K_SPACE:
                    None
        
        spx += spxchange
        spy += spychange
        

        if spx <0:
            spx = 0
        elif spx > x - 64:
            spx = x - 64
        elif spy > y - 64:
            spy = y - 64
        elif spy < 400:
            spy = 400
        
        for i in range(num_of_enemies):
            if end == True:
                ex[i] += exchange[i]
                ey[i] += eychange[i]
                if ex[i] < 0:
                    ex[i] = 0
                    exchange[i] = exvel
                elif ex[i] >= 800-32:
                    ex[i] = 800 - 32
                    exchange[i] = - exvel
                elif ey[i] > 300:
                    ey[i] = 300
                    eychange[i] = - exvel
                elif ey[i] < 0:
                    eychange[i] = exvel

            distance = ((bx-ex[i])**2 + (by-ey[i])**2)**(0.5) - 10
            if distance < 15:
                ex[i] = random.randint(0,736)
                ey[i] = random.randint(0,300)
                bstate = 'not fired'
                bx = spx
                by = spy
                score_value += 1
                

            enemy(ex[i],ey[i],i)

        if bstate == "fired":
            bullet(bx+20,by-7)
            bx += 0
            by -= bychange
        if by < 0:
            bstate = "not fired"
            bx = spx
            by = spy
        pygame.display.update()


mainmenu()


