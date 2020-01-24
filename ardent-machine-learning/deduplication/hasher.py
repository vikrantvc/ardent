import hashlib

def metaHashing(data):
    hash_list = []
    data["MD5HASH"] = ""
    temp = data[["Name", "Size", "DateModified"]].astype('str')
    for idx, row in temp.iterrows():
        hasher = hashlib.md5()
        hasher.update(row["Name"].encode('utf-8'))
        hasher.update(row["Size"].encode('utf-8'))
        hasher.update(row["DateModified"].encode('utf-8'))
        md5hash = hasher.hexdigest()
        hash_list.append(md5hash)
    data["MD5HASH"] = hash_list
    return data
