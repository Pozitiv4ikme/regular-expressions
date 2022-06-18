import zipfile
import re
import os


def search_log_in_file():
    dirname = os.path.dirname(__file__)
    zip_log = zipfile.ZipFile(os.path.join(dirname, 'access_log_Jul95.zip'))
    log_file = zip_log.open('access_log_Jul95.txt')
    pattern = r'.*(01/Jul/1995:01:3[5-8]:\d{2}).*(5\d{2}) (\d+)'
    counter_of_failed = 0

    for line in log_file:
        log = re.search(pattern, str(line))
        if log:
            counter_of_failed = counter_of_failed + 1
            # print(line)
    print(f"Amount of failed is {counter_of_failed}")
    zip_log.close()

    # with ZipFile(file_name) as zip_log:
    #     with zip_log.open("access_log_Jul95.txt") as log_file:
    #         for line in log_file:
    #             log = re.search(pattern, str(line))
    #             if log:
    #                 counter_of_failed = counter_of_failed + 1
    #                 print(line)
    #    print(f"Amount of failed is {counter_of_failed}")
