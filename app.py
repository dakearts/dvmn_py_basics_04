from PIL import Image

image = Image.open("lenna.jpg")
rgb_image = image.convert("RGB")
red_channel, green_channel, blue_channel = rgb_image.split()

offset = 50

right_shift_coordinates = (0, 0, image.width-offset, image.height)
left_shift_coordinates = (offset, 0, image.width, image.height)
middle_shift_coordinates = (offset/2, 0, image.width-offset/2, image.height)

middle_red = red_channel.crop(right_shift_coordinates)
middle_green = green_channel.crop(left_shift_coordinates)
middle_blue = blue_channel.crop(middle_shift_coordinates)

cropped_red = red_channel.crop(left_shift_coordinates)
cropped_blue = blue_channel.crop(right_shift_coordinates)

blended_red = Image.blend(cropped_red, middle_red, 0.5)
blended_blue = Image.blend(cropped_blue, middle_blue, 0.5)

blended_image = Image.merge("RGB", (blended_red, middle_green, blended_blue))
blended_image.thumbnail((80, 80))
blended_image.save("blended_image.jpg")
