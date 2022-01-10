import helium
import time


def scroll_results_page(driver):
    end = False
    while not end:
        try:
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            helium.click('Show more matches')
            time.sleep(2)
        except LookupError:
            end = True
