# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.item_Itr = iter(items)
        self.uniqlst = set()
        self.ignore_case = kwargs.get('ignore_case')

    def uniq(self, item):
        if self.ignore_case:
            item =str(item)
            item = item.lower()
            len1 = len(self.uniqlst)
            self.uniqlst.add(item)
            if len1 == len(self.uniqlst):
                return True
            else:
                return False
        else:
            len1 = len(self.uniqlst)
            self.uniqlst.add(item)
            if len1 == len(self.uniqlst):
                return True
            else:
                return False

    def __next__(self):
        val = next(self.item_Itr)
        while self.uniq(val):
            val = next(self.item_Itr)
        return val

    def __iter__(self):
        return self


