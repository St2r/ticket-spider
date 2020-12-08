# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TicketItem(scrapy.Item):
    number = scrapy.Field()
    start_station_name = scrapy.Field()
    start_station_type = scrapy.Field()
    arrival_station_name = scrapy.Field()
    arrival_station_type = scrapy.Field()
    time_start = scrapy.Field()
    time_arrival = scrapy.Field()
    time_total = scrapy.Field()
    arrival_today = scrapy.Field()

    ShangWuZuo = scrapy.Field()
    YiDengZuo = scrapy.Field()
    ErDengZuo = scrapy.Field()

    GaoJiRuanWo = scrapy.Field()
    RuanWo = scrapy.Field()
    DongWo = scrapy.Field()
    YingWo = scrapy.Field()

    RuanZuo = scrapy.Field()
    YingZuo = scrapy.Field()
    WuZuo = scrapy.Field()







