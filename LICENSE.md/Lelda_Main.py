
#Initialisation
import pygame, math, os
from pygame.locals import *
from PIL import *

pygame.init()

#Facilitation d'accès aux fichiers
def chemin_assets(fichier):

    return os.path.join('assets', fichier)

#Couleur
BLANC = (255,255,255)
NOIR = (0,0,0)
SOL = (252,216,168)
VERTARBRE = (0, 168, 0)

#Fenêtre
Taille_Fenetre = (1024,768)
Fenetre = pygame.display.set_mode(Taille_Fenetre)

#Niveaux
Accueil = pygame.image.load("logo.png").convert()

Niveau_1 = pygame.image.load(chemin_assets("Niveau1.png")).convert()
Niveau_2 = pygame.image.load(chemin_assets("Niveau2.png")).convert()
Niveau_3 = pygame.image.load(chemin_assets("Niveau3.png")).convert()
Niveau_4 = pygame.image.load(chemin_assets("Niveau4.png")).convert()
Donjon = pygame.image.load(chemin_assets("Donjon.png")).convert()

#Zones
Niveau1_rect = pygame.Rect((70,115), (850,550))
Niveau2_rect = pygame.Rect((150,185), (825, 460))
Niveau3_rect = pygame.Rect((0,190), (965,490))
Niveau4_rect = pygame.Rect((100, 190), (1024,480))
Donjon_rect = pygame.Rect((125,145),(735,510))

#Transitions
Niveau1_Donjon = pygame.Rect((211,105),(280,115))
Niveau1_Niveau2 = pygame.Rect((865, 350), (865+50,350+85))
Donjon_Niveau1 = pygame.Rect((430,600), (550, 650))
Niveau2_Niveau1 = pygame.Rect((145,445), (200,640))
Niveau2_Niveau3 = pygame.Rect((800,180), (965, 225))
Niveau3_Niveau2 = pygame.Rect((800, 600), (960, 670))
Niveau3_Niveau4 = pygame.Rect((0,400), (70,500))
Niveau4_Niveau3 = pygame.Rect((990,190), (1024, 670))
Niveau4_Donjon = pygame.Rect((400,90), (440, 150))

#PNG
Benzona = pygame.image.load(chemin_assets("Benzona.png")).convert_alpha()
Lelda = pygame.image.load(chemin_assets("Lelda.png")).convert()

#Dialogues
SpeechB = pygame.image.load(chemin_assets("SpeechBenzona.png")).convert()
SpeechB.set_colorkey(NOIR)

SpeechL = pygame.image.load(chemin_assets("SpeechLelda.jpg")).convert()
SpeechL.set_colorkey(NOIR)

#Lainque
LainqueTest = pygame.image.load(chemin_assets("LainqueB1.png")).convert_alpha()
LainqueTestimg = LainqueTest

LainqueTest = { 'rect' : LainqueTest.get_rect(center = (512, 384)),
                'vitesse' : (0,0)}
LainqueTest['position'] = LainqueTest['rect'].topleft

LainqueB1 = pygame.image.load(chemin_assets("LainqueB1.png")).convert_alpha()
LainqueB2 = pygame.image.load(chemin_assets("LainqueB2.png")).convert_alpha()
LainqueH1 = pygame.image.load(chemin_assets("LainqueH1.png")).convert_alpha()
LainqueH2 = pygame.image.load(chemin_assets("LainqueH2.png")).convert_alpha()
LainqueG1 = pygame.image.load(chemin_assets("LainqueG1.png")).convert_alpha()
LainqueG2 = pygame.image.load(chemin_assets("LainqueG2.png")).convert_alpha()
LainqueD1 = pygame.image.load(chemin_assets("LainqueD1.png")).convert_alpha()
LainqueD2 = pygame.image.load(chemin_assets("LainqueD2.png")).convert_alpha()

LainqueAD = pygame.image.load(chemin_assets("LainqueAD.png")).convert_alpha()
LainqueAG = pygame.image.load(chemin_assets("LainqueAG.png")).convert_alpha()
LainqueAH = pygame.image.load(chemin_assets("LainqueAH.png")).convert_alpha()
LainqueAB = pygame.image.load(chemin_assets("LainqueAB.png")).convert_alpha()

#Fonctions

def Mouvement (LainqueTest, acceleration):

    vx, vy = LainqueTest['vitesse']
    ax, ay = acceleration
    LainqueTest['vitesse'] = (vx + ax, vy + ay)

    return LainqueTest['vitesse']

def Position (LainqueTest) :

    vx, vy = LainqueTest['vitesse']
    x, y = LainqueTest['position']
    x += vx
    y += vy
    LainqueTest['position'] = (x, y)
    LainqueTest['rect'].topleft = (x, y)

def Delimitation (LainqueTest, Zone) :

    x, y = LainqueTest['position']
    largeur, hauteur = LainqueTest['rect'].size

    if x < Zone.left :
        x = Zone.left
    elif x + largeur > Zone.right :
        x = Zone.right - largeur
    if y < Zone.top :
        y = Zone.top
    elif y + hauteur > Zone.bottom :
        y = Zone.bottom - hauteur

    LainqueTest['position'] = (x,y)
    LainqueTest['rect'].topleft = (x,y)

