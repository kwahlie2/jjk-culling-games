from gamelib import *
import copy

game = Game(900,600,"jjk culling games")
firehouse = Animation("firehouse.png",8,game,4000/5,672/2,-4)
moonstage = Animation("moon stage.png",20,game,3200/5,1920/4,5)
dragonstage = Animation("dragon stage.png",8,game,3200/5,644/2,5)
mss=Image("malevolent shrine.png",game)
jjhs=Image("jujitsu high.png",game)
bk =Image("startscreen.png",game)
bk.resizeTo(game.width,game.height)
ivs=Image("infinite void.png",game)
bfs1 =Image ("box for select.jpg",game)
bfs1.resizeBy(-60)
bfs1.moveTo(100,300)
bfs2 =Image ("box for select.jpg",game)
bfs2.resizeBy(-60)
bfs2.moveTo(100,480)
bfs3 =Image ("box for select.jpg",game)
bfs3.resizeBy(-60)
bfs3.moveTo(280,300)
bfs4 =Image ("box for select.jpg",game)
bfs4.resizeBy(-60)
bfs4.moveTo(280,480)
bfs5 =Image ("box for select.jpg",game)
bfs5.resizeBy(-60)
bfs5.moveTo(460,300)
bfs6 =Image ("box for select.jpg",game)
bfs6.resizeBy(-60)
bfs6.moveTo(460,480)
bfs7 =Image ("box for select.jpg",game)
bfs7.resizeBy(-60)
bfs7.moveTo(640,300)
bfs8 =Image ("box for select.jpg",game)
bfs8.resizeBy(-60)
bfs8.moveTo(640,480)
bfs9=Image ("box for select.jpg",game)
bfs9.resizeBy(-60)
bfs9.moveTo(810,370)
gojop=Image ("gojo p.png",game)
gojop.moveTo(810,370)
gojop.resizeBy(-40)
yujip=Image ("yuji p.png",game)
yujip.moveTo(640,480)
yujip.resizeBy(-35)
yutap=Image ("yuta p.png",game)
yutap.moveTo(640,300)
yutap.resizeBy(-55)
sukunap=Image("sukuna p.png",game)
sukunap.moveTo(460,480)
sukunap.resizeBy(-45)
tojip=Image("toji p.png",game)
tojip.moveTo(460,300)
tojip.resizeBy(10)
megumip=Image("megumi p.png",game)
megumip.moveTo(280,480)
megumip.resizeBy(-40)
todop=Image("todo p.png",game)
todop.moveTo(280,300)
todop.resizeBy(-30)
makip=Image("maki p.png",game)
makip.moveTo(100,480)
makip.resizeBy(-40)
nobrap=Image("nobra p.png",game)
nobrap.moveTo(100,300)
nobrap.resizeBy(-40)
jjklogo=Image("jjk logo.png",game)
jjklogo.resizeBy(-30)
jjklogo.moveTo(450,100)
start=Image("start.png",game)
start.moveTo(450,400)
housep=Image("hosuep.gif",game)
housep.resizeBy(-50)
housep.moveTo(170,200)
dragonp=Image("dragonp.gif",game)
dragonp.moveTo(760,400)
moonp=Image("moonp.jpg",game)
moonp.resizeBy(-50)
moonp.moveTo(170,400)
jjh=Image("jujitsu highp.png",game)
jjh.resizeBy(-50)
jjh.moveTo(460,400)
ms=Image("MVp.png",game)
ms.resizeBy(-50)
ms.moveTo(460,200)
iv=Image("infinite void.png",game)
iv.resizeBy(-60)
iv.moveTo(760,200)
cs= Image("cs.png",game)
cs.resizeBy(-30)
cs.moveTo(400,100)
ss=Image("ss.png",game)
ss.resizeBy(-60)
p1=Image("player1.png",game)
p1.resizeBy(-20)
p1.moveTo(700,100)
p2=Image("player2.png",game)
p2.resizeBy(-20)
p2.moveTo(700,100)
healthbarp1 = Shape("bar",game, p1.health, 10, green)
healthbarp1.moveTo( 20, 60)
healthbarp2 = Shape("bar",game, p2.health, 10, green)
healthbarp2.moveTo( 750, 60)
gojostand=Animation("gojo stand6.png",4,game,92/4,49/1,4)
gojostand.resizeBy(500)
yujistand=Animation("yuji sprite.png",5,game,189/5,55/1,4)
yujistand.resizeBy(500)
yujistand.moveTo(10,400)
yujirun=Animation("yujirun.png",6,game,322/6,54/1,4)
yujirun.resizeBy(500)
yujipunchd=Animation("yujipunchD.png",5,game,242/5,58/1,4)
yujijump=Animation("yujijump.png",4,game,173/4,64,1,10)
yujijump.resizeBy(500)
yujipunchd.resizeBy(400)
yujipunchr=Animation("yujipunchR.png",5,game,223/5,57/1,4)
yujipunchr.resizeBy(500)
yujipunchl=Animation("yujipunchL.png",5,game,191/5,58/1,4)
yujipunchl.resizeBy(500)
yujipunchu=Animation("yujipunchU.png",6,game,206/6,59/1,4)
yujipunchu.resizeBy(500)
sukunastand=Animation("sukunastand.png",4,game,151/5,88/1,4)
sukunarun=Animation("sukunastand.png",4,game,151/5,88/1,4)
makistand=Animation("makistand.png",4,game,195/5,67/1,4)
makistand.resizeBy(400)
tojistand=Animation("tojistand.png",6,game,322/6,69/1,4)
tojistand.resizeBy(400)
tojistand.moveTo(200,400)
tojirun=Animation("tojiwalk.png",7,game,356/7,69/1,4)
tojirun.resizeBy(400)
tojijump=Animation("tojijump.png",7,game,383/7,80/1,4)
tojijump.resizeBy(400)
tojipunch=Animation("tojipunch.png",8,game,404/8,69/1,4)
tojipunch.resizeBy(400)
tojikick=Animation("tojikick.png",5,game,335/5,76/1,4)
tojikick.resizeBy(400)
tojislash=Animation("tojislash2.png",6,game,434/6,63/1,4)
tojislash.resizeBy(400)
tojigun=Animation("tojigun.png",6,game,363/6,68/1,4)
tojigun.resizeBy(400)
tojiwin=Animation("tojiwin2.png",36,game,812/36,149/2,4)
tojiwin.resizeBy(400)
yujiwin=Animation("yujiwin.png",4,game,204/4,55/1,4)
yujiwin.resizeBy(400)
while not game.over:
    game.setBackground(bk)
    game.processInput()
    bk.draw()
    jjklogo.draw()
    start.draw()

    if mouse.collidedWith (start, "rectangle") and mouse.LeftClick:
        game.over = True


    game.update(30)

