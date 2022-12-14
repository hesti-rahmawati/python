# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
img1 = pg.image.load("images/cartoon.png")
img1 = pg.transform.scale(img1,(50,50))
myimage = pg.Rect(-50,300,50,50)
myrect = pg.Rect(-100,100,100,150)

# 2.この下をずっとループする
while True:
   if myrect.x >= 800:
      myrect.x = 0
   if myimage.x >= 790:
      myimage.x = 0
   # 3.画面を初期化する
   screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
   myrect.x = myrect.x + 1 
   myimage.x = myimage.x + 1
   pg.draw.rect(screen, pg.Color("RED"), myrect)
   screen.blit(img1, myimage)

    # 6.画面を表示する
   pg.display.update()
   pg.time.Clock().tick(80)
    # 7.閉じるボタンが押されたら、終了する
   for event in pg.event.get():
       if event.type == pg.QUIT:
            pg.quit()
            sys.exit()