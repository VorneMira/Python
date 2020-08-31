import pygame
import random
import time

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Bruh")
naytto.fill((0, 0, 0))
gameOver = False
def theEnd():
   global gameOver 
   gameOver = True
   print('Bruh moment')
   
    



def piirraKuva(kuvatiedosto, x, y):
  
    naytto.blit("Krisse.png", (x, y))
    naytto.blit("Demon.png", (x, y))

def piirtaminen(naytto, Hyvikset, Pahikset):
    if Hyvikset:
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
    if Hyvikset:
        paahahmo = Hyvikset[0]
        Demoni = Pahikset[0]
       
        
            

        

        for vihollinen in Pahikset:
            if   (Hyvikset[0][1] <= Pahikset[0][1] +50 and Hyvikset[0][1] >= Pahikset[0][1] -50) and (Hyvikset[0][2] <= Pahikset[0][2]+50 and Hyvikset[0][2] >= Pahikset[0][2]-50):
                theEnd()
            elif  (Hyvikset[0][1] <= Pahikset[1][1] +50 and Hyvikset[0][1] >= Pahikset[1][1] -50) and (Hyvikset[0][2] <= Pahikset[1][2]+50 and Hyvikset[0][2] >= Pahikset[1][2]-50):
                theEnd()
            elif  (Hyvikset[0][1] <= Pahikset[2][1] +50 and Hyvikset[0][1] >= Pahikset[2][1] -50) and (Hyvikset[0][2] <= Pahikset[2][2]+50 and Hyvikset[0][2] >= Pahikset[2][2]-50):
                theEnd()
            elif  (Hyvikset[0][1] <= Pahikset[3][1] +50 and Hyvikset[0][1] >= Pahikset[3][1] -50) and (Hyvikset[0][2] <= Pahikset[3][2]+50 and Hyvikset[0][2] >= Pahikset[3][2]-50):
                theEnd()
            else:
                if Demoni[1] > 640:
                    Demoni[1] = -50
                    randomY = random.randint(50, 350)
                    Demoni[2] = randomY
                else:
                    Demoni[1] += 1
                if Pahikset[1][1] < -100:
                    Pahikset[1][1] = 690
                    randomY = random.randint(50, 350)
                    Pahikset[1][2] = randomY
                else:
                    Pahikset[1][1] -= 1.9

                if Pahikset[2][2] < -100:
                    Pahikset[2][2] = 450
                    randomX = random.randint(50, 590)
                    Pahikset[2][1] = randomX
                else:
                    Pahikset[2][2] -= 1.2
                if Pahikset[3][2] > 500:
                    Pahikset[3][2] = -50
                    randomX = random.randint(50, 590)
                    Pahikset[3][1] = randomX
                else:
                    Pahikset[3][2] += 1.5
            

                
        Oikealle = False
        Vasemmalle = False
        Ylös = False
        Alas = False  
    
        if tapahtuma.type == pygame.KEYDOWN:
           
            if tapahtuma.key == pygame.K_SPACE:
                Hyvikset[0][3] = True
                Pahikset[0][3] = True
                Pahikset[1][3] = True
                Pahikset[2][3] = True
                Pahikset[3][3] = True
            
            if tapahtuma.key == pygame.K_RIGHT: 
                Oikealle = True
            if tapahtuma.key == pygame.K_LEFT:
                Vasemmalle = True
            if tapahtuma.key == pygame.K_UP:
                Ylös = True
            if tapahtuma.key == pygame.K_DOWN: 
                Alas = True

        if tapahtuma.type == pygame.KEYUP:
          
            if tapahtuma.key == pygame.K_RIGHT:
                Oikealle = False
            if tapahtuma.key == pygame.K_LEFT:
                Vasemmalle = False
            if tapahtuma.key == pygame.K_UP:
                Ylös = False
            if tapahtuma.key == pygame.K_DOWN:
                Alas = False
        
        if Oikealle and paahahmo[1] < 540:
            paahahmo[1] += 10
        if Vasemmalle and paahahmo[1] > 0:
            paahahmo[1] -= 10
        if Ylös and  paahahmo[2] > 0:
            paahahmo[2] -= 10
        if Alas and  paahahmo[2] < 300:
            paahahmo[2] += 10
           
       
            

def main():
   Krisse = ["Krisse.png", 100, 100, False]
   Pahis = ["Demon.png", 200, 200, False]
   Pahis1 = ["Demon.png", 450, 300, False]
   Pahis2 = ["Demon.png", 450, 300, False]
   Pahis3 = ["Demon.png", 450, 300, False]
   Hyvikset = [Krisse]
   Pahikset = [Pahis, Pahis1, Pahis2, Pahis3]
   
   while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        if gameOver == True:
            print("GAME OVER!")
            break
        kontrolli(Hyvikset, tapahtuma, Pahikset)
        piirtaminen(naytto, Hyvikset, Pahikset)


main()