game.over=False

select_player =Animation("yuji sprite.png",5,game,189/5,55/1,4)
select_player_run = None
select_player_stand = None
select_player_punchd = None
select_player_punchr = None
select_player_punchl = None
select_player_jump = None
select_player_punchu= None

select_player2 =Animation("yuji sprite.png",5,game,189/5,55/1,4)
select_player_run2 = None
select_player_stand2 = None
select_player_punchd2 = None
select_player_punchr2 = None
select_player_punchl2 = None
select_player_jump2 = None
select_player_punchu2= None

#character selection1
while not game.over:
    game.setBackground(bk)
    game.processInput()
    bk.draw()
    bfs1.draw()
    bfs2.draw()
    bfs3.draw()
    bfs4.draw()
    bfs5.draw()
    bfs6.draw()
    bfs7.draw()
    bfs8.draw()
    bfs9.draw()
    gojop.draw()
    yujip.draw()
    yutap.draw()
    sukunap.draw()
    tojip.draw()
    megumip.draw()
    todop.draw()
    makip.draw()
    nobrap.draw()
    cs.draw()
    p1.draw()
    

    if mouse.collidedWith (bfs1) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs2) and mouse.LeftClick:
       select_player_stand = makistand
       game.over = True
    if mouse.collidedWith (bfs3) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs4) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs5) and mouse.LeftClick:
        #select_player= tojistand
        select_player_stand= tojistand
        select_player_run= tojirun
        select_player_jump= tojijump
        select_player_punchr = tojipunch
        select_player_punchl = tojikick
        select_player_punchd= tojislash
        select_player_punchu = tojigun
        select_player_win = tojiwin
        game.over = True
    if mouse.collidedWith (bfs6) and mouse.LeftClick:
        #select_player= sukunastand
        game.over = True
    if mouse.collidedWith (bfs7) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs8) and mouse.LeftClick:
        #select_player = yujistand
        select_player_stand = yujistand
        select_player_run=yujirun
        select_player_jump=yujijump
        select_player_punchd=yujipunchd
        select_player_punchr = yujipunchr
        select_player_punchl = yujipunchl
        select_player_punchu = yujipunchu
        select_player_win = yujiwin
        game.over = True
    if mouse.collidedWith (bfs9) and mouse.LeftClick:
        #select_player = gojostand
        game.over = True

    game.update(30)

