class RTSP:

    @staticmethod
    def get_rtsp_url(cam_ip: str, cam_port: int,
                     cam_user: str, cam_pass: str,
                     cam_channel: int) -> str:

        if None in (cam_ip, cam_port, cam_user, cam_pass, cam_channel) \
                or "" in (cam_ip, cam_port, cam_user, cam_pass, cam_channel):
            raise ValueError("The parameter was necessary to generate rtsp url")

        return f"rtsp://{cam_ip}:{cam_port}/" \
               f"user={cam_user}&password={cam_pass}&" \
               f"channel={cam_channel}&stream=0.sdp?"
