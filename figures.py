#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
impo
populationOfFinland = pd.read_csv('https://raw.githubusercontent.com/holyunicornie/amy-toolsfordataanalysis/main/csvData.csv')
fig = px.line(populationOfFinland, x = 'Year', y = 'TotalPopulation',
          title = "Finland Population by Year",
          labels = {
              'x' : 'Year',
              'y' : "people"
          }
)
fig.show()


# In[16]:


import pandas as pd
import plotly.express as px
populationOfFinland = pd.read_csv('https://raw.githubusercontent.com/holyunicornie/amy-toolsfordataanalysis/main/csvData.csv')
fig = px.scatter(populationOfFinland, x = 'TotalPopulation', y = 'GrowthRate',
          title = "Relationship between Total Population and Growth Rate of Finland",
          labels = {
              'x' : 'Total Population',
              'y' : 'Grow Rate'
              
          },
                 trendline = 'ols'
              
              
)
fig.show()


# In[6]:


import pandas as pd
import plotly.express as px
gdpGrowth = pd.read_csv('https://raw.githubusercontent.com/holyunicornie/amy-toolsfordataanalysis/main/Asian%20Development%20Outlook%20Update%202020%20(September%202020)%20-%20GDP%20Growth.csv')
fig = px.histogram(gdpGrowth, x = 'Year', y = 'GDP Growth',
          title = "GDP Growth in Asia",
          labels = {
              'x' : 'Year',
              'y' : "GDP Growth in %"
          },
          color = 'Regional Member'
)
fig.show()


# In[ ]:




