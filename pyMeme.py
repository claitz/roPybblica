from PIL import Image, ImageDraw, ImageFont
import markovify
import textwrap

#### SETUP ####

# Assets locations
fontName = 'assets/Roboto.ttf'
rawText = 'raw_text/testo.txt'
bgImage = 'assets/blank_error_single.png'

# Load the raw text
with open(rawText) as f:
    text = f.read()

# Build the mode
text_model = markovify.Text(text)

# set font and size
font = ImageFont.truetype(fontName, size=35)
fontM = ImageFont.truetype(fontName, size=30)
fontS = ImageFont.truetype(fontName, size=25)
fontXS = ImageFont.truetype(fontName, size=15)

#### USER PROMPT ####
imgNum = input('Input how many images you need [1]: ')
fileName = input('Enter the desidered filename [output]: ')

if imgNum == '':
    imgNum = 1
print('Ok, I\'m going to generate ' + str(imgNum) + ' images..')

#### MAGIC HAPPENS# ####

for nn in range(int(imgNum)):

    # create Image object with the input image
    image = Image.open(bgImage)
    
    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(image)

    # generate one short sentence of maximum 300 chars
    message = text_model.make_short_sentence(300)

    # wrap the text at 50 chars
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=message) 
    message_wrap = ''
    for ii in word_list[:-1]:
        message_wrap = message_wrap + ii + '\n'
    message_wrap += word_list[-1]
    
    ### SET THE TEXTS ###
    # window title
    (x, y) = (55, 15)
    title = "Alert"
    color = 'rgb(255, 255, 255)'
    # draw the title
    draw.text((x, y), title, fill=color, font=fontM)

    # main message
    (x, y) = (130, 80)
    color = 'rgb(0, 0, 0)'
    draw.multiline_text((x,y), message_wrap, fill=color, font=fontXS, anchor=None, spacing=3, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)

    # button message
    (x, y) = (190, 205)
    CTA = 'OK'
    color = 'rgb(0, 0, 0)'
    #draw.text((x, y), CTA, fill=color, align='center', font=fontS)
    draw.multiline_text((x,y), CTA, fill=color, font=fontS, anchor=None, spacing=3, align='center', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)

    # save the edited image
    if fileName == '':
        fileName = 'output'
    image.save('output/'+fileName+str(nn+1)+'.png')
    print('-- Saved image #'+str(nn+1)+' as '+fileName+str(nn+1)+'.png --')