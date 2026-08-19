# 🕷️ Python Job Listings Scraper

> A lightweight Python web scraper that extracts job listings from the **Fake Python Jobs** demo site and exports them to CSV and HTML.

Built as part of the [Roadmap.sh Job Listings Scraper project](https://roadmap.sh/projects/job-listings-scraper).

---

## 🎯 Project Overview

This project demonstrates a simple end-to-end web scraping workflow in Python:

```text
Web page
   ↓
HTTP request
   ↓
HTML parsing with BeautifulSoup
   ↓
Job data extraction
   ↓
CSV export
   ↓
HTML report generation
```

The scraper collects the main information from each job listing and stores it in a structured CSV file. A second script converts that CSV data into a readable HTML table.

---

## ✨ Features

- 🌐 Fetch job listings from a public demo website.
- 🔎 Parse HTML with **BeautifulSoup4**.
- 📋 Extract job title, company, location, and job detail URL.
- 💾 Export results to `jobs.csv`.
- 📊 Generate a browser-friendly `jobs.html` report.
- 🔗 Convert job URLs into clickable links.
- 🛡️ Handle missing fields without stopping the extraction process.
- 🪶 Keep the implementation lightweight with minimal dependencies.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Application and data processing |
| **Requests** | HTTP requests |
| **BeautifulSoup4** | HTML parsing and data extraction |
| **CSV** | Structured data export |
| **Pathlib** | File handling |
| **HTML / CSS** | Generated job listings report |

`requests`, `csv`, and `pathlib` are part of the Python standard library. The only external dependency is **BeautifulSoup4**.

---

## 📁 Project Structure

```text
python-job-listings-scraper/
│
├── scraper.py            # Scrapes job listings and creates jobs.csv
├── view_jobs_html.py     # Converts jobs.csv into jobs.html
└── README.md
```

The following files are generated when the scripts are executed:

```text
jobs.csv                  # Scraped job data
jobs.html                 # HTML report
```

---

## ⚙️ Requirements

- **Python 3.8 or later**
- Internet connection

Install the required dependency:

```bash
pip install beautifulsoup4
```

If `requests` is not available in your Python environment, install it with:

```bash
pip install requests
```

---

## 🚀 Usage

### 1. Clone the repository

```bash
git clone https://github.com/Serio120/python-job-listings-scraper.git
cd python-job-listings-scraper
```

### 2. Run the scraper

```bash
python scraper.py
```

The script retrieves the job listings and creates:

```text
jobs.csv
```

Expected output:

```text
Extraction completed. Data saved to jobs.csv
```

### 3. Generate the HTML report

```bash
python view_jobs_html.py
```

This creates:

```text
jobs.html
```

Open `jobs.html` in a web browser to view the extracted listings in a formatted table.

### 4. Run the complete workflow

```bash
python scraper.py
python view_jobs_html.py
```

---

## 📊 Extracted Data

Each job listing contains the following fields:

| Field | Description |
|---|---|
| `title` | Job title |
| `company` | Company name |
| `location` | Job location |
| `detail_url` | URL of the job detail page |

Missing values are represented as `N/A` rather than causing the extraction process to fail.

---

## 🧠 What This Project Demonstrates

Although intentionally small, this project covers several fundamental concepts that are useful when building data collection tools with Python:

- HTTP requests and response handling.
- HTML document parsing.
- DOM element selection.
- Defensive extraction of optional fields.
- Structured CSV generation.
- Transformation of structured data into HTML.
- Basic file-system operations.
- Separation of data collection from presentation.

---

## ⚠️ Notes & Limitations

This project targets the **Fake Python Jobs** website provided by Real Python for learning and scraping practice. It is a static demonstration site, so JavaScript rendering is not required.

The scraper is intentionally simple and is not designed as a production-grade crawling system. It does not include features such as pagination, retries, rate limiting, persistent databases, or scheduled execution.

---

## 📚 Reference

- [Roadmap.sh — Job Listings Scraper](https://roadmap.sh/projects/job-listings-scraper)
- [Fake Python Jobs — Real Python](https://realpython.github.io/fake-jobs/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

## 📄 License

No license is currently specified for this repository.

---

<p align="center">
  <i>Learn by building · Scrape · Transform · Explore</i>
</p>
