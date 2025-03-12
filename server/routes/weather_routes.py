from flask import jsonify
from routes import weather_bp
from config import system_state

@weather_bp.route('/report', methods=['GET'])
def weather_report():
    weather_info = system_state["weather"]
    message = f"Thời tiết: {weather_info['condition']}, Nhiệt độ: {weather_info['temperature']}°C, Dự báo: {weather_info['forecast']}"
    system_state["interaction"]["last_command"] = "Báo cáo thời tiết"
    system_state["interaction"]["last_response"] = message
    print(message)
    return jsonify({
        "status": "success",
        "weather": weather_info,
        "message": message
    })