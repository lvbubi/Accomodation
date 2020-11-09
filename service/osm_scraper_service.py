from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import service.settings as settings


def create_driver():
    options = Options()
    options.headless = settings.HEADLESS
    return webdriver.Chrome(options=options, executable_path=settings.DRIVER_PATH)


def scrape_page(counties):
    DRIVER = create_driver()

    print(f"Accessing page at {settings.OSM_URL} ...")
    DRIVER.get(settings.OSM_URL)
    print("Done!")
    sidebar = DRIVER.find_element_by_css_selector('#sidebar')
    query = sidebar.find_element_by_css_selector('input#query')
    search = sidebar.find_element_by_name('commit')

    coordinates = []
    for county in counties:
        query.clear()
        query.send_keys(county)
        search.click()
        DRIVER.implicitly_wait(10)
        result = sidebar.find_elements_by_css_selector('.search_results_entry a').pop(0)
        coordinates.append({"name": county,
                            "extractedName": result.get_attribute('data-name'),
                            "longitude": result.get_attribute('data-lat'),
                            "latitude": result.get_attribute('data-lon')
                            })
    print(coordinates)
