import json
import pandas as pd

buffer = 0
# def read_parse(file):
#     all_data = None
#     list_json_data = []

#     with open(file, "r") as file:
#         all_data = file.readlines()

#     for line in all_data:
#         list_json_data.append(json.loads(line))

#     parsed_df = pd.DataFrame(list_json_data)
#     # df.set_index("remote_ip", inplace=True)
    
#     return parsed_df

def read_parse(file_path="./inputs/nginx_json_logs.txt"):
    try:
        with open(file_path, "r") as file:
            list_json_data = [json.loads(line) for line in file]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return pd.DataFrame()
    return pd.DataFrame(list_json_data)


def count_frequency(df, col):
    return df[col].value_counts()

#reading parsing
file = "./inputs/nginx_json_logs.txt"
buffer = read_parse(file)
print(buffer.head())

# print(len(buffer))

#counting the frequency of response codes
counts = count_frequency((buffer if(len(buffer)) else read_parse(file)), 'response')
print(counts)

# top IP addresses by request frequency
freq = count_frequency((buffer if(len(buffer)) else read_parse(file)), 'remote_ip')
print(freq)