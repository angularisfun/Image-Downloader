import urllib.request

def image_downloader(image_url,image_name):
    full_name = image_name + ".jpg"
    urllib.request.urlretrieve(image_url , full_name)


img_name = input("enter image name:")
image_downloader("http://www.online-image-editor.com//styles/2014/images/example_image.png",img_name)


