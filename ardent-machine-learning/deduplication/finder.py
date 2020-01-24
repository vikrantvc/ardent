import pandas as pd
from itertools import combinations
from elasticsearch import Elasticsearch

def createIndex(data):
    es = Elasticsearch()
    for idx in range(data.shape[0]):
        es.index(index="file_dupes", body=data.iloc[idx].to_json())
    return

def metaDuplicates(data):
    combi = data.copy()
    combi["Name"] = combi["Name"].str[:5]
    final_df = pd.DataFrame(columns=["File_Name", "Count", "Duplicates", "Chance"])

    # Identifying highest chances of duplications
    for idx, grp in combi.groupby(by=['Name', 'DateModified', 'Path', 'Size']):
        if grp.shape[0] > 1:
            temp = {"File_Name" : data['Name'][grp.index[0]], "Count" : grp.shape[0], \
                    "Duplicates" : str(grp["Id"].to_list()), "Chance": "Highest"}
            final_df = final_df.append(temp, ignore_index=True)
            combi.drop(index = grp.index, inplace = True)
            # break

    # Identifying higher chances of duplications
    for col_names in combinations(['DateModified', 'Path', 'Size'], 2):
        col_names = list(col_names)
        col_names.append('Name')
        for idx, grp in combi.groupby(by=col_names):
            if grp.shape[0] > 1:
                temp = {"File_Name" : data['Name'][grp.index[0]], "Count" : grp.shape[0], \
                        "Duplicates" : str(grp["Id"].to_list()), "Chance": "Higher"}
                final_df = final_df.append(temp, ignore_index=True)
                combi.drop(index = grp.index, inplace = True)
        #         break
        # break

    # Identifying medium chances of duplications
    for col_names in combinations(['DateModified', 'Path', 'Size'], 1):
        col_names = list(col_names)
        col_names.append('Name')
        for idx, grp in combi.groupby(by=col_names):
            if grp.shape[0] > 1:
                temp = {"File_Name" : data['Name'][grp.index[0]], "Count" : grp.shape[0], \
                        "Duplicates" : str(grp["Id"].to_list()), "Chance": "Medium"}
                final_df = final_df.append(temp, ignore_index=True)
                combi.drop(index = grp.index, inplace = True)
        #         break
        # break

    # Identifying lower chances of duplications
    for idx, grp in combi.groupby(by=['Name']):
        if grp.shape[0] > 1:
            temp = {"File_Name" : data['Name'][grp.index[0]], "Count" : grp.shape[0], \
                    "Duplicates" : str(grp["Id"].to_list()), "Chance": "Lower"}
            final_df = final_df.append(temp, ignore_index=True)
            combi.drop(index = grp.index, inplace = True)
            # break

    createIndex(final_df)
    return
