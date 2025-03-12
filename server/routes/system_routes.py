from flask import jsonify
from routes import system_bp
from config import system_state

@system_bp.route('/system/status', methods=['GET'])
def system_status():
    """Lấy trạng thái tổng thể hệ thống."""
    return jsonify({
        "status": "success",
        "system_state": system_state
    })

@system_bp.route('/', methods=['GET'])
def home():
    """Trang chủ với thông tin API."""
    return """
    <html>
        <head>
            <title>IoT Server for Emotion Recognition System</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
                h1 { color: #2c3e50; }
                ul { list-style-type: none; padding: 0; }
                li { margin-bottom: 10px; }
                code { background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; }
            </style>
        </head>
        <body>
            <h1>IoT Server for Emotion Recognition System</h1>
            <p>Server đang hoạt động! Sử dụng các API endpoints sau để tương tác:</p>
            <ul>
                <li><code>GET /light/on</code> - Bật đèn</li>
                <li><code>GET /light/off</code> - Tắt đèn</li>
                <li><code>GET /light/status</code> - Kiểm tra trạng thái đèn</li>
                <li><code>GET /music/play?playlist=happy</code> - Phát nhạc theo playlist chỉ định (happy, sad, neutral, angry, surprise)</li>
                <li><code>GET /music/play</code> - Phát nhạc theo cảm xúc hiện tại</li>
                <li><code>GET /music/stop</code> - Dừng nhạc</li>
                <li><code>GET/POST /music/volume</code> - Lấy/điều chỉnh âm lượng</li>
                <li><code>GET /music/status</code> - Kiểm tra trạng thái nhạc</li>
                <li><code>GET /temperature</code> - Lấy nhiệt độ phòng</li>
                <li><code>GET /weather/report</code> - Xem báo cáo thời tiết</li>
                <li><code>POST /emotion/update</code> - Cập nhật cảm xúc (gửi JSON: {"emotion": "happy", "confidence": 95})</li>
                <li><code>GET /emotion/current</code> - Lấy cảm xúc hiện tại</li>
                <li><code>POST /emotion/suggestion/accept/1</code> - Chấp nhận đề xuất 1 (điều khiển đèn)</li>
                <li><code>POST /emotion/suggestion/accept/2</code> - Chấp nhận đề xuất 2 (phát nhạc)</li>
                <li><code>GET /system/status</code> - Lấy trạng thái tổng thể hệ thống</li>
            </ul>
        </body>
    </html>
    """