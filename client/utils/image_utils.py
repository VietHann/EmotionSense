import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def put_text_pil(img, text, org, font_path="arial.ttf", font_size=22, color=(0, 255, 0)):

    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()
        
    draw.text(org, text, font=font, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def draw_emotion_box(frame, emotion, confidence, x, y, w, h, emotion_labels, emotion_colors, font_path="arial.ttf"):

    if emotion in emotion_labels:
        label = emotion_labels[emotion]
        color = emotion_colors[emotion]
        frame = put_text_pil(frame, label, (x, y-30), font_path=font_path, font_size=25, color=color)
        frame = put_text_pil(frame, f"{confidence:.0f}%", (x, y+h+10), font_path=font_path, font_size=22, color=(255, 255, 255))
    return frame