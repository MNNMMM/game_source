# 깃허브 테스트

import pygame
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
######################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임, 게임 이미지, 좌표, 속도, 폭트 등)
    # 배경 이미지 불러오기
    # 캐릭터 불러오기
    # 적 불러오기

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 설정


    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


    # 3. 게임 캐릭터 위치 정의
        # 가로 경계값 처리
        # 세로 경계값 처리


    # 4. 충돌처리


    # 5. 화면에 그리기
    pygame.display.update() # 게임화면을 다시 그리기!
    
pygame.quit()