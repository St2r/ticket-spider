import scrapy
from scrapy_splash import SplashRequest
from core.items import TicketItem
from datetime import datetime


class TicketSpider(scrapy.Spider):
    name = 'ticket'
    allowed_domains = ['kyfw.12306.cn']
    today = datetime.now().strftime('%Y-%m-%d')
    start_urls = [
        f'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=北京,BJP&ts=天津,TJP&date={today}&flag=N,N,Y'
    ]

    def start_requests(self):  # 重新定义起始爬取点
        for url in self.start_urls:
            yield SplashRequest(url, args={'timeout': 8, 'images': 0, 'wait': 5})

    @staticmethod
    def parse_col(item, ticket_item, col_name, col_number):
        try:
            item[col_name] = ticket_item.xpath(f'./td[{col_number}]/text()').extract()[0]
        except IndexError:
            item[col_name] = ticket_item.xpath(f'./td[{col_number}]/div/text()').extract()[0]

    def parse(self, response, **kwargs):
        ticket_table = response.xpath('/html/body/div[8]/div[7]/table/tbody[1]/tr')
        for ticket_item in ticket_table[::2]:
            item = TicketItem()

            item['number'] = ticket_item.xpath('./td[1]/div/div[1]/div/a/text()').extract()[0]
            item['start_station_name'] = ticket_item.xpath('./td[1]/div/div[2]/strong[1]/text()').extract()[0]
            item['arrival_station_name'] = ticket_item.xpath('./td[1]/div/div[2]/strong[2]/text()').extract()[0]

            item['time_start'] = ticket_item.xpath('./td[1]/div/div[3]/strong[1]/text()').extract()[0]
            item['time_arrival'] = ticket_item.xpath('./td[1]/div/div[3]/strong[2]/text()').extract()[0]
            if item['time_start'] != '-----':
                item['time_total'] = ticket_item.xpath('./td[1]/div/div[4]/strong/text()').extract()[0]
                item['arrival_today'] = ticket_item.xpath('./td[1]/div/div[4]/span/text()').extract()[0]
            else:
                item['time_total'] = '-----'
                item['arrival_today'] = '-----'

            TicketSpider.parse_col(item, ticket_item, 'ShangWuZuo', 2)
            TicketSpider.parse_col(item, ticket_item, 'YiDengZuo', 3)
            TicketSpider.parse_col(item, ticket_item, 'ErDengZuo', 4)
            TicketSpider.parse_col(item, ticket_item, 'GaoJiRuanWo', 5)
            TicketSpider.parse_col(item, ticket_item, 'RuanWo', 6)
            TicketSpider.parse_col(item, ticket_item, 'DongWo', 7)
            TicketSpider.parse_col(item, ticket_item, 'YingWo', 8)
            TicketSpider.parse_col(item, ticket_item, 'RuanZuo', 9)
            TicketSpider.parse_col(item, ticket_item, 'YingZuo', 10)
            TicketSpider.parse_col(item, ticket_item, 'WuZuo', 11)

            yield item

