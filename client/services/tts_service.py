import queue
import threading
import time
from utils.audio_utils import text_to_speech

class TTSService:
    def __init__(self):
        self.tts_queue = queue.Queue()
        self.is_speaking = False
        self.tts_thread = threading.Thread(target=self._tts_worker)
        self.tts_thread.daemon = True
        self.tts_thread.start()
        
    def _tts_worker(self):

        while True:
            text = self.tts_queue.get()
            if text is None:
                break
                

            if not text.startswith("Các đề xuất:"):
                filtered_text = text
                phrases_to_filter = [
                    "bạn có vẻ buồn", "tạo không gian", "yên tĩnh", "phát một bản nhạc",
                    "nhẹ nhàng", "giúp bạn thư giãn", "nhạc vui", "nhạc buồn"
                ]
                
                for phrase in phrases_to_filter:
                    if phrase.lower() in filtered_text.lower():
                        filtered_text = filtered_text.lower().replace(phrase.lower(), "[đề xuất]")
            else:
                filtered_text = text
            
            self.is_speaking = True
            
            if not self._should_skip(filtered_text):
                text_to_speech(filtered_text)
            
            time.sleep(0.2)
            
            self.is_speaking = False
            
            self.tts_queue.task_done()
            
    def _should_skip(self, text):

        return text.startswith("Lỗi") or "không nhận diện" in text.lower()
            
    def speak(self, text):

        self.tts_queue.put(text)
        
    def is_busy(self):

        return self.is_speaking
        
    def stop(self):

        self.tts_queue.put(None)