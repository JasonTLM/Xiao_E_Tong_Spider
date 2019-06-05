import requests
import json
import csv
import xlwt


class XiaoETSpider:
    def __init__(self):
        self.start_url = "https://fenxiao.xiaoe-tech.com/pc/get_classify_list?page={}&order=1&classify_id={}&page_size=15"

        self.url_next = "https://fenxiao.xiaoe-tech.com/pc/distribute_content?id={}&content_app_id={}"

        self.headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
         "Referer": "https://fenxiao.xiaoe-tech.com/",
         "cookie": "XIAOEID=2304b679d406348d6026563ab301d865; cookie_referer=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00f7b2k_077-b07dHy0AZ6OuT000007bM2dC00000Xi2mym.THLfCUU_1p60UWdBmy-bIfK15ycLrjNWrycsnj0sPyFbuWD0IHYvfW6LPWnvrRR3fHuKPW0YwDR4rHTdPRfsPjTkwjbLw0K95gTqFhdWpyfqn1cYPWD1PWDYPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz43py7EuidYuyPCQhPEUitOmv99Uh4-UjYzQHDdPW60mLFW5HcdnHc1%26tpl%3Dtpl_11533_19125_15129%26l%3D1512777561%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525B0%25258F%2525E9%2525B9%252585%2525E9%252580%25259A-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E5%252586%252585%2525E5%2525AE%2525B9%2525E4%2525BB%252598%2525E8%2525B4%2525B9%2525E7%25259A%252584%2525E6%25258A%252580%2525E6%25259C%2525AF%2525E6%25259C%25258D%2525E5%25258A%2525A1%2525E5%252595%252586%2526xp%253Did%28%252522m3246136144_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D18%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E5%25B0%258F%25E9%25B9%2585%25E9%2580%259A%26rqlang%3Dcn; cookie_channel=2-1568; Hm_lvt_32573db0e6d7780af79f38632658ed95=1559659404; Hm_lpvt_32573db0e6d7780af79f38632658ed95=1559659404; dataUpJssdkCookie={'wxver':"",'net':"",'sid':""}; cookie_is_signed=1; channel=homepage; Hm_lvt_081e3681cee6a2749a63db50a17625e2=1559663291,1559663299,1559663322,1559663374; cookie_session_id=fPABJOjeazbt6zZu5ohIaZiWUF0H0iQf; Hm_lpvt_081e3681cee6a2749a63db50a17625e2=1559671022"
         }

    def parse_url(self,url):
        """发送请求"""
        print(url)
        response = requests.get(url,headers=self.headers)
        # json_str = response.content.decoded()
        # print(type(json_str))
        # dict_ret = json.loads(json_str)
        return response.content.decode().encode('utf-8')

    def get_content_list(self,json_str):
        """
        提取第一次jason数据
        :param json_str:
        :return:
        """

        dict_ret = json.loads(json_str)
        app_ids = dict_ret["data"]["list"]
        app_id = [i["app_id"] for i in app_ids]
        resource_ids = dict_ret["data"]["list"]
        resource_id = [j["resource_id"] for j in resource_ids]
        contentTotal = dict_ret["data"]["contentTotal"]
        return app_id,resource_id,contentTotal

    def get_test_datas(self,jsons_strs):
        dictr_rets = json.loads(jsons_strs)
        datas = dictr_rets["data"]
        return datas

    def get_content_list_json(self,json_strs):

        """
        实现第二次提取
        :param json_str:
        :return:
        """
        dict_rets = json.loads(json_strs)
        name = dict_rets["data"]["name"]
        summary = dict_rets["data"]["summary"]
        price = dict_rets["data"]["price"]
        order_price = dict_rets["data"]["shop_info"]["order_price"]
        shop_name = dict_rets["data"]["shop_info"]["shop_name"]
        wx_name = dict_rets["data"]["shop_info"]["wx_name"]
        study_num = dict_rets["data"]["study_num"]
        code_num = dict_rets["code"]
        # print(type(name))

        image_src = dict_rets["data"]["org_content"]
        catalogs = dict_rets["data"]["catalog"]["data"]
        # catalog = [i["title"] for i in catalogs]
        verify_type = dict_rets["data"]["verify_type"]
        org_content = dict_rets["data"]["org_content"]
        # print(name,"\n")
        # print(summary,"\n")
        # print(price,"\n")
        # print(order_price,"\n")
        # print(study_num,"\n")
        # print(shop_name,"\n")
        # print(wx_name,"\n")


        # print(catalogs,"\n")
        return name, summary, price, order_price, shop_name, wx_name, \
               study_num, image_src, catalogs, verify_type, org_content
        # return dict_rets["name"]


    def save_content_list(self, name, summary, price, order_price, shop_name, wx_name, study_num, image_src, catalogs, verify_type, org_content, app_id):
        sheaders = ['名称','简介','售价','预售收益','学习人次','店名','微信号']
        values = [
            (name,summary,price,order_price,study_num,shop_name,wx_name)
        ]
        # with open('/home/jason/文档/xiao_teach/XETSpider.xls','w') as f:
        #     writer = csv.DictWriter
        with open ('test.csv','a',newline='') as fp:
            writer = csv.writer(fp)
            # writer.writerow(sheaders)
            writer.writerows(values)
            # writer.writerows('\n')
        catalog_titles = [i["title"] for i in catalogs]
        catalog_id = [j["id"] for j in catalogs]
        url_lists = []
        # for li, lis in zip(app_id, resource_id):
        for calog_id, ap_id in zip(catalog_id, app_id):
            url_overs = "https://fenxiao.xiaoe-tech.com/#/try_page/{}/{}/{}"
            url_over = url_overs.format(verify_type, ap_id, calog_id)
            url_lists.append(url_over)
        # print(type(name))
        with open (name,"a",encoding='utf-8') as f:
            for catalog_title, url_list in zip(catalog_titles,url_lists):
                f.write(catalog_title)
                f.write('\n'*2)
                f.write(url_list)
                f.write('\n'*2)
                f.write(org_content)
                f.write('\n'*2)

    def run(self):

        for x in range(28, 84):
            y = 1
            m = 1
            code_num = 0
            contentTotal = 15
            while y < int(contentTotal / 15) + 1:
                json_str = self.parse_url(self.start_url.format(m, x))
                app_id,resource_id,contentTotal= self.get_content_list(json_str)
                # dict_ret = json.loads(json_str)
                for li, lis in zip(app_id, resource_id):
                    json_strs = self.parse_url(self.url_next.format(lis, li))
                    datas = self.get_test_datas(json_strs)
                    if datas == []:
                        continue
                    else:
                        name, summary, price, order_price, shop_name, wx_name, \
                        study_num, image_src, catalogs, verify_type, org_content, = self.get_content_list_json(json_strs)
                        self.save_content_list(name, summary, price, order_price, shop_name, wx_name, study_num, image_src, catalogs, verify_type, org_content, app_id)

                m += 1
                y += 1


if __name__ == "__main__":
    xet = XiaoETSpider()
    xet.run()

# for x in range(29, 30):
#     y = 0
#     m = 1
#     contentTotal = 15
#     while y < int(contentTotal/15) + 1 and m <= 2:
#         response = requests.get(url.format(m, x), headers=headers)
#         json_str = response.content.decode("utf-8")
#         dict_ret = json.loads(json_str)
#         app_ids = dict_ret["data"]["list"]
#         app_id = [i["app_id"] for i in app_ids]
#         resource_ids = dict_ret["data"]["list"]
#         resource_id = [j["resource_id"] for j in resource_ids]
#         contentTotal = dict_ret["data"]["contentTotal"]
#         for li, lis in zip(app_id, resource_id):
#             print(url_next.format(lis, li))
#             re = requests.get(url=url_next.format(lis, li),headers=headers)
#             json_really = re.content.decode("utf-8")
#             dict_rets = json.loads(json_really)
#
#
#             # print(resp)
#             # print("*"*100)
#         # print(app_id)
#         # print(resource_id)
#         # print(contentTotal)
#         m += 1
#         y += 1

