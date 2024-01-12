from PIL import Image, ImageFont, ImageDraw, ImageFilter # 10.2.0
import random

def generate_random_equation():
    # Choose a random mathematical operation (+, -, *)
    operation = random.choice(['+', '-', '*'])

    # Create two random numbers
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)

    # Ensure the result is positive for subtraction
    if operation == '-' and number1 < number2:
        number1, number2 = number2, number1  # Swap the numbers

    # Calculate the result
    result = eval(f"{number1} {operation} {number2}")

    # Create the equation
    equation = f"{number1} {operation} {number2} ="

    return equation, result

# Test the function
random_equation, result = generate_random_equation()

def backcolor():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

def wordcolor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 270
height = 100

# Create a new image with a white background
image = Image.new("RGB", (width, height), (255, 255, 255))
font = ImageFont.load_default(72)

draw = ImageDraw.Draw(image)

# Fill the image with random background colors
for x in range(width):
    for y in range(height):
        draw.point((x, y), backcolor())

# Draw the random equation text on the image with random text colors
for i in range(4):
    draw.text((60 * i + 20, 10), random_equation.split(' ')[i], fill=wordcolor(), font=font)

# Apply a blur filter to the image
image = image.filter(ImageFilter.BLUR)

# Save the blurred image as "verification.jpg"
image.save("verification.jpg", "jpeg")
#image.show()
# Print the result of the random equation
print(result)
