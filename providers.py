import json

class GithubProvider(object):

  def __init__(self):
    f = open('github_data.txt','rb')
    f.readline()
    f.readline()
    self.data = json.loads(f.readline())

  def get_nodes(self):
    return self.data.keys()

  def get_edges(self, node, otherNodes):
    result = []
    for n2 in otherNodes:
      value = self.data[node["text"]].get(n2["text"])
      if value is None:
        value = 0
      value = 0.75 + 0.25 * (float(value) / 10)
      result.append(value)

    return result

  def get_related_nodes(self, nodes):
    newNodesSet = set()
    for node in nodes:
      relatedNodes = self.data[node['text']].keys()
      i = 0
      while i < len(relatedNodes):
        relatedNode = relatedNodes[i]
        newNodesSet.add(relatedNode)
        i += 1
    return [{"text": node} for node in newNodesSet]