from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

from hidden import VISION_KEY, VISION_ENDPOINT


client = ComputerVisionClient(VISION_ENDPOINT, CognitiveServicesCredentials(VISION_KEY))

image_url = "https://www.specseatshop.com/cdn/shop/files/2_04f2ac7f-7b42-46d8-b2bb-b8d2352dc9da_360x.png?v=1738021410"

result = client.describe_image(image_url)

if result.captions:
    print("Caption:")
    print(result.captions[0].text)
else:
    print("No caption found.")

