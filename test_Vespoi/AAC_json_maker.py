import re
import json


def preprocessing_text_data(file_path): #txt 파일 텍스트 정리 /로 구분
    file = open(file_path, encoding='UTF8')

    data = file.read()

    split_data = data.split('/')

    text_data = []
    for i in split_data:
        new_str = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s0-9]", "", i)
        new_str = new_str.replace(" ", "")
        #print(new_str)
        text_data.append(new_str)
    
    return list(set(text_data))

def preprocessing_text_data_with_space(file_path): #txt 파일 텍스트 정리 /로 구분
    file = open(file_path, encoding='UTF8')

    data = file.read()

    split_data = data.split('/')

    text_data = []
    for i in split_data:
        new_str = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s0-9]", "", i)
        #print(new_str)
        text_data.append(new_str)
    
    return list(set(text_data))

def preprocessing_text_data_dot(file_path): #txt 파일 텍스트 정리 ,으로 구분
    file = open(file_path, encoding='UTF8')

    data = file.read()

    split_data = data.split(',')

    text_data = []
    for i in split_data:
        new_str = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s0-9]", "", i)
        new_str = new_str.replace(" ", "")
        #print(new_str)
        text_data.append(new_str)
    
    return list(set(text_data))

def preprocessing_text_data_ai(file_path): #ai txt 파일에 사용
    file = open(file_path, encoding='UTF8')

    data = file.read()

    split_data = data.split(',')

    text_data = []
    for i in split_data:
        new_str = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s]", "", i)
        new_str = new_str.replace(" ", "")
        #print(new_str)
        text_data.append(new_str)
    
    return list(set(text_data))

def preprocessing_text_data_category(file_path): #카테고리 txt 파일에 사용
    file = open(file_path, encoding='UTF8')

    data = file.read()

    split_data = data.split('/')

    text_data = []
    for i in split_data:
        new_str = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s0-9]", "", i)
        new_str = new_str.replace(" ", "")
        #print(new_str)
        text_data.append(new_str+":")
    
    return list(set(text_data))

def preprocessing_text_data_urgency(file_path): #긴급 txt 파일에 사용
    file = open(file_path, encoding='UTF8')

    data = file.read()

    split_data = data.split(',')

    text_data = []
    for i in split_data:
        new_str = re.sub(r"[^\uAC00-\uD7A3a-zA-Z\s0-9/]", "", i)
        #new_str = new_str.replace(" ", "")
        #print(new_str)
        text_data.append(new_str)
    
    return list(set(text_data))

