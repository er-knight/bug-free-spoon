import requests

def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')
    


# https://sumit-ghosh.com/articles/python-download-progress-bar/
# https://docs.python-requests.org/en/latest/api/#requests.Response
# https://docs.python-requests.org/en/latest/api/#requests.request
# https://github.com/willmcgugan/rich/blob/master/examples/downloader.py
