import unittest
import parabank as pb


class ParabankPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_register_account():
        pb.setUp()
        pb.register()
        pb.log_out()
        pb.log_in()
        pb.log_out()
        pb.tearDown()