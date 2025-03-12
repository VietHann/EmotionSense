import requests
from utils.audio_utils import play_sound

class IoTService:
    def __init__(self, server_url, command_success_sound):
        self.server_url = server_url
        self.command_success_sound = command_success_sound
        self.command_keywords = {
            "bật đèn": self.turn_on_light,
            "mở đèn": self.turn_on_light,
            "cho đèn sáng": self.turn_on_light,
            "tắt đèn": self.turn_off_light,
            "đóng đèn": self.turn_off_light,
            "bật nhạc": self.play_music,
            "mở nhạc": self.play_music,
            "phát nhạc": self.play_music,
            "cho nghe nhạc": self.play_music,
            "tắt nhạc": self.stop_music,
            "dừng nhạc": self.stop_music,
            "tạm dừng nhạc": self.stop_music,
            "thời tiết": self.weather_report,
            "dự báo thời tiết": self.weather_report,
            "nhiệt độ": self.room_temperature,
            "nóng quá": self.room_temperature,
            "lạnh quá": self.room_temperature,
            "tăng âm lượng": lambda: self.adjust_volume(10),
            "to hơn": lambda: self.adjust_volume(10),
            "giảm âm lượng": lambda: self.adjust_volume(-10),
            "nhỏ hơn": lambda: self.adjust_volume(-10),
            "nhạc vui": lambda: self.play_music_by_emotion("happy"),
            "nhạc buồn": lambda: self.play_music_by_emotion("sad"),
            "nhạc bình thường": lambda: self.play_music_by_emotion("neutral"),
            "nhạc tức giận": lambda: self.play_music_by_emotion("angry"),
            "nhạc ngạc nhiên": lambda: self.play_music_by_emotion("surprise"),
            "trạng thái": self.get_system_status,
        }
        
    def play_command_success_sound(self):

        return play_sound(self.command_success_sound)
        
    def process_command(self, command_text, tts_service):

        if not command_text:
            return None
            
        command_text = command_text.lower()
        result = None
        command_found = False
        
        for keyword, handler in self.command_keywords.items():
            if keyword in command_text:
                print(f"Đã nhận diện từ khóa: '{keyword}' trong '{command_text}'")
                result = handler()
                command_found = True
                break
        
        if not command_found:
            print(f"Không nhận diện được lệnh trong: '{command_text}'")
            result = "Không nhận diện được lệnh"
            
        if result and tts_service and command_found:
            tts_service.speak(result)
            
        return result

    def turn_on_light(self):

        print("Đang gửi lệnh BẬT ĐÈN đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/light/on")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return data.get("message", "Đã bật đèn")
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi bật đèn: {str(e)}"

    def turn_off_light(self):

        print("Đang gửi lệnh TẮT ĐÈN đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/light/off")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return data.get("message", "Đã tắt đèn")
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi tắt đèn: {str(e)}"

    def play_music(self):

        print("Đang gửi lệnh MỞ NHẠC đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/music/play")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return data.get("message", "Đang phát nhạc")
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi phát nhạc: {str(e)}"

    def play_music_by_emotion(self, emotion):

        print(f"Đang gửi lệnh MỞ NHẠC {emotion} đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/music/play?playlist={emotion}")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return data.get("message", f"Đang phát nhạc {emotion}")
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi phát nhạc {emotion}: {str(e)}"

    def stop_music(self):

        print("Đang gửi lệnh DỪNG NHẠC đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/music/stop")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return data.get("message", "Đã dừng nhạc")
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi dừng nhạc: {str(e)}"

    def adjust_volume(self, change):

        print(f"Đang điều chỉnh âm lượng ({change:+}%) đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/music/volume")
            data = response.json()
            current_volume = data.get("volume", 50)
            
            new_volume = max(0, min(100, current_volume + change))
            
            response = requests.post(
                f"{self.server_url}/music/volume",
                json={"volume": new_volume},
                headers={"Content-Type": "application/json"}
            )
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return data.get("message", f"Đã điều chỉnh âm lượng thành {new_volume}%")
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi điều chỉnh âm lượng: {str(e)}"

    def weather_report(self):

        print("Đang gửi lệnh THÔNG BÁO THỜI TIẾT đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/weather/report")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            weather_info = data.get("weather", {})
            return f"Thời tiết: {weather_info.get('condition', '')}, Nhiệt độ: {weather_info.get('temperature', '')}°C, Dự báo: {weather_info.get('forecast', '')}"
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi lấy thông tin thời tiết: {str(e)}"

    def room_temperature(self):

        print("Đang gửi lệnh LẤY NHIỆT ĐỘ PHÒNG đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/temperature")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            return f"Nhiệt độ phòng: {data.get('temperature', '')}°C, Độ ẩm: {data.get('humidity', '')}%"
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi lấy nhiệt độ: {str(e)}"

    def get_system_status(self):

        print("Đang gửi lệnh LẤY TRẠNG THÁI HỆ THỐNG đến thiết bị IoT")
        try:
            response = requests.get(f"{self.server_url}/system/status")
            data = response.json()
            print(f"Phản hồi từ server: {data}")
            self.play_command_success_sound()
            
            system_state = data.get("system_state", {})
            light = "Đang BẬT" if system_state.get("light", False) else "Đang TẮT"
            music = system_state.get("music", {})
            music_status = "Đang phát" if music.get("playing", False) else "Đã dừng"
            playlist = music.get("current_playlist", "Không có")
            volume = music.get("volume", 0)
            
            return f"Đèn: {light}, Nhạc: {music_status}, Playlist: {playlist}, Âm lượng: {volume}%"
        except Exception as e:
            print(f"Lỗi khi gửi lệnh: {str(e)}")
            return f"Lỗi khi lấy trạng thái hệ thống: {str(e)}"