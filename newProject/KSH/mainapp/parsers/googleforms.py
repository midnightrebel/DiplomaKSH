from pprint import pprint
import datetime
import pandas as pd
now = datetime.datetime.now()

namefile = 'KSHGoogle' + str(now.year) + '.xlsx'
googleforms = pd.read_excel(namefile,usecols=[1,2,3,4,5,6])