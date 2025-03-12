from flask import jsonify
from routes import sensor_bp
from config import system_state

@sensor_bp.route('/temperature', methods=['GET'])
def get_temperature():
    message = f"Nhiệt độ trong phòng: {system_state['temperature']}°C, Độ ẩm: {system_state['humidity']}%"
    system_state["interaction"]["last_command"] = "Lấy nhiệt độ"
    system_state["interaction"]["last_response"] = message
    print(message)
    return jsonify({
        "status": "success",
        "temperature": system_state["temperature"],
        "humidity": system_state["humidity"],
        "message": message
    })