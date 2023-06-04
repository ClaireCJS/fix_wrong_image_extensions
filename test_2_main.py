import os
import fnmatch
import unittest
import fix_wrong_image_extensions
from colorama import Fore, Back, Style, init
init()

#plyint: disable=C0103,C0114,C0115
class TestClaireFiles(unittest.TestCase):
    @staticmethod
    def create_test_file(filename):
        with open(filename, 'w') as f: f.write('Test file')

    @staticmethod
    def sub_test_announce(subtest):
        #print(f"\t{Fore.LIGHTBLACK_EX}* Test #{subtest}:")
        print(Fore.YELLOW)

    @staticmethod
    def delete_test_files():
        for filename in os.listdir('.'):
            if fnmatch.fnmatch(filename, '*.tst'):
                os.remove(filename)
                assert not os.path.exists(filename), f"{filename} not deleted"



    def setUp(self):
        self.delete_test_files()
        formatting_blanks = "                                                                                              "
        msg = f"BEGIN: {self._testMethodName}"
        centered_msg = msg.center(len(formatting_blanks))
        print(f"\n\n\n\n\n{Back.LIGHTGREEN_EX}{Fore.BLACK}{centered_msg}{Back.BLACK}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}{Back.BLACK}* Starting test:{Back.BLACK} {Style.BRIGHT}{Fore.GREEN}{self._testMethodName}{Back.BLACK}{Style.NORMAL}{Fore.YELLOW}")

    def run(self, result=None):                                                                                             #override the default run function to collect our result
        super().run(result)

    def tearDown(self):
        self.delete_test_files()
        formatting_blanks = "                                                                                              "
        msg = f"DONE:  {self._testMethodName}"
        centered_msg = msg.center(len(formatting_blanks))
        print(f"{Back.LIGHTBLACK_EX}{Fore.BLACK}{centered_msg}{Back.BLACK}{Fore.WHITE}")






    def test_remove_duplicate_extension_1(self):
        input           = "something.extension.extension"
        output_expected = "something.extension"
        output_received = fix_wrong_image_extensions.remove_duplicate_extension(input)
        self.assertNotEqual(output_expected,input)                                          #it should not be unchanged
        self.assertEqual   (output_expected,output_received)                                #and should be changed to what we expect

    def test_remove_duplicate_extension_2(self):
        input           = "blah.jpg.jpg"
        output_expected = "blah.jpg"
        output_received = fix_wrong_image_extensions.remove_duplicate_extension(input)
        self.assertNotEqual(output_expected,input)                                          #it should not be unchanged
        self.assertEqual   (output_expected,output_received)                                #and should be changed to what we expect



    def test_remove_duplicate_extension_repeated_many_times(self):
        input           = "blah.jpg.jpg.jpg.jpg.jpg.jpg.jpg.jpg.jpg.jpg.jpg.jpg.jpg"
        output_expected = "blah.jpg"
        output_received = fix_wrong_image_extensions.remove_duplicate_extension(input)
        self.assertNotEqual(output_expected,input)                                          #it should not be unchanged
        self.assertEqual   (output_expected,output_received)                                #and should be changed to what we expect








    def test_fix_wrong_image_extension_generic_use_case_2(self):
        self.sub_test_announce(2)
        testing_images_true_extension = "png"
        testing_filename   = "a.jpg"
        expected_filename  = "a.png"
        bad_rename_1       = "a.jpg"
        bad_rename_2       = "a.gif"
        _, new_filename    = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual   (new_filename,expected_filename)
        self.assertNotEqual(new_filename,     bad_rename_1)
        self.assertNotEqual(new_filename,     bad_rename_2)







    def test_remove_duplicate_extension_but_not_duplications_in_base_filename_1(self):
        input              = "blah.blah.jpg"
        output_expected    = "blah.blah.jpg"
        output_received    = fix_wrong_image_extensions.remove_duplicate_extension(input)
        self.assertEqual(output_expected,input)                                            #it should not be changed
        self.assertEqual(output_expected,output_received)                                  #and it should match what we expect

    def test_remove_duplicate_extension_but_not_duplications_in_base_filename_2(self):
        input              = "foo.foo.jpg.jpg.jpg.jpg.jpg"
        output_expected    = "foo.foo.jpg"
        output_received    = fix_wrong_image_extensions.remove_duplicate_extension(input)
        self.assertNotEqual(output_expected,input)                                          #it should not be unchanged
        self.assertEqual   (output_expected,output_received)                                #and should be changed to what we expect






    def test_fix_wrong_image_extension_double_extension_weirdness(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "jpg"
        testing_filename              = "1831450523.jpg.crdownload"
        output_expected               = "1831450523.crdownload.jpg"
        _, output_received            = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.CYAN}* received output = {output_received}",flush=True)
        self.assertEqual(output_received, output_expected)



    def test_fix_wrong_image_extension_generic_use_case_1(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "gif"
        testing_filename              = "a.jpg"
        expected_filename             = "a.gif"
        bad_rename_1                  = "a.jpg"
        _, new_filename               = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual   (new_filename,expected_filename)
        self.assertNotEqual(new_filename,     bad_rename_1)



    def test_z_fix_wrong_image_extension_generic_use_case_annoying_case(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "jpg"
        testing_filename              = "1831450523.jpg.crdownload.jpg"
        expected_filename             = "1831450523.crdownload.jpg"
        _, new_filename               = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual(new_filename,expected_filename)


    def test_z_do_nothing(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "jpg"
        testing_filename              = "a.jpg"
        expected_filename             = testing_filename
        _, new_filename               = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual(new_filename,expected_filename)





    def test_zz_realword_annouance(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "png"
        testing_filename              = "2021-06-02 19.23.23.png"
        expected_filename             = "2021-06-02 19.23.23.png"
        _, new_filename               = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual(new_filename,expected_filename)







    def test_no_extension_1(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "gif"
        testing_filename              = "a"
        expected_filename             = "a.gif"
        _, new_filename               = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual(new_filename,expected_filename)



    def only_extension_1(self):
        self.sub_test_announce(1)
        testing_images_true_extension = "gif"
        testing_filename              = "jpg"
        expected_filename             = "jpg.gif"
        _, new_filename               = fix_wrong_image_extensions.detect_wrong_image_extension(".",0,testing=True, testing_filename=testing_filename, testing_images_true_extension=testing_images_true_extension)
        print(f"{Fore.BLUE}filename: testing={testing_filename}, expected_filename={expected_filename}, new_filename={new_filename}{Fore.YELLOW}")
        self.assertEqual(new_filename,expected_filename)









if __name__ == '__main__':
    unittest.main()
