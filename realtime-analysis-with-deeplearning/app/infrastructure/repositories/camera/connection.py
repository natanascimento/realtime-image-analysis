class CameraConnection:

    @staticmethod
    def get_connection_url(cam_ip: str, cam_port: int,
                     cam_user: str, cam_pass: str,
                     cam_channel: int, protocol: str) -> str:

        if None in (cam_ip, cam_port, cam_user, cam_pass, cam_channel, protocol) \
                or "" in (cam_ip, cam_port, cam_user, cam_pass, cam_channel, protocol):
            raise ValueError("The parameter was necessary to generate connection url")

        return f"{protocol}://{cam_user}:{cam_pass}@{cam_ip}:{cam_port}/cam/realmonitor?channel=1&subtype=0"
