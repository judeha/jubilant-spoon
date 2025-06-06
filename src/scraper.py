import urllib.request
import sys
import yaml
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Read in config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
LOWER_BOUND = config["LOWER_BOUND"]
UPPER_BOUND = config["UPPER_BOUND"]
KEYWORD = config["KEYWORD"]
YEAR = config["YEAR"]
MONTH = config["MONTH"]

agent = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11" 

# Init reader
reader = urllib.request.build_opener()
reader.addheaders = [('User-Agent', agent)]
urllib.request.install_opener(reader)

# Define a threading event to signal when the keyword is found
found_event = threading.Event()

def search_url(i, keyword):
    """!@brief Searches a single URL for a keyword.
    @param i: The index of the URL to search.
    @param keyword: The keyword to search for in the URL content.
    @return: URL if the keyword is found, False otherwise.
    @note: Uses a threading event to stop searching if the keyword is found.
    """
    if found_event.is_set():
        return False  # early stop
    
    # Construct the URL based on the index and year
    url = f"https://ijs.usfigureskating.org/leaderboard/results/{YEAR}/{i}/index.asp"
    # Check URL response for keyword 
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode()
            if keyword.casefold() in content.casefold():
                found_event.set()
                return url
    except Exception as e:
        pass  # or log error

    return False

def search_urls(lb, ub, keyword, max_threads=10):
    """!@brief Searches a range of URLs for a keyword using multithreading.
    @param lb: Lower bound of the URL index range.
    @param ub: Upper bound of the URL index range.
    @param keyword: The keyword to search for in the URL content.
    @param max_threads: Maximum number of threads to use for searching.
    @return: A list of matching URLS if they exist
    """
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Create a list of futures for each URL in the range
        futures = [executor.submit(search_url, i, keyword) for i in range(lb, ub + 1)]

        relevant_urls = []
        # Wait for all futures to complete
        for future in as_completed(futures):
            # Check if the keyword was found
            if future.result():
                relevant_urls.append(future.result())
    print(f"Found {len(relevant_urls)} URLs containing the keyword '{keyword}'")
    for url in relevant_urls:
        print(url)
    return relevant_urls

search_urls(LOWER_BOUND, UPPER_BOUND, KEYWORD)