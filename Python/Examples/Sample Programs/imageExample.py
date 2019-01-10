from PIL import Image
flowerIm = Image.open('flower.png')
width,height = flowerIm.size
print width
print height
print flowerIm.filename
print flowerIm.format
print flowerIm.format_description

croppedIm = flowerIm.crop((335, 345, 565, 560))
croppedIm.save('croppedFlower.png')

