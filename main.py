
from crawler.argparse import parse_args
from crawler.web_crawler import WebCrawler


def main():
    args = parse_args()

    crawler = WebCrawler(args)

    crawler.start()


if __name__ == '__main__':
    main()
