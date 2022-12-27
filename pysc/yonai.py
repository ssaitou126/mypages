import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyodide.http import open_url
from datetime import datetime

nowmon = datetime.now().month

url = 'http://www1.river.go.jp/cgi-bin/DspWaterData.exe?\
KIND=2&ID=302082182211130&BGNDATE=20221201&ENDDATE=20221231&KAWABOU=NO'

def yonaiplt():
  dfs = pd.read_html(open_url(url))
  # dfs.encoding = dfs.apparent_encoding
  df = dfs[1].iloc[2:30,1:].replace(['^(?![+-]?(?:\d+\.?\d*|\.\d+)).+$'],'NaN',regex=True)
  arr = np.array(df,dtype=float).ravel()
  grf = pd.Series(arr)

  smin = grf.min()
  smax = grf.max()
  # rname = dfs[0].iloc[1,3],dfs[0].iloc[1,1]
  rvname = '阿仁川'
  stname = '米内沢'
  ldata = f'{nowmon}月水位　最大={smax}m 　最小={smin}m'

  x = [*range(0,672)]
  fig = plt.figure(figsize=(12,4))
  plt.plot(grf)
  plt.fill_between(x,grf,smin-0.2,color='c',alpha=0.2)

  plt.xticks(np.arange(0, 744, 24),np.arange(1,32))
  plt.ylim(smin-0.2,smax+0.2)
  # plt.text(0,0.46,'text', fontsize=14)
  plt.subplots_adjust(top=1)
  plt.grid()
  # plt.show()
  return fig,rvname,stname,ldata