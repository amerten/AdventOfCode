from PIL import Image
import numpy as np


width, height = 101, 103
robots = set()
# for line in open(0).read().splitlines():
#    a, b = line.split()
#    x, y = map(int, a.split('=')[1].split(','))
#    dx, dy = map(int, b.split('=')[1].split(','))
#    robots.add((x, y, dx, dy))
# time = 1
# while time < 10:
#     positions = set()
#     for robot in robots:
#         x, y = (robot[0] * robot[2] * time) % width, (robot[1] + robot[3] * time) % height
#         positions.add((x, y))
#     with open(str(time) + ".txt", "w") as f:
#         for y in range(height):
#             for x in range(width):
#                 if (x, y) in positions:
#                     f.write('#')
#                 else:
#                     f.write(' ')
#             f.write('\r\n')
#     time += 1

pixels = [
   [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
   [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
   [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
   [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
]

# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')
