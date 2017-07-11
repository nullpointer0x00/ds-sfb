import pandas as pd
from pandas.io import sql
import sqlite3

conn = sqlite3.connect('backpain.db')

data = pd.read_csv('./Dataset_spine.csv', low_memory=False)
data.head()
data.to_sql('spine',
            con=conn,
            if_exists='replace',
            index=False)
print data.head()

df = pd.read_sql("SELECT "
                "pelvic_incidence, pelvic_tilt,lumbar_lordosis_angle,sacral_slope,"
                "pelvic_radius,degree_spondylolisthesis,pelvic_slope,direct_tilt,"
                "thoracic_slope,cervical_tilt,sacrum_angle,scoliosis_slope,"
                  "case when Class_att = 'Abnormal' then 1 else 0 end as classification "
                  "FROM spine s", con=conn)

cmap = {'0': 'r', '1': 'g', '2': 'b' }
df['cclassification'] = df.classification.apply(lambda x: cmap[str(x)])
df.plot('pelvic_incidence', 'pelvic_tilt', kind='scatter', c=df.cclassification)
print df.describe()