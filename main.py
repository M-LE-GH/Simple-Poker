import pygame
import random
from card import Card

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

#functions

def generate_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(Card(suit, value))
    return deck

deck = generate_deck()
random.shuffle(deck)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "black", (100, 100, 200, 200)) 
    ewidth = 800
    eheight = 400
    pygame.draw.ellipse(screen, "black", (width/2 - ewidth/2, height/2 - eheight/2, ewidth, eheight))
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
