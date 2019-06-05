import requests
import json
#
# class XiaoeSpider:
#     def __init__(self):
#         self.url_temp = "https://fenxiao.xiaoe-tech.com/pc/get_classify_list?page={}&order=1&classify_id={}&page_size=15"
#         self.url_next = "https://fenxiao.xiaoe-tech.com/#/market/detail/{}/{}/detail"
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
#     def parse_url(self, url):  # 发送请求，获取响应
#         print(url)
#         response = requests.get(url, headers=self.headers)
#         return response.content.decode()
#     def get_content_list(self, json_str):  # 提取是数据
#         dict_ret = json.loads(json_str)
#         app_ids = dict_ret["app_id"]
#         resource_ids = dict_ret["resource_id"]
#         contentTotal = dict_ret["contentTotal"]
#         return app_id, resource_id, contentTotal
#
#     def run(self):  # 实现主要逻辑
#         num = 0
#         contentTotal = 100  # 假设有第一页
#         if num < contentTotal +15:
#             while num < contentTotal + 15:
#                 # 1.start_url
#                 url = url_next.format(appid, resource_id)
#
#                 # 2.发送请求，获取响应
#                 json_str = self.parse_url(url)
#                 # 3.提取是数据
#                 app_ids, resource_ids, contentTotal = self.get_content_list(json_str)
#                 for app_id in app_ids and resource_id in resource_ids:
#                     url = url_next.format(appid, resource_id)
#
#                 # 4.保存
#                 # self.save_content_list(content_list, url_temp["country"])
#                 # if len(content_list)<18:
#                 #     break
#                 # 5.构造下一页的url地址,进入循环
#                 num += 15
#
#

url = "https://fenxiao.xiaoe-tech.com/pc/get_classify_list?page={}&order=1&classify_id={}&page_size=15"
url_next = "https://fenxiao.xiaoe-tech.com/#/market/detail/{}/{}/detail"

headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
         "Referer": "https://fenxiao.xiaoe-tech.com/",
         "cookie": "XIAOEID=2304b679d406348d6026563ab301d865; cookie_referer=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00f7b2k_077-b07dHy0AZ6OuT000007bM2dC00000Xi2mym.THLfCUU_1p60UWdBmy-bIfK15ycLrjNWrycsnj0sPyFbuWD0IHYvfW6LPWnvrRR3fHuKPW0YwDR4rHTdPRfsPjTkwjbLw0K95gTqFhdWpyfqn1cYPWD1PWDYPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz43py7EuidYuyPCQhPEUitOmv99Uh4-UjYzQHDdPW60mLFW5HcdnHc1%26tpl%3Dtpl_11533_19125_15129%26l%3D1512777561%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525B0%25258F%2525E9%2525B9%252585%2525E9%252580%25259A-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E5%252586%252585%2525E5%2525AE%2525B9%2525E4%2525BB%252598%2525E8%2525B4%2525B9%2525E7%25259A%252584%2525E6%25258A%252580%2525E6%25259C%2525AF%2525E6%25259C%25258D%2525E5%25258A%2525A1%2525E5%252595%252586%2526xp%253Did%28%252522m3246136144_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D18%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E5%25B0%258F%25E9%25B9%2585%25E9%2580%259A%26rqlang%3Dcn; cookie_channel=2-1568; Hm_lvt_32573db0e6d7780af79f38632658ed95=1559659404; Hm_lpvt_32573db0e6d7780af79f38632658ed95=1559659404; dataUpJssdkCookie={'wxver':"",'net':"",'sid':""}; cookie_is_signed=1; channel=homepage; Hm_lvt_081e3681cee6a2749a63db50a17625e2=1559663291,1559663299,1559663322,1559663374; cookie_session_id=fPABJOjeazbt6zZu5ohIaZiWUF0H0iQf; Hm_lpvt_081e3681cee6a2749a63db50a17625e2=1559671022"
         }


for x in range(29, 30):
    y = 0
    m = 1
    contentTotal = 15
    while y < int(contentTotal/15) + 1 and m <= 2:
        response = requests.get(url.format(m, x), headers=headers)
        json_str = response.content.decode("utf-8")
        dict_ret = json.loads(json_str)
        app_ids = dict_ret["data"]["list"]
        app_id = [i["app_id"] for i in app_ids]
        resource_ids = dict_ret["data"]["list"]
        resource_id = [j["resource_id"] for j in resource_ids]
        contentTotal = dict_ret["data"]["contentTotal"]
        for li, lis in zip(app_id, resource_id):
            respo = requests.get(url=url_next.format(li, lis),headers=headers)
            print(respo)
        # print(app_id)
        # print(resource_id)
        # print(contentTotal)
        m += 1
        y += 1


