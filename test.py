import argparse
import csv
import os

import pandas as pd

# # data = {"a":1,"b":3}
# # with open("test.csv", "a+", newline="") as file:
# #     writer = csv.writer(file)
# #     for k, v in data.items():
# #         writer.writerow([k,v])
# # dict = {'name': '1', 'site': 2, 'age': 3}
# # df = pd.DataFrame(dict,index=[1])
 
# # # 保存 dataframe
# # df.to_csv('test.csv')
parser = argparse.ArgumentParser(
        description='Arguments to eval the tracking ATE.'
    )
parser.add_argument('--output', type=str, default='output/Replica/office1/mesh/final_mesh_eval_rec.ply')
args = parser.parse_args()
output =  args.output
path = output.split("/")[1].split("_")[0]
# path = os.path.abspath(os.path.join(output, "../../.."))
# path = os.path.split(os.path.dirname(output))[0]
# path = output.split("/")[-1]
# print(f"{os.path.split(os.path.dirname(output))[0]}/test.csv")
print(path)
fieldnames = ['path','first_name', 'last_name']
# # with open('test.csv', 'a+', newline='') as csvfile:

# #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #     if path == "room0":
# #         print("h")
# #         writer.writeheader()
# #     writer.writerow({'path': path, 'first_name': 'Baked', 'last_name': 'Beans'})
# #     # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
# #     # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# with open('test.csv', 'a+', newline='') as csvfile:

#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'path': path, 'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'path': path, 'first_name': 'Wonderful', 'last_name': 'Spam'})
# with open('test.csv', newline='') as csvfile:
#     rows = csv.reader(csvfile)
#     result = ["2","W"]
#     for row in rows:
#         row.append(result)
# with open('test.csv',"w+", newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(rows)


# data_csv = pd.read_csv(r"output_imap/Replica/Replica.csv") # 读取刚才写入的文件
# print("csv文件原始数据为：")
# print(data_csv)

# data_csv['sresult'] = 98 # 新增列sresult 并写入数据
# data_csv['sresult'] = 87
# data_csv.to_csv("output_imap/Replica/Replica.csv", index=False, sep=',') # 将新增的列数据，增加到原始数据中

# data_csv = pd.read_csv(r"output_imap/Replica/Replica.csv") # 读取新增列后的csv文件
# print("新增后csv文件数据为：")
# print(data_csv)
