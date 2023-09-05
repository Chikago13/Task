from random import randint

def list_dict(lenlist: int):
    d = []
    list_name = ['Alex', 'Tim', 'Alen', 'Olga', 'Nik', 'Svet']
    for i in range(lenlist):
        d.append({'name':f'{list_name[randint(0, len(list_name)-1)]}', 'number': f'{randint(50, 100)}'})
    return d

def new_dict(list_val, k):
    if k.isdigit():
        return list(filter(lambda x:  x['number']==k, list_val))
    else:
        return list(filter(lambda x:  x['name']==k, list_val))

res = list_dict(10)
print(res)
print(new_dict(res, '92'))