#Musique et autres
Icone = pygame.image.load("logo.png").convert()
pygame.display.set_icon(Icone)

pygame.display.set_caption("The Legend Of Lelda")

pygame.mixer.init()
Musique = pygame.mixer.music.load(chemin_assets("Overworld.mp3"))
pygame.mixer.music.play(42, 0.0)

#Variables
Continuer = 1
Niveau = 0

#Boucle du jeu
while Continuer == 1 :

    for event in pygame.event.get() :

        if event.type == QUIT :

            Continuer = 0

        elif event.type == KEYDOWN :

            if event.key == K_ESCAPE :

                Continuer = 0

            elif event.key == K_RIGHT or event.key == K_d :

                Mouvement(LainqueTest, (2, 0))
                LainqueTestimg = LainqueD1

            elif event.key == K_LEFT or event.key == K_q :

                Mouvement(LainqueTest, (-2, 0))
                LainqueTestimg = LainqueG1

            elif event.key == K_UP or event.key == K_z :

                Mouvement(LainqueTest, (0, -2))
                LainqueTestimg = LainqueH1

            elif event.key == K_DOWN or event.key == K_s :

                Mouvement(LainqueTest, (0, 2))
                LainqueTestimg = LainqueB1

        elif event.type == KEYUP :

            if event.key == K_RIGHT or event.key == K_d :

                Mouvement(LainqueTest, (-2, 0))
                LainqueTestimg = LainqueD2

            elif event.key == K_LEFT or event.key == K_q :

                Mouvement(LainqueTest, (2, 0))
                LainqueTestimg = LainqueG2

            elif event.key == K_UP or event.key == K_z :

                Mouvement(LainqueTest, (0, 2))
                LainqueTestimg = LainqueH2

            elif event.key == K_DOWN or event.key == K_s :

                Mouvement(LainqueTest, (0, -2))
                LainqueTestimg = LainqueB2

    Position(LainqueTest)
    print (LainqueTest['rect'].topleft)

    if Niveau == 0 :

        Fenetre.fill(Color("White"))
        Fenetre.blit(Accueil, (322, 284))


        for event in pygame.event.get() :

            if event.type == KEYDOWN :

                if event.key == K_SPACE or event.key == K_RETURN :

                    Niveau = 1
                    NiveauBefore = 0

    if Niveau == 1 :

        Fenetre.blit(Niveau_1, (0,0))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Niveau1_rect)

        if Niveau1_Donjon.contains(LainqueTest['rect'])  :

            Niveau = 10
            LainqueTest['position'] = (490, 560)

        if Niveau1_Niveau2.contains(LainqueTest['rect']) :

            Niveau = 2
            LainqueTest['position'] = (275, 420)

    if Niveau == 10 :

        Fenetre.blit(Donjon, (0,0))
        Fenetre.blit(Benzona, (475, 340))
        Fenetre.blit(SpeechB, (275, 240))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Donjon_rect)

        if Donjon_Niveau1.contains(LainqueTest['rect']) :

            Niveau = 1
            LainqueTest['position'] = (230, 320)

    if Niveau == 2 :

        Fenetre.blit(Niveau_2, (0,0))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Niveau2_rect)

        if Niveau2_Niveau1.contains(LainqueTest['rect']):

            Niveau = 1
            LainqueTest['position'] = (765, 370)

        if Niveau2_Niveau3.contains(LainqueTest['rect']) :

            Niveau = 3
            LainqueTest['position'] = (850, 560)

    if Niveau == 3 :

        Fenetre.blit(Niveau_3, (0,0))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Niveau3_rect)

        if Niveau3_Niveau2.contains(LainqueTest['rect']) :

            Niveau = 2
            LainqueTest['position'] = (799, 200)

        if Niveau3_Niveau4.contains(LainqueTest['rect']) :

            Niveau = 4
            LainqueTest['position'] = (900, 470)

    if Niveau == 4 :

        Fenetre.blit(Niveau_4, (0,0))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Niveau4_rect)

        if Niveau4_Donjon.contains(LainqueTest['rect']) :

            Niveau = 20
            LainqueTest['position'] = (490, 560)

        if Niveau4_Niveau3.contains(LainqueTest['rect']):

            Niveau = 3
            LainqueTest['position'] = (60, 400)

    if Niveau == 20 :

        Fenetre.blit(Donjon, (0,0))
        Fenetre.blit(Lelda, (475,340))
        Fenetre.blit(SpeechL, (390, 250))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Donjon_rect)

        if Donjon_Niveau1.contains(LainqueTest['rect']) :

            Niveau = 4
            LainqueTest['position'] = (510, 230)

    if Niveau == 4 :

        Fenetre.blit(Niveau_4, (0,0))
        Fenetre.blit(LainqueTestimg, LainqueTest['rect'])
        Delimitation(LainqueTest, Niveau4_rect)

        if Niveau4_Donjon.contains(LainqueTest['rect']) :

            Niveau = 20
            LainqueTest['position'] = (490, 560)

        if Niveau4_Niveau3.contains(LainqueTest['rect']):

            Niveau = 3
            LainqueTest['position'] = (60, 470)

    pygame.display.flip()

pygame.quit()
