import os
from config import MUSIC_DIRECTORIES, music_playlists

def initialize_directories():
    """Tạo cấu trúc thư mục và file nhạc giả lập."""
    for directory in MUSIC_DIRECTORIES:
        os.makedirs(directory, exist_ok=True)
    
    # Tạo file MP3 giả lập để test với header MP3 hợp lệ hơn
    # Đây chỉ là một gói dữ liệu tối thiểu để pygame có thể nhận dạng là MP3
    # Lưu ý: Đây vẫn không phải là một file MP3 hoàn chỉnh nhưng sẽ ít gây lỗi hơn
    dummy_mp3 = (
        b'\xff\xfb\x50\xc4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x54\x41\x47\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )
    
    for playlist in music_playlists:
        for song_path in music_playlists[playlist]:
            if not os.path.exists(song_path):
                os.makedirs(os.path.dirname(song_path), exist_ok=True)
                with open(song_path, 'wb') as f:
                    f.write(dummy_mp3)
                print(f"Đã tạo file nhạc giả lập: {song_path}")