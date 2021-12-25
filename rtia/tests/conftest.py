import os


def pytest_configure(config):
  os.environ['CAM_IP'] = '123.456.789.000'
  os.environ['CAM_PORT'] = '1234'
  os.environ['CAM_USER'] = 'test'
  os.environ['CAM_PASS'] = 'test'
  os.environ['CAM_CHANNEL'] = '1'
  return config