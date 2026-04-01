from playwright.sync_api import Page

def test_homepage_loads(page: Page):
    page.goto("https://www.businesspromanagement.co.za/")
    assert "Free Accounting Software by Zoho - BPM" in page.title()