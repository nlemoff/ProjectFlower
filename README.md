# Project Flower

This Python script automates the scraping of product information from online shops using Selenium WebDriver with Chrome for Testing.

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Chrome for Testing
- ChromeDriver

## Required Python Packages

```bash
pip install selenium pandas
```

## Chrome for Testing and ChromeDriver Setup

1. Visit the official Chrome for Testing downloads page:
   [Chrome for Testing Downloads](https://googlechromelabs.github.io/chrome-for-testing/)

2. Download both Chrome for Testing and ChromeDriver that match your system architecture (Windows, Mac Intel, Mac ARM64, or Linux)

3. Create a project directory and extract both downloads:
   ```bash
   mkdir -p ProjectFlower
   # Extract your downloads into this directory
   ```

## Setting Up Permissions (Mac/Linux Users Only)

### Chrome for Testing Permissions
```bash
chmod +x "ProjectFlower/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
xattr -d com.apple.quarantine "ProjectFlower/chrome-mac-arm64/Google Chrome for Testing.app"
```

### ChromeDriver Permissions
```bash
chmod +x ProjectFlower/chromedriver-mac-arm64/chromedriver
xattr -d com.apple.quarantine ProjectFlower/chromedriver-mac-arm64/chromedriver
```

## Usage

1. Update the paths in the script to match your directory structure:
   ```python
   chrome_binary_path = 'ProjectFlower/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
   chromedriver_path = 'ProjectFlower/chromedriver-mac-arm64/chromedriver'
   ```
2. Run the script:
   ```bash
   python main.py
   ```

## Ideal Output

The script once completed will create a CSV file named `cbcb_products.csv` containing:
- Product Name
- Price
- Description

## License

This project is licensed under the MIT License - see the LICENSE file for details.
