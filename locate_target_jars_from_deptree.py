import json


def dfs(tree, target, path=[]):
    """
    Perform a depth-first search in a tree to find the target node.

    :param tree: The tree to search, represented as a dictionary.
    :param target: The target node value to find.
    :param path: The path taken to reach the current node.
    :return: The path from the root to the target node, or None if not found.
    """
    if isinstance(tree, dict):
        for dep in tree['dependencies']:
            # Append the current node to the path
            new_path = path + [dep['group_id']+'|'+dep['artifact_id']+'|'+dep['version']]
            if dep['group_id']+'|'+dep['artifact_id']+'|'+dep['version'] == target:
                return new_path
            result = dfs(dep, target, new_path)
            if result:
                return result

    return None

with open('scantist-meta-engine-input_78531-dependency-tree.json') as f:
    tree = json.load(f)['projects'][0]

    
# The format is 'group|artifact|version'
path = dfs({'dependencies':[tree]}, "idna|idna|3.4")
print(f"Path to the target: {path}")
# Then these GAVs could be used to extract call graphs for reachability analysis