"""
Here's a breakdown of the script:

1. The script imports the necessary libraries: `os` for file operations, `imghdr` for image type detection, and `colorama` for color console output.
2. The `detect_wrong_image_extension` function takes a directory path as an argument.
3. It retrieves all files in the directory using `os.listdir`.
4. For each file, it checks if it is a file (not a directory) using `os.path.isfile`.
5. If the file is identified as an image using `imghdr.what`, it checks if the detected image type matches the file extension.
6. If the extension and the detected image type don't match, it generates the correct filename by replacing the extension with the correct one.
7. It renames the file using `os.rename` to the correct filename.
8. It prints a warning message using `colorama` to highlight the message in yellow.

Note: This script assumes that the images have valid content and that only the file extension is incorrect.
It uses `imghdr.what` to detect the image type based on the file's contents. H
owever, this method is not foolproof and may not correctly identify all image types.
Therefore, it's always a good idea to manually verify the detected image types before renaming the files.

"""
import os
import sys
import imghdr
from colorama import Fore, Style, init
import clairecjs_utils as claire
init()



known_image_extensions = ["jpg", "jpg_large", "jpeg", "jfif",
                          "png", "png_large",
                          "gif", "webp", "bmp",
                          "tif", "tiff",
                          "ico", "pcx", "art", "dcm" ]


def remove_duplicate_extension(filename, image_type=None, testing=False):
    global known_image_extensions

    name_parts = filename.split('.')
    if len(name_parts) < 2:
        # Filename has no extension
        if image_type:
            name_parts.append(image_type.lower())
        return '.'.join(name_parts)

    main_part = name_parts[0]
    extensions = name_parts[1:]

    # Remove any duplicate extensions at the end
    while len(extensions) >= 2 and extensions[-1] == extensions[-2]:
        #print(f"\nExtensions are {extensions}\nExtensions[-1] is {extensions[-1]}\nExtensions[-2] is {extensions[-2]}")
        extensions.pop()

    seen = []                                                                                       # Remove the duplicate and incorrect extensions
    for ext in extensions:
        if ext.lower() in seen and ext.lower() in known_image_extensions: continue                  # Check if image type is specified and remove any non-matching known image extensions
        if image_type and ext.lower() in known_image_extensions:
            if ext.lower() == image_type.lower() and image_type.lower() not in seen:
                seen.append(ext.lower())
            continue
        #een.append(ext.lower())
        seen.append(ext)    #try preserving case of it's not a real extension

    # If image type is specified, ensure it is the last extension if present
    if image_type:
        if image_type.lower() not in seen:
            seen.append(image_type.lower())
        else:
            seen.remove(image_type.lower())
            seen.append(image_type.lower())

    return '.'.join([main_part] + seen)









