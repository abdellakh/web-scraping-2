from bs4 import BeautifulSoup as sp
import requests
import pandas as pd
new_df=pd.DataFrame()
for i in [1,2,3,4,5,6,7,8,9,10]:
	url='https://starngage.com/app/global/influencer/ranking/morocco?page='+str(i)
	r=requests.get(url)
	web_page= sp(r.content)
	table=web_page.select('table')[0]
	coulums = table.find('thead').find_all('th')
	coulume_names=[c.string for c in coulums]
	rows=table.find('tbody').find_all('tr')
	l = []
	for tr in rows:
		td = tr.find_all('td')
		row = [str(tr.get_text()).strip() for tr in td]
		l.append(row)
	df = pd.DataFrame(l, columns=coulume_names)

	new_df=pd.concat([new_df,df],ignore_index=True)
new_df.to_csv('all.csv',index=False)
