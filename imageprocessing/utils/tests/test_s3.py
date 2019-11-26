import unittest
from utils import s3

class TestS3Utils(unittest.TestCase):

    def test_download_if_not_exist(self):
        pass
        s3.download_file('family-dashboard', 'test.txt', 'utils/tests/test.txt')

    def test_upload(self):
        s3.upload_file('family-dashboard', 'requirements.txt', 'file.txt')