def init_dict(dict_aac, path):
    location_label="10" #장소
    index = 0
    for i in preprocessing_text_data(path):
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(location_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_location(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - 장소
    location_label="10" #장소
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "10":
            #print(str(i["id"])[:2])
            index = int(str(i["id"])[2:])
            #print(index)

    aac_data = preprocessing_text_data(PATH)
    for i in aac_data:
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(location_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_category(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - 장소 아래 카테고리
    location_label="20" #카테고리
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "20":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data_category(PATH)
    for i in aac_data:
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(location_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_flow(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - 장소 아래 대화형
    location_label="30" #순서형
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "30":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data(PATH)
    for i in aac_data:
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(location_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_AAC(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - 카테고리 아래 AAC
    aac_label = "40" #기본 AAC
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "40":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data(PATH)
    for i in aac_data:
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(aac_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_urgency(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - 긴급 카테고리
    urgency_label = "50" #긴급 카테고리
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "50":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data_urgency(PATH)
    for i in aac_data:  
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(urgency_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_urgency_aac(dict_urgency_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - 긴급 카테고리
    urgency_label = "60" #긴급 카테고리
    index = 0
    for i in dict_urgency_aac["AAC"]:
        if str(i["id"])[:2] == "60":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data_with_space(PATH)
    for i in aac_data:  
        index = index + 1
        dict_urgency_aac["AAC"].append({
            "id": int(urgency_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_txt_dict_ai_response(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - AI 응답
    ai_res_label = "80" #AI response 카테고리
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "80":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data_with_space(PATH)
    for i in aac_data:  
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(ai_res_label + str(index)),
            "node" : [],
            "name" : i
        })

def add_list_dict_ai_response(dict_aac,dict_ai_res): #텍스트 파일로 딕셔너리 만들기 - AI 응답
    ai_res_label = "80" #AI response 카테고리
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "80":
            index = int(str(i["id"])[2:])

    for i in dict_ai_res['intence']:  
        for j in i['response']:
            index = index + 1
            dict_aac["AAC"].append({
                "id": int(ai_res_label + str(index)),
                "node" : [],
                "name" : j
            })

def add_txt_dict_ai(dict_aac,PATH): #텍스트 파일로 딕셔너리 만들기 - AI 카테고리
    ai_label = "90" #AI 카테고리
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "90":
            index = int(str(i["id"])[2:])

    aac_data = preprocessing_text_data_ai(PATH)
    for i in aac_data:  
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(ai_label + str(index)),
            "node" : [],
            "name" : i
        })
        #print(i)
    #print(dict_data)

def add_list_dict_ai(dict_aac,dict_ai_res): #텍스트 파일로 딕셔너리 만들기 - AI 카테고리
    ai_label = "90" #AI 카테고리
    index = 0
    for i in dict_aac["AAC"]:
        if str(i["id"])[:2] == "90":
            index = int(str(i["id"])[2:])

    for i in dict_ai_res['intence']:  
        index = index + 1
        dict_aac["AAC"].append({
            "id": int(ai_label + str(index)),
            "node" : [],
            "name" : i['tag']
        })
        #print(i)
    #print(dict_data)

def id_finder(dict_data, name): #이름(name)으로 id 찾기
    for i in dict_data["AAC"]:
        if(i["name"]==name):
            return i["id"]

def id_finder_multi(dict_data, name_list): #이름(name) 목록(list) 으로 id 찾기
    id_list = []

    for i in dict_data["AAC"]:
        for j in name_list:
            if(i["name"]==j):
                id_list.append(i["id"])
    return id_list

def node_add_single(dict_data, id, node): #node에 숫자(id) 하나(node <- int) 추가
    for i in dict_data["AAC"]:
        if(i["id"]==id):
            i["node"].append(node)

def node_add_multi(dict_data, id, node_list): #node 에 숫자(id) 여러개(node <- list(int)) 추가
    for i in dict_data["AAC"]:
        if(i["id"]==id):
            for j in node_list:
                i["node"].append(j)

def add_multi_to_multi(dict_data, list_where, node_list): #list_where: 추가 할 곳(ex 이것, 저것) , node_list 추가할 노드(ex 있습니다, 없습니다 )
    for i in list_where:
        id = id_finder(dict_data, i)
        node_add_multi(dict_data, id, node_list)

def add_single_to_multi(dict_data, list_where, name_single): #list_where: 추가 할 곳(ex 이것, 저것) , node_list 추가할 노드(ex 주세요 )
    for i in list_where:
        id = id_finder(dict_data, i)
        node_add_single(dict_data, id, name_single)

def dupe_node_remover(dict_data):
    for i in dict_data["AAC"]:
        i['node'] = list(set(i['node']))
    return dict_data

def open_json(PATH): #json 불러오기
    with open (PATH, "r",encoding='utf-8') as f:
        dict_data = json.load(f)
    return dict_data

def make_json(dict_data,path): #json 저장
    json_data = json.dumps(dict_data, indent="\t", ensure_ascii=False)
    with open(path.split('/')[-1], 'w', encoding='utf-8') as f:
        f.write(json_data)

def make_json_urgency(dict_data): #json 저장
    json_data = json.dumps(dict_data, indent="\t", ensure_ascii=False)
    with open('json_data_urgency.json', 'w', encoding='euc-kr') as f:
        f.write(json_data)



def main():
    path = 'C:/Users/for/Study/ComPass/Back_Test/Server_Master/test_Vespoi/json/json_data_230924.json'
    with open (path, "r",encoding='euc-kr') as f:
        dict_aac = json.load(f)
    dict_ai_res = open_json('C:/Users/for/Study/ComPass/Back_Test/Server_Master/test_Vespoi/json/selected_data3.json')

    add_list_dict_ai_response(dict_aac,dict_ai_res)
    add_list_dict_ai(dict_aac,dict_ai_res)

    index_8 = 1
    index_9 = 1
    label_res = '80'
    label_cat = '90'

    for i in dict_ai_res['intence']:
        label_cat = label_cat + str(index_9)
        for i in range(len(i['response'])):
            label_res = label_res + str(index_8)
            node_add_single(dict_aac, int(label_cat) , int(label_res))
            index_8 = index_8 + 1
            label_res = '80'
        index_9 = index_9 + 1
        label_cat = '90'
        


    make_json(dict_aac,path)



if __name__ == "__main__":
    main()

