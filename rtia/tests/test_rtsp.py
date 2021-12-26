import pytest

from app.core.rtsp import RTSP


def test_rtsp_url_generator_when_has_all_correct_parameters():
    rtsp_url = RTSP().get_rtsp_url(cam_ip="123.456.789.000", cam_port=1234,
                                   cam_user="test", cam_pass="test",
                                   cam_channel=1)

    assert rtsp_url == "rtsp://123.456.789.000:1234" \
                       "/user=test&password=test" \
                       "&channel=1&stream=0.sdp?"


def test_rtsp_url_generator_when_a_parameter_is_null():
    with pytest.raises(ValueError) as raiseError:
        RTSP().get_rtsp_url(cam_ip=None, cam_port=1234,
                            cam_user="test", cam_pass="test",
                            cam_channel=1)

    assert "The parameter was necessary to generate rtsp url" == str(raiseError.value)


def test_rtsp_url_generator_when_a_parameter_is_blank():
    with pytest.raises(ValueError) as raiseError:
        RTSP().get_rtsp_url(cam_ip="123", cam_port=1234,
                            cam_user="test", cam_pass="",
                            cam_channel=1)

    assert "The parameter was necessary to generate rtsp url" == str(raiseError.value)