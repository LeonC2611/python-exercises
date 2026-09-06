import json

with open("budget_preseason.json") as file:
    preseason_read = file.read()
    merge_dict = json.loads(preseason_read)

with open("budget_update.json") as f:
    update_read = f.read()
    update_dict = json.loads(update_read)

for key in update_dict:
    if (
        key in merge_dict
        and isinstance(merge_dict[key], dict)
        and isinstance(update_dict[key], dict)
    ):
        if key == "spending":
            for item in update_dict[key]:
                if item in merge_dict[key]:
                    merge_dict[key][item] += update_dict[key][item]
                else:
                    merge_dict[key][item] = update_dict[key][item]
    else:
        merge_dict[key] = update_dict[key]

with open("merge_budget.json", "w") as merge_file:
    json.dump(merge_dict, merge_file)
