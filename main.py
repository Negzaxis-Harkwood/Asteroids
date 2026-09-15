import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #intialize pygame
    pygame.init()

    # dt /clock and /fps 
    clock = pygame.time.Clock()
    dt = 0.0


    # set gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add player to our groups
    Player.containers = (updatable, drawable)

    # Add Asteroid to our groups
    Asteroid.containers = (updatable, drawable, asteroids)

    # Add AsteroidField to our groups
    AsteroidField.containers = (updatable,)

    # Add Shots to our groups
    Shot.containers = (shots, updatable, drawable)

    # instaniate player
    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)

    # create the asteroid field
    asteroid_field = AsteroidField()


    # Game Loop
    while True:
        log_state()
        # process pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        # player - asteroid collision check
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print(f"Game over!")
                sys.exit()
        # asteroid - shot collision check
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


    # console print statements 
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
