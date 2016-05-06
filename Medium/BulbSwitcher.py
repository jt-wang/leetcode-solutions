import math


class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None:
            return 0

        if n < 0:
            return 0

        return int(math.sqrt(n))

'''
思路:
using set() will result in time out.
Consider from the mathematic way.
每个数都在它的质因数次被toggle, 计算一个数有多少个因数，就把这个数拆成质因数的(次方+1)相乘。
（对于每个质因数, 都可以选0次, 1次 直到该质因数次数)。
只有当因数个数是奇数时, 最后它才会亮着。(因为第1次开)
只有质因数的次方是偶数时, 因数个数才会是奇数. ( (a+1) * (b+1) )

因为只要出现一个 a 为 奇数, 则 (a+1) 为偶数, 整体为偶数,
所以必须每个质因数的次方必须是偶数。
则所有质因数的乘积 是 某个数的平方
则最后开着灯的个数, 就是 1 到 n 有多少平方数
count = 0
for i in range(n+1):
    if i**2 < n+1:
    count += 1

则n开根即可。
'''
