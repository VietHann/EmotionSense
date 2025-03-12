
import cv2
import pygame
import threading
import time
import os

from config import *
from utils.audio_utils import ensure_sounds_exist
from services.emotion_service import EmotionService
from services.voice_service import VoiceService
from services.tts_service import TTSService
from services.iot_service import IoTService
from ui.display import DisplayManager

class EmotionDetectionSystem:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
        
        pygame.mixer.init()
        
        ensure_sounds_exist(SOUND_DIR, EMOTION_SOUNDS, COMMAND_SUCCESS_SOUND)
        
        self.tts_service = TTSService()
        self.emotion_service = EmotionService(IOT_SERVER_URL, EMOTION_LABELS, EMOTION_COLORS)
        self.voice_service = VoiceService(FILTER_KEYWORDS)
        self.iot_service = IoTService(IOT_SERVER_URL, COMMAND_SUCCESS_SOUND)
        self.display_manager = DisplayManager()
        
        self.face_detected_before = False
        self.listening = False
        self.voice_command = None
        self.last_command_response = None
        self.last_command_time = 0
        self.emotion_timer = None
        
        self.listen_thread = threading.Thread(target=self.listen_and_process)
        self.listen_thread.daemon = True
        self.listen_thread.start()
        
    def listen_and_process(self):

        while True:
            if self.listening and not self.tts_service.is_busy():
                current_time = time.time()
                enough_time_passed = current_time - self.last_command_time > 0.3
                not_playing_sound = not pygame.mixer.music.get_busy()
                
                if self.emotion_timer:
                    emotion_cooldown = current_time - self.emotion_timer > EMOTION_COOLDOWN
                else:
                    emotion_cooldown = True
                
                if enough_time_passed and not_playing_sound and emotion_cooldown:
                    command_text = self.voice_service.listen()
                    
                    if command_text:
                        processed_command = self.voice_service.preprocess_command(command_text)
                        
                        if processed_command:
                            if "đọc đề xuất" in processed_command.lower() or "đọc đề nghị" in processed_command.lower() or "nghe đề xuất" in processed_command.lower():
                                self.voice_command = "đọc đề xuất"
                                suggestions_text = self.emotion_service.get_suggestions_text()
                                self.tts_service.speak(suggestions_text)
                                self.last_command_response = "Đang phát âm đề xuất"
                                self.last_command_time = current_time
                                continue
                            
                            is_suggestion, suggestion_index = self.voice_service.check_suggestion_command(
                                processed_command, 
                                len(self.emotion_service.suggestions)
                            )
                            
                            if is_suggestion and suggestion_index >= 0:
                                self.voice_command = f"chọn đề xuất {suggestion_index + 1}"
                                result = self.emotion_service.accept_suggestion(suggestion_index)
                                self.tts_service.speak(result)
                                self.last_command_response = result
                                self.last_command_time = current_time
                                continue
                            
                            self.voice_command = processed_command
                            result = self.iot_service.process_command(processed_command, self.tts_service)
                            self.last_command_response = result
                            self.last_command_time = current_time
                            
            time.sleep(0.1)
            
    def run(self):

        face_disappeared_frames = 0
        max_disappeared_frames = 10
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            frame = cv2.flip(frame, 1)
            faces = self.emotion_service.detect_faces(frame)
            
            current_face_detected = len(faces) > 0
            
            if current_face_detected:
                face_disappeared_frames = 0
                
                if not self.face_detected_before:
                    print("Phát hiện khuôn mặt mới!")
                    self.face_detected_before = True
                    self.emotion_service.emotion_processed = False
                    self.emotion_timer = None
                
                x, y, w, h = faces[0]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                if w > 100 and h > 100 and not self.emotion_service.emotion_processed:
                    face_frame = frame[y:y+h, x:x+w]
                    face_frame = cv2.resize(face_frame, (224, 224))
                    
                    print("Đang phát hiện cảm xúc...")
                    emotion, confidence = self.emotion_service.detect_emotion(face_frame)
                    if emotion:
                        print(f"Đã phát hiện cảm xúc: {emotion} ({confidence:.1f}%)")
                        self.emotion_service.current_emotion = emotion
                        self.emotion_service.current_confidence = confidence
                        
                        emotion_label = EMOTION_LABELS.get(emotion, emotion)
                        message, suggestions_message = self.emotion_service.update_emotion_to_server(emotion, confidence)
                        
                        combined_message = f"Phát hiện cảm xúc {emotion_label}"
                        if suggestions_message:
                            combined_message += f". {suggestions_message}"
                            
                        print(f"Đang phát âm (kết hợp): {combined_message}")
                        self.tts_service.speak(combined_message)
                        
                        self.emotion_service.emotion_processed = True
                        self.listening = True
                        
                        self.emotion_timer = time.time()
            else:
                face_disappeared_frames += 1
                
                if self.face_detected_before and face_disappeared_frames >= max_disappeared_frames:
                    print("Khuôn mặt đã biến mất.")
                    self.face_detected_before = False
                    self.emotion_service.emotion_processed = False
                    self.emotion_service.current_emotion = None
                    self.emotion_service.current_confidence = None
                    self.emotion_timer = None
                    self.listening = False
            
            system_state = {
                'face_detected': current_face_detected,
                'emotion': self.emotion_service.current_emotion,
                'confidence': self.emotion_service.current_confidence,
                'face_coords': faces[0] if current_face_detected else None,
                'listening': self.listening,
                'voice_command': self.voice_command,
                'command_result': self.last_command_response,
                'suggestions': self.emotion_service.suggestions,
                'emotion_labels': EMOTION_LABELS,
                'emotion_colors': EMOTION_COLORS
            }
            
            key = self.display_manager.update_frame(frame, system_state)
            if key == ord('q'):
                break
        
        self.cap.release()
        self.display_manager.close()
        self.tts_service.stop()

if __name__ == "__main__":
    system = EmotionDetectionSystem()
    system.run()