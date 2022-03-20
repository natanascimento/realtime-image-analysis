from app.domain import CreateCameraAnalysis

__version__ = '0.1.0'

def main():
    print("[INFO] Object Detection v1.0, Loading...")
    CreateCameraAnalysis().execute()
    