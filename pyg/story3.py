# 1.ゲームの準備をする
# from curses import BUTTON2_CLICKED, BUTTON3_CLICKED, BUTTON4_CLICKED
import pygame as pg, sys
pg.init()

screen = pg.display.set_mode((800, 600))
## 紙芝居
img1 = pg.image.load("images/flower1.png")
img2 = pg.image.load("images/flower2.png")
img3 = pg.image.load("images/flower3.png")
img4 = pg.image.load("images/flower4.png")
img5 = pg.image.load("images/root3.png")
img6 = pg.image.load("images/root4.png")
img7 = pg.image.load("images/root5.png")
## ボタン
next_img = pg.image.load("images/nextbtn.png")
teasure = pg.image.load("images/box.png")
replay_img = pg.image.load("images/replaybtn.png")
pushFlag = False
## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = newpage
            pushFlag = True
    else:
        pushFlag =False
        


def page1():
    # 3.画面を初期化する
    screen.blit(img1, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 2)

def page2():
    # 3.画面を初期化する
    screen.blit(img2, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 3)

def page3():
    # 3.画面を初期化する
    screen.blit(img3, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 4)

def page4():
    # 3.画面を初期化する
    screen.blit(img4, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1,5)

def page5():
    # 3.画面を初期化する
    screen.blit(img5, (0,0))
    btn1 = screen.blit(teasure,(200, 200))
    btn2 = screen.blit(teasure,(500, 200))

    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1,7)
    button_to_jump(btn2,6)
def page6():
    # 3.画面を初期化する
    screen.blit(img6, (0,0))
    btn1 = screen.blit(replay_img,(600,540))
    button_to_jump(btn1,1)
def page7():
    # 3.画面を初期化する
    screen.blit(img7, (0,0))
    btn1 = screen.blit(replay_img,(600,540))
    button_to_jump(btn1,1)




page = 1
# 2.この下をずっとループする
while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    elif page == 3:
        page3()
    elif page == 4:
        page4()
    elif page == 5:
        page5()
    elif page == 6:
        page6()
    elif page == 7:
        page7()



    
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()