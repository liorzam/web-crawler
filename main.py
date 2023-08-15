
from crawler.argparse import parse_args
from crawler.web_crawler import WebCrawler

if __name__ == '__main__':
    args = parse_args()

    crawler = WebCrawler(args)

    crawler.start()
