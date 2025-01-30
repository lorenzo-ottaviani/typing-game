import pygame
import math

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Lancer de Projectile")

# Paramètres du projectile
masse = 10  # kg (non utilisé directement dans la trajectoire)
g = 10  # m/s², gravité
vitesse_initiale = 50  # m/s, vitesse initiale
angle = 45  # angle en degrés
x0, y0 = 100, hauteur_fenetre - 50  # position initiale du projectile
theta = math.radians(angle)  # conversion de l'angle en radians

# Variables de simulation
temps_initial = pygame.time.get_ticks()  # Temps initial (en millisecondes)
running = True
clock = pygame.time.Clock()

# Boucle principale
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calcul du temps écoulé
    t = (pygame.time.get_ticks() - temps_initial) / 1000  # temps en secondes

    # Calcul des positions x et y du projectile
    x = x0 + vitesse_initiale * math.cos(theta) * t
    y = y0 - (vitesse_initiale * math.sin(theta) * t - 0.5 * g * t**2)

    # Condition de fin de trajectoire (quand le projectile touche le sol)
    if y > hauteur_fenetre:
        y = hauteur_fenetre
        running = False

    # Effacer l'écran
    fenetre.fill((255, 255, 255))

    # Dessiner le projectile
    pygame.draw.circle(fenetre, (255, 0, 0), (int(x), int(y)), 10)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Limiter le nombre de frames par seconde
    clock.tick(60)

# Quitter Pygame
pygame.quit()