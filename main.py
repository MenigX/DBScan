from src.point import Point
from src.graph import Graph
import pygame
import sys
import random

EPS = 50
MIN_PTS = 3

def get_cluster_color(cluster_id):
    if cluster_id == 0:
        return (255, 0, 0)
    random.seed(cluster_id * 12345)
    return (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))


def main():
    graph = Graph(EPS, MIN_PTS)
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    last_point = None
    is_pressed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_pressed = False         
                
        if is_pressed:
            x, y = pygame.mouse.get_pos()
            point = Point(x, y)
            if last_point == None or last_point.dist(point) > 3:
                graph.push_point(point)
                last_point = point

        window.fill((255, 255, 255))
        points = graph.get_keys()
        for point in points:
            pygame.draw.circle(window, get_cluster_color(point.get_color()), point.get_cords(), 2)
        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()
