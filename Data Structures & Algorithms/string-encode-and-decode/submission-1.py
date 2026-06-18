class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'None'
        return ','.join([elem.replace(',', 'comma') for elem in strs])

    def decode(self, s: str) -> List[str]:
        if s == 'None':
            return []
        return [elem.replace('comma', ',') for elem in s.split(',')]
