import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver を自動ダウンロードして起動


def search(query, start: int, driver=None, quit=False, save_html_path=None):
    if driver is None:
        driver = webdriver.Chrome()

    driver.get(f"https://scholar.google.co.jp/scholar?start={start}&q={query}")
    time.sleep(10)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    main = soup.find("div", {"id": "gs_res_ccl"})
    article_list = main.find_all("div", {"class": "gs_r gs_or gs_scl"})

    if save_html_path:
        with open(save_html_path, "w", encoding="utf-8-sig") as f:
            f.write(page_source)

    if quit:
        driver.quit()
        driver = None
    
    result = []
    for card in article_list:
        # タイトルとリンク
        title_tag = card.select_one("h3.gs_rt a")
        title = title_tag.get_text().strip() if title_tag else None
        url = title_tag.get("href") if title_tag  else None

        # 種別 [PDF] [書籍] など（あれば）
        kind_tag = card.select_one("h3.gs_rt span.gs_ctc span.gs_ct1")
        kind = kind_tag.get_text(strip=True) if kind_tag else None

        # 著者・ジャーナル名・年 などが混ざっている部分
        meta_tag = card.select_one("div.gs_a")
        raw_meta = meta_tag.get_text(" ").strip() if meta_tag else None
        if raw_meta is not None:
            meta = raw_meta.replace("…", "")
            meta_items = re.split("[,-]", meta)
            authors = [atr.strip() for atr in meta_items[:-2]]
            year = int(meta_items[-2].strip())
            jarnal = meta_items[-1].strip()
        else:
            meta = None
            authors = []
            year = None
            jarnal = None

        # 概要（スニペット）
        snippet_tag = card.select_one("div.gs_rs")
        snippet = snippet_tag.get_text(" ", strip=True) if snippet_tag else None

        # 被引用数
        cited = None
        for a in card.select("div.gs_fl a"):
            text = a.get_text(strip=True)
            if text.startswith("被引用数:"):
                # "被引用数: 8" から数字だけ取り出す
                try:
                    cited = int(text.split(":", 1)[1].strip())
                except ValueError:
                    cited = None
                break

        pdf_url = None
        #  [PDF] ボックスにあるリンクを優先して取る
        pdf_tag = card.select_one(".gs_ggs a[href]")
        if pdf_tag:
            href = pdf_tag["href"]
            if ".pdf" in href.lower():
                pdf_url = href

        # 見つからなければ、そのカード内の a タグから .pdf を探す
        if pdf_url is None:
            for a in card.select("a[href]"):
                href = a["href"]
                if ".pdf" in href.lower():
                    pdf_url = href
                    break

        result.append({
            "title": title,
            "url": url,
            "pdf_url": pdf_url,
            "summary": snippet,
            "cited": cited,
            "authors": authors,
            "year": year,
            "jarnal": jarnal,
            "meta": raw_meta,
        })

    return driver, page_source, article_list, result
