class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        sorted_citations = sorted(citations)
        n = len(citations)
        for i in range(n):
            if sorted_citations[i] >= n - i:
                return n - i
        return 0
        '''
        n = len(citations)

        # count[i] = number of papers with i citations
        # count[n] also stores all papers with >= n citations
        count = [0] * (n + 1)

        for c in citations:
            count[min(c, n)] += 1

        paper = 0

        # Try possible h-index from largest to smallest
        for h in range(n, -1, -1):
            # Number of papers with at least h citations
            paper += count[h]

            # At least h papers have at least h citations
            if paper >= h:
                return h

        return 0