import re

def extract_video_id(url):
    # Expresión regular para extraer el ID del video de YouTube
    match = re.search(r'(?<=v=|\/)([0-9A-Za-z_-]{11})', url)
    return match.group(0) if match else None