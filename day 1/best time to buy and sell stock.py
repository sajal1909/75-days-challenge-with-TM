class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string_no = ''

        for x in digits[0:]:
            string_no = string_no + str(x)

        string_no = int(string_no) + 1
        string_no = str(string_no)

        final_ans = []
        for x in string_no:
            final_ans.append(x)

        return final_ans