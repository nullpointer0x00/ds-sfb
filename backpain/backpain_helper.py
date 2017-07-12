import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import sqlite3
import os;

class BackpainHelper:

    def __init__(self):
        self.conn = sqlite3.connect('backpain.db')
        self.data = pd.read_csv('../Dataset_spine.csv', low_memory=False)
        self.data.to_sql('spine',
            con=self.conn,
            if_exists='replace',
            index=False)

    def get_spine_data(self, print_head = False):
        data = pd.read_sql("SELECT "
                "pelvic_incidence, pelvic_tilt,lumbar_lordosis_angle,sacral_slope,"
                "pelvic_radius,degree_spondylolisthesis,pelvic_slope,direct_tilt,"
                "thoracic_slope,cervical_tilt,sacrum_angle,scoliosis_slope,"
                "case when Class_att = 'Abnormal' then 1 else 0 end as classification "
                "FROM spine s", con=self.conn)
        if print_head :
            print data.head()
        return data

    def scatter_plot_combos(self, df, columns):
        cmap = {'0': 'g', '1': 'r'}
        tmp_columns = columns[:]
        while len(tmp_columns) >= 2:
            x_column = tmp_columns.pop(0)
            for column in tmp_columns :
                df['cclassification'] = df.classification.apply(lambda x: cmap[str(x)])
                plot = df.plot(x_column, column, kind='scatter', c=df.cclassification)
                plot.legend(df.classification, loc='best')

    def heat_map(self, df):
        corr = df.corr()
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        f, ax = plt.subplots(figsize=(11, 9))
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})

    def box_plot(self, df, column) :
        title = column.replace("_", " ")
        sns.set_style("whitegrid")
        ax = sns.boxplot(x=df[column])
        ax.set_title(title)
