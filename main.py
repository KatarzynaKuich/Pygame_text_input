import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text input")

# Creating text
base_font = pygame.font.Font(None, 32)
user_text = 'Hello :)'

input_rect = pygame.Rect(100, 100, 140, 32)
color_active = pygame.Color('blue')
color_passive = pygame.Color('gray15')
color = color_passive

active = False  # check if box selected
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:  # any button pressed
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # delete last letter
                else:
                    user_text += event.unicode  # display what is written on screen
    screen.fill((0, 0, 0,))
    pygame.draw.rect(screen, color, input_rect, 2)  # 2 border
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)
