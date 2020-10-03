# https://towardsdatascience.com/understand-and-build-fp-growth-algorithm-in-python-d8b989bab342

class FPTreeNode:
    def __init__(self):
        self.count = 0
        self.parent = None
        self.link = None


class FPGrowthTree:
    def __init__(self, support):
        self.support = support
        self.vocab = {}
        self.vocab_position = {}

        self.dataset = {}
        self.dataset_position = {}
        self.frequent_items = []

        self.fp_tree_root = {}
        self.fp_tree = {}

    def init(self):
        self.dataset = {}
        self.dataset_position = {}
        self.frequent_items = []

        self.fp_tree_root = {}
        self.fp_tree = {}

    def read_vocab(self, file_name):
        with open(file_name, 'r') as fp_in:
            for items in fp_in:
                data = items.split()
                self.vocab[data[0]] = data[1]
        self.vocab = {k: v for k, v in
                      sorted(self.vocab.items(), key=lambda item: item[1])}

        keys = self.vocab.keys()
        for _i, key in enumerate(keys):
            self.vocab_position[key] = _i

    def read_file(self, file_name, selector):
        with open(file_name, 'r') as fp_in:
            for items in fp_in:
                data = items.split()
                if selector == "First":
                    self.compute_frequency(data)
                elif selector == "Second":
                    self.ordered_frequent_items(data)

    def compute_frequency(self, data):
        for datum in data:
            if datum not in self.dataset:
                self.dataset[datum] = 0
            self.dataset[datum] += 1

    def ordered_frequency(self):
        self.dataset = {k: v for k, v in self.dataset.items() if v >= self.support}
        self.dataset = {k: v for k, v in
                        sorted(self.dataset.items(), key=lambda item: item[1], reverse=True)}

        key_list = list(self.dataset.keys())
        index, length = 0, len(key_list)
        dict1 = {}
        while index < length - 1:
            if self.dataset[key_list[index]] == self.dataset[key_list[index + 1]]:
                temp = {key_list[index]: self.vocab_position[key_list[index]]}
                while index < length - 1 and self.dataset[key_list[index]] == self.dataset[key_list[index + 1]]:
                    temp[key_list[index + 1]] = self.vocab_position[key_list[index + 1]]
                    index += 1
                temp = {k: v for k, v in sorted(temp.items(), key=lambda item: item[1])}
                for k, v in temp:
                    dict1[k] = self.dataset[k]
            else:
                dict1[key_list[index]] = self.dataset[key_list[index]]
            index += 1
        self.dataset = dict1

        keys = self.dataset.keys()
        for _i, key in enumerate(keys):
            self.dataset_position[key] = _i

    def ordered_frequent_items(self, data):
        temp_pos = {}
        for datum in data:
            if datum in self.dataset:
                temp_pos[datum] = self.dataset_position[datum]
        if len(temp_pos) > 0:
            temp_pos = {k: v for k, v in sorted(temp_pos.items(), key=lambda item: item[1])}
            temp = []
            for k, v in temp_pos.items():
                temp.append(k)
            self.frequent_items.append(temp)

    def add_to_fp_tree(self, item) -> FPTreeNode:
        if item not in self.fp_tree:
            self.fp_tree[item] = FPTreeNode()
        root = self.fp_tree[item]
        while root.link is not None:
            root = root.link
        root.link = FPTreeNode()
        root = root.link
        root.count += 1

        return root

    def construct_fp_tree(self):
        for item in self.frequent_items:
            for _i, _item in enumerate(item):
                if _i == 0:
                    if _item not in self.fp_tree_root:
                        root = self.add_to_fp_tree(_item)
                        self.fp_tree_root[_item] = root
                    else:
                        self.fp_tree_root[_item].count += 1
                else:
                    


if __name__ == '__main__':
    obj = FPGrowthTree(400)
    obj.read_vocab("vocab.txt")
    for i in range(1):
        obj.init()

        obj.read_file("topic-{}.txt".format(i), "First")
        obj.ordered_frequency()

        obj.read_file("topic-{}.txt".format(i), "Second")
        obj.construct_fp_tree()
