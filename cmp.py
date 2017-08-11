import pandas as pd
import xlrd
import xlwt

df0 = pd.ExcelFile("countryPopulationJuly2016.xlsx").parse("countryPopulation")
df1 = pd.ExcelFile("countrySqKM.xlsx").parse("countrySqKM")
#df0 = df0.set_index(41)
#df1 = df1.set_index("ID")

a0, a1 = df0.align(df1)
different = (a0 != a1).any(axis=1)
comp = a0[different].join(a1[different], lsuffix='_old', rsuffix='_new')
#print(comp)
comp.to_excel("comparison.xlsx")