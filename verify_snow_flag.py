from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Test case 1: Snow should be visible
        page.goto('http://localhost:8000?snow=true')
        page.screenshot(path='/home/swebot/jules-scratch/verification/snow-visible-with-flag.png')

        # Test case 2: Snow should NOT be visible
        page.goto('http://localhost:8000')
        page.screenshot(path='/home/swebot/jules-scratch/verification/snow-not-visible-without-flag.png')

        browser.close()

if __name__ == "__main__":
    run()
