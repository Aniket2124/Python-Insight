# JSON array
import json
json_val = [{"name": "ani", "age": 29, "city": "York",
             "actor": {"id": 68180173, "login": "aaa"}},
            {"name": "abi", "age": 28, "city": "New York",
             "actor": {"id": 68180174, "login": "zzz"}}]
parsed_json_val = json.dumps(json_val)


print(parsed_json_val)
print("\n")
# parse x:
y = json.loads(parsed_json_val)
print(y[0]["name"])
print(y[1]["actor"]["login"])
