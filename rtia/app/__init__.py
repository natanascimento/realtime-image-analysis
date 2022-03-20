from app.domain import CreateCameraAnalysis

__version__ = '1.0.0'

def main():
    print(f"[INFO] Object Detection v{__version__}, Loading...")
    CreateCameraAnalysis().execute()
    