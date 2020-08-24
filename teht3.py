import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Krisse simulaattori")
naytto.fill((0, 0, 0))



def piirraKuva(kuvatiedosto, x, y):
    naytto.blit("Krisse.png", (x, y))
    naytto.blit("Demon.png", (x, y))

def piirtaminen(naytto, Hyvikset, Pahikset):
   
    for hyvis in Hyvikset:
        if hyvis[3] == True:
            HyvisKuva = pygame.image.load(hyvis[0]).convert()
            naytto.blit(HyvisKuva, (hyvis[1], hyvis[2]))
    pygame.display.flip()
    for pahis in Pahikset:
        if pahis[3] == True:
            PahisKuva = pygame.image.load(pahis[0]).convert()
            naytto.blit(PahisKuva, (pahis[1], pahis[2]))
    pygame.display.flip()

def kontrolli(Hyvikset, tapahtuma, Pahikset):
    paahahmo = Hyvikset[0]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            Hyvikset[0][3] = True
            Pahikset[0][3] = True
        elif tapahtuma.key == pygame.K_RIGHT and paahahmo[1] < 540:
           
            paahahmo[1] += 10
        elif tapahtuma.key == pygame.K_LEFT and paahahmo[1] > 0:
           
            paahahmo[1] -= 10
        elif tapahtuma.key == pygame.K_UP and paahahmo[2] > 0:
            
            paahahmo[2] -= 10
        elif tapahtuma.key == pygame.K_DOWN and paahahmo[2] < 300:
           
            paahahmo[2] += 10
       
            

def main():
   Krisse = ["Krisse.png", 100, 100, False]
   Pahis = ["Demon.png", 200, 200, False]
   Hyvikset = [Krisse]
   Pahikset = [Pahis]
   
   while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(Hyvikset, tapahtuma, Pahikset)
        piirtaminen(naytto, Hyvikset, Pahikset)


main()