import json
def parse_input(infile):
    #content = []
    #
    #for line in open(infile):
    #    line = line.replace("{","")
    #    line = line.replace("}","")
    #    content.append(line)
    #    print(line)
    content = json.load(open(infile))
    parsed_content = {}
    parsed_content["database_name"]=content["database_name"]
    schema = []
    parsed_content["tables"] = []
    for table in content["tables"]:
        for column in table["schema"]:
            schema.append((column["column_name"],column["column_type"]))
        table_info = {"tablename":table["tablename"],"schema": schema,"data":table["data"]}
        parsed_content["tables"].append(table_info)
    print(parsed_content)
    print(parsed_content["database_name"])
    return parsed_content

