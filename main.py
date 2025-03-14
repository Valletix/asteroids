import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for d in drawable:
            d.draw(screen)
        updateable.update(dt)
        player.timer -= dt
        for a in asteroids:
            if a.collide(player):
                print("Game Over!")
                sys.exit()
            for s in shots:
                if a.collide(s):
                    a.split()
                    s.kill()

        pygame.display.flip()
        dt = (clock.tick(60))/1000

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
