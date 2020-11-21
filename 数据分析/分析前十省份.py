import csv
import datetime

import matplotlib.pyplot as plt

pro_dic={}
pronum_dic={}

# 将前十的省份和平均数存进列表
province_dict_keys = []
province_dict_values = []
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

with open("集美大学各省录取分数.csv", "r", encoding='GBK', newline='') as filereader:
    with open("本一批理工科.csv", "w", encoding='utf-8',newline='') as filewriter:
        filereader = csv.reader(filereader)
        filewriter = csv.writer(filewriter)
        header =next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            pici =str(row_list[1]).strip()
            kelei =str(row_list[2]).strip()
            pattern = re.compile(r'(.*本一.*)', re.I)
            if pattern.search(pici):
                pici="本一批"

            #判断是否符合
            if pici =="本科A批":
                pici="本一批"
            if pici =="本一批" and kelei=="理工":

                pro=str(row_list[0]).strip()
                #存入
                if pro not in pro_dic:
                    #pro_list.append(pro)
                    aver = float(str(row_list[6]).strip())
                    pro_dic[pro]=aver
                    pronum_dic[pro]= 1

                    year = str(row_list[7]).strip()
                else:
                    aver = str(row_list[6]).strip()
                    pro_dic[pro]=float(pro_dic[pro])+float(aver)
                    pronum_dic[pro]+=1


        #排序
        pro_dic_ave={}
        for e in pro_dic.keys():
            print(e)
            pro_dic_ave[e]=pro_dic[e]/pronum_dic[e]

        pro_dic_top=sorted(pro_dic_ave.items(), key = lambda x:(x[1]),reverse=True)

        for e in pro_dic_top[:10]:
            province_dict_keys.append(e[0])
            print(e)
            province_dict_values.append(e[1])

        print(province_dict_keys)
        print(province_dict_values)
        plt.bar(x=province_dict_keys, height=province_dict_values, alpha=0.8)
        for x, y in enumerate(province_dict_values):
            plt.text(x, y, '%s' % y, ha='center', va='bottom')
        # 设置标题
        plt.title("排名前10的省份")
        # 为两条坐标轴设置名称
        plt.xlabel("省份")
        plt.ylabel("平均分")

        plt.show()
