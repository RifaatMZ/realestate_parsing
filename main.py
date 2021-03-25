from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from uae_realesate import settings
from uae_realesate.spiders.propertyfinder import PropertyfinderSpider

if __name__ == '__main__':
    crawl_settings = Settings()
    crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    crawl_proc.crawl(PropertyfinderSpider)
    crawl_proc.start()
