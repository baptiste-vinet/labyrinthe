import pygame
import constants

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((constants.cote_fenetre, constants.cote_fenetre))
#Icone
#icone = pygame.image.load(image_icone)
#pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption("DK game")