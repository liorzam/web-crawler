# Web Crawler

Web Crawler is a Python-based command-line tool for crawling web pages and extracting information about links and page ranks. It supports crawling HTTP and HTTPS URLs up to a specified depth limit.

## Features

- Crawls web pages and processes links up to a specified depth.
- Calculates page rank based on the ratio of same-domain links.
- Supports HTTP and HTTPS URLs.
- Avoids re-downloading pages already visited during the current execution.
- Customizable logging and verbose output.

## Installation

1. Clone the repository
2. Install the required dependencies using Poetry: `poetry install`
   <!-- #TODO: Upload to my personal git -->
   ```sh
   git clone https://github.com/liorzam/web-crawler.git
   cd web-crawler
   poetry install
   ```

## Usage

### Logging and Verbose Mode
The crawler supports different levels of logging verbosity. By default, the log level is set to 'info', providing essential information about the crawling process. You can increase the verbosity to 'debug' level to get more detailed logs, which can be helpful for debugging.

To enable 'debug' level logging, set the LOG_LEVEL environment variable to 'debug' before running the crawler:

```sh
LOG_LEVEL=debug poetry run crawler https://example.com
```

### Run the crawler and specify a starting URL:
#### Using bash:
   * `<root_url>`: The URL of the starting web page for crawling.
   * -d or --depth_limit: (Optional) The recursion depth limit for crawling (default: 3).
   * -l or --page_link_limit: (Optional) The maximum number of page href links to collect (default: 10).

   ```sh 
   $ # crawler <root_url> [-d <depth_limit>] [-l <page_link_limit>]
   $ crawler <root_url> --depth_limit 3 --page_link_limit 10
   $ crawler <root_url> -d 3 -l 10
   
   ```

#### Using Docker:
   ```sh 
   $ docker-compose run crawler -d 3 -l 10 <root_url>
   ```

#### Using python:
   ```sh
$ python main.py -h
   
usage: main.py [-h] [-d DEPTH_LIMIT] [-l PAGE_LINK_LIMIT] root_url

Web Crawler

positional arguments:
root_url              The root URL to start crawling from

optional arguments:
-h, --help            show this help message and exit
-d DEPTH_LIMIT, --depth_limit DEPTH_LIMIT
                        The recursion depth limit (default: 3)
-l PAGE_LINK_LIMIT, --page_link_limit PAGE_LINK_LIMIT
                        Page href link limit (default: 10)

   ```

Replace `<root_url>` with the URL of the root page to start crawling from, and `<depth_limit>` with a positive integer representing the recursion depth limit.

The crawler will output a TSV file containing URL, depth, and rank information.

<!-- #TODO: Deploy docker to dockerhub -->
<!-- #TODO: Add how to use with docker  -->

## Publish new version

1. *Prepare Your Package* - Before publishing your package, make sure your project structure is well-organized, and you have defined the necessary metadata in your pyproject.toml file. Ensure that your package includes the required files and dependencies.
1. *Increment Version* - If you're updating your package, consider incrementing the version number in your pyproject.toml file to indicate the new version. You can update the version field under [tool.poetry]. <!-- TODO: Github action that do that automatically  -->
1. *Build and Publish the Package* - The --build option tells Poetry to build the distribution files before publishing.
   ```sh
   poetry publish --build
   ```



### Dependencies
This project uses the following dependencies:

* requests: For fetching web pages.
* beautifulsoup4: For HTML parsing.
* argparse: For command-line argument parsing.

You can find the complete list of dependencies in the pyproject.toml file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

##
Feel free to contribute to this project by opening issues or pull requests. Happy crawling!!