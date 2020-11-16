from PIL import Image, ImageDraw, ImageFont
import markovify, textwrap, random

#### SETUP ####

# Assets locations
# fontName = 'assets/Roboto.ttf'
fontName = 'assets/Merriweather-Bold.ttf'
rawText = 'raw_text/titoli.txt'

# Load the raw text
with open(rawText) as f:
    text = f.read()

# Build the mode
# text_model = markovify.Text(text)
text_model = markovify.NewlineText(text)

# set font and size
fontXS = ImageFont.truetype(fontName, size=20)
fontS = ImageFont.truetype(fontName, size=40)
font = ImageFont.truetype(fontName, size=50)
fontL = ImageFont.truetype(fontName, size=60)
fontXL = ImageFont.truetype(fontName, size=70)



#### USER PROMPT ####
imgNum = input('Input how many images you need [1]: ')
fileName = input('Enter the desidered filename [output]: ')

if imgNum == '':
    imgNum = 1
print('Ok, I\'m going to generate ' + str(imgNum) + ' images..')

#### MAGIC HAPPENS# ####

for nn in range(int(imgNum)):

    x=random.randint(1,256)
    y=random.randint(1,256)
    z=random.randint(1,256)
    image = Image.new('RGB', (1080, 1080), (x, y, z))

    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(image)

    # generate one short sentence of maximum 300 chars
    message = text_model.make_short_sentence(600)

    # wrap the text at 50 chars
    wrapper = textwrap.TextWrapper(width=30) 
    word_list = wrapper.wrap(text=message) 
    message_wrap = ''
    for ii in word_list[:-1]:
        message_wrap = message_wrap + ii + '\n'
    message_wrap += word_list[-1]

    # main message
    x = 60

    if len(message) > 300:
        y = 110
    else:
        y = 300

    (x, y) = (x, y)
    color = 'rgb(0, 0, 0)'
    draw.multiline_text((x,y), message_wrap, fill=color, font=font, anchor=None, spacing=3, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)

    # La Ropubblica
    (x, y) = (60, 850)
    color = 'rgb(255, 255, 255)'
    titolo = 'la Яopubblica'
    draw.multiline_text((x,y), titolo, fill=color, font=font, anchor=None, spacing=3, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)

    # save the edited image
    if fileName == '':
        fileName = 'output'
    image.save('output/'+fileName+str(nn+1)+'.png')
    print('-- Saved image #'+str(nn+1)+' as '+fileName+str(nn+1)+'.png --')
    
    # save the caption
    with open('output/captions.txt', 'w') as captionFile:
            captionFile.write('#' + str(nn+1) + ' ' + message)
            captionFile.write('\n')
            captionFile.close()
    print('-- Save caption #' + str(nn+1) + ' to captions.txt --')
