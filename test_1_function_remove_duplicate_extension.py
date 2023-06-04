import unittest
import fix_wrong_image_extensions

class TestRemoveDuplicateExtension(unittest.TestCase):                                                                                                      #plyint: disable=C0103,C0114,C0115

    def test_remove_duplicate_extension_no_extension_present_but_has_a_valid_type(self):
        input_filename  = "a"
        image_type      = "jpg"
        expected_result = "a.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_no_extension_present_and_no_image_type(self):
        input_filename  = "file_without_extension_and_no_image_type"
        image_type      = None
        expected_result = input_filename
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_single_extension(self):
        input_filename  = "file.jpg"
        image_type      = "jpg"
        expected_result = input_filename
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_duplicate_extension(self):
        input_filename  = "file.jpg.jpg"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_multiple_extensions(self):
        input_filename  = "file.jpg.png.gif.jpg"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_multiple_extensions_2(self):
        input_filename  = "file.jpg.png.milkshake.jpg"
        image_type      = "jpg"
        expected_result = "file.milkshake.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_possibly_redundant_chatgpt_inspired_2(self):
        input_filename  = "file.png.gif.jpg"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_possibly_redundant_chatgpt_inspired_2B(self):
        input_filename  = "file.png.gif.jpg.jpg"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_possibly_redundant_chatgpt_inspired_2C(self):
        input_filename  = "file.png.gif.jpg.jpg.gif"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_possibly_redundant_chatgpt_inspired_2D(self):
        input_filename  = "file.png.gif.jpg.jpg.gif.jpg"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_interleaved_extensions(self):
        input_filename  = "file.jpg.png.jpg.gif"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_remove_duplicate_extension_image_type_not_in_extensions(self):
        input_filename  = "file.png.png.gif"
        image_type      = "jpg"
        expected_result = "file.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    #########################################################################################################################################
    ############ Finally got the above 12 working, so can finally talke this one -- which actualy worked right the first time yayyyy
    #########################################################################################################################################

    def test_annoying_outer_case_1(self):
        input_filename  = "1831450523.jpg.crdownload.jpg"
        image_type      = "jpg"
        expected_result = "1831450523.crdownload.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_annoying_outer_case_2(self):
        input_filename  = "1831450523.jpg.crdownload.jpg.jpg"
        image_type      = "jpg"
        expected_result = "1831450523.crdownload.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_annoying_realworld_case_2(self):
        input_filename  = "2021-06-02 19.23.23.png"
        image_type      = "png"
        expected_result = input_filename
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_repeating_nonimage_ext_at_end_1(self):
        input_filename  = "something.extension.extension"
        image_type      = None
        expected_result = "something.extension"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)


    def test_repeating_nonimage_ext_at_end_2(self):
        input_filename  = "something.extension.extension"
        image_type      = "jpg"
        expected_result = "something.extension.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_repeating_extension_only(self):
        input_filename  = "jpg.jpg"
        image_type      = "jpg"
        expected_result = "jpg.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_unwritten_functionality_1(self):
        input_filename  = "media_FM6TGSyXsAE4bRp.jpg_name=orig"
        image_type      = "jpg"
        expected_result = "media_FM6TGSyXsAE4bRp.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)

    def test_unwritten_functionality_2(self):
        input_filename  = "whatever.jpg_large"
        image_type      = "jpg"
        expected_result = "whatever.jpg"
        result          = fix_wrong_image_extensions.remove_duplicate_extension(input_filename, image_type, testing=True)
        self.assertEqual(result, expected_result)



    # ^^^^^^^^^^^^^^^ do this before running python-only of this onto porn-main [new already done]

if __name__ == '__main__':
    unittest.main()
