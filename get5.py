import copy
def pretty_print(datas, num, prin):
    error_type = []
    if datas == [[]]:
        print('\t' * num, '[]')
    elif type(datas) == list:
        if prin:
            print('\t' * (num), '[')
        for data in datas:
            if data == []:
                continue
            elif type(data) == list or type(data) == dict:
                error_type += pretty_print(data, num + 1, True)
            else:
                print('\t' * (num), data)
        if prin:
            print('\t' * (num), ']')
    elif type(datas) == dict:
        print('\t' * (num), '{')
        for k in datas:
            if type(datas[k]) == list or type(datas[k]) == dict:
                print('\t' * num, k, ':')
                error_type += pretty_print(datas[k], num + 1, False)
            else:
                if datas[k] == "error type found":
                    error_type.append(k)
                print('\t' * (num), k, ':\n' + '\t' * (num + 1), datas[k], '\n')
        print('\t' * (num), '}')
    return error_type


all_things = []
all_values = {}


def getthem(datas, key_name):
    global all_things
    if type(datas) == dict:

        for key in datas:
            for item in datas[key]:
                getthem(item, key_name + '+' + str(key))
    elif type(datas) == list:
        if Ifpurelist(datas):
            if key_name in all_things:
                if datas not in all_values[key_name]:
                    all_values[key_name] += [datas]
                return
            else:
                all_things += [key_name]
                all_values[key_name] = [datas]
                return
        else:
            for data in datas:
                getthem(data, key_name + '+[]')
    else:
        if key_name in all_things:
            if datas not in all_values[key_name]:
                all_values[key_name] += [datas]
            return
        else:
            all_things += [key_name]
            all_values[key_name] = [datas]
            return


final_dict = {}


def merger_dict(dic, f):
    f_dict=copy.copy(f)
    if type(f_dict) == dict:
        if type(dic) == dict:
            key = list(dic.keys())[0]
            if key not in f_dict.keys():
                if not Ifpurelist(dic[key]):
                    f_dict[key] = merger_dict(dic[key][0],{})
                else:
                    f_dict[key] = dic[key]
                return f_dict
            else:
                f_dict[key] = merger_dict(dic[key][0], f_dict[key])
                return f_dict
        else:
            if f_dict=={} and not Ifpurelist(dic):
                return [merger_dict(dic[0],f_dict)]
            elif f_dict=={}:
                return dic
            return [f_dict] + [dic]
    elif type(f_dict) == list:
        if f_dict[0] != 'error type found':
            if type(dic) == list:
                if Ifpurelist(dic):
                    if (dic==[] and dic not in f_dict) or dic[0] not in f_dict:
                        return f_dict + [dic]
                    return f_dict
                elif type(dic[0]) == dict:
                    change = False
                    for num in range(len(f_dict)):
                        if type(f_dict[num]) == dict:
                            if list(dic[0].keys())[0] in f_dict[num].keys():
                                change = True
                                return [merger_dict(dic[0], f_dict[0])]
                            else:
                                f_dict[num][list(dic[0].keys())[0]]=merger_dict(dic[0][list(dic[0].keys())[0]],{})
                                return f_dict
            else:
                return f_dict + [dic]
        else:
            if type(dic) == list or type(dic) == dict:
                change = False
                for index in range(len(f_dict)):
                    if type(dic) == type(f_dict[index]):
                        f_dict[index] = merger_dict(dic, f_dict[index])
                        change = True
                if change:
                    f_dict += [dic]
                return f_dict
            else:
                if dic not in f_dict:
                    f_dict += [dic]
                    return f_dict


def creat_dict(datas, value):
    if datas == []:
        return value
    else:
        if datas[0] == '[]':
            return [creat_dict(datas[1:], value)]
        else:
            diction = {}
            if len(datas) == 1:
                diction[datas[0]] = creat_dict(datas[1:], value)
            else:
                diction[datas[0]] = [creat_dict(datas[1:], value)]
            return diction


def Ifpurelist(datas):
    for data in datas:
        if type(data) == list:
            result = Ifpurelist(data)
            if not result:
                return False
            else:
                continue
        elif type(data) == dict:
            return False
    return True


def compress(scheme, key, data):
    if key in scheme.keys():
        if scheme[key][0] == "error type found":
            return scheme[key]
        else:
            return scheme[key] + [data]
    else:
        return [data]


def isversion(keyname):
    if '_' not in keyname:
        return False
    keys = keyname.split('_')
    for key in keys:
        if key.isdigit():
            return True
    return False


def getType(data):
    scheme = {}
    if type(data) == dict:
        for k in data:
            if type(data[k]) == dict:

                if k.isdigit():

                    scheme[type(1)] = compress(scheme, type(1), getType(data[k]))
                elif isversion(k):
                    scheme['version'] = compress(scheme, 'version', getType(data[k]))
                else:

                    scheme[k] = compress(scheme, k, getType(data[k]))


            elif type(data[k]) == list:
                type_list = []
                if data[k] != []:
                    for small_key in data[k]:
                        if type(small_key) == list:

                            type_list += getType(small_key)
                        elif type(small_key) == dict:
                            type_list.append(getType(small_key))
                        else:
                            if not (type(small_key) in type_list):
                                type_list.append(type(small_key))

                if k.isdigit():

                    scheme[type(1)] = compress(scheme, type(1), type_list)
                elif isversion(k):
                    scheme['version'] = compress(scheme, 'version', type_list)
                else:

                    scheme[k] = compress(scheme, k, type_list)

            else:

                if k.isdigit():

                    scheme[type(1)] = compress(scheme, type(1), type(data[k]))
                elif isversion(k):
                    scheme['version'] = compress(scheme, 'version', type(data[k]))
                else:

                    scheme[k] = compress(scheme, k, type(data[k]))
        return scheme

    elif type(data) == list:
        temp_list = []
        sub_scheme = {}
        sub_list = []
        for k in data:

            if type(k) == dict:
                sub_scheme = getType(k)
            elif type(k) == list:
                type_list = []
                if k != []:
                    for small_key in k:
                        if (type(small_key) == dict or type(small_key) == list):

                            sub_scheme = getType(small_key)
                        else:
                            if not (type(small_key) in type_list):
                                type_list.append(type(small_key))

                sub_list.append(type_list)

            else:
                sub_list.append(type(k))
            if sub_scheme != {}:
                temp_list.append(copy.deepcopy(sub_scheme))
        if sub_list != []:
            temp_list.append(sub_list)
        return temp_list

import pymongo

connection=pymongo.MongoClient()
database=connection['new_adn']
collection=database.tabs
datas=collection.find()

d=[]
for data in datas:
    d+=[data]

result=getType(d)
getthem(result,'')

dics=[]
for thing in all_things:
    temp=thing[4:].split('+')
    dic=creat_dict(temp,all_values[thing])
    dics+=[dic]
f=open('c.txt','w')
f.write(str(dics))
f.close()
b=len(dics)
i=0
for dic in dics:
    final_dict=merger_dict(dic,final_dict)
pretty_print(final_dict,0,False)
print(final_dict)

