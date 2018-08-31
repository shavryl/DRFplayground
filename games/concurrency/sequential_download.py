import urllib.request
from games.concurrency.decorators import timeit


def download_image(image_path, file_name):
    print('Downloading image from ', image_path)
    urllib.request.urlretrieve(image_path, file_name)


@timeit
def main():
    for i in range(5):
        image_name = "temp/image-" + str(i) + ".jpg"
        download_image("http://lorempixel.com/400/200/sports", image_name)


main()
