# str2img
This is a python script that makes an image with text from the text you provide it. See text.png for a sample output.

---------

## Usage
 - Download [`str2img`](https://github.com/blawar/nut/archive/master.zip)
 - Install Python 3.6+ to your PATH (make sure `python` opens up a Python 3 shell)
 - Install the required modules via `pip`:
 	 - `pip3 install -r requirements.txt`
 - Run `python3 str2png.py --help` to understand options

---------

## Examples
Example usage:
```
$ python3 str2img.py -t 'Hello World' -c 255 0 0 -b 0 0 0 -s 20 -o helloworld.png
```

Example output:

![alt text](https://raw.githubusercontent.com/liamkesatoran/str2img/master/text.png)