def detect_wrong_image_extension(directory=".", num_image_files_renamed=0, testing=False, testing_filename="test.jpg.jpg", testing_images_true_extension="jpg"):
    ANNOUNCE_OUR_RENAMES = True
    ANNOUNCE_EACH_FILE   = False
    VIDEO_FILE_SUPPORT   = False
    global known_image_extensions

    #print(f"* detect_wrong_image_extension({directory})")
    if os.path.isfile(directory):
        files     = [os.path.basename(directory)]
        directory = os.path.dirname(directory)
    elif os.path.isdir(directory):
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    else:
        msg = f'{Fore.RED}{Style.BRIGHT}Invalid path: {Style.NORMAL}"{directory}"'
        raise ValueError(msg)
        #can't return num_image_files_renamed after raising an error

    if testing: files=[testing_filename]

    #ANNOUNCE_EACH_FILE = True #rem goat

    correct_filename = ""
    last_corrected_filename = ""
    file_count = 0
    for file in files:
        file_count +=1
        if ANNOUNCE_EACH_FILE:
            print(f'{Fore.GREEN}\t- Processing file "{file}"',flush=True,end="")
            if testing: print(f'{Fore.YELLOW}...testmode, testing_images_true_extension={Fore.RED}{testing_images_true_extension}{Fore.WHITE}',flush=True,end="")
            print()
        else:
            if file_count % 5 == 1:
                print('.',end="",flush=True)
                claire.tick(mode="fg")                                              # cycle the color of the dots for visual flaire

        file_path = os.path.join(directory, file)
        if not testing: image_type = imghdr.what(file_path)                         # get image type, or use the type we sent for unit testing
        else:           image_type = testing_images_true_extension


        #OLD: extension = os.path.splitext(file)[1][1:]
        index = file.rfind(".")                                                     # Extract file extension only from the LAST dot. os.splitext is buggy if you ask me. i disagree with their approach
        base_name       = file[:index]
        additional_part = file[index:]
        extension       = additional_part[1:]                                       # will be ".crdownload" for a file ending in ".jpg.crdownload"
        correct_filename = base_name + additional_part

        # skip for files that end in ~ or .bak
        skip_file = False
        if file.endswith("~") or file.endswith(".bak"): skip_file = True

        # correct name based on inspection, but skip for certain files
        if image_type is not None and skip_file is False: correct_filename = correct_filename + '.' + image_type
        if testing: print(f"\t{Fore.CYAN}- base_name={base_name}, additional_part={additional_part}, extension={extension}, image_type={image_type}, current 'correct'_filename={correct_filename}")

        if image_type is not None:
            if image_type.lower() == "jpeg": image_type = "jpg"                                                                         #fix pesky .jpegs to .jpg
            if VIDEO_FILE_SUPPORT:
                if image_type.lower() == "mpeg": image_type = "mpg"                                                                     #fix pesky .mpegs to .mpg

        #if extension.lower() != image_type:
        if testing: print(f"\t- correct_filename  is now[0] = {correct_filename}")                                                      #has .jpg.jpg in some situations

        correct_filename = remove_duplicate_extension(correct_filename, image_type)
        correct_filenames_extracted_extension = os.path.splitext(correct_filename)[1][1:]
        if testing: print(f"\t- correct_filenames_extracted_extension is now[C] = {correct_filenames_extracted_extension}")
        correct_file_path = os.path.join(directory, correct_filename)                                                                   #if testing: print(f"\t- correct_file_path is now[C] = {correct_file_path}")

        if not skip_file:
            if file_path.lower() != correct_file_path.lower():                                                                              #added lower() to stoprenaming when case difference is the only difference
                last_corrected_filename = correct_filename
                if not testing: claire.rename(file_path, correct_file_path)
                else:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}claire.rename({file_path}, {correct_file_path}){Fore.WHITE}{Style.NORMAL}")
                    return(1,correct_filename)
                num_image_files_renamed += 1
                warning_msg = f"\n{Style.BRIGHT}- Incorrect/wrong extension #{num_image_files_renamed} detected: {Style.NORMAL}{file} {Style.BRIGHT}-->{Style.NORMAL} {correct_filename}"
                if ANNOUNCE_OUR_RENAMES: print(f"{Fore.YELLOW}{warning_msg}{Fore.WHITE}",flush=True)
            else:
                last_corrected_filename = correct_filename                                                                                 #same thing as correct_filename in this situation

    claire.tock()                                                                                                                      #reset text color after cycling

    return num_image_files_renamed, last_corrected_filename


def get_usage_msg():
    return f"""

      fix_wrong_image_extensions.py - incorrect image extension corrector

    * Add /c to correct image extensions in the current folder
    * Add /s to correct image extensions in this and all subfolders!s

    Image extensions known to this program: {known_image_extensions}
"""


def usage():
    print(get_usage_msg())
    sys.exit(666)





def main():
    if len(sys.argv) < 2: usage()
    if sys.argv[1].lower() in ["?","-?","help","-help","--help","-h","/h","--h","/?"]:
        usage()

    num_image_files_renamed = 0

    if   sys.argv[1].lower() == "/c":
        num_image_files_renamed, _     = detect_wrong_image_extension('.'    , num_image_files_renamed)
    elif sys.argv[1].lower() == "/s":
        for dirpath, _, filenames in os.walk('.'):                                                                                                  #pylint: disable=W0612
            print(f'\n{Fore.CYAN}{Style.BRIGHT}* Processing folder "{dirpath}"{Style.NORMAL}')
            num_image_files_renamed, _ = detect_wrong_image_extension(dirpath, num_image_files_renamed)
    else:
        usage()

    print(f"\n{Fore.GREEN}* Found: {Fore.YELLOW}{Style.BRIGHT}{num_image_files_renamed}{Style.NORMAL}{Fore.GREEN} invalid image extensions{Fore.WHITE}")

if __name__ == "__main__":
    main()
