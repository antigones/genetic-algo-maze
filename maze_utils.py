import numpy as np
from PIL import Image, ImageDraw, ImageFont

def carve_maze(grid: np.ndarray, size: int) -> np.ndarray:
    output_grid = np.empty([size*3, size*3], dtype=str)
    output_grid[:] = '#'

    i = 0
    j = 0
    while i < size:
        w = i*3 + 1
        while j < size:
            k = j*3 + 1
            toss = grid[i, j]
            output_grid[w, k] = ' '
            if toss == 0 and k+2 < size*3:
                output_grid[w, k+1] = ' '
                output_grid[w, k+2] = ' '
            if toss == 1 and w-2 >= 0:
                output_grid[w-1, k] = ' '
                output_grid[w-2, k] = ' '

            j = j + 1

        i = i + 1
        j = 0

    return output_grid


def preprocess_grid(grid: np.ndarray, size: int) -> np.ndarray:
    # fix first row and last column to avoid digging outside the maze external borders
    first_row = grid[0]
    first_row[first_row == 1] = 0
    grid[0] = first_row
    for i in range(1, size):
        grid[i, size-1] = 1
    return grid

def add_grid_to_image_list(grid:np.ndarray, image_list:list, fit:int) -> list :
    """
    creates a copy of the current grid to be converted in an image by replacing 
    its values with actual pixel colors.

    outputs the current grid status to an image, to be added to
    image_list to produce an animated gif
    """
    img_grid = grid.copy()
 
    img_grid[img_grid==0] = 100
    img_grid[img_grid==1] = 0
    im = Image.fromarray(img_grid)
    
    
    if im.mode != 'RGB':
        im = im.convert('RGB')
    size = 300, 300
    img = im.resize(size, Image.NEAREST)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 26)
    draw.text((0, 0), text=str(fit), fill='white', stroke_fill='white', font=font)
    image_list.append(img)
    if fit == 0:
        image_list.append(img)
        image_list.append(img)
        image_list.append(img)
        image_list.append(img)
        image_list.append(img)
        image_list.append(img)
