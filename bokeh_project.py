#!/usr/bin/env python
# coding: utf-8

# In[15]:


get_ipython().system('pip install bokeh')
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import CustomJS
from ipywidgets import widgets
healthEx = pd.read_csv('https://raw.githubusercontent.com/holyunicornie/amy-toolsfordataanalysis/main/healh-ex-per-capita-2010-2018.csv')
lifeExpectancy = pd.read_csv('https://raw.githubusercontent.com/holyunicornie/amy-toolsfordataanalysis/main/life-expectancy-2010-2018.csv')
population = pd.read_csv('https://raw.githubusercontent.com/holyunicornie/amy-toolsfordataanalysis/main/population-2010-2018-oecd.csv')
healthEx["country_year"] = healthEx["Country"].astype(str) + healthEx["Reference Period"].astype(str)
lifeExpectancy["country_year"] = lifeExpectancy["Country"].astype(str) + lifeExpectancy["Year"].astype(str)
population["country_year"] = population["Country"].astype(str) + population["Time"].astype(str)
healthEx["healthExp"] = healthEx["Value"]
lifeExpectancy["lifeX"] = lifeExpectancy["Value"]
population["pop"] = population["Value"]
data = population.merge(lifeExpectancy, how="left", left_on=["country_year"], right_on=["country_year"])
df = data.merge(healthEx, how="left", left_on=["country_year"], right_on=["country_year"])
df = df[["Country", "Year_x", "pop", "lifeX", "healthExp"]]
x_values = 'healthX'
p = figure(title = "OECD Countries from 2010-2018")
p.xaxis.axis_label = 'health ex per capita'
p.yaxis.axis_label = 'life expectancy'
p = figure(plot_width=600, plot_height=450, title = "Testing",toolbar_location=None,
          tools="hover", tooltips="@Country_x: @pop")
p.scatter('lifeX','healthExp', source=df, fill_alpha=0.6, size=10)
p.xaxis.axis_label = 'life expectancy'
p.yaxis.axis_label = 'health expense'
show(p)


# In[16]:


show(p)


# In[7]:


p2015 = df[df["Year_x"] == 2015]


# In[14]:


p = figure(title = "OECD Countries 2015")
p.xaxis.axis_label = 'health ex per capita'
p.yaxis.axis_label = 'life expectancy'
p = figure(plot_width=600, plot_height=450, title = "Testing",toolbar_location=None,
          tools="hover", tooltips="@Country_x: @pop")
p.scatter('lifeX','healthExp', source=p2015, fill_alpha=0.4, size=10)
p.xaxis.axis_label = 'life expectancy'
p.yaxis.axis_label = 'health expense'
show(p)


# In[ ]:




