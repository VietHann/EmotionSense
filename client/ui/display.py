import cv2
from utils.image_utils import put_text_pil, draw_emotion_box

class DisplayManager:

    def __init__(self, window_name="Nhận dạng cảm xúc", width=1280, height=720):
        self.window_name = window_name
        self.width = width
        self.height = height
        self._setup_window()
        
    def _setup_window(self):

        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.window_name, self.width, self.height)
        
    def update_frame(self, frame, system_state):

        if system_state.get('face_detected') and system_state.get('emotion'):
            emotion = system_state['emotion']
            confidence = system_state['confidence']
            x, y, w, h = system_state.get('face_coords', (0, 0, 0, 0))
            
            frame = draw_emotion_box(
                frame, 
                emotion, 
                confidence, 
                x, y, w, h, 
                system_state['emotion_labels'], 
                system_state['emotion_colors']
            )
        
        listening_status = "ĐANG LẮNG NGHE" if system_state.get('listening', False) else "KHÔNG LẮNG NGHE"
        frame = put_text_pil(frame, listening_status, (10, 30), font_size=20, 
                            color=(0, 255, 0) if system_state.get('listening', False) else (0, 0, 255))
        
        if system_state.get('voice_command'):
            frame = put_text_pil(frame, f"Lệnh: {system_state['voice_command']}", (10, 60), font_size=18, color=(255, 255, 0))
            
        if system_state.get('command_result'):
            frame = put_text_pil(frame, f"Kết quả: {system_state['command_result']}", (10, 90), font_size=18, color=(0, 255, 255))
        
        if system_state.get('suggestions'):
            y_pos = 120
            frame = put_text_pil(frame, "ĐỀ XUẤT:", (10, y_pos), font_size=18, color=(255, 165, 0))
            for i, suggestion in enumerate(system_state['suggestions'], 1):
                y_pos += 30
                msg = suggestion.get('message', '')
                if len(msg) > 40:
                    msg = msg[:37] + "..."
                frame = put_text_pil(frame, f"{i}. {msg}", (10, y_pos), font_size=16, color=(255, 165, 0))
        
        cv2.imshow(self.window_name, frame)
        return cv2.waitKey(1) & 0xFF
        
    def close(self):

        cv2.destroyAllWindows()