import colorgram


"""Creation of color_list. Feel free to change the "image.jpg" for the name of your image
 and the number 7 for the number of colors you want to extract from the image"""

rgb_colors = []
colors = colorgram.extract("image.jpg", 7)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

if __name__ == "__main__":
    print(rgb_colors)

color_list = [(234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35)]
