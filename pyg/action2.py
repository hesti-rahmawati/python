# 1.ゲームの準備をする
from enum import Flag
import pygame as pg, sys
import random

pg.init()
screen = pg.display.set_mode((800, 600))
## プレイヤーデータ
myimgR = pg.image.load("images/playerR.png")
myimgR = pg.transform.scale(myimgR, (40, 50))
myimgL = pg.transform.flip(myimgR, True, False)
myimgU = pg.image.load("images/playerU.png")
myimgU = pg.transform.scale(myimgU,(40, 50))
myimgD = pg.image.load("images/playerD.png")
myimgD = pg.transform.scale(myimgD,(40, 50))
myrect = pg.Rect(50,200,40,50)

## 障害物データ
boxrect = pg.Rect(300,200,100,100)
boxrect.x =random.randint(0,700)
boxrect.y =random.randint(0,500)
     
## メインループで使う変数
a = 0

## ゲームステージ
def gamestage():
    global a
    # 3.画面を初期化する
    screen.fill(pg.Color("DEEPSKYBLUE"))
    vx = 0
    vy = 0
    # 4.ユーザーからの入力を調べる
    key = pg.key.get_pressed()
    # 5.絵を描いたり、判定したりする
    if key[pg.K_RIGHT]:
        vx =4
        a = 0
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -4
        a = 1
        rightFlag = False
    if key[pg.K_UP]:
        vy = -4
        a = 2
        screen.blit(myimgU, myrect)
    if key[pg.K_DOWN]:
        vy = 4
        a = 3
        screen.blit(myimgD, myrect)

    myrect.x = myrect.x+0
    if myrect.x >800:
        myrect.x=-100
    if myrect.y >600:
        myrect.y=-100
    
    ## プレイヤーの処理
    myrect.x += vx
    myrect.y += vy
    if myrect.x >=800:
        myrect.x=0
    if myrect.x < 0:
        myrect.x =800
    if myrect.colliderect(boxrect):
        myrect.x -= vx
        myrect.y -= vy
    if a == 0:
        screen.blit(myimgR, myrect)
    if a == 1:
        screen.blit(myimgL, myrect)
    if a == 2:
        screen.blit(myimgU, myrect)
    if a == 3:
        screen.blit(myimgD, myrect)
            
    
  
    ## 障害物の処理
    pg.draw.rect(screen, pg.Color("DARKGREEN"), boxrect)
    
# 2.この下をずっとル
   
while True:
    if boxrect.x == 0:
        boxrect.x = 800
    gamestage()
    # 6.画面を表示する
    boxrect.x = boxrect.x + 1 
    screen.blit(boxrect, boxrect)

    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()