game.over=False

#player2selection
while not game.over:
    game.setBackground(bk)
    game.processInput()
    bk.draw()
    bfs1.draw()
    bfs2.draw()
    bfs3.draw()
    bfs4.draw()
    bfs5.draw()
    bfs6.draw()
    bfs7.draw()
    bfs8.draw()
    bfs9.draw()
    gojop.draw()
    yujip.draw()
    yutap.draw()
    sukunap.draw()
    tojip.draw()
    megumip.draw()
    todop.draw()
    makip.draw()
    nobrap.draw()
    cs.draw()
    p2.draw()

    if mouse.collidedWith (bfs1) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs2) and mouse.LeftClick:
       select_player_stand2 = makistand
       game.over = True
    if mouse.collidedWith (bfs3) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs4) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs5) and mouse.LeftClick:
        #select_player2 = tojistand
        select_player_stand2= tojistand
        select_player_run2= tojirun
        select_player_jump2= tojijump
        select_player_punchr2 = tojipunch
        select_player_punchl2 = tojikick
        select_player_punchd2= tojislash
        select_player_punchu2 = tojigun
        select_player_win2 = tojiwin
        game.over = True
    if mouse.collidedWith (bfs6) and mouse.LeftClick:
        select_player2= sukunastand
        game.over = True
    if mouse.collidedWith (bfs7) and mouse.LeftClick:
        game.over = True
    if mouse.collidedWith (bfs8) and mouse.LeftClick:
        #select_player2 = yujistand
        select_player_stand2 = yujistand
        select_player_run2=yujirun
        select_player_jump2=yujijump
        select_player_punchd2=yujipunchd
        select_player_punchr2 = yujipunchr
        select_player_punchl2 = yujipunchl
        select_player_punchu2 = yujipunchu
        select_player_win2 = yujiwin
        game.over = True
    if mouse.collidedWith (bfs9) and mouse.LeftClick:
        #select_player = gojostand
        game.over = True

    game.update(30)

game.over=False



select_bk = None
#stage selection
while not game.over:
    game.processInput()
    bk.draw()
    housep.draw()
    dragonp.draw()
    moonp.draw()
    jjh.draw()
    ms.draw()
    iv.draw()
    ss.draw()
    if mouse.collidedWith (housep) and mouse.LeftClick:
        select_bk = firehouse
        game.over = True

    if mouse.collidedWith (dragonp) and mouse.LeftClick:
        select_bk = dragonstage
        game.over = True
        

    if mouse.collidedWith (moonp) and mouse.LeftClick:
        select_bk = moonstage
        game.over = True


    if mouse.collidedWith (jjh) and mouse.LeftClick:
        select_bk = jjhs
        game.over = True

    if mouse.collidedWith (ms) and mouse.LeftClick:
        select_bk = mss
        game.over = True

    if mouse.collidedWith (iv) and mouse.LeftClick:
        select_bk = ivs
        game.over = True

    
    game.update(30)

game.over=False


