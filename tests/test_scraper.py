import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import scraper
from view_jobs_html import render_jobs_html


SAMPLE_HTML = """
<div class="card-content">
  <h2 class="title">Python Developer</h2>
  <h3 class="company">Example Ltd</h3>
  <p class="location">Madrid</p>
  <a href="/jobs/python-developer">Apply</a>
</div>
<div class="card-content">
  <h2 class="title">Data Engineer</h2>
</div>
"""


class ExtractJobsTests(unittest.TestCase):
    def test_extracts_fields_and_resolves_relative_url(self):
        jobs = scraper.extract_jobs(
            SAMPLE_HTML, base_url="https://example.test/jobs/"
        )

        self.assertEqual(len(jobs), 2)
        self.assertEqual(jobs[0]["titulo"], "Python Developer")
        self.assertEqual(jobs[0]["empresa"], "Example Ltd")
        self.assertEqual(jobs[0]["ubicacion"], "Madrid")
        self.assertEqual(
            jobs[0]["url_detalle"],
            "https://example.test/jobs/python-developer",
        )

    def test_missing_fields_use_na(self):
        job = scraper.extract_jobs(SAMPLE_HTML)[1]

        self.assertEqual(job["empresa"], "N/A")
        self.assertEqual(job["ubicacion"], "N/A")
        self.assertEqual(job["url_detalle"], "N/A")

    @patch("scraper.requests.get")
    def test_fetch_uses_timeout_and_checks_http_status(self, get):
        response = Mock()
        response.text = SAMPLE_HTML
        get.return_value = response

        jobs = scraper.fetch_jobs(timeout=7)

        get.assert_called_once_with(scraper.BASE_URL, timeout=7)
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(len(jobs), 2)

    def test_csv_export_uses_documented_headers(self):
        jobs = scraper.extract_jobs(SAMPLE_HTML)

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "jobs.csv"
            scraper.write_jobs_csv(jobs, output)

            with output.open(newline="", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                self.assertEqual(reader.fieldnames, scraper.FIELDNAMES)
                self.assertEqual(len(list(reader)), 2)


class HtmlReportTests(unittest.TestCase):
    def test_escapes_scraped_content(self):
        html = render_jobs_html(
            [{
                "titulo": "<script>alert(1)</script>",
                "empresa": "Example & Co",
                "ubicacion": "Madrid",
                "url_detalle": "https://example.test/job?id=1&x=2",
            }]
        )

        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("Example &amp; Co", html)
        self.assertIn("rel=\"noopener noreferrer\"", html)

    def test_does_not_link_non_http_urls(self):
        html = render_jobs_html(
            [{
                "titulo": "Developer",
                "empresa": "Example",
                "ubicacion": "Remote",
                "url_detalle": "javascript:alert(1)",
            }]
        )

        self.assertNotIn('href="javascript:', html)
        self.assertIn("javascript:alert(1)", html)


if __name__ == "__main__":
    unittest.main()
