import sys
import pygame

from settings import Settings

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init();
    ai_settimgs = Settings()
    scree = pygame.display.set_mode((ai_settimgs.screen_width,ai_settimgs.screen_height);
    pygame.display.set_caption("Alien Invasion");

    #设置背景颜色
    bg_color = (230,230,230);

    #开始游戏主体循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();

        #每次循环时都重绘屏幕
        scree.fill(ai_settimgs.ba_color)

        #让最近绘制的屏幕可见
        pygame.display.flip();


run_game();

