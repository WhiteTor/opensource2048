import pygame

pygame.init()
screen_width = 540
screen_height = 725

screen = pygame.display.set_mode((screen_width, screen_height))#배경
pygame.display.set_caption("2048")
background = pygame.image.load("C:/Users/hth09/OneDrive/바탕 화면/desktop/2048/start_screen.jpg")
screen.blit(background, (0,0))

start_button = pygame.Rect(150, 550, 250 , 100)#종료 버튼

start = False
running = True
while running:
  click_pos = None

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP:
      click_pos = pygame.mouse.get_pos()
      print(click_pos)

  if click_pos != None:
    if start_button.collidepoint(click_pos):
      start = True
      running = False

  
  pygame.display.update()

pygame.quit()