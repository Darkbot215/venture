print("JEFF IS BACK")
print("JEFF")
scale = 1
import pygame

pygame.init()
size = (int(800 * scale), int(600 * scale))
screen = pygame.display.set_mode(size)
import sys
import random
import time

x = [1, 3, 1]
print("cow")
# NEW X FORMAT: x,y,room,Username,TextEntered.
onlyst = [1]
GameStatus = [1, 0]
waitForIt = False
playerStats = [1, 1, 20, 10, 2, 20]
# attack is first| second is critical bonus|health is 3rd |mp is 4th| and 5th is mp attacks|6th is max hp|
npc1 = ["Jeff", 10, 10]
npc6A = ["Priest", 4, 7]
npc6B = ["Priest", 7, 7]
npc7A = ["Priest", 8, 10]
room = 1
En1 = [1, 10, 1, "Polar Bear", 5, 1, 2, 1, 60, 70]
# Before battle system. ITs all messed up
enemies = [[1, 10, 1, "Polar Bear", 5, 1, 2, 1, 60, 70, "BigMeat", 95]]
# a is name b is hp c is attack power low end. d is high end f is weekness g and h are part of rng last one is Item it drops and chance of  dropping it
rooms = [[], [1, 5, 2, 5, 3, 5, 1, 1, 2, 1, 3, 1, 3, 2, 3, 4], [1, 7, 1, 6, 2, 6, 3, 6, 4, 6, 5, 7], [], [], [],[3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 4, 8, 4, 4, 5, 8, 6, 8, 7, 8, 8, 8, 8, 7, 8, 6, 8, 5, 8, 4, 7, 4],[7, 10, 7, 9, 7, 8, 8, 8], [], [], [], [], [], [], [1, 1, 1, 2, 1, 3, 8, 8], [], [], [], [], [], [], [], [],[], [], [1, 9]]

