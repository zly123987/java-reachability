import csv

import os
import csv
from collections import deque

def load_data_from_csv(dir):
    adjacency_list = {}
    for file in os.listdir(dir):
        if file.endswith('.csv') and not file.endswith('_NameList.csv'):
            with open(os.path.join(dir, file), 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] not in adjacency_list:
                        adjacency_list[row[0]] = [row[1]]
                    else:
                        adjacency_list[row[0]].append(row[1])
    return adjacency_list


def find_path(adjacency_list, start, end):
    if start not in adjacency_list:
        print(f"{start} cannot reach any other nodes.")
        return None

    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]
        if vertex == end:
            return path
        elif vertex not in visited:
            visited.add(vertex)
            for neighbor in adjacency_list.get(vertex, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    # print(f"No path from {start} to {end} could be found.")
    return None


def find_reachable_path(start, end, dir):
    adjacency_list = load_data_from_csv(dir)

    path = find_path(adjacency_list, start, end)

    if path:
        print("The path from entry to exit is: ", ' -> '.join(path))
    else:
        print(f"No path from {start} to {end} could be found.")
    return path

if __name__=='__main__':
    # Usage: java -jar ../libs/callGraphGeneration.jar path/to/target/jar <nameOfGAV>. This will generate a <nameOfGAV>.csv consisting of all call edges with a format as "<src>","<dst>". A <nameOfGAV>_Namelist.csv containing all methods in the target jar.
    os.system('java -jar libs/callGraphGeneration.jar jars/hazelcast-3.6.2.jar hazelcast-3.6.2')
    os.system('java -jar libs/callGraphGeneration.jar reachability_test/target/reachability_test-1.0-SNAPSHOT.jar reachability_test')
    # https://github.com/CGCL-codes/MavenEcoSysResearch/blob/main/analyseJar/example/callstack/CVE-2016-10750%40com.hazelcast%3Ahazelcast%3A3.6.2
    find_reachable_path('ReachabilityTest:main(java.lang.String[])', 'com.hazelcast.config.AbstractXmlConfigHelper:parseSerialization(org.w3c.dom.Node)', 'graph/')
    find_reachable_path('ReachabilityTest$Test:<init>()', 'com.hazelcast.config.AbstractXmlConfigHelper:parseSerialization(org.w3c.dom.Node)', 'graph/')