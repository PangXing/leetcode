# coding:utf-8

class Solution(object):
    def removeSingle(self, boxes):
        single_dict = dict()
        val = 0
        for i in range(len(boxes)):
            tmp = boxes[i]
            if tmp in single_dict:
                single_dict[tmp] = -1
            else:
                single_dict[tmp] = i
        for i in single_dict.values():
            if i > -1:
                val += 1
                boxes.pop(index=i)
        return val

    def removeContinue(self, boxes):
        def _get_con_dict(b):
            con_dict = dict()
            for i in range(len(b)):
                tmp = b[i]
                con_dict.setdefault(tmp, list())
                con_dict[tmp].append(i)
            return con_dict

        def _get_con_score(boxes, con_dict):
            score = 0
            for v in con_dict.values():
                cnt = len(v)
                cnt_tmp = max(v)- min(v) + 1
                if cnt == cnt_tmp:
                    score += (cnt * cnt)
                    for i in v:
                        boxes.pop(index=i)
            return score

        def _get_max_item(con_dict):
            max_cnt = 0
            max_item = 0
            for k, v in con_dict.items():
                if len(v) > max_cnt:
                    max_item = k
                    max_cnt = len(v)
            return max_item

        res = 0
        con_dict = _get_con_dict(boxes)
        score = _get_con_score(con_dict)
        while score > 0:
            res += score
            con_dict = _get_con_dict(boxes)
            score = _get_con_score(con_dict)
        max_item = _get_max_item(con_dict)
        return res, max_item


    def removeBoxes(self, boxes):
        if not boxes:
            return 0
        res = self.removeSingle(boxes)
        score, max_item = self.removeContinue(boxes)
        res += score
        if boxes:
            pass



