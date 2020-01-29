import re
class Helpers:
    @staticmethod
    def remove_special(s):
        if type(s) is str:
            l = ["\\", '"', "'", "\0", ]
            for i in l:
                if i in s:
                    s = s.replace(i, "")
            return s
        if type(s) is dict:
            tempDict = {}
            for key, value in s.items():
                k = Helpers.remove_special(key)
                v = Helpers.remove_special(value)
                tempDict[k] = v
            return tempDict
        return s