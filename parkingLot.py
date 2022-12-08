import pandas as pd
pd.set_option('mode.chained_assignment', None)

import numpy as np

data = pd.read_csv('./제주특별자치도_제주시_주차장정보_20210818.csv', index_col = 0, encoding = 'CP949', engine = 'python')
data.head()

addr = pd.DataFrame(data['소재지지번주소'].apply(lambda v: v.split()[1:3]).tolist(), columns = ('시도', '읍면동'))
addr.head() #작업 확인용 출력

addr['읍면동'].unique()

addr['시도읍면동'] = addr.apply(lambda r: r['시도'] + ' ' + r['읍면동'], axis = 1)
addr.head() #작업 확인용 출력

addr['count'] = 0
addr.head() #작업 확인용 출력

addr_group = addr.groupby(['시도', '읍면동', '시도읍면동'], as_index = False).count()
addr.head()

addr_group = addr.groupby(['시도', '읍면동', '시도군구'], as_index = False).count()

addr_group = addr_group.set_index('시도군구')
addr_group.head() #작업 확인용 출력


##### 여기까지 자동차 등록 현황 .xlsx 


#### 여기서부터 읍면동별_세대 및 인구. xlsx


### 제주특별자치도_제주시_주차장정보 .csv







