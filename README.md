# fix_wrong_image_extensions

fix_wrong_image_extensions is a filename fixer that fixes the extension of images saved with wrong/duplicate/no extensions

## What "wrong" filenames does it fix, specifically?

1) wrong extensions 

  * jpg saved as gif (would be renamed back to jpg)
  * gif saved as jpg (would be renamed back to gif)

    
2) missing extensions

  * a jpg file named "foo" will be renamed "foo.jpg"

3) extra extensions 

  * a gif named "hello.png.jpg.kitty.gif" would be named "hello.kitty.gif"


4) repeating extensions

  * changes ".jpg.jpg.jpg" to ".jpg"
  * changes "foo.jpg.bar.jpg" to "foo.bar.jpg"
  * leaves repeating non-image extensions untouched

5) mis-positioned extensions

  * "foo.jpg.bar" will become "foo.bar.jpg"

6) annoying minor variances

  * jpgs saved as .jpeg
  * jpgs saved as .jfif
  * jpgs saved as .jpg_large
  * jpgs saved as .jpg_name=orig



## Installation: Python

Install the appropriate packages:

```bash
pip install -r requirements.txt
```

Get clairecjs_utils
```bash
pip install clairecjs_utils
```

Or if that doesn't work grab the actual clairecjs_utils files from [here](https://github.com/ClaireCJS/clairecjs_utils)

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

