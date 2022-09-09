# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("PINK"))
    # 5.絵を描いたり、判定したりする
    pg.draw.rect(screen, pg.Color("PURPLE"), (100, 100, 100, 150),5)
    pg.draw.line(screen, pg.Color("GREEN"), (200, 90), (100, 250),5)
    pg.draw.ellipse(screen, pg.Color("YELLOW"), (110, 150, 80, 80),5)
    # 6.画面を表示する
    pg.display.update()
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    