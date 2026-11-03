# Python Job Listings Scraper

A small Python scraper that extracts job listings from the [Real Python Fake Python Jobs demo site](https://realpython.github.io/fake-jobs/) and exports them to CSV and HTML.

Built as a learning project for the [Roadmap.sh Job Listings Scraper challenge](https://roadmap.sh/projects/job-listings-scraper).

## Features

- Fetch the demo job board using Requests.
- Parse listing cards with Beautiful Soup.
- Extract title, company, location and detail URL.
- Resolve relative detail links against the source URL.
- Export a UTF-8 CSV file.
- Render a standalone HTML report.
- Escape scraped values before inserting them into HTML.
- Apply an HTTP request timeout and fail clearly on unsuccessful responses.
- Unit tests for extraction, URL handling, CSV output and HTML escaping.

## Requirements

- Python 3.8 or later
- Internet access to fetch the demo page

Install dependencies:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python scraper.py
```

This creates `jobs.csv` with the columns:

| Column | Description |
|---|---|
| `title` | Job title |
| `company` | Company name |
| `location` | Job location |
| `detail_url` | Absolute URL to the listing |

Generate the HTML report:

```bash
python view_jobs_html.py
```

This creates `jobs.html`. Open it in a browser to view the extracted listings.

## Tests

Run the standard-library unittest suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests use mocked HTTP responses and local HTML fixtures, so they do not require a network connection.

## Project structure

```text
python-job-listings-scraper/
├── scraper.py
├── view_jobs_html.py
├── requirements.txt
├── tests/
│   └── test_scraper.py
└── README.md
```

Generated files (`jobs.csv` and `jobs.html`) are runtime outputs and should not be committed.

## Notes and limitations

This project targets a static demonstration site intended for learning. It is not a general-purpose crawler and does not implement pagination, persistent storage, scheduling or production-scale crawling. When adapting it to another site, respect that site's terms, robots policies, rate limits and privacy requirements.

## References

- [Real Python Fake Python Jobs](https://realpython.github.io/fake-jobs/)
- [Requests documentation](https://requests.readthedocs.io/)
- [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)

## License

No license is currently specified for this repository. Check the repository owner’s licensing intentions before reusing the code.
