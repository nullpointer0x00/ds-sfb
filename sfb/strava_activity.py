def read_cached_files(self, path):
    cache_files = [f for f in listdir(path) if isfile(join(path, f))]
    json_objects = []
    for file_name in cache_files:
        file = open(join(path, file_name), "r")
        json_str = ""
        for line in file.readlines():
            json_str += line
        json_objects.append(json.loads(json_str))
    return json_objects