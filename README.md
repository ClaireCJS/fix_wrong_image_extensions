# fix_wrong_image_extensions

fix_wrong_image_extensions is a filename fixer that fixes the extension of images saved with wrong/duplicate/no extensions

## What does it fix, specifically?

Wrong filenames, such as:

* extensions of the wrong format

       * jpg saved as gif
       * gif saved as jpg
       * extra extensions of wrong format (a gif named "hello.png.jpg.kitty.gif" would be named "hello.kitty.gif")

* missing extensions

        * a jpg file named "foo" will be renamed "foo.jpg"

* repeating extensions

        * changes ".jpg.jpg" to ".jpg"
	* will even change "foo.jpg.bar.jpg" to "foo.bar.jpg", assuming it's a jpg
        * leaves repeating non-image extensions untouched

* mis-positioned extensions

	* "foo.jpg.bar" will become "foo.bar.jpg"

* annoying minor variances

	* jpg saved as .jpg_large
	* jpg saved as .jpg_name=orig
	* jpg saved as .jpeg
	* jpg saved as .jfif



## Installation: Python

Install the appropriate packages:

```bash
pip install -r requirements.txt
```

Get clairecjs_utils
```bash
pip install clairecjs_utils
```

Or if that doesn't work grab the actual clairecjs_utils files from 

 ## Testing

Two unit test files provided to prove it actually works




## Contributing: Modification

Feel free to make your own version with neato changes, if you are so inspired.

## Those wacky BAT files?

I use TCC -- Take Command Command Line.
Technically, my .BAT files are .BTM files.
If you want to get the ones I have working, I'd love to help.


## License

[The Unlicense](https://choosealicense.com/licenses/unlicense/)

