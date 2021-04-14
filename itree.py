class ITree:
    def __init__(self):
        self.links = [{}]
        self.counts = [{}]

    # input: a list of node identifiers
    # starts the itree and then starts a new level
    def start(self, nodes):
        for node in nodes:
            self.links[0][node] = []
            self.counts[0][node] = 1
        
        # start next level
        self.links.append({})
        self.counts.append({})

    # input:
    # a list, each element is a tuple: a previous_node - node link.
    # [...(prev_node, node)]
    def add(self, new_links):
        prev_links = self.links[-2]
        links = self.links[-1]
        prev_counts = self.counts[-2]
        counts = self.counts[-1]
        for n1, n in new_links:
            k1 = prev_counts[n1]
            try:
                links[n] += [n1]
                counts[n] += k1
            except:
                links[n] = [n1]
                counts[n] = k1
    
    # this level is finished.  prune and start the next level.
    def next(self):
        # prune
        level = len(self.links) - 1
        while level > 0:
            nodes_that_continued = set().union(*self.links[level].values())
            prev_links = self.links[level - 1]
            prev_counts = self.counts[level - 1]
            nodes_to_prune = set(prev_links) - nodes_that_continued
            if not nodes_to_prune:
                break
            for n in nodes_to_prune:
                del prev_links[n]
                del prev_counts[n]
            level -= 1
        
        # start next level
        self.links.append({})
        self.counts.append({})
    
    # returns the total number of paths in the itree
    def len(self):
        return sum(self.counts[-1].values())