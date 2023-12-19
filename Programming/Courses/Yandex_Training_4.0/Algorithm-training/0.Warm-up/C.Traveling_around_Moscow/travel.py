from decimal import Decimal
xa, ya, xb, yb = map(Decimal, input().split())
a = (xa - xb) ** 2 + (ya - yb) ** 2
print(a.sqrt())