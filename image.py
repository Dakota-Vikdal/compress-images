from PIL import Image, ImageFilter

img = Image.open('./images/venti-views-AYPGMMtWVIY-unsplash.jpg')
img.thumbnail((100, 250))
# more_filter = filtered_img.filter(ImageFilter.SHARPEN)
# even_more = more_filter.filter(ImageFilter.SHARPEN)
newnew = img.save('mountainpeak.png', 'png')


