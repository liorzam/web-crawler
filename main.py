
from crawler.argparse import parse_args
from crawler.web_crawler import WebCrawler
from crawler.multi_crawler import start_multiprocess_crawling

if __name__ == '__main__':
    args = parse_args()

    crawler = WebCrawler(args)
    
    crawler.start()