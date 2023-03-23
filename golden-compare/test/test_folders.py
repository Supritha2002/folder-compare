from compare_folder import compare_folder_contents
import unittest


class TestFolder(unittest.TestCase):
    # checks for length of additional files is greater or equal to zero

        
        
    def test_for_missing_files(self):  # checks for length of missing files is equal to zero
        missingfiles, _ = compare_folder_contents("folder", "standardfile.json")
        self.assertEqual(len(missingfiles), 0)
        self.assertTrue(len(additionalfiles) >= 0)

       


if __name__ == '__main__':
    unittest.main()
