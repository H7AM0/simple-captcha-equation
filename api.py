from flask import *
from telegraph import upload_file
from PIL import Image, ImageFont, ImageDraw, ImageFilter # 10.2.0
import random

def generate_random_equation():
    operation = random.choice(['+', '-', '*'])
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    if operation == '-' and number1 < number2:
        number1, number2 = number2, number1
    result = eval(f"{number1} {operation} {number2}")
    equation = f"{number1} {operation} {number2} ="
    return equation, result

def backcolor():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

def wordcolor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def verification():
    try:
        random_equation, result = generate_random_equation()
        width = 270
        height = 100
        image = Image.new("RGB", (width, height), (255, 255, 255))
        font = ImageFont.load_default(72)
        draw = ImageDraw.Draw(image)
        for x in range(width):
            for y in range(height):
                draw.point((x, y), backcolor())
        for i in range(4):
            draw.text((60 * i + 20, 10), random_equation.split(' ')[i], fill=wordcolor(), font=font)
        image = image.filter(ImageFilter.BLUR)
        image.save("verification.jpg", "jpeg")
        up = upload_file('verification.jpg')
        linkk = f'https://telegra.ph{up[0]}'
        hamoo= {'status':True,'photo':f'{linkk}','result':f'{result}'}
    except:
        hamoo= {'status':False}
    json_data = json.dumps(hamoo, sort_keys=True, indent=4 , ensure_ascii=False)
    response = Response(json_data, content_type="application/json; charset=utf-8")
    return response



if __name__ == "__main__":
    app.run(debug=True)