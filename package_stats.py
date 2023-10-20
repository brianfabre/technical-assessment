import gzip
import requests
import sys
from io import BytesIO


def get_data(arch, url):
    """
    Returns contents from link using mirror URL and user specified architecture
    """
    download_url = f"{url}/Contents-{arch}.gz"
    data = requests.get(download_url)
    if is_valid_url(data):
        return BytesIO(data.content)


def is_valid_url(data):
    """
    Checks if URL is valid
    """
    try:
        data.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        raise


def count_packages(data):
    """
    Returns sorted list of top 10 packages and count using the downloaded data
    """
    counts = {}
    with gzip.open(data, "rt") as f:
        for line in f:
            pair = tuple(line.split())
            package = pair[-1].split("/")[-1]
            counts[package] = counts.get(package, 0) + 1

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]


def main():
    mirror_url = "http://ftp.uk.debian.org/debian/dists/stable/main"
    arch = sys.argv[1]

    list = count_packages(get_data(arch, mirror_url))

    print("Top 10 packages:")
    for i, (k, v) in enumerate(list):
        print("{:<6d}{:<20s}{:>20d}".format(i + 1, k, v))


if __name__ == "__main__":
    main()
