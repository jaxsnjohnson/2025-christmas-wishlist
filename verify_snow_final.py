from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # --- Test Case 1: Snow should be visible with URL flag ---

        # Capture console messages
        messages = []
        page.on("console", lambda msg: messages.append(msg.text))

        # Navigate to the page with the snow flag
        page.goto('http://localhost:8000?snow=true')

        # 1. Check for the console log
        assert "Creating snow..." in messages, "The 'Creating snow...' message was not found in the console."

        # 2. Verify that snowflake elements exist
        snowflakes = page.locator('.snowflake')
        expect(snowflakes).to_have_count(100)

        # 3. Take a screenshot for visual confirmation
        page.screenshot(path='/home/swebot/jules-scratch/verification/snow-finally-visible.png')

        # --- Test Case 2: Snow should NOT be visible without URL flag ---

        # Navigate to the page without the flag
        page.goto('http://localhost:8000')

        # Verify that NO snowflake elements exist
        snowflakes_without_flag = page.locator('.snowflake')
        expect(snowflakes_without_flag).to_have_count(0)

        # Take a screenshot for visual confirmation
        page.screenshot(path='/home/swebot/jules-scratch/verification/snow-correctly-not-visible.png')

        browser.close()

        print("Verification successful! The snow animation is working as expected with the URL flag.")

if __name__ == "__main__":
    run()
