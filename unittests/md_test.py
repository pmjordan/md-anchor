import unittest
import mdanchor

class TestProcessFile(unittest.TestCase):
    def setUp(self):
        # Create a sample input file
        self.input_file_path = 'test_input.md'
        with open(self.input_file_path, 'w') as f:
            f.write('This is a test.\n')
            f.write('# no number\n')
            f.write('# 1 Heading\n')
            f.write('## 1.1 Heading\n')
            f.write('# 10 Heading\n')
            f.write('## 10.1 Heading\n')
            f.write('## 10.2 Two Word\n')
            f.write('## 10.3 Hyphen-word Heading\n')
            f.write('### 10.4.1 Three word Heading\n')
            f.write('## Not a number\n')

        # Create an expected output file
        self.expected_output_file_path = 'expected_output.md'
        with open(self.expected_output_file_path, 'w') as f:
            f.write('This is a test.\n')
            f.write('# no number\n')
            f.write('# 1 Heading <a name=heading></a>\n')
            f.write('## 1.1 Heading <a name=heading></a>\n')
            f.write('# 10 Heading <a name=heading></a>\n')
            f.write('## 10.1 Heading <a name=heading></a>\n')
            f.write('## 10.2 Two Word <a name=two-word></a>\n')
            f.write('## 10.3 Hyphen-word Heading <a name=hyphen-word-heading></a>\n')
            f.write('### 10.4.1 Three word Heading <a name=three-word-heading></a>\n')
            f.write('## Not a number\n')

        # Path for the actual output file
        self.output_file_path = 'test_output.md'

    def test_process_file(self):
        # Run the function
        mdanchor.add_anchors_to_markdown(self.input_file_path, self.output_file_path)

        # Compare the output file to the expected output file
        with open(self.output_file_path, 'r') as outfile, open(self.expected_output_file_path, 'r') as expectedfile:
            self.assertEqual(outfile.read(), expectedfile.read())

    def tearDown(self):
        # Clean up the files
        import os
        os.remove(self.input_file_path)
        os.remove(self.output_file_path)
        os.remove(self.expected_output_file_path)

if __name__ == '__main__':
    unittest.main()
