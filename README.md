# web_parsing

This project demonstrates a web scraping script that collects information from multiple pages of a chosen website using the requests and BeautifulSoup modules in Python. The script is designed to handle pagination, extracting data from 5 consecutive pages, and includes a logical delay between requests to avoid overwhelming the server.

How It Works
Website Selection: The script targets a specific website known for having paginated content.
Data Extraction: It uses requests to fetch the HTML content of each page and BeautifulSoup to parse and extract the required information.
Delay Implementation: A delay of 15-20 seconds is introduced between each page request to comply with ethical scraping practices.
Data Storage: Extracted data is saved into a CSV file for further analysis or use.
