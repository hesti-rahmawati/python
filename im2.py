# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
img1 = pg.image.load("images/images.jpg")
img1 = pg.transform.scale(img1,(150,100))
img2 = pg.image.load("images/images1.jpg")
img2 = pg.transform.scale(img2,(500,300))
img3 = pg.image.load("images/cartoon.png")
img3 = pg.transform.scale(img3,(200,100))


# 2.この下をずっとループする
while (True):
    # 3.画面を初期化する
    screen.fill(pg.Color("RED"))
    # 5.絵を描いたり、判定したりする
    screen.blit(img1, (50,50))
    screen.blit(img2, (250,100))
    screen.blit(img3, (50,50))
    
    # 6.画面を表示する
    pg.display.update()
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()