from collections import deque

class ITree:
    def __init__(self):
        self.itree = [{}]
        self.terminals = []
        self.LLT = False

    def build(self, links = None, t_links = None, continue_level = False):
        if not continue_level:
            self.itree.append({})
        prev_level = self.itree[-2]
        level = self.itree[-1]
        for nodes, prev_nodes in links + t_links:
            for n in nodes:
                for n1 in prev_nodes:
                    k1, v1 = prev_level[n1]
                    try:
                        k, v = level[n]
                        level[n] = (k + k1, v + [n1])
                    except:
                        level[n] = (k1, [n1])

        li = len(self.itree) - 1
        for nodes, _ in t_links:
            for n in nodes:
                self.terminals += (li, n)
    
    def __recursive_prune(self, index, node):
        prev_level = self.itree[index - 1]
        level = self.itree[index]
        v = level[node][1]
        for n1 in v:
            prune_n1 = True
            v1 = prev_level[n1][1]
            for n in v1:
                vn = level[n][1]:
                if len(vn) > 1:
                    prune_n1 = False
                    break
            if prune_n1:
                pass

    def prune(self, end_nodes):
        li = len(self.itree) - 1
        for n in end_nodes:
            self.__recursive_prune(li, n)

    def len(self):
        if self.LLT:
            total = 0
            for k, _ in self.itree[-1].values():
                total += k
            return total
        
        total = 0
        for li, n in self.terminals:
            k, _ = self.itree[li][n]
            total += k
        return total
    
    def chain_generator():
        if self.LLT:
            li = len(self.itree) - 1
            terminal_nodes = [(li, n) for n in self.itree[-1].keys()]
        else:
            terminal_nodes = self.terminals
        
        for li, n in terminal_nodes:
            first_chain = deque([n])
            for i in range(li, -1, -1)
                node = first_chain[0]
                n1 = self.itree[i][node][1][0]
                first_chain.appendleft[n1]
            
            

            

