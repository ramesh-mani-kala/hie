import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
@pytest.fixture(scope="function")
def setup(request):
    """
    Setup fixture to initialize the WebDriver dynamically based on command-line arguments.
    """
    browser = request.config.getoption("--browser").lower()
    url = request.config.getoption("--url")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")

    driver = None

    # Initialize the appropriate WebDriver based on the browser specified
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif Config.BROWSER.lower() == "firefox":

        firefox_options = FirefoxOptions()

        firefox_options.add_argument("--start-maximized")

        # Try using the default binary location, fallback to specified path if needed

        try:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

        except Exception as e:

            print(f"Default Firefox binary location not found: {e}")

            # Use the custom binary location as a fallback (if required for specific systems)

            firefox_options.binary_location = "/usr/bin/firefox"  # Replace with the path used on your system

            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Navigate to the URL and pass credentials dynamically
    driver.implicitly_wait(10)
    driver.get(url)

    # Add credentials to the request object for further use in tests
    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password

    yield
    driver.quit()
def pytest_addoption(parser):
    """
    Add custom command-line options for URL, username, password, and browser.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge")
    parser.addoption("--url", action="store", required=True, help="URL of the application")
    parser.addoption("--username", action="store", required=True, help="Username for login")
    parser.addoption("--password", action="store", required=True, help="Password for login")
