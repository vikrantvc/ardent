import os
# if you have diffrent speces(user area) then mention in command url here space is "/s/test"
#while exporting data export dashboard along with visualisation,controls,discovers & tables
#the below code will send the data in kibana which we export in export.ndjson file
command='curl -X POST "localhost:5601/s/test/api/saved_objects/_import" -H "kbn-xsrf: true" --form file=@/home/vikrant/Downloads/export_1.ndjson'
results=os.system(command)
print(results)
