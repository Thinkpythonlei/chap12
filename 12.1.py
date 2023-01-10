a="afghukajbrfwuihcznlknvgkushgnvsdkhfao8whnflqawisefhalwinjf"
b=list(a)
print(b)

import pandas as pd
c=pd.Series(b).value_counts()
d=dict(c)
print(d)