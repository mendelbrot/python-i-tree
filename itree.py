

class ITree:
    def __init__(self):
        self.itree = [{}]
        self.terminals = []
        self.last_level_terminal = False

    def build(self, links = None, terminals = None, continue_level = False):
        if not continue_level:
            self.itree.append({})
        prev_level = self.itree[-2]
        level = self.itree[-1]
        for nodes, prev_nodes in links + terminals:
            for n in nodes:
                for n1 in prev_nodes:
                    k1, v1 = prev_level[n1]
                    try:
                        k, v = level[n]
                        level[n] = (k + k1, v + [n1])
                    except:
                        level[n] = (k1, [n1])

        for nodes, _ in terminals:
            self.terminals += nodes

    def prune(self, end_nodes):
        pass

    def len(self):
        if self.last_level_terminal:
            total = 0
            for k, _ in self.itree[-1].values():
                total += k
            return total
        
        total = 0
        for level, node in self.terminals:
            k, _ = self.itree[level][node]
            total += k
        return total

    def __getitem__(self, key):
        pass
    
    