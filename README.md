# 🎓 DaiNam University 

<div align="center">

<p align="center">
  <img src="docs/images/logo.png" alt="DaiNam University Logo" width="200"/>
  <img src="docs/images/AIoTLab_logo.png" alt="AIoTLab Logo" width="170"/>
</p>

[![Made by AIoTLab](https://img.shields.io/badge/Made%20by%20AIoTLab-blue?style=for-the-badge)](https://fit.dainam.edu.vn)
[![Faculty of IT](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-green?style=for-the-badge)](https://fit.dainam.edu.vn)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-red?style=for-the-badge)](https://dainam.edu.vn)




# 🧠 Hệ Thống Nhận Diện Cảm Xúc và Tương Tác Môi Trường
</div>
Hệ thống thông minh nhận diện cảm xúc của người dùng qua khuôn mặt và giọng nói, kết hợp với điều khiển các thiết bị IoT (đèn, nhạc, nhiệt độ) để tạo môi trường phù hợp với trạng thái cảm xúc.

![t-SNE](https://i.imgur.com/VvuPDLz.png)


## 🌟 Tổng Quan

Hệ thống bao gồm ba thành phần chính:

1. **📱 Ứng dụng Client**: Chạy trên máy tính, sử dụng camera để nhận diện cảm xúc qua khuôn mặt và micro để nhận diện lệnh giọng nói
2. **⚙️ IoT Server**: Điều khiển và quản lý các thiết bị IoT (đèn, nhạc, cảm biến)
3. **💡 Thiết Bị IoT**: ESP32 kết nối với đèn và các thiết bị thông minh khác
      
Kiến trúc:
<p align="center">
  <img src="docs/images/das.png" alt="System Architecture" width="800"/>
</p>


## 🏗️ Giới thiệu

- **🧠 Nhận diện cảm xúc**: Phát hiện 7 cảm xúc cơ bản (vui vẻ, buồn, tức giận, bình thường, ngạc nhiên, sợ hãi, kinh tởm)
- **🎤 Điều khiển bằng giọng nói**: Nhận diện và thực hiện lệnh điều khiển thiết bị
- **💡 Tự động đưa ra đề xuất**: Dựa trên cảm xúc để điều chỉnh môi trường (bật/tắt đèn, phát nhạc phù hợp)
- **🔊 Phản hồi bằng giọng nói**: Thông báo và phản hồi bằng giọng nói tiếng Việt

## 🛠️ CÔNG NGHỆ SỬ DỤNG

<div align="center">

### 📡 Phần cứng
[![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)](https://www.espressif.com/)
[![LED](https://img.shields.io/badge/LED-green?style=for-the-badge)]()
[![WiFi](https://img.shields.io/badge/WiFi-2.4GHz-orange?style=for-the-badge)]()
[![Camera](https://img.shields.io/badge/Camera-blue?style=for-the-badge)]()
[![Microphone](https://img.shields.io/badge/Microphone-purple?style=for-the-badge)]()

### 🖥️ Phần mềm
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![DeepFace](https://img.shields.io/badge/DeepFace-AI-red?style=for-the-badge)](https://github.com/serengil/deepface)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-yellow?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-blue?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-orange?style=for-the-badge)](https://pypi.org/project/SpeechRecognition/)
[![gTTS](https://img.shields.io/badge/Google-TTS-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://pypi.org/project/gTTS/)
[![Pygame](https://img.shields.io/badge/Pygame-Audio-darkgreen?style=for-the-badge&logo=pygame)](https://www.pygame.org/)
[![Arduino IDE](https://img.shields.io/badge/Arduino-IDE-00979D?style=for-the-badge&logo=arduino&logoColor=white)](https://www.arduino.cc/en/software)

### 🔄 Kết nối & Giao thức
[![HTTP](https://img.shields.io/badge/HTTP-RESTful-green?style=for-the-badge)]()
[![JSON](https://img.shields.io/badge/JSON-Data-lightgrey?style=for-the-badge&logo=json)]()
[![MQTT](https://img.shields.io/badge/MQTT-IoT-yellow?style=for-the-badge)](https://mqtt.org/)

</div>


## ⚙️ Cài Đặt và Chạy

### 1. Cài đặt các gói phụ thuộc

```bash
pip install -r requirements.txt
```

### 2. Khởi động Server IoT

```bash
cd server
python app.py
```

Server sẽ chạy ở địa chỉ: http://localhost:5000

### 3. Khởi động Client

```bash
cd client
python main.py
```

### 4. Nạp code cho ESP32 (tùy chọn)

Nếu có ESP32, hãy nạp code từ thư mục `done/done.ino` sử dụng Arduino IDE.

## 📋 Hướng Dẫn Sử Dụng

1. **🧠 Nhận diện cảm xúc**:
   - Đứng trước camera để hệ thống nhận diện khuôn mặt và phân tích cảm xúc
   - Hệ thống sẽ thông báo cảm xúc đã phát hiện và đưa ra các đề xuất


2. **🎤 Điều khiển bằng giọng nói**:
   - Nói các câu lệnh như: "bật đèn", "tắt đèn", "phát nhạc", "dừng nhạc", v.v.
   - Hoặc tương tác với đề xuất: "đọc đề xuất", "chọn đề xuất một"


3. **📱 Xem trạng thái hệ thống**:
   - Truy cập vào giao diện web của server tại http://localhost:5000
   - Hoặc sử dụng lệnh giọng nói "trạng thái"
   

## 🗣️ Các Lệnh Giọng Nói

- **💡 Điều khiển đèn**: "bật đèn", "tắt đèn", "mở đèn", "đóng đèn"
- **🎵 Điều khiển nhạc**: "bật nhạc", "tắt nhạc", "phát nhạc", "dừng nhạc"
- **😊 Nhạc theo cảm xúc**: "nhạc vui", "nhạc buồn", "nhạc bình thường", "nhạc tức giận"
- **🔊 Điều chỉnh âm lượng**: "tăng âm lượng", "giảm âm lượng", "to hơn", "nhỏ hơn"
- **🌤️ Thông tin khác**: "thời tiết", "nhiệt độ", "trạng thái"
- **💬 Tương tác đề xuất**: "đọc đề xuất", "chọn đề xuất một", "chọn đề xuất hai"

## 😊 Cảm Xúc Được Hỗ Trợ

- 😊 Vui vẻ (Happy)
- 😢 Buồn (Sad)
- 😡 Tức giận (Angry)
- 😮 Ngạc nhiên (Surprise)
- 😨 Sợ hãi (Fear)
- 🤢 Kinh tởm (Disgust)
- 😐 Bình thường (Neutral)

## ⚙️ Tùy Chỉnh

### Thay đổi cấu hình

Chỉnh sửa file `client/config.py` để thay đổi:
- Địa chỉ server IoT
- Cấu hình camera
- Âm thanh và nhãn cảm xúc
## POSTER

  <img src="Poster_N11_finalfinal-1.png" alt="DaiNam University Logo"/>

## ⚠️ Giải Quyết Sự Cố

1. **🧠 Không nhận diện được khuôn mặt**:
   - Đảm bảo khuôn mặt đủ sáng
   - Điều chỉnh CAMERA_WIDTH và CAMERA_HEIGHT trong config.py

2. **🎤 Không nhận diện được giọng nói**:
   - Kiểm tra kết nối microphone
   - Điều chỉnh tham số trong hàm listen() của VoiceService

3. **📡 Không kết nối được với server**:
   - Kiểm tra địa chỉ IP trong config.py
   - Đảm bảo server đang chạy

## 🚀 Phát Triển Thêm

Một số ý tưởng để phát triển mở rộng:

1. 🎤 Thêm nhận diện cảm xúc qua giọng nói
2. 🏠 Tích hợp với các nền tảng IoT phổ biến (HomeAssistant, Google Home, etc.)
3. 🖥️ Thêm giao diện web cho client
4. 🧠 Cải thiện thuật toán nhận diện cảm xúc
5. 🌡️ Thêm hỗ trợ cho các cảm biến thực (thay vì dữ liệu giả lập)
