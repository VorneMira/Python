import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")


#def main():
 #   while True:
  #      tapahtuma = pygame.event.poll()
   #     if tapahtuma.type == pygame.QUIT:
    #        break

     #   naytto.fill((0, 0, 0))
      #  kuva = pygame.image.load("pixil-frame-0.png").convert()
       # naytto.blit(kuva, (200,200))
        #pygame.display.flip()

#main()

kuva = pygame.image.load("pixil-frame-0.png").convert()
def piirräkuva(kuva, x, y):
    while True:
      tapahtuma = pygame.event.poll()
      if tapahtuma.type == pygame.QUIT:
            break

      naytto.fill((0, 0, 0))
      naytto.blit(kuva, (x,y))
      pygame.display.flip()


piirräkuva(kuva, 200, 200)
