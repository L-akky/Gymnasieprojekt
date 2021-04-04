import newspaper
import configparser
from newspaper import Article
from storage import Storage
from article import Article as ev_article
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read("config.ini")
class NewspaperExtractor:

    def get_text_for_keywords():
        PATH = config([Selenium.Config][PATH])
        driver = webdriver.Firefox(PATH)
        sg = Storage()
        keywords = sg.get_all_keywords()
        papers = sg.get_newspapers()
        for paper in papers:
            for keyword in keywords:
                if paper.url.startswith("https://www.aftonbladet.se/"):
                    print("Aftonbladet")
                    driver.get(paper.url)
                    search = driver.find_element_by_class_name("_5Ypyy")
                    search.send_keys(keyword.text)
                    search.send_keys(Keys.RETURN)
                    search_results = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "YoSxy"))
                    )
                    for x in range(0,10):
                        elems = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._2-Ff7.abThemeBgTeaser._2rWp1.K5r0I._34Te4 [href]"))
                        )
                        links = [elem.get_attribute("href") for elem in elems]
                        scroll_page_down = "window.scrollTo(0, document.body.scrollHeight);"
                        driver.execute_script(scroll_page_down)
                        WebDriverWait(driver, 5)   
                        print(len(links))
                        print("Links")
                    for link in links:
                        article = Article(link)
                        article.download()
                        article.parse()
                        a = ev_article()
                        a.text = article.text
                        keywordid = sg.get_keywordnewspaper_mapping(paper.id, keyword.id)
                        a.keyword_id = keywordid.keyword_mapping_id
                        sg.save_article(a)
            
                
                elif paper.url.startswith("https://www.svd.se/"):
                    print("Svenska Dagbladet")
                    driver.get(paper.url)
                    search = driver.find_element_by_id("q")
                    search.send_keys(keyword.text)
                    search.send_keys(Keys.RETURN)
                    search_results = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Grid.Grid-space--negativeTop.Grid-space--smallBottom"))
                    )
                    for x in range(0,10):
                        elems = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".Grid-item.Grid-item--smallVerticalGutter [href]"))
                        )
                        links = [elem.get_attribute("href") for elem in elems]
                        scroll_page_down = "window.scrollTo(0, document.body.scrollHeight);"
                        driver.execute_script(scroll_page_down)
                        WebDriverWait(driver, 5)   
                    for link in links:
                        article = Article(link)
                        article.download()
                        article.parse()
                        a = ev_article()
                        a.text = article.text
                        keywordid = sg.get_keywordnewspaper_mapping(paper.id, keyword.id)
                        a.keyword_id = keywordid.keyword_mapping_id
                        sg.save_article(a)
            
                else:
                    driver.quit()
                    papers = sg.get_newspapers()
                    keywords = sg.get_all_keywords()
                    web_paper = newspaper.build(paper.url.format(keyword.text), language="sv", memoize_articles=False )
                    for keyword in keywords:
                        for article in web_paper.articles:
                            article.download()
                            article.parse()
                            a = ev_article()
                            a.text = article.text
                            keywordid = sg.get_keywordnewspaper_mapping(paper.id, keyword.id)
                            a.keyword_id = keywordid.keyword_mapping_id
                            sg.save_article(a)



