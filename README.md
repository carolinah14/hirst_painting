# hirst_painting (Python)

A Python Turtle graphics project that generates a 10x10 grid of colored dots inspired by Damien Hirst-style paintings. The project separates color extraction logic using the colorgram library and uses structured code to create visual patterns.

# ▶️ How to Run

1. Make sure you have Python installed on your computer.

2. Download or clone this repository.

3. Ensure the following files are in the same folder:

   main.py  
   extract_colors.py  
   image.jpg (optional, for color extraction)

4. Open a terminal (or your preferred Python IDE).

5. Navigate to the folder containing the files.

6. Run the script using:

   python main.py
   
A Turtle graphics window will open displaying the generated dot painting.

(Optional) Extracting colors from an image:
The extract_colors.py file uses the colorgram library to extract RGB values from an image.  
You can modify the image file and number of colors to generate a custom palette.

# 🧠 Concepts Practiced

- Working with Turtle graphics for visual output
- Using loops to create repeated patterns (grid structure)
- Creating and using functions to organize code
- Using docstrings for readability and documentation
- Random color selection with random.choice()
- Working with RGB color values and colormode(255)
- Separating concerns by organizing code into modules
- Extracting color palettes from images using the colorgram library
- Positioning elements using coordinates (x, y)
- Controlling drawing flow with penup(), pendown(), and movement
- Structuring programs for better readability and scalability
