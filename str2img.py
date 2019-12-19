#!/usr/bin/python

import sys, argparse
from PIL import Image, ImageDraw, ImageFont
import textwrap


ap = argparse.ArgumentParser(description='Converts text to a png image')

ap.add_argument("-o", "--output", required=False,
   default='text.png', type = str, help="output file (default text.png)")
   
ap.add_argument('-s',"--fontsize", type = int, required=False, default= 10,
   help="fontsize (default 10)")
   
ap.add_argument('-f','--font', type = str, required=False, default= 'arial.ttf',
   help="font (default 'arial.ttf') ")
   
ap.add_argument('-c','--text_color', type = int, nargs=3, required=False, default=(0,0,0),
	help="text color (default (0,0,0) : black))")
	
ap.add_argument('-b','--bg_color', type = int, nargs=3, required=False, default=(255,255,255),
	help="background color (default (255,255,255) : white))")
	
ap.add_argument('-t', '--text', type = str, required = True, help='text')

ap.add_argument('-w', '--wrap', type = int, required = False,default =70,
 help='text wrapping limit (default = 70 chars)')

args = vars(ap.parse_args())


def main(args):
	text = ' '+args['text']+' ' #Small padding on the sizes
	fontsize =  args['fontsize'] # starting font size
	font = ImageFont.truetype(args['font'], fontsize)
	text_color = tuple(args['text_color'])
	bg_color = tuple(args['bg_color'])
	of = args['output']
	lines = textwrap.wrap(text, width=args['wrap'])
	
	max_width = 0
	num_lines = 0
	for line in lines:
		num_lines+=1
		line_width, line_height = font.getsize(line)
		if line_width > max_width:
			max_width = line_width
	image = Image.new('RGB', (max_width+(fontsize*2), line_height*num_lines+ fontsize//3), color = bg_color)
	draw = ImageDraw.Draw(image)
	image_width, image_height = image.size
	y_text = 0
	for line in lines:
		line_width, line_height = font.getsize(line)
		draw.text(((image_width - line_width) / 2, y_text), line, font=font, fill=text_color)
		y_text += line_height
	image.save(of)

if __name__=='__main__':
	main(args)
	print('Done!')
