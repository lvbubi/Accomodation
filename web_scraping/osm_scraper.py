from selenium import webdriver
import webdriver_manager.chrome
import selenium.webdriver.chrome.options
import web_scraping.settings


def create_driver():
    options = selenium.webdriver.chrome.options.Options()
    options.headless = web_scraping.settings.HEADLESS
    return webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install(), options=options)


def scrape_page(counties):
    driver = create_driver()

    print(f"Accessing page at {web_scraping.settings.OSM_URL} ...")
    driver.get(web_scraping.settings.OSM_URL)
    sidebar = driver.find_element_by_css_selector('#sidebar')
    query = sidebar.find_element_by_css_selector('input#query')
    search = sidebar.find_element_by_name('commit')

    coordinates = []
    for county in counties:
        query.clear()
        query.send_keys(county)
        search.click()
        driver.implicitly_wait(10)
        result = sidebar.find_elements_by_css_selector('.search_results_entry a').pop(0)
        print(('downloading', county))
        coordinates.append({"title": county,
                            "extractedName": result.get_attribute('data-name'),
                            "coordinate": [float(result.get_attribute('data-lon')), float(result.get_attribute('data-lat'))],
                            })
    print('DONE')
    return coordinates
