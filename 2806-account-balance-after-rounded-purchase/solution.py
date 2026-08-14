class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        roundedAmount = ((purchaseAmount + 5) // 10) * 10
        return 100 - roundedAmount