select_bk.resizeTo(game.width,game.height)
#game
player1move = ""
player2move = ""
healthbarp1.moveTo( 20, 60)
healthbarp2.moveTo( 780, 60)
select_player.moveTo(100,300)
select_player2.moveTo(600,300)
p1.moveTo(50,30)
p1.resizeBy(-60)
p2.moveTo( 850, 20)
p2.resizeBy(-60)
while not game.over:
    game.processInput()
    select_bk.draw()
    healthbarp1.width = p1.health
    healthbarp2.width = p2.health
    healthbarp1.draw()
    healthbarp2.draw()
    p2.draw()
    p1.draw()
    player1move = ""
    player2move = ""

    #player 1
    if keys.Pressed[K_d]:
        select_player.images = select_player_run.images
        select_player.x += 2
        select_player.offsetX = -25
        select_player.flipV = False
    elif keys.Pressed[K_a]:
        select_player.flipV = True
        select_player.images = select_player_run.images
        select_player.x -= 2
        select_player.offsetX = -75
    elif keys.Pressed[K_s]:
        player1move = "PunchDown"
        select_player.images = select_player_punchd.images
        select_player.offsetX = -50
    elif keys.Pressed[K_w]:
        select_player.images = select_player_jump.images
        select_player.offsetX = -50
    elif keys.Pressed[K_e]:
        player1move = "PunchRight"
        select_player.images = select_player_punchr.images
        select_player.offsetX = -50
    elif keys.Pressed[K_q]:
        player1move = "PunchLeft"
        select_player.images = select_player_punchl.images
        select_player.offsetX = -50
    elif keys.Pressed[K_r]:
        player1move = "PunchUp"
        select_player.images = select_player_punchu.images
        select_player.offsetX = -50
    elif keys.Pressed[K_g]:
        player2move = "win"
        select_player.images = select_player_win.images
        select_player.offsetX = -50
    else:
        select_player.images = select_player_stand.images
        if select_player.flipV:
            select_player.offsetX = -100
        else:
            select_player.offsetX = 0       
    


    #player2
    if keys.Pressed[K_l]:
        select_player2.images = select_player_run2.images
        select_player2.x += 2
        select_player2.offsetX = -25
        select_player2.flipV = False
    elif keys.Pressed[K_j]:
        select_player2.flipV = True
        select_player2.images = select_player_run2.images
        select_player2.x -= 2
        select_player2.offsetX = -75
    elif keys.Pressed[K_k]:
        player2move = "Slash"
        select_player2.images = select_player_punchd2.images
        select_player2.offsetX = -50
    elif keys.Pressed[K_i]:
        select_player2.images = select_player_jump2.images
        select_player2.offsetX = -50
    elif keys.Pressed[K_o]:
        player2move = "Punch"
        select_player2.images = select_player_punchr2.images
        select_player2.offsetX = -50
    elif keys.Pressed[K_u]:
        player2move = "Kick"
        select_player2.images = select_player_punchl2.images
        select_player2.offsetX = -50
    elif keys.Pressed[K_p]:
        player2move = "gun"
        select_player2.images = select_player_punchu2.images
        select_player2.offsetX = -50
    elif keys.Pressed[K_y]:
        player2move = "win"
        select_player2.images = select_player_win2.images
        select_player2.offsetX = -50
    else:
        select_player2.images = select_player_stand2.images
        if select_player2.flipV:
            select_player2.offsetX = -100
        else:
            select_player2.offsetX = 0
    
    if select_player.collidedWith(select_player2):
        #print(player1move, player2move,player1move == "PunchDown" and player2move == "Kick")
        if player1move != "" and player2move == "":
             p2.health -= 1
        if player1move == "" and player2move != "":
             p1.health -= 1
             

        if player1move == "PunchDown" and player2move == "Kick":
             p2.health -= 1

        if player1move == "PunchUp" and player2move == "Kick":
             p2.health -= 1

        if player1move == "PunchLeft" and player2move == "Kick":
             p1.health -= 1

        if player1move == "PunchRight" and player2move == "Kick":
             p1.health -= 1

        if player1move != "" and player2move == "gun":
             p1.health -= 1

        if player1move == "PunchDown" and player2move == "slash":
             p2.health -= 1

        if player1move == "PunchUp" and player2move == "slash":
             p2.health -= 1

        if player1move == "PunchLeft" and player2move == "slash":
             p1.health -= 1

        if player1move == "PunchRight" and player2move == "slash":
             p1.health -= 1

        if player1move == "PunchDown" and player2move == "Punch":
             p2.health -= 1

        if player1move == "PunchUp" and player2move == "punch":
             p1.health -= 1


        if player1move == "PunchLeft" and player2move == "punch":
             p1.health -= 1

        
        if player1move == "PunchRight" and player2move == "Punch":
             p2.health -= 1
             p1.health -= 1
 

    if p1.health <= 0 or p2.health <=0:
       game.over = True

       


    select_player.draw()
    select_player2.draw()
    game.update(30)






    
game.quit()
