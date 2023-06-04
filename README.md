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

Just install the appropriate packages, and the script should be ready to go.

```bash
pip install -r requirements.txt
```

 ## Testing

Two unit test files

## Usage: Monitor mode / Service mode

To monitor a folder (c:\calendar by default) for new ics files saved into that folder, simply run the program with no options, or double-click the EXE (if you have one):

```python
python ingest_ics.py
```

Note that this will create the monitor folder if it doesn't exist, but it will also mention this on the screen so you will know.


## Usage: File mode

To process a single ics file:

```python
python ingest_ics.py <some_filename.ics>
```

This will process a single ics file.  This is useful for testing, batch scripting, or if you have a user saving these .ics files on a network share so that they can be processed later on a different machine.

## Why not just use a browser plugin?

Some websites let you export events to your calendar.

But some force a download of ics files, rather than providing a link to one. 

Browser plugins for ics files are usually designed to process links (at least, the ones I looked at).

What is needed is an endpoint on our PC that processes these files. 

This is that endpoint solution.

## Contributing: Compiling

I absolutely would love to have other people -- as long as you don't live in the GMT timezone -- to compile versions for architectures other than my own (Windows 10). Just make sure to check that your event times are properly translating, first.  The GMT-offset bug in compiled EXEs requires modification in the spec file to work.  Mine can be seen [here](https://github.com/ClioCJS/ingest_ics/blob/main/ingest_ics.spec)

## Contributing: Modification

Feel free to make your own version with neato changes, if you are so inspired.

## Those wacky BAT files?

I use TCC -- Take Command Command Line.
Technically, my .BAT files are .BTM files.
If you want to get the ones I have working, contact me, I can help.

## License

[The Unlicense](https://choosealicense.com/licenses/unlicense/)

