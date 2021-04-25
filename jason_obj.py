# JSON object
import json
json_val = '{"name": "ani", "age": 29, "city": "York", "actor": "aaa"}'
#validated_json_val = json.dumps(json_val)
# print(validated_json_val)
print("\n")
# parse x:
parsed_json_val = json.loads(json_val)
print(parsed_json_val["name"])
print(parsed_json_val["actor"])
