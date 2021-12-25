from app.core.rtsp import RTSP


def test_rtsp_url_generator_when_has_all_variables():
    rtsp_url = RTSP().get_rtsp_url()
    
    assert rtsp_url == "rtsp://123.456.789.000:1234/user=test&password=test&channel=1&stream=0.sdp?"