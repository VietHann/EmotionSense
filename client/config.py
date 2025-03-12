
# Server IoT
# IOT_SERVER_URL = "http://127.0.0.1:5000"
IOT_SERVER_URL = "http://172.20.10.3:5000"

# Cấu hình camera
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

# Cấu hình âm thanh
SOUND_DIR = 'sounds'
EMOTION_SOUNDS = {
    'happy': 'sounds/happy.mp3',
    'sad': 'sounds/sad.mp3',
    'angry': 'sounds/angry.mp3',
    'neutral': 'sounds/neutral.mp3',
    'surprise': 'sounds/surprise.mp3',
    'fear': 'sounds/neutral.mp3',
    'disgust': 'sounds/neutral.mp3'
}
COMMAND_SUCCESS_SOUND = 'sounds/command_success.mp3'

# Cấu hình nhận diện cảm xúc
EMOTION_LABELS = {
    'angry': 'TỨC GIẬN',
    'disgust': 'TỨC GIẬN',
    'fear': 'NGẠC NHIÊN',
    'happy': 'VUI VẺ',
    'sad': 'BUỒN',
    'surprise': 'NGẠC NHIÊN',
    'neutral': 'BÌNH THƯỜNG'
}

EMOTION_COLORS = {
    'angry': (0, 0, 255),
    'disgust': (0, 0, 255),
    'fear': (255, 165, 0),
    'happy': (0, 255, 255),
    'sad': (255, 0, 0),
    'surprise': (255, 165, 0),
    'neutral': (128, 128, 128)
}

# Danh sách từ khóa cần lọc khi nhận diện giọng nói
FILTER_KEYWORDS = [
    "có vẻ", "phát hiện", "cảm xúc", "vui vẻ", "buồn", "tức giận", "bình thường",
    "không gian", "yên tĩnh", "phát một bản", "nhẹ nhàng", "thư giãn"
]

# Cấu hình font chữ
DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_SIZE = 22

# Thời gian
EMOTION_COOLDOWN = 2.0  # Thời gian chờ giữa các lần phát hiện cảm xúc (giây)
AMBIENT_NOISE_DURATION = 0.2  # Thời gian điều chỉnh tiếng ồn xung quanh (giây)