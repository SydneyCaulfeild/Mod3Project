from PIL import Image
im = Image.open(pathlib.path("image title"))
 # opening image , https://pillow.readthedocs.io/en/stable/reference/open_files.html#file-handling
im = Image.crop(box=L, uL, R, lL)
# crop image, coordinate system L= bottom left corner, uL = upper left, R = upper Right...

from PIL import ImageFilter
im = im.filter(ImageFilter. )
#runs image thru filter, edge enhance/ edge enhance more/ find edges

im = PIL.ImageOps.grayscale("image")
# greyscale the image
