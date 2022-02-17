import pygame

pygame.init()

window = pygame.display.set_mode([400,480])

window.fill((255, 255, 255))

black = (0, 0, 0)

pygame.draw.line(window, black, (160, 120), (120, 160), 2)

pygame.draw.line(window, black, (120, 160), (120, 240), 2)

pygame.draw.line(window, black, (120, 240), (80, 320), 2)

pygame.draw.line(window, black, (80, 320), (120, 320), 2)

pygame.draw.line(window, black, (120, 320), (120, 380), 2)

pygame.draw.line(window, black, (120, 380), (160, 400), 2)

pygame.draw.line(window, black, (160, 400), (200, 400), 2)

pygame.draw.line(window, black, (160, 120), (160, 100), 2)

pygame.draw.line(window, black, (160, 100), (320, 100), 2)

pygame.draw.line(window, black, (320, 100), (320, 280), 2)

pygame.draw.line(window, black, (320, 280), (280, 280), 2)

pygame.draw.line(window, black, (280, 280), (160, 120), 2)

pygame.draw.line(window, black, (290, 280), (290, 400), 2)

pygame.draw.line(window, black, (170, 220), (140, 240), 2)

pygame.draw.line(window, black, (170, 220), (200, 240), 2)

pygame.draw.line(window, black, (170, 255), (140, 240), 2)

pygame.draw.line(window, black, (170, 255), (200, 240), 2)

pygame.draw.line(window, black, (170, 220), (170, 240), 2)

pygame.draw.line(window, black, (170, 240), (155, 240), 2)

pygame.draw.line(window, black, (155, 240), (155, 230), 2)

pygame.draw.line(window, black, (120, 340), (170, 340), 2)

pygame.draw.line(window, black, (170, 340), (190, 330), 2)

pygame.display.flip()

input("Please press the Enter key to proceed")
