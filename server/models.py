import pygame
from config import system_state, music_playlists
import os
import random


class MusicPlayer:
    @staticmethod
    def initialize():
        """Khởi tạo mixer."""
        try:
            pygame.mixer.init()
            print("Đã khởi tạo hệ thống âm thanh")
        except Exception as e:
            print(f"Lỗi khi khởi tạo hệ thống âm thanh: {str(e)}")
    
    @staticmethod
    def play(playlist):
        """Phát nhạc từ playlist được chỉ định."""
        if playlist not in music_playlists:
            playlist = 'neutral'
            
        try:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                
            if len(music_playlists[playlist]) > 0:
                # Chọn một bài hát ngẫu nhiên từ playlist thay vì luôn chọn bài đầu tiên
                song = random.choice(music_playlists[playlist])
                
                if os.path.exists(song):
                    try:
                        pygame.mixer.music.load(song)
                        pygame.mixer.music.set_volume(system_state["music"]["volume"] / 100)
                        pygame.mixer.music.play()
                        system_state["music"]["playing"] = True
                        system_state["music"]["current_playlist"] = playlist
                        message = f"Đang phát nhạc từ playlist {playlist}"
                    except Exception as e:
                        message = f"Lỗi khi phát file: {str(e)}"
                        print(message)
                        # Thử phát bài khác nếu có lỗi với bài hiện tại
                        if len(music_playlists[playlist]) > 1:
                            remaining_songs = [s for s in music_playlists[playlist] if s != song]
                            if remaining_songs:
                                alt_song = random.choice(remaining_songs)
                                try:
                                    pygame.mixer.music.load(alt_song)
                                    pygame.mixer.music.set_volume(system_state["music"]["volume"] / 100)
                                    pygame.mixer.music.play()
                                    system_state["music"]["playing"] = True
                                    system_state["music"]["current_playlist"] = playlist
                                    message = f"Đang phát nhạc từ playlist {playlist} (bài thay thế)"
                                except:
                                    system_state["music"]["playing"] = False
                                    message = f"Không thể phát bất kỳ bài nào từ playlist {playlist}"
                else:
                    message = f"Không tìm thấy file nhạc: {song}"
            else:
                message = f"Playlist {playlist} trống"
                
            system_state["interaction"]["last_command"] = f"Phát nhạc ({playlist})"
            system_state["interaction"]["last_response"] = message
            print(message)
            
            return {
                "status": "success", 
                "message": message,
                "playing": system_state["music"]["playing"],
                "playlist": system_state["music"]["current_playlist"]
            }
            
        except Exception as e:
            error_message = f"Lỗi khi phát nhạc: {str(e)}"
            print(error_message)
            return {"status": "error", "message": error_message}
    
    @staticmethod
    def stop():
        """Dừng phát nhạc."""
        try:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                
            system_state["music"]["playing"] = False
            message = "Đã dừng phát nhạc"
            system_state["interaction"]["last_command"] = "Dừng nhạc"
            system_state["interaction"]["last_response"] = message
            print(message)
            
            return {
                "status": "success", 
                "message": message,
                "playing": system_state["music"]["playing"]
            }
            
        except Exception as e:
            error_message = f"Lỗi khi dừng nhạc: {str(e)}"
            print(error_message)
            return {"status": "error", "message": error_message}
    
    @staticmethod
    def set_volume(volume):
        """Điều chỉnh âm lượng."""
        volume = max(0, min(100, volume))
        system_state["music"]["volume"] = volume
        
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.set_volume(volume / 100)
            
        message = f"Đã điều chỉnh âm lượng thành {volume}%"
        system_state["interaction"]["last_command"] = f"Điều chỉnh âm lượng: {volume}%"
        system_state["interaction"]["last_response"] = message
        print(message)
        
        return {"status": "success", "message": message, "volume": volume}
    
    @staticmethod
    def get_status():
        """Lấy trạng thái nhạc hiện tại."""
        status = "Đang phát" if system_state["music"]["playing"] else "Đã dừng"
        playlist = system_state["music"]["current_playlist"] if system_state["music"]["current_playlist"] else "Không có"
        message = f"Nhạc: {status}, Playlist: {playlist}, Âm lượng: {system_state['music']['volume']}%"
        
        return {
            "status": "success",
            "playing": system_state["music"]["playing"],
            "playlist": system_state["music"]["current_playlist"],
            "volume": system_state["music"]["volume"],
            "message": message
        }

class EmotionHandler:
    """Xử lý nhận diện cảm xúc và đề xuất."""
    @staticmethod
    def update_emotion(emotion, confidence=0):
        """Cập nhật cảm xúc và đưa ra đề xuất."""
        system_state["last_emotion"] = emotion
        message = f"Đã cập nhật cảm xúc: {emotion} (độ tin cậy: {confidence}%)"
        system_state["interaction"]["last_command"] = "Cập nhật cảm xúc"
        system_state["interaction"]["last_response"] = message
        print(message)
        
        suggestions = []
        
        if emotion == "happy":
            suggestions.append({
                "type": "light",
                "action": "on",
                "message": "Bạn có vẻ vui vẻ! Bạn có muốn bật đèn sáng lên không?"
            })
            suggestions.append({
                "type": "music",
                "action": "play",
                "playlist": "happy",
                "message": "Bật nhạc vui để tiếp thêm năng lượng tích cực?"
            })
        elif emotion == "sad":
            suggestions.append({
                "type": "light",
                "action": "off",
                "message": "Bạn có vẻ buồn. Bạn có muốn tắt đèn để tạo không gian yên tĩnh không?"
            })
            suggestions.append({
                "type": "music",
                "action": "play",
                "playlist": "sad",
                "message": "Phát một bản nhạc nhẹ nhàng để giúp bạn thư giãn?"
            })
        elif emotion == "angry":
            suggestions.append({
                "type": "light",
                "action": "on",
                "message": "Bạn có vẻ đang tức giận. Bật đèn sáng có thể giúp cải thiện tâm trạng!"
            })
            suggestions.append({
                "type": "music",
                "action": "play",
                "playlist": "neutral",
                "message": "Phát nhạc nhẹ nhàng để giúp bạn bình tĩnh lại?"
            })
        
        return {
            "status": "success",
            "message": message,
            "emotion": emotion,
            "confidence": confidence,
            "suggestions": suggestions
        }

class SensorData:
    """Quản lý dữ liệu cảm biến."""
    @staticmethod
    def update_simulated_data():
        """Cập nhật dữ liệu nhiệt độ, độ ẩm theo thời gian."""
        system_state["temperature"] += (random.random() - 0.5)
        system_state["temperature"] = round(system_state["temperature"], 1)
        system_state["humidity"] += (random.random() - 0.5) * 4
        system_state["humidity"] = max(0, min(100, round(system_state["humidity"])))