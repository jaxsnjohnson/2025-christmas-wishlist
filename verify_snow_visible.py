from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000')
        page.screenshot(path='/home/swebot/jules-scratch/verification/snow-effect-visible.png')
        browser.close()

if __name__ == "__main__":
    run()
