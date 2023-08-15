import multiprocessing
from functools import partial
from crawler.url.manager import UrlManager

from crawler.web_crawler import WebCrawler

def crawl_worker(root_url, depth_limit, page_link_limit, worker_id, urls_to_crawl, result_queue):
    crawler = WebCrawler(root_url, depth_limit, page_link_limit)
    url = urls_to_crawl.get()

    while url:
        print(f"Worker {worker_id} is crawling {url}")
        crawler._crawl(url, 1)
        url = urls_to_crawl.get()

    result_queue.put(crawler.get_url_manager())

def start_multiprocess_crawling(args, num_workers):
    try:
        manager = multiprocessing.Manager()
        urls_to_crawl = manager.Queue()
        result_queue = manager.Queue()

        crawler = WebCrawler(args)

        for url in crawler._explore_urls_to_visit_v2(crawler.fetch_page(root_url), root_url):
            urls_to_crawl.put(url)

        pool = multiprocessing.Pool(processes=num_workers)
        worker_func = partial(crawl_worker, root_url, depth_limit, page_link_limit)
        pool.map(worker_func, [i for i in range(num_workers)])

        merged_manager = UrlManager()

        while not result_queue.empty():
            merged_manager.merge(result_queue.get())

        sorted_urls_by_rank = merged_manager.get_urls_sorted_by_rank()

        if sorted_urls_by_rank:
            print(f"Highest Ranked {sorted_urls_by_rank[0]}")

        for url in sorted_urls_by_rank[1:5]:
            print(f"Ranked {url}")

    except ValueError as e:
        print("Error:", e)