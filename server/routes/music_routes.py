from flask import jsonify, request
from routes import music_bp
from models import MusicPlayer
from config import system_state

@music_bp.route('/play', methods=['GET'])
def play_music():
    """Phát nhạc từ playlist được chỉ định hoặc theo cảm xúc hiện tại."""
    playlist = request.args.get('playlist')
    
    if not playlist:
        emotion = system_state["last_emotion"]
        if emotion in ["happy", "sad", "neutral", "angry", "surprise"]:
            playlist = emotion
        else:
            playlist = "neutral" 
    
    return jsonify(MusicPlayer.play(playlist))

@music_bp.route('/stop', methods=['GET'])
def stop_music():
    """Dừng phát nhạc."""
    return jsonify(MusicPlayer.stop())

@music_bp.route('/volume', methods=['GET', 'POST'])
def adjust_volume():
    """Điều chỉnh hoặc lấy thông tin âm lượng."""
    if request.method == 'POST':
        data = request.get_json()
        if 'volume' in data:
            volume = int(data['volume'])
            return jsonify(MusicPlayer.set_volume(volume))
        else:
            return jsonify({"status": "error", "message": "Thiếu thông tin âm lượng"})
    else:
        response = MusicPlayer.get_status()
        return jsonify({
            "status": "success", 
            "volume": response["volume"],
            "message": f"Âm lượng hiện tại: {response['volume']}%"
        })

@music_bp.route('/status', methods=['GET'])
def music_status():
    """Lấy trạng thái nhạc hiện tại."""
    return jsonify(MusicPlayer.get_status())