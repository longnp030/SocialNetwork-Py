from os import listdir
import ast

def data(folder):
    sep = '/'

    data = {}
    data_if_no_topic = []

    for file in listdir(folder):
        with open(folder + sep + file, 'r', encoding='utf-8') as f:
            raw_data = ast.literal_eval(f.read())
            if raw_data['content'] == '':
                continue

            topics = raw_data['categories']
            text = raw_data['title'] + ' ' + raw_data['content']
            if len(topics) == 0:
                data_if_no_topic.append(text)
            else:
                topic = topics[0]
                if not topic in data:
                    data[topic] = [text]
                else:
                    data[topic].append(text)

    with open('topic/data/data.txt', 'w+') as f:
        print(data, file=f)
    with open('topic/data/data_no_topic.txt', 'w+') as f:
        print(data_if_no_topic, file=f)
