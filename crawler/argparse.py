import argparse

from crawler.web_crawler import WebCrawler

def parse_args():
    parser = argparse.ArgumentParser(description="Web Crawler")
    parser.add_argument("root_url", type=str, help="The root URL to start crawling from")
    parser.add_argument("-d", "--depth_limit", type=int,  default=3, help="The recursion depth limit (default: 3)")
    parser.add_argument("-l", "--page_link_limit", type=int, default=10, help="Page href link limit (default: 10)")

    args = parser.parse_args()

    crawler = WebCrawler(root_url=args.root_url,
                          depth_limit=args.depth_limit,
                          page_link_limit=args.page_link_limit)
    
    crawler.start_crawling()