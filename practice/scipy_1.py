from scipy.misc import imresize, imsave, imread

# Read an image into numpy array
img = imread('img/cat.jpg')
print( img.dtype, img.shape)

# Tint
# by value [ 1, 0.95, 0.9] of RGB
img_tinted = img * [ 1, 0.95, 0.9]

# Resize the tinted image to be 300 x 300 pixels
img_tinted = imresize( img_tinted, (300,300))

# Write the tinted image to disk
imsave('img/cat_tinted.jpg', img_tinted)

