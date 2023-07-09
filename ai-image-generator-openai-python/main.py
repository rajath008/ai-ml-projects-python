import openai
import urllib.request
from PIL import Image
openai.api_key=open("API_KEY","r").read()

user_prompt=str(input('Enter prompt for the image : '))
number_of_images=int(input('Enter number of images required : '))


response=openai.Image.create(
    prompt=user_prompt,
    n=number_of_images,
    size="1024x1024"
)


count=0
for i in range (number_of_images):
    image_url=response['data'][i]['url']
    count=count+1

    urllib.request.urlretrieve(
        image_url,
       f"image {count}.png")
    
    img = Image.open(f"image {count}.png")
    img.show()
