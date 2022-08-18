import random,csv,os

class Goods():
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=int(quantity)

goods_list=[]
people_list=[]
num=0#分ける物の合計個数
count=0#合計個数までのカウント
index=0

#分ける物について
exists=os.path.exists("choice.csv")
if exists==False:
    kind_quantity=int(input("何種類ありますか？"))
    for i in range(kind_quantity):
        goods_name=input("分ける物の名前を入力してください")
        goods_quantity=int(input('個数を入力してください'))
        with open('choice.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([goods_name,goods_quantity])
    print()#コンソールで見やすくするためにつけた
#分ける人について
exists=os.path.exists("people.csv")
if exists==False:
    number_of_people=int(input("人数を入力してください"))
    for i in range(number_of_people):
        people_name=input("名前を入力してください")
        with open('people.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([people_name])
#読み込み
with open('people.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        people_list.append(row)
with open('choice.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #row[0]は分ける物の名前、row[1]は個数
        goods=Goods(row[0],row[1])
        goods_list.append(goods)
#ここで人と分ける物をランダムにする
people_list=random.sample(people_list, len(people_list))
goods_list=random.sample(goods_list, len(goods_list))
#分ける物の個数を数える
for i in range(len(goods_list)):
    num+=goods_list[i].quantity
#配分する
for i in range(num):#分ける物の個数分
    for j in range(len(people_list)):#人
        if count==num:#全て配り終わったら
            break
        while True:#途中で物がなくなったときに戻ってくるため
            people_list[j].append(goods_list[index].name)
            goods_list[index].quantity-=1
            if goods_list[index].quantity==0:#在庫がなくなったら次の物にする
                index+=1
            count+=1#平等に配分するためのカウント
            break
#結果
with open('result.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(people_list)