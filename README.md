
# BigBasket Web Scraper

## Introduction

This repository contains a web scraper for extracting product information from the BigBasket website's fruits and vegetables category. The scraper is built using Scrapy and Selenium, leveraging the strengths of both libraries to handle dynamic content and efficiently gather data.

## Features

- **Automatic Scrolling**: The scraper automatically scrolls the webpage for a specified number of seconds to load images and additional content.
- **Product Extraction**: Extracts detailed product information including brand, product name, discounted price, original price, and image URL.
- **Pagination Handling**: Navigates through multiple pages of product listings to gather comprehensive data.

## Installation

1. Ensure Python is installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install scrapy selenium
   ```

## Running the Scraper

1. Ensure that you have Chrome WebDriver installed and its path is configured in your environment.
2. Create a new Scrapy project and navigate to its directory:
   ```bash
   scrapy startproject bigbasket_scraper
   cd bigbasket_scraper
   ```
3. Create a new spider file (e.g., `bigbasket_spider.py`) in the `spiders` directory and copy the provided code into it.
4. Run the scraper using the command:
   ```bash
   scrapy crawl bigbasket -o output.csv
   ```
   Replace `bigbasket` with the spider name specified in the `name` attribute of the spider class.
5. The scraped data will be saved to the specified output file (e.g., `output.csv`) in CSV format.

## Output

The scraper generates a CSV file containing the following fields for each product:

- **Category**: The category of the product (e.g., fruits, vegetables).
- **Brand**: The brand name of the product.
- **Product Name**: The name of the product.
- **Discounted Price**: The discounted price of the product.
- **Original Price**: The original price of the product.
- **Image URL**: The URL of the product image.

## Limitations

- The scraper may require adjustments if the structure of the BigBasket website changes.
- It relies on time-based scrolling to load content, which may not be efficient for all scenarios.
- Usage of web scraping should comply with the website's terms of service and legal requirements.

## Conclusion

The BigBasket web scraper provides a convenient way to extract product information from the BigBasket website for various purposes such as market analysis, price tracking, and inventory management. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Scrapy](https://scrapy.org/) - An open-source and collaborative web crawling framework for Python.
- [Selenium](https://www.selenium.dev/) - A suite of tools for automating web browsers.

---

Feel free to contribute to the project by opening issues or submitting pull requests. Happy scraping!
