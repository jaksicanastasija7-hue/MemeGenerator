from flask import Flask, request, render_template
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/generated"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def draw_text(draw, text, font, position, outline=3):
    x, y = position
    for dx in range(-outline, outline+1):
        for dy in range(-outline, outline+1):
            draw.text((x+dx, y+dy), text, font=font, fill="black")
    draw.text(position, text, font=font, fill="white")

def fit_text(draw, text, image_width, font_path, max_fraction=0.9):
    font_size = int(image_width / 2)
    font = ImageFont.truetype(font_path, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    while text_width > image_width * max_fraction:
        font_size -= 2
        font = ImageFont.truetype(font_path, font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
    return font

@app.route("/", methods=["GET", "POST"])
def meme_generator():
    if request.method == "POST":
        image_file = request.files["image"]
        top_text = request.form["top_text"]
        bottom_text = request.form["bottom_text"]
        if image_file:
            img = Image.open(image_file)
            draw = ImageDraw.Draw(img)
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

            top_font = fit_text(draw, top_text, img.width, font_path)
            top_bbox = draw.textbbox((0, 0), top_text, font=top_font)
            top_w, top_h = top_bbox[2] - top_bbox[0], top_bbox[3] - top_bbox[1]
            top_position = ((img.width - top_w) / 2, 10)
            draw_text(draw, top_text, top_font, top_position)

            bottom_font = fit_text(draw, bottom_text, img.width, font_path)
            bottom_bbox = draw.textbbox((0, 0), bottom_text, font=bottom_font)
            bottom_w, bottom_h = bottom_bbox[2] - bottom_bbox[0], bottom_bbox[3] - bottom_bbox[1]
            bottom_position = ((img.width - bottom_w) / 2, img.height - bottom_h - 10)
            draw_text(draw, bottom_text, bottom_font, bottom_position)

            file_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
            img.save(file_path)
            return render_template("index.html", meme_url=file_path)
    return render_template("index.html", meme_url=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
