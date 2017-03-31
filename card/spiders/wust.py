# -*- coding: utf-8 -*-
import scrapy
from card.items import CardItem


class WustSpider(scrapy.Spider):
    name = "wust"
    # allowed_domains = ["card.wust.edu.cn"]
    start_urls = ['http://card.wust.edu.cn/default.aspx']

    def parse(self, response):
        cookies = {
            "ASP.NET_SessionId":"jwofwnq2k253ek45ltr4ywu3",
        }

        return scrapy.FormRequest.from_response(response,
                formdata = {"ddlYear":"2017", "ddlMonth":"1"},
                method = "POST",
                url = "http://card.wust.edu.cn/Cardholder/Queryhistory.aspx",
                callback = self.after_login,
                cookies = cookies)

        # yield scrapy.Request(
        #     "", self.home, cookies=cookies)
    def after_login(self, response):
        return scrapy.Request("http://card.wust.edu.cn/Cardholder/QueryhistoryDetailFrame.aspx", self.home)

    def home(self, response):
        item = CardItem()
        # print response.body
        #表头部分
        table_head = '//tr[@class="dg_header"]'
        head = response.xpath(table_head)
        head_time = head.xpath('./td[9]/text()').extract()[0]   #到账时间
        head_tnover = head.xpath('./td[8]/text()').extract()[0]  #交易额
        head_balance = head.xpath('./td[11]/text()').extract()[0]   #卡余额
        head_type = head.xpath('./td[5]/text()').extract()[0]   #商户类型
        item["head_time"] = head_time
        item["head_type"] = head_type
        item["head_tnover"] = head_tnover
        item["head_balance"] = head_balance
        #表体部分
        table_body = '//tr[@valign="middle" and @align="center" and not(contains(@class,"dg_header"))]'
        body = response.xpath(table_body)
        body_time = body.xpath('./td[9]/text()').extract()
        body_tnover = body.xpath('./td[8]/text()').extract()
        body_balance = body.xpath('./td[11]/text()').extract()
        body_type = body.xpath('./td[5]/text()').extract()

        bodys = []
        for i in range(len(body_time)):

            bodys.append({"body_time":body_time[i], "body_type":body_type[i], \
                          "body_tnover":body_tnover[i], "body_balance":body_balance[i]})

        item["bodys"] = bodys
        yield item





