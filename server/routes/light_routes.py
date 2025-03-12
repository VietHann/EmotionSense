from flask import jsonify
from routes import light_bp
from config import system_state

@light_bp.route('/on', methods=['GET'])
def turn_on_light():
    """Bật đèn."""
    system_state["light"] = True
    system_state["interaction"]["last_command"] = "Bật đèn"
    system_state["interaction"]["last_response"] = "Đã bật đèn"
    print("Đã BẬT đèn")
    return jsonify({"status": "success", "message": "Đèn đã được bật", "state": system_state["light"]})

# @light_bp.route('/suggestion/accept/1', methods=['GET'])
# def turn_on_light():
#    ...

@light_bp.route('/off', methods=['GET'])
def turn_off_light():
    """Tắt đèn."""
    system_state["light"] = False
    system_state["interaction"]["last_command"] = "Tắt đèn"
    system_state["interaction"]["last_response"] = "Đã tắt đèn"
    print("Đã TẮT đèn")
    return jsonify({"status": "success", "message": "Đèn đã được tắt", "state": system_state["light"]})

@light_bp.route('/status', methods=['GET'])
def light_status():
    """Lấy trạng thái đèn."""
    status = "Đang bật" if system_state["light"] else "Đang tắt"
    return jsonify({"status": "success", "light": system_state["light"], "message": status})