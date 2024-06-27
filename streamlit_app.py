import pandas as pd
import random as rd
import numpy as np
import streamlit as st
import csv 


st.title("小学生成長見守り")

st.caption('ランダムな生徒、学校の名前と、タイムが生成されます。生徒数を最初に決めてから実行してください。')
st.caption('ここでは一年生のタイム順でソートされています。個人で解析を行いたい場合、結果の生成後に表示されるダウンロードボタンからcsvファイルをダウンロードしてください。')


#生徒数
num_students = st.slider("生徒数",5,100)

if st.button("実行"):


    #タイムつくる＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in range(num_students):
        exec("student_times" + str(i) + "= []")


    #空白のリストに６年間のタイムを記録していく関数定義
    def time_gen(i):
        rng = np.random.default_rng()
        first_times = rng.normal(11.46, 0.59, 1)
        exec("student_times" + str(i) + ".append(round(first_times[0],2))")

        parsonal_growth_rate = rng.normal(1, 0.07, 1)

        for j in range(5):
            base_improve = rng.normal(0.48, 0.08, 1)
            improve = parsonal_growth_rate * base_improve
            exec("student_times" + str(i) + ".append(round(student_times" + str(i) + "[j] - improve[0],2))")
    #========地名関数============================================================================================================
    place_names_first = ["牛","鷲","犬","猫","鼠","羊","馬","雀","象","窯","闇","濁",
        "桜","月","星","風","火","雪","雷","雨","雲","山","海","川",
        "森","林","花","草","鳥","魚","虫","土","空","光","影","石",
        "玉","金","銀","銅","鉄","砂","泥","水","氷","霧","風","嵐",
        "虹","霜","嶺","丘","谷","洞","野","平","原","沼","湖","浜",
        "港","渓","波","流","湯","泉","滝","岬","島","陸","岸","湾",
        "潮","瀬","瀧","礁","漂","晶","灯","輝","黙","澄","凍","緑",
        "赤","青","白","黒","紫","黄","茶","桃","瑠","璃","翡翠",
        "琉","璃","紺","橙","柿","蔓","蓮","苔","笹","竹","樹",
        "松","桧","杉","柏","楓","椿","樺","梅","栗","李","柳","桂",
        "檜","桃","桐","蘭","菖","蒲","蒲","蕗","菩","提","藤","蘇",
        "葛","萩","葵","菊","薔","薇","胡","蝶","蜻","蛉","蛾","蛍",
        "貝","甲","蛇","龍","鳳","凰","虎","豹","熊","狼","駿","兎",
        "犀","鹿","鷹","鶴","鳩","烏","鴉","鷺","鵺","鷹","鴉"]
    place_names_second = [ "田", "山", "川", "村", "原", "谷", "町", "島", "野", "橋", 
        "崎", "城", "沢", "浜", "港", "庄", "池", "泉", "井", "森", 
        "畑", "林", "浦", "河", "岡", "岩", "戸", "根", "滝", "浜", 
        "平", "沢", "久", "住", "滝", "丘", "宮", "館", "坂", "浜", 
        "沢", "森", "庭", "園", "崎", "村", "畑", "平", "田", "野", 
        "浦", "浦", "内", "崎", "館", "浦", "園", "城", "原", "泉","ヶ丘"]
    place_names_last = ["東","西","南","北","第二","第一","第三","第四","第五"]


    def gen_place_names(first,second,last):
        rd.shuffle(first)
        rd.shuffle(second)
        rd.shuffle(last)
        if rd.randrange(10) > 3:
            return  first[0]+second[0]
        else :
            return  first[0]+second[0]+last[0]

    #＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝名前つくる＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

    first_names =[ "翔太", "大輔", "蓮", "陸", "悠真", "太一", "颯太", "翼", "健太", "悠斗",
        "拓海", "大和", "悠", "翔", "隼人", "光", "颯", "健", "瑛太", "颯真",
        "悠人", "航", "海斗", "海翔", "一真", "隼", "裕太", "悠生", "陽", "勇太",
        "涼太", "匠", "京介", "優", "大輝", "結衣", "花", "葵", "美咲", "さくら",
        "優奈", "莉子", "莉奈", "杏奈", "美月", "菜々子", "楓", "あかり", "美優", "遥",
        "萌", "紗良", "七海", "優衣", "結", "愛", "ひなた", "ひかり", "咲", "美緒",
        "あおい", "唯", "心", "愛莉", "優美", "真央", "あやか", "美桜", "優花", "光",
        "絵美", "沙羅", "玲奈", "結奈", "瑠奈", "悠花", "涼", "実", "果歩", "彩",
        "桜", "桜子", "紗希", "明日香", "奈央", "桃子", "琴音", "未来", "琴乃", "雫",
        "菜月", "一華", "友梨", "美帆", "美咲", "怜", "千夏", "光", "若菜", "詩織",
        "志保", "志穂", "千春", "千尋", "美奈", "美緒", "菜々", "美希", "怜奈", "千絵",
        "栞", "樹里", "梨沙", "佳奈", "聖", "遥香", "望", "桜", "由美", "杏",
        "京子", "彩乃", "菜々美", "美優", "歩", "沙彩", "明香", "夏帆", "優月", "美沙",
        "志保", "理沙", "千香", "優菜", "優希", "恵", "唯奈", "美玲", "穂香", "優",
        "聡太", "龍之介", "晃", "結斗", "颯一郎", "修平", "瑛斗", "竜馬", "一輝", "陽太",
        "正人", "悠翔", "大翔", "颯太郎", "達也", "圭", "悠馬", "祐介", "湊", "隼輝",
        "楓太", "陽介", "啓太", "誠", "航太", "航平", "翔吾", "海斗", "瑛", "紘太",
        "航大", "駿", "祐", "徹", "智也", "諒", "佑介", "元気", "優弥", "悠斗",
        "奏太", "京", "一樹", "光太", "陽向", "竜一", "真", "亮介", "圭祐", "祐樹",
        "駿介", "優人", "健斗", "颯一", "結太", "蒼", "瑛士", "龍生", "瑛介", "瑛汰"
    ]

    last_names = ["佐藤", "鈴木", "高橋", "田中", "渡辺", "伊藤", "山本", "中村", "小林", "加藤",
        "吉田", "山田", "佐々木", "山口", "松本", "井上", "木村", "林", "斎藤", "清水",
        "山崎", "森", "阿部", "池田", "橋本", "山下", "石井", "中島", "前田", "藤田",
        "小川", "後藤", "岡田", "長谷川", "村上", "近藤", "石田", "遠藤", "斉藤", "坂本",
        "福田", "太田", "西村", "藤井", "藤原", "岡本", "三浦", "金子", "中野", "中川",
        "原田", "松田", "竹内", "小野", "田村", "中西", "和田", "石川", "工藤", "森田",
        "上田", "原", "平野", "柴田", "宮崎", "秋山", "桜井", "大野", "杉山", "松井",
        "古川", "中田", "土屋", "高木", "佐野", "尾崎", "黒田", "吉川", "荒木", "木下",
        "大西", "安田", "丸山", "宮本", "田辺", "望月", "大塚", "菊地", "矢野", "菅原",
        "松浦", "森本", "大谷", "久保", "青木", "服部", "永井", "小島", "小松", "古賀",
        "白石", "川口", "本田", "田口", "松岡", "野村", "新井", "渡部", "高田", "岩崎",
        "浅野", "河野", "永田", "川崎", "片山", "川上", "平田", "福島", "荒井", "島田",
        "松田", "八木", "岩田", "増田", "岡", "菊池", "西田", "辻", "福井", "辻",
        "津田", "田島", "佐伯", "大竹", "大村", "村田", "岩本", "松下", "栗原", "安藤",
        "竹田", "村松", "広瀬", "堀", "三宅", "浅井", "松山", "片桐", "杉本", "村山",
        "辻", "栗山", "竹本", "植田", "中沢", "永田", "石橋", "杉浦", "長田", "大和田",
        "浅香", "吉野", "藤村", "柳田", "渡邉", "藤森", "志賀", "南", "横山", "浜田",
        "小倉", "川島", "菅", "高柳", "坂口", "小泉", "大森", "大石", "浜崎", "吉岡",
        "小沢", "中谷", "鶴田", "有馬", "中原", "大杉", "堀田", "熊谷", "梶原", "高山",
        "野田", "大平", "神田", "広田", "岸本", "河本", "上野", "岩井", "小出", "小田",
        "松村", "黒木", "山岡", "有田", "塚本", "川畑", "大城", "浦田", "古田", "大原",
        "池谷", "富田", "奥村", "細川", "南野", "三好", "今村", "川原", "高木", "花田",
        "水谷", "横田", "大場", "樋口", "高島", "清水", "梶", "早川", "角田", "岡村",
        "井口", "須藤", "高橋", "小畑", "志田", "松崎", "岸", "板倉", "新田", "五十嵐",
        "平井", "松田", "柏木", "田原", "安西", "国分", "久保田", "山根", "小西", "梅田",
        "川口", "菅野", "岩渕", "石黒", "杉山", "大石", "南", "吉澤", "寺田", "柳沢",
        "千葉", "古畑", "佐々木", "池谷", "高松", "早坂", "大槻", "坂上", "松永", "工藤",
        "牧野", "長野", "武藤", "南雲", "神谷", "大山", "新田", "篠原", "岩崎", "村岡",
        "竹中", "浜崎", "赤松", "大城", "平松", "水原", "浜口", "安藤", "樋口", "中井",
        "杉原", "立石", "柿沼", "牧", "桜田", "山野", "成瀬", "野崎", "寺田", "大河原",
        "吉澤", "梅原", "浦田", "早乙女", "水原", "水口", "江口", "香取", "山城", "鎌田",
        "山中", "鴨井", "北原", "深澤", "須崎", "望月", "室田", "城戸", "北村", "平川"
    ]


    def gen_names(first_names, last_names):

        rd.shuffle(first_names)
        rd.shuffle(last_names)

        random_names = [f"{last_name} {first_name}" for first_name, last_name in zip(first_names, last_names)]
        return random_names
  
    
    #タイム関数実行
    loop = 0
    while loop < num_students:
        time_gen(loop)
        loop += 1
    #名前リスト関数実行
    names = gen_names(first_names, last_names)#ランダム名前リスト
    students_names = names[0:num_students]  #生徒数分だけリストから取り出し
    #学校名実行
    school_name = gen_place_names(place_names_first,place_names_second,place_names_last)


    #df作成
    grade =  [1,2,3,4,5,6,]
    results = pd.DataFrame(student_times0)

    for i in range(0,num_students):
        exec("results[i] = student_times" +str(i))


    results.columns = students_names
    results.columns.name = "name"
    results.index = grade
    results.index.name = "grade"
    

    st.write("---")
    st.write(school_name+"小学校　50m走の結果！")
    st.write(results.sort_values(1 , axis = 1))
    
    @st.cache_data
    def convert_df(results):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return results.to_csv().encode("shift-jis")

    csv = convert_df(results)

    st.download_button(
        label="出力結果をcsv形式で保存",
        data=csv,
        file_name=school_name+"小学校50m走.csv",
        mime="text/csv",
    )
    #st.write(results.mean(axis=1))