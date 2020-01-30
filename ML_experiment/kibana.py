import os
y='curl -X POST "localhost:5601/s/test/api/saved_objects/_import" -H "kbn-xsrf: true" --form file=@/home/vikrant/Downloads/export_1.ndjson'
x=os.system(y)
print(x)
