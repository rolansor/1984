import pygame
import os


pygame.mixer.pre_init(16500, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()                              #initialize pygame

# look for sound & music files in subfolder 'data'
pygame.mixer.music.load(os.path.join('sounds', 'marcha.mp3'))#load music
inicio1 = pygame.mixer.Sound(os.path.join('sounds','Inicio1.wav'))  #load sound
inicio2 = pygame.mixer.Sound(os.path.join('sounds','Inicio2.wav'))  #load sound
final = pygame.mixer.Sound(os.path.join('sounds','Final.wav'))  #load sound
GH1 = pygame.mixer.Sound(os.path.join('sounds','GH2.wav'))  #load sound
GH2= pygame.mixer.Sound(os.path.join('sounds','GH1.wav'))  #load sound
OBa = pygame.mixer.Sound(os.path.join('sounds','OBa.wav'))  #load sound
OBb = pygame.mixer.Sound(os.path.join('sounds','OBb.wav'))  #load sound
OBc = pygame.mixer.Sound(os.path.join('sounds','OBc.wav'))  #load sound
OB1a = pygame.mixer.Sound(os.path.join('sounds','OB1a.wav'))  #load sound
OB1b = pygame.mixer.Sound(os.path.join('sounds','OB1b.wav'))  #load sound
OB1c = pygame.mixer.Sound(os.path.join('sounds','OB1c.wav'))  #load sound
OB11a = pygame.mixer.Sound(os.path.join('sounds','OB11a.wav'))  #load sound
OB11b = pygame.mixer.Sound(os.path.join('sounds','OB11b.wav'))  #load sound
OB12a = pygame.mixer.Sound(os.path.join('sounds','OB12a.wav'))  #load sound
OB2 = pygame.mixer.Sound(os.path.join('sounds','OB2.wav'))  #load sound
OB111 = pygame.mixer.Sound(os.path.join('sounds','OB111.wav'))  #load sound
OB112a = pygame.mixer.Sound(os.path.join('sounds','OB112a.wav'))  #load sound
OB112b = pygame.mixer.Sound(os.path.join('sounds','OB112b.wav'))  #load sound
OBI = pygame.mixer.Sound(os.path.join('sounds','OBI.wav'))  #load sound
GHI = pygame.mixer.Sound(os.path.join('sounds','GHI.wav'))  #load sound
WSI = pygame.mixer.Sound(os.path.join('sounds','WSI.wav'))  #load sound
# play music non-stop
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)                           

inicio1.play()
pygame.time.delay(22000)
# game loop
gameloop = True

while gameloop:
    inicio2.play()
    pygame.time.delay(23000)
    answer1 = raw_input("Ingresa el numero del personaje con el que deseas avanzar")
    answer1 = answer1.lower()
    if "1" in answer1:
        WSI.play()
    elif "2" in answer1:
        GHI.play()
        pygame.time.delay(3000)
        GH2.play()
        pygame.time.delay(19000)
        final.play()
        pygame.time.delay(11000)
        answer2 = raw_input("Escoge la Opcion")
        answer2 = answer2.lower()
        if "1" in answer2:
            gameloop= False
        elif "3" in answer2:
            gameloop = True
    elif "3" in answer1:
        OBI.play()
        pygame.time.delay(3000)
        OBa.play()
        pygame.time.delay(12000)
        OBb.play()
        pygame.time.delay(19000)
        OBc.play()
        pygame.time.delay(11000)
        answer3 = raw_input("Escoge la Opcion que desees")
        answer3 = answer3.lower()
        if "1" in answer3:
            OB1a.play()
            pygame.time.delay(12000)
            OB1b.play()
            pygame.time.delay(9000)
            OB1c.play()
            pygame.time.delay(9000)
            answer4 = raw_input("Escoge la Opcion que desees")
            answer4 = answer4.lower()
            if "1" in answer4:
                OB11a.play()
                pygame.time.delay(8000)
                OB11b.play()
                pygame.time.delay(13000)
                answer5 = raw_input("Escoge la Opcion que desees")
                answer5 = answer5.lower()
                if "1" in answer5:
                    OB111.play()
                    pygame.time.delay(9000)
                    final.play()
                    pygame.time.delay(11000)    
                    answer6 = raw_input("Escoge la Opcion")
                    answer6 = answer6.lower()
                    if "1" in answer6:
                        gameloop= False
                    elif "3" in answer6:
                        gameloop = True
                elif "2" in answer5:
                    OB112a.play()
                    pygame.time.delay(11000)
                    OB112b.play()
                    pygame.time.delay(10000)
                    final.play()
                    pygame.time.delay(11000)    
                    answer7 = raw_input("Escoge la Opcion")
                    answer7 = answer7.lower()
                    if "1" in answer7:
                        gameloop= False
                    elif "3" in answer7:
                        gameloop = True
            elif "2" in answer4:
                OB12a.play()
                pygame.time.delay(8000)  
                final.play()
                pygame.time.delay(11000)    
                answer = raw_input("Escoge la Opcion")
                answer = answer.lower()
                if "1" in answer:
                    gameloop= False
                elif "3" in answer:
                    gameloop = True
                
        elif "2" in answer3:
            OB2.play()
            pygame.time.delay(11000)  
            final.play()
            pygame.time.delay(11000)    
            answer = raw_input("Escoge la Opcion")
            answer = answer.lower()
            if "1" in answer:
                gameloop= False
            elif "3" in answer:
                gameloop = True


pygame.quit() # clean exit 