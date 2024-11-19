import base64
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By


def capture_screenshot(driver):
    """Capture the visible part of the browser window as a screenshot."""
    screenshot_base64 = driver.get_screenshot_as_base64()
    return base64.b64decode(screenshot_base64)


def annotate_page(driver, knowledge):
    """Simulate adding annotations to the page."""
    # Simulate an RPC or JavaScript execution for annotations.
    # Example: Inject JavaScript to modify the page.
    driver.execute_script(
        f"""
    const annotations = {knowledge};
    // Example: Add visual labels to the page
    annotations.forEach((annotation, index) => {{
        const label = document.createElement('div');
        label.textContent = `Label ${index + 1}: ${annotation}`;
        label.style.position = 'absolute';
        label.style.top = `${100 + index * 30}px`;
        label.style.left = '20px';
        label.style.backgroundColor = 'yellow';
        label.style.padding = '5px';
        label.style.border = '1px solid black';
        document.body.appendChild(label);
    }});
    """
    )
    time.sleep(0.3)  # Wait for annotations to render


def remove_annotations(driver):
    """Simulate removing annotations from the page."""
    driver.execute_script(
        """
    const annotations = document.querySelectorAll('div');
    annotations.forEach(annotation => annotation.remove());
    """
    )
    time.sleep(0.3)


def merge_images(images, captions):
    """Merge two images and add captions."""
    pil_images = [Image.open(BytesIO(img)) for img in images]
    widths, heights = zip(*(img.size for img in pil_images))

    total_height = sum(heights)
    max_width = max(widths)

    merged_image = Image.new("RGB", (max_width, total_height), (255, 255, 255))

    y_offset = 0
    for img, caption in zip(pil_images, captions):
        merged_image.paste(img, (0, y_offset))
        y_offset += img.height

    return merged_image


def build_annotated_screenshots(driver, knowledge):
    """Generate annotated screenshots."""
    # Step 1: Capture the original screenshot
    img_data_raw = capture_screenshot(driver)

    # Step 2: Annotate the page
    annotate_page(driver, knowledge)

    # Step 3: Capture the annotated screenshot
    img_data_annotated = capture_screenshot(driver)

    # Step 4: Merge the screenshots
    merged_image = merge_images(
        [img_data_raw, img_data_annotated], ["Clean Screenshot", "Annotated Screenshot"]
    )

    # Step 5: Remove annotations
    remove_annotations(driver)

    # Save or return the merged image
    merged_image.save("annotated_screenshot.png")
    return merged_image


# Example usage:
if __name__ == "__main__":
    # Initialize Selenium WebDriver (ChromeDriver required)
    driver = webdriver.Chrome()

    try:
        # Open a webpage
        driver.get("https://example.com")
        driver.maximize_window()

        # Example knowledge data
        knowledge = ["Important Section", "Highlight Area"]

        # Generate annotated screenshots
        build_annotated_screenshots(driver, knowledge)

    finally:
        driver.quit()
