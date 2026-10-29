# Web Scraping Application

A Python-based web scraping utility that searches for a company or business name along with its location, extracts contact details such as email and phone number from the resulting web pages, and saves the output into a CSV file.

This project demonstrates how to combine Google search results, HTML parsing, regex-based extraction, and data export to automate the process of collecting business contact information.

## Features

- Reads business names and locations from an input CSV file
- Searches Google for each query using the `googlesearch` library
- Fetches the search result page content using `requests`
- Parses HTML using `BeautifulSoup`
- Extracts email addresses with regular expressions
- Extracts phone numbers from paragraphs and spans using validation patterns
- Stores the extracted results in a CSV output file

## Project Structure

```text
Web-Scraping-application/
├── extract.py          # Main Python script
├── nameloc.csv         # Input file with company names and locations
├── file1.csv           # Output file generated after scraping
├── README.md           # Project documentation
├── SeeThis.txt         # Quick project notes
├── Market Tract.docx   # Project documentation/report
```

## Input Format

The input file `nameloc.csv` should contain at least these columns:

```csv
name,location
HCL Technologies Ltd,nagpur
Infosys Ltd,Bangalore
aditi digital solutions,hyderabad
```

## How It Works

1. The script reads the CSV file and extracts the `name` and `location` columns.
2. It creates a search query using the company name and location, such as:
   `HCL Technologies Ltd nagpur`
3. It searches the web and fetches the first result page.
4. It parses the HTML content with `BeautifulSoup`.
5. It uses `re` (regular expressions) to detect email IDs and phone numbers.
6. It saves the results to `file1.csv`.

## Requirements

Install the required dependencies using:

```bash
pip install beautifulsoup4 requests pandas google
```

## Usage

1. Open `nameloc.csv` and add the business names and their locations.
2. Run the script:

```bash
python extract.py
```

3. The extracted data will be saved in `file1.csv`.

Example output:

```csv
,email,phone
0,hcl-nagpur@hcl.com,not found
1,not found,not found
2,admin@aditidigitalsolutions.com,+91 836 748 7105
```

## Notes

- This project is designed as a learning/demo application for scraping and data extraction.
- Website structure varies across sites, so the script may not reliably extract all data from every source.
- Some websites block automated scraping or require JavaScript rendering, which this script does not handle.
- Always respect the terms of service and privacy policies of the websites you scrape.

## License

This project is intended for educational and research purposes. Please check the repository owner for any licensing details before commercial use.

## Disclaimer

This tool is built for learning and experimentation. It should not be used for unethical, unauthorized, or high-volume scraping activities that may violate website policies or applicable laws.
