# Scrapy settings for FocusEngine project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
BOT_NAME = 'FocusEngine'

SPIDER_MODULES = ['FocusEngine.spiders']
NEWSPIDER_MODULE = 'FocusEngine.spiders'

ITEM_PIPELINES = [
    'FocusEngine.pipelines.FocusEnginePipeline'
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FocusEngine (+http://www.yourdomain.com)'
