from PIL import Image

image = Image.open("lenna.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()
red.save("red_lenna.jpg")
green.save("green_lenna.jpg")
blue.save("blue_lenna.jpg")
print(f"Ширина - {rgb_image.width}\nВысота - {rgb_image.height}\nЦветовая модель - {rgb_image.mode}")