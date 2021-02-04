BOT_NAME = 'nedbankprivatewealth'

SPIDER_MODULES = ['nedbankprivatewealth.spiders']
NEWSPIDER_MODULE = 'nedbankprivatewealth.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'nedbankprivatewealth.pipelines.NedbankprivatewealthPipeline': 100,

}