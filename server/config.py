import os

# Trạng thái hệ thống
system_state = {
    "light": False,  
    "music": {
        "playing": False,  
        "current_playlist": None,  
        "volume": 50  
    },
    "last_emotion": None, 
    "temperature": 25.0, 
    "humidity": 60, 
    "weather": {
        "condition": "sunny", 
        "temperature": 25.0, 
        "forecast": "Trời nắng, nhiệt độ từ 22-25°C" 
    },
    "interaction": {
        "last_command": None, 
        "last_response": None  
    }
}

# Danh sách nhạc theo cảm xúc
music_playlists = {
    "happy": [
        "music/happy/song1.mp3",
        "music/happy/song2.mp3",
        "music/happy/song3.mp3",
    ],
    "sad": [
        "music/sad/song1.mp3",
        "music/sad/song2.mp3",
        "music/sad/song3.mp3",
    ],
    "neutral": [
        "music/neutral/song1.mp3",
        "music/neutral/song2.mp3",
    ],
    "angry": [
        "music/angry/song1.mp3",
        "music/angry/song2.mp3",
    ],
    "surprise": [
        "music/surprise/song1.mp3",
        "music/surprise/song2.mp3",
    ]
}

# Cấu hình server
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
DEBUG_MODE = False

# Thư mục lưu trữ nhạc
MUSIC_DIRECTORIES = ["music/happy", "music/sad", "music/neutral", "music/angry", "music/surprise"]