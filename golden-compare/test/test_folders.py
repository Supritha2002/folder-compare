from compare_folder import compare_folder_contents
import unittest


class TestFolder(unittest.TestCase):
    # checks for length of additional files is greater or equal to zero
    def test_for_additional_files(self):
        _, additionalfiles = compare_folder_contents("folder_missing_files","standardfile.json")
        self.assertTrue(len(additionalfiles) > 0)

       


if __name__ == '__main__':
    unittest.main()
