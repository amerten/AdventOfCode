from PIL import Image
import numpy as np


white, black = (255, 255, 255), (0, 0, 0)
width, height = 101, 103
robots = set()
for line in open(0).read().splitlines():
   a, b = line.split()
   x, y = map(int, a.split('=')[1].split(','))
   dx, dy = map(int, b.split('=')[1].split(','))
   robots.add((x, y, dx, dy))
time = 1
while time < 10000:
    positions = set()
    for robot in robots:
        x, y = (robot[0] + robot[2] * time) % width, (robot[1] + robot[3] * time) % height
        positions.add((x, y))
    pixels = []
    for y in range(height):
       new_line = []
       for x in range(width):
          new_line.append(black if (x, y) in positions else white)
       pixels.append(new_line)
    array = np.array(pixels, dtype=np.uint8)
    im = Image.fromarray(array)
    im.save(str(time) + '.png')
    time += height
