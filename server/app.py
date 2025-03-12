from flask import Flask
from flask_cors import CORS
import threading
import time

from utils import initialize_directories
from models import MusicPlayer, SensorData
from routes import register_routes
from config import SERVER_HOST, SERVER_PORT, DEBUG_MODE

app = Flask(__name__)
CORS(app)

register_routes(app)

def update_simulated_data():
    while True:
        SensorData.update_simulated_data()
        time.sleep(10)

if __name__ == "__main__":
    initialize_directories()
    
    MusicPlayer.initialize()
    
    update_thread = threading.Thread(target=update_simulated_data)
    update_thread.daemon = True
    update_thread.start()
    
    print("Khởi động IoT Server cho Hệ thống Nhận diện Cảm xúc...")
    print(f"Server đang chạy tại địa chỉ: http://{SERVER_HOST}:{SERVER_PORT}/")
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG_MODE)