from pathlib import Path
import sys

# Absolute path of the current file
file_path = Path(__file__).resolve()

# Absolute path to the parent directory of the current file, which is the project root
ROOT = file_path.parent

# Add the root path to the sys.path list if it is not already there
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))



# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, RTSP, YOUTUBE]

# Configuration for sources, using the absolute ROOT path for resource directories
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'us_image1.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'us_image1_detected.jpg'
COVER_IMAGE = IMAGES_DIR / 'cover.png'

VIDEO_DIR = ROOT / 'videos'
VIDEO_1_PATH = VIDEO_DIR / 'us_video_1.mp4'
VIDEOS_DICT = {'us_video_1.mp4': VIDEO_1_PATH}

MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best_x8_det.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'best_x8_seg.pt'

WEBCAM_PATH = 0