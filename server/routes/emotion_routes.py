from flask import jsonify, request
from routes import emotion_bp
from config import system_state
from models import EmotionHandler, MusicPlayer
from routes.light_routes import turn_on_light, turn_off_light

@emotion_bp.route('/update', methods=['POST'])
def update_emotion():
    data = request.get_json()
    if 'emotion' in data:
        emotion = data['emotion']
        confidence = data.get('confidence', 0)
        return jsonify(EmotionHandler.update_emotion(emotion, confidence))
    else:
        return jsonify({"status": "error", "message": "Thiếu thông tin cảm xúc"})

@emotion_bp.route('/current', methods=['GET'])
def get_current_emotion():
    emotion = system_state["last_emotion"]
    message = f"Cảm xúc hiện tại: {emotion}" if emotion else "Chưa có cảm xúc nào được phát hiện"
    return jsonify({
        "status": "success",
        "emotion": emotion,
        "message": message
    })

@emotion_bp.route('/suggestion/accept/1', methods=['POST', 'GET'])
def accept_suggestion_1():
    emotion = system_state["last_emotion"]
    
    if not emotion:
        return jsonify({"status": "error", "message": "Chưa có cảm xúc nào được phát hiện"})
    
    if emotion == "happy" or emotion == "angry":
        return turn_on_light()
    elif emotion == "sad":
        return turn_off_light()
    else:
        return jsonify({"status": "error", "message": "Không có đề xuất phù hợp cho cảm xúc hiện tại"})

@emotion_bp.route('/suggestion/accept/2', methods=['POST', 'GET'])
def accept_suggestion_2():
    emotion = system_state["last_emotion"]
    
    if not emotion:
        return jsonify({"status": "error", "message": "Chưa có cảm xúc nào được phát hiện"})
    
    if emotion == "happy":
        return jsonify(MusicPlayer.play("happy"))
    elif emotion == "sad":
        return jsonify(MusicPlayer.play("sad"))
    elif emotion == "angry":
        return jsonify(MusicPlayer.play("neutral"))
    else:
        return jsonify(MusicPlayer.play("neutral"))