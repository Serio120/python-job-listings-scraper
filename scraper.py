"""Scrape the Real Python demo job board and export listings to CSV."""

import csv
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.github.io/fake-jobs/"
CSV_FILE = Path("jobs.csv")
FIELDNAMES = ["title", "company", "location", "detail_url"]
REQUEST_TIMEOUT = 15


def extract_jobs(html: str, base_url: str = BASE_URL) -> List[Dict[str, str]]:
    """Extract job listings from a page of HTML."""
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    for card in soup.find_all("div", class_="card-content"):
        title = card.find("h2", class_="title")
        company = card.find("h3", class_="company")
        location = card.find("p", class_="location")
        apply_link = next(
            (
                link
                for link in card.find_all("a")
                if link.get_text(strip=True).lower() == "apply"
            ),
            None,
        )

        href = apply_link.get("href") if apply_link else None
        jobs.append(
            {
                "title": title.get_text(strip=True) if title else "N/A",
                "company": company.get_text(strip=True) if company else "N/A",
                "location": location.get_text(strip=True) if location else "N/A",
                "detail_url": urljoin(base_url, href) if href else "N/A",
            }
        )

    return jobs


def fetch_jobs(url: str = BASE_URL, timeout: int = REQUEST_TIMEOUT) -> List[Dict[str, str]]:
    """Download the job board and return its extracted listings."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return extract_jobs(response.text, base_url=url)


def write_jobs_csv(
    jobs: List[Dict[str, str]], output_path: Union[Path, str] = CSV_FILE
) -> Path:
    """Write extracted listings to a UTF-8 CSV file."""
    output = Path(output_path)
    with output.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(jobs)
    return output


def main() -> None:
    jobs = fetch_jobs()
    output = write_jobs_csv(jobs)
    print("Extraction completed. {} jobs saved to {}".format(len(jobs), output))


if __name__ == "__main__":
    main()
