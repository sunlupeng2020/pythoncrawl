import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'uuid=ef64183f-7220-4884-d16a-7cfc00831154; ganji_uuid=7773749105698522765034; gr_user_id=a536f5be-6652-4247-a187-65885d1b5e9c; antipas=0848g7950r3526003YP6970343B; cityDomain=cs; clueSourceCode=%2A%2300; user_city_id=204; sessionid=c3fdbefb-8efb-4d5f-97c7-469b02ef4944; lg=1; gr_session_id_bf5e6f1c1bf9a992=c4eeb8d4-c7f5-47fc-a3ce-2f8b30b5c2f0; gr_session_id_bf5e6f1c1bf9a992_c4eeb8d4-c7f5-47fc-a3ce-2f8b30b5c2f0=true; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22ef64183f-7220-4884-d16a-7cfc00831154%22%2C%22ca_city%22%3A%22zz%22%2C%22sessionid%22%3A%22c3fdbefb-8efb-4d5f-97c7-469b02ef4944%22%7D; preTime=%7B%22last%22%3A1595465360%2C%22this%22%3A1592014853%2C%22pre%22%3A1592014853%7D'
}

def parse_detail_page(url):
    resp = requests.get(detail_url, headers=headers)
    text = resp.content.decode('utf-8')
    html = etree.HTML(text)
    # print(html)
    title = html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
    title = title.replace(r'\r\n', '').strip()
    # print(title)
    info = html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
    # print(info)
    infos = {}
    # cardtime = info[0]
    km = info[2]
    # print(km)
    displacement = info[3]
    speedbox = info[4]
    infos['title'] = title
    infos['km'] = km
    infos['displacement'] = displacement
    infos['speedbox'] = speedbox
    # print(infos)
    return infos


def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    text = resp.content.decode('utf-8')
    # print(text)
    html = etree.HTML(text)
    # print(html)
    ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
    # print(ul)
    lis = ul.xpath('./li')
    #空列表
    detail_urls = []
    # print(lis)
    for li in lis:
        # print(li)
        detail_url = li.xpath('./a/@href')
        # print(detail_url)
        detail_url = 'https://www.guazi.com' + detail_url[0]
        # print(detail_url)
        detail_urls.append(detail_url)
    return detail_urls


def main():
    url = 'https://www.guazi.com/cs/buy/01'
    detail_urls = get_detail_urls(url)
    for detail_url in detail_urls:
        infos = parse_detail_page(detail_url)
        print(infos)


if __name__ == '__main__':
    main()


# print(__name__)