roomspace = [[], [1, 4, 1, 3, 1, 2, 2, 4, 2, 3, 2, 2, 3, 3], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], []]
roomflower = [[], [5, 5], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],[]]
roomB = [[], [5, 6], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
roomC = [[], [5, 7], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
roomD = [[], [5, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
roomConnections = [[-1, -1, -1, -1], [2, 5, 4, 3], [6, 10, 1, 11], [11, 1, 12, 7], [1, 13, 8, 12], [10, 9, 13, 1],[-1, 25, 2, 14], [16, 3, 17, -1], [4, 20, -1, 19], [23, -1, 22, 5], [25, 23, 5, 2], [14, 2, 3, 16],[3, 4, 19, 17], [5, 22, 20, 4], [-1, 6, 11, 15], [-1, 14, 16, -1], [15, 11, 7, -1], [7, 12, 18, -1],[17, 19, -1, -1], [12, 8, -1, 18], [13, 21, -1, 8], [22, -1, -1, 20], [9, -1, 21, 13],[24, -1, 9, 10], [-1, -1, 23, 25], [-1, 24, 10, 6]]
# connections work w,a,s,d
items = []
enter = ""

npc = [[1, 1, 8, "Jeff", 1, 1, 1, 1, "Jeff", "yellow"], [1, 10, 9, "Billy Bo Bob", 1, 1, 1, 1, "BillyBoBob", "fat"],[6, 4, 7, "Priest", 0, 0, 1, 0, "Priest", "purple"], [6, 7, 7, "Priest", 0, 0, 1, 0, "Priest", "purple"]]
# 9 is image
# after npc name is where you can talk to them.
# plan b  is just make a loop checking each one for the room you are in.


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)


def render():
    screen.fill(BLACK)
    i = 40
    ix = 0
    i9 = 11
    i8 = 0
    while (ix < 420 * scale):
        i = 0
        i8 = 0
        while (i < 420 * scale):
            if (printout[i9][i8] == "roomflower"):
                screen.blit(flowertile, (i, ix))
            elif (printout[i9][i8] == "roomB"):
                screen.blit(grassB, (i, ix))
            elif (printout[i9][i8] == "roomC"):
                screen.blit(grassC, (i, ix))
            elif (printout[i9][i8] == "roomD"):
                screen.blit(grassD, (i, ix))
            elif (printout[i9][i8] == "enemy"):
                screen.blit(swordA, (i, ix))
            elif (printout[i9][i8] == "npcfat"):
                screen.blit(fatNpc, (i, ix))
            elif (printout[i9][i8] == "npcyellow"):
                screen.blit(yellowNpc, (i, ix))
            elif (printout[i9][i8] == "npcpurple"):
                screen.blit(purpleNpc, (i, ix))
            elif (printout[i9][i8] == "wall"):
                screen.blit(wall, (i, ix))
            elif (printout[i9][i8] == ['roomA']):
                screen.blit(grassA, (i, ix))
            elif (printout[i9][i8] == "player"):
                screen.blit(player, (i, ix))
            elif (printout[i9][i8] == "edge" or printout[i9][i8] == ['edge']):
                screen.blit(edge, (i, ix))
            elif (printout[i9][i8] == "wallgrass" or printout[i9][i8] == ['wallgrass']):
                screen.blit(wallgrass, (i, ix))
            elif (printout[i9][i8] == "ghost"):
                screen.blit(Ghost, (i, ix))
            elif (printout[i9][i8] == "stone"):
                screen.blit(stone, (i, ix))

            i = i + 35 * scale
            i8 = i8 + 1
        ix = ix + 35 * scale
        i9 = i9 - 1
    screen.blit(playerA, (x[0] * 35 * scale, (11 - x[1]) * 35 * scale))


def move(nio):
    global printout
    global room
    global waitForIt
    global roomConnections
    waitForIt = False
    i = 0
    ran = 0
    global roomA
    global x
    global enter

    if (nio == "w"):
        if (x[1] != 10):
            while (i < len(rooms[x[2]]) / 2):
                if (x[0] == rooms[x[2]][i * 2]):
                    if (x[1] == rooms[x[2]][i * 2 + 1] - 1):
                        ran = 1

                        # print("You can't run through a wall!")

                        break
                i = i + 1
            if (ran == 0):
                x[1] = x[1] + 1
        elif (((x[0] == 5) or (x[0] == 6)) and roomConnections[x[2]][0] != -1):

            x[2] = roomConnections[x[2]][0]
            x = [x[0], 1, x[2]]
        else:
            "Cow"

            # print("You have reached the edge of the map.")

        #  move()
    elif (nio == "s"):
        if (x[1] != 1):
            while (i < len(rooms[x[2]]) / 2):
                if (x[0] == rooms[x[2]][i * 2]):
                    if (x[1] == rooms[x[2]][i * 2 + 1] + 1):
                        ran = 1

                        # print("You can't run through a wall!")

                        break
                i = i + 1
            if (ran == 0):
                x[1] = x[1] - 1
        elif (((x[0] == 5) or (x[0] == 6)) and roomConnections[x[2]][2] != -1):

            x[2] = roomConnections[x[2]][2]
            x = [x[0], 10, x[2]]
        else:
            "Cow"

            # print("You have reached the edge of the map.")

        # move()
    elif (nio == "a"):
        if (x[0] != 1):
            while (i < len(rooms[x[2]]) / 2):
                if (x[1] == rooms[x[2]][i * 2 + 1]):
                    if (x[0] == rooms[x[2]][i * 2] + 1):
                        ran = 1

                        # print("You can't run through a wall!")

                        break
                i = i + 1
            if (ran == 0):
                x[0] = x[0] - 1
        elif (((x[1] == 5) or (x[1] == 6)) and roomConnections[x[2]][1] != -1):

            x[2] = roomConnections[x[2]][1]
            x = [10, x[1], x[2]]
        else:
            "Cow"

            # print("You have reached the edge of the map.")

            # move()
    elif (nio == "d"):
        if (x[0] != 10):
            while (i < len(rooms[x[2]]) / 2):
                if (x[1] == rooms[x[2]][i * 2 + 1]):
                    if (x[0] == rooms[x[2]][i * 2] - 1):
                        ran = 1

                        # print("You can't run through a wall!")

                        break
                i = i + 1
            if (ran == 0):
                x[0] = x[0] + 1
        elif (((x[1] == 5) or (x[1] == 6)) and roomConnections[x[2]][3] != -1):

            x[2] = roomConnections[x[2]][3]
            x = [1, x[1], x[2]]
        else:
            "Cow"
            # print("You have reached the edge of the map.")

            # move()

    if (ran == 1):
        "Cow"
    #    move()

    else:
        "Cow"

        # print("Enter 'w' 'a' 's' or 'd' to move.")


#    move()


def npcs():
    global npc
    global npc1
    global room
    global x
    global En1
    ix = 0
    iq = 0
    ii = 0
    npcinter = []
    eninter = []
    print(x[2])
    while (ix < len(npc)):
        print("Name is jeff")
        if (x[2] == npc[ix][0]):
            print("Cow")
            npcinter.append(npc[ix])
        ix = ix + 1
    ix = 0
    while (ix < len(enemies)):
        if (x[2] == enemies[ix][0]):
            eninter.append(enemies[ix])
        ix = ix + 1
    yOrn = ""
    while (ii < len(eninter)):
        print(ii)
        if ((eninter[ii][1] == x[0] and (
                (eninter[ii][2] == x[1] + 1) or (eninter[ii][2] == x[1]) or (eninter[ii][2] == x[1] - 1))) or (
                eninter[ii][2] == x[1] and ((eninter[ii][1] == x[0] + 1) or (eninter[ii][1] == x[0] - 1)))):

            Battle(eninter[ii][3], eninter[ii][4], eninter[ii][5], eninter[ii][6], eninter[ii][7], eninter[ii][8],
                   eninter[ii][9])
            i6 = 0
            while (i6 < len(enemies)):
                if (enemies[i6][0] == eninter[ii][0] and enemies[i6][1] == eninter[ii][1] and enemies[i6][3] ==
                        eninter[ii][3]):
                    enemies[i6][1] = -1
                    enemies[i6][2] = -1
                    i6 = i6 + 100000
                i6 = i6 + 1
            ii = ii + len(eninter)
        ii = ii + 1
    while (iq < len(npcinter)):
        if (npcinter[iq][4] == 1):
            if (x[0] == npcinter[iq][1] and x[1] - 1 == npcinter[iq][2]):
                scroll("Would you like to talk with " + npcinter[iq][3] + "? (y/n)", 0, "")
                y0rn = boxes("Yes", "No", "", "")

                if yOrn == "y":
                    clear(69)
                    board()
                    if (npcinter[iq][8] == "Jeff"):
                        NpcOps.Jeff(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "BillyBoBob"):
                        NpcOps.BillyBoBob(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "Priest"):
                        NpcOps.Priest(npcinter[iq][3], npcinter[iq][0])

        if (npcinter[iq][5] == 1):
            if (x[1] == npcinter[iq][2] and x[0] - 1 == npcinter[iq][1]):
                board()
                scroll("Would you like to talk with " + npcinter[iq][3] + "? (y/n)")
                clear(4)
                yOrn = input().lower()
                if yOrn == "y":
                    clear(69)
                    board()
                    if (npcinter[iq][8] == "Jeff"):
                        NpcOps.Jeff(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "BillyBoBob"):
                        NpcOps.BillyBoBob(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "Priest"):
                        NpcOps.Priest(npcinter[iq][3], npcinter[iq][0])

        if (npcinter[iq][6] == 1):
            if (x[0] == npcinter[iq][1] and x[1] + 1 == npcinter[iq][2]):
                board()
                scroll("Would you like to talk with " + npcinter[iq][3] + "? (y/n)")
                clear(4)
                yOrn = input().lower()
                if yOrn == "y":
                    clear(69)
                    board()
                    if (npcinter[iq][8] == "Jeff"):
                        NpcOps.Jeff(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "BillyBoBob"):
                        NpcOps.BillyBoBob(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "Priest"):
                        NpcOps.Priest(npcinter[iq][3], npcinter[iq][0])
        if (npcinter[iq][7] == 1):
            if (x[1] == npcinter[iq][2] and x[0] + 1 == npcinter[iq][1]):
                board()
                scroll("Would you like to talk with " + npcinter[iq][3] + "? (y/n)")
                clear(4)
                yOrn = input().lower()
                if yOrn == "y":
                    clear(69)
                    board()
                    if (npcinter[iq][8] == "Jeff"):
                        NpcOps.Jeff(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "BillyBoBob"):
                        NpcOps.BillyBoBob(npcinter[iq][3], npcinter[iq][0])
                    elif (npcinter[iq][8] == "Priest"):
                        NpcOps.Priest(npcinter[iq][3], npcinter[iq][0])
        if (x[0] == npcinter[iq][1] and x[1] == npcinter[iq][2]):
            board()
            scroll("Would you like to talk with " + npcinter[iq][3] + "? (y/n)")
            clear(4)
            yOrn = input().lower()
            if yOrn == "y":
                clear(69)
                board()
                if (npcinter[iq][8] == "Jeff"):
                    NpcOps.Jeff(npcinter[iq][3], npcinter[iq][0])
                elif (npcinter[iq][8] == "BillyBoBob"):
                    NpcOps.BillyBoBob(npcinter[iq][3], npcinter[iq][0])
                elif (npcinter[iq][8] == "Priest"):
                    NpcOps.Priest(npcinter[iq][3], npcinter[iq][0])

        iq = iq + 1


def boxes(a, b, c, d):
    global done
    global scale
    # add 200 each time
    i = 0
    easycount = 1
    texty = ""
    pos = (0, 0)
    coolrunnings = True
    while (coolrunnings == True):
        # screen.fill(BLACK)
        # render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                coolrunnings = False
            pos = pygame.mouse.get_pos()
            print(pygame.mouse.get_pressed()[0])
        if pygame.mouse.get_pressed()[0] and done == False:
            pos = pygame.mouse.get_pos()

            print("WAAASUP")
            if (pos[0] > 30 * scale and pos[0] < 180 * scale and pos[1] > 550 * scale and pos[
                1] < 595 * scale and a != ""):
                coolrunnings = False
                return (1)
            elif (pos[0] > 230 * scale and pos[0] < 380 * scale and pos[1] > 550 * scale and pos[
                1] < 595 * scale and b != ""):
                coolrunnings = False
                return (2)
            elif (pos[0] > 430 * scale and pos[0] < 580 * scale and pos[1] > 550 * scale and pos[
                1] < 595 * scale and c != ""):
                coolrunnings = False
                return (3)
            elif (pos[0] > 630 * scale and pos[0] < 780 * scale and pos[1] > 550 * scale and pos[
                1] < 595 * scale and d != ""):
                coolrunnings = False
                return (4)
        i = 0
        easycount = 1
        texty = ""

        while (i < 601 * scale):
            pygame.draw.rect(screen, BLACK, [30 + i, 550 * scale, 150 * scale, 45 * scale])
            print(i)
            if (easycount == 1):
                texty = a
            elif (easycount == 2):
                texty = b
            elif (easycount == 3):
                texty = c
            elif (easycount == 4):
                texty = d
            if (texty != ""):
                if (pos[0] > 30 + i and pos[0] < 180 + i and pos[1] > 550 * scale and pos[1] < 595 * scale):
                    pygame.draw.rect(screen, BLUE, [30 + i, 550 * scale, 150 * scale, 45 * scale])
                else:
                    pygame.draw.rect(screen, WHITE, [30 + i, 550 * scale, 150 * scale, 45 * scale], 2)

                font = pygame.font.Font("MERCY.ttf", 32 * scale)
                text = font.render(texty, True, WHITE)
                if (texty == "Yes"):

                    screen.blit(text, [75 + i, 550 * scale])
                elif (texty == "No"):
                    screen.blit(text, [83 + i, 550 * scale])
                else:
                    screen.blit(text, [40 + i, 550 * scale])

            i = i + (200 * scale)
            print(i)

            easycount = easycount + 1
        pygame.display.flip()


def scroll(strr, ti, name, fontsize):
    global done

    tri = ""
    font = pygame.font.Font("DejaVuSerif.ttf", fontsize * scale)

    p = 0
    pygame.draw.rect(screen, WHITE, [25 * scale, 425 * scale, 750 * scale, 100 * scale], 2)
    pygame.draw.rect(screen, WHITE, [600 * scale, 380 * scale, 175 * scale, 45 * scale], 2)
    text = font.render(name, True, WHITE)
    screen.blit(text, [610 * scale, 385 * scale])

    while (p < len(strr)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return
        tri = tri + strr[p]
        text = font.render(tri, True, WHITE)
        screen.blit(text, [50 * scale, 430 * scale])
        # render()
        pygame.display.flip()
        time.sleep(0.05)

        p = p + 1
    don = False
    t = time.time()
    while don == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return
        if (time.time() > t + ti):
            don = True


scalesize = int(35 * scale)
playerA = pygame.image.load("4DC563D2-7586-4EE7-89BB-37F0A81DF816.png").convert_alpha()
playerA = pygame.transform.scale(playerA, (scalesize, scalesize))
player = pygame.image.load("IMG_0071.png").convert()
player = pygame.transform.scale(player, (scalesize, scalesize))
flowertile = pygame.image.load("IMG_0068 (2).png").convert()
flowertile = pygame.transform.scale(flowertile, (scalesize, scalesize))
wall = pygame.image.load("Brick.png").convert()
wall = pygame.transform.scale(wall, (scalesize, scalesize))
grassA = pygame.image.load("IMG_0069.png").convert()
grassA = pygame.transform.scale(grassA, (scalesize, scalesize))
grassB = pygame.image.load("IMG_0069 (2).png").convert()
grassB = pygame.transform.scale(grassB, (scalesize, scalesize))
print("all good")
grassC = pygame.image.load("GrassC.png").convert()
grassC = pygame.transform.scale(grassC, (scalesize, scalesize))
print("Still running")
grassD = pygame.image.load("IMG_0069 - Copy (2).png").convert()
grassD = pygame.transform.scale(grassD, (scalesize, scalesize))
edge = pygame.image.load("Tower.png").convert()
edge = pygame.transform.scale(edge, (scalesize, scalesize))
swordA = pygame.image.load("IMG_0074.png").convert()
swordA = pygame.transform.scale(swordA, (scalesize, scalesize))
swordB = pygame.image.load("IMG_0072 (2).png").convert()
swordB = pygame.transform.scale(swordA, (scalesize, scalesize))
fatNpc = pygame.image.load("IMG_0078 (2).png").convert()
fatNpc = pygame.transform.scale(fatNpc, (scalesize, scalesize))
yellowNpc = pygame.image.load("IMG_0075 (2).png").convert()
yellowNpc = pygame.transform.scale(yellowNpc, (scalesize, scalesize))
purpleNpc = pygame.image.load("IMG_0076 (2).png").convert()
purpleNpc = pygame.transform.scale(purpleNpc, (scalesize, scalesize))
Ghost = pygame.image.load("IMG_0079.png").convert()
Ghost = pygame.transform.scale(Ghost, (scalesize, scalesize))
stone = pygame.image.load("Stone.png").convert()
stone = pygame.transform.scale(stone, (scalesize, scalesize))
wallgrass = pygame.image.load("Wallgrass.png").convert()
wallgrass = pygame.transform.scale(wallgrass, (scalesize, scalesize))

done = False

while (done == False):
    print(done)
    # time.sleep(.1)
    # Amount of slowdown between reload of the screen (Why yes that is 10 fps I might change it.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move("w")
            elif event.key == pygame.K_s:
                move("s")
            elif event.key == pygame.K_a:
                move("a")
            elif event.key == pygame.K_d:
                move("d")
            elif event.key == pygame.K_p:
                scroll("My name is jeff.", 3, "Jeff", 25)
            elif event.key == pygame.K_q:
                scroll("Would you like to talk with JEff? (y/n)", 0, "Game", 25)
                y0rn = boxes("Yes", "No", "", "")

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Arial', 50, False, False)

    printout = [[["edge"], ["edge"], ["edge"], ["edge"], ["edge"], ["wallgrass"], ["wallgrass"], ["edge"], ["edge"], ["edge"],["edge"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["wallgrass"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["roomA"], ["wallgrass"]],[["wallgrass"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["roomA"], ["wallgrass"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"], ["roomA"],["roomA"], ["edge"]],[["edge"], ["edge"], ["edge"], ["edge"], ["edge"], ["wallgrass"], ["wallgrass"], ["edge"], ["edge"], ["edge"],["edge"], ["edge"]]]
    print(printout[9][9])
    # fist section is y and second is x
    # using name in string to show what to print where
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line reates an image of the letters,
    # but does not put it on thce screen yet.
    i = 0

    while (i < len(rooms[x[2]])):
        print(rooms[x[2]][i + 1])
        print(rooms[x[2]][i])
        printout[rooms[x[2]][i + 1]][rooms[x[2]][i]] = "wall"
        i = i + 2
    i = 0
    while (i < len(roomflower[x[2]])):
        printout[roomflower[x[2]][i + 1]][roomflower[x[2]][i]] = "roomflower"
        i = i + 2
    i = 0
    while (i < len(roomB[x[2]])):
        printout[roomB[x[2]][i + 1]][roomB[x[2]][i]] = "roomB"
        i = i + 2
    i = 0
    while (i < len(roomC[x[2]])):
        printout[roomC[x[2]][i + 1]][roomC[x[2]][i]] = "roomC"
        i = i + 2
    i = 0
    while (i < len(roomD[x[2]])):
        printout[roomD[x[2]][i + 1]][roomD[x[2]][i]] = "roomD"
        i = i + 2
    i = 0
    while (i < len(roomspace[x[2]])):
        printout[roomspace[x[2]][i + 1]][roomspace[x[2]][i]] = "stone"
        i = i + 2

    i = 0
    iq = 0
    iw = 0
    printnpcfat = []
    printnpcyellow = []
    printnpcpurple = []
    printenemies = []
    while (iq < len(npc)):
        if (x[2] == npc[iq][0] and npc[iq][9] == "fat"):
            printnpcfat.append(npc[iq])
        iq = iq + 1
    iq = 0
    while (iq < len(npc)):
        if (x[2] == npc[iq][0] and npc[iq][9] == "yellow"):
            printnpcyellow.append(npc[iq])
        iq = iq + 1
    iq = 0
    while (iq < len(npc)):
        if (x[2] == npc[iq][0] and npc[iq][9] == "purple"):
            printnpcpurple.append(npc[iq])
        iq = iq + 1
    while (iw < len(enemies)):
        if (x[2] == enemies[iw][0]):
            printenemies.append(enemies[iw])
        iw = iw + 1
    i = 0
    while (i < len(printenemies)):
        print(i)
        print(printenemies[i][1])
        printout[printenemies[i][2]][printenemies[i][1]] = "enemy"
        i = i + 1
    i = 0
    while (i < len(printnpcfat)):
        printout[printnpcfat[i][2]][printnpcfat[i][1]] = "npcfat"
        i = i + 1
    i = 0
    while (i < len(printnpcyellow)):
        printout[printnpcyellow[i][2]][printnpcyellow[i][1]] = "npcyellow"
        i = i + 1
    i = 0
    while (i < len(printnpcpurple)):
        printout[printnpcpurple[i][2]][printnpcpurple[i][1]] = "npcpurple"
        i = i + 1
    # printout[x[1]][x[0]]="player"

    # text = font.render("OOO",True,WHITE)

    # Put the image of the text on the screen at 250x250
    i = 0
    if (roomConnections[x[2]][0] == -1):
        printout[11][5] = "edge"
        printout[11][6] = "edge"
    if (roomConnections[x[2]][1] == -1):
        printout[5][0] = "edge"
        printout[6][0] = "edge"
    if (roomConnections[x[2]][2] == -1):
        printout[0][6] = "edge"
        printout[0][5] = "edge"
    if (roomConnections[x[2]][3] == -1):
        printout[5][11] = "edge"
        printout[6][11] = "edge"

    render()
    i = 0

    #  screen.blit(text, [0, 0])
    # screen.blit(font.render("0 00",True,WHITE),[0,30] )
    # screen.blit(font.render("░░░",True,WHITE),[0,60])
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)

print("#RIP")
pygame.quit()
