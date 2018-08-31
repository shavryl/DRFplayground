import threading, time, urllib.request
from games.concurrency.decorators import timeit


def download_image(image_path, file_name):
    print('Downloading from ', image_path)
    urllib.request.urlretrieve(image_path, file_name)
    print('Completed Download')


def execute_thread(num):
    image_name = "temp/image-" + str(num) + ".jpg"
    download_image("http://lorempixel.com/400/200/sports", image_name)


@timeit
def main():
    threads = []
    for number in range(5):
        thread = threading.Thread(target=execute_thread, args=(number, ))
        threads.append(thread)
        thread.start()

    for worker in threads:
        worker.join()


main()
