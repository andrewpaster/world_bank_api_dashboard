import pandas as pd
import numpy as np
import plotly.graph_objs as go
from collections import OrderedDict
import requests

  # indictaors = ['AG.LND.ARBL.HA', 'AG.LND.FRST.K2', 'SP.RUR.TOTL']
  # country_codes = {'Canada':'CAN',
  # 'United States':'USA',
  # 'Brazil':'BRA',
  # 'France':'FRA',
  # 'India':'IND',
  # 'Italy':'ITA',
  # 'Germany':'DEU',
  # 'United Kingdom':'GBR',
  # 'China':'CHN',
  # 'Japan':'JPA'}


  # http://api.worldbank.org/v2/countries/usa;bra/indicators/AG.LND.ARBL.HA?date=1990:2015&per_page=1000&format=json

# default list of all countries - in other words no filter
country_default = OrderedDict([('Canada', 'CAN'), ('United States', 'USA'), 
  ('Brazil', 'BRA'), ('France', 'FRA'), ('India', 'IND'), ('Italy', 'ITA'), 
  ('Germany', 'DEU'), ('United Kingdom', 'GBR'), ('China', 'CHN'), ('Japan', 'JPN')])

def return_figures(countries=country_default):

  if not bool(countries):
    countries = country_default

  # prepare filter data
  country_filter = list(countries.values())
  country_filter = [x.lower() for x in country_filter]
  country_filter = ';'.join(country_filter)

  # create urls for the indicators of interest with the country filter
  indicators = ['AG.LND.ARBL.HA.PC', 'SP.RUR.TOTL.ZS', 'SP.RUR.TOTL', 'AG.LND.FRST.K2']
  urls = []

  # store the data frames with the indicator data of interest
  data_frames = []

  # get and clean data
  for indicator in indicators:
    url = 'http://api.worldbank.org/v2/countries/' + country_filter +\
    '/indicators/' + indicator + '?date=1990:2015&per_page=1000&format=json'
    urls.append(url)

    try:
      r = requests.get(url)
      data = r.json()[1]
    except:
      print('could not load data ', indicator)

    for i, value in enumerate(data):
      value['indicator'] = value['indicator']['value']
      value['country'] = value['country']['value']

    data_frames.append(data)
  
  graph_one = []
  df_one = pd.DataFrame(data_frames[0])
  df_one = df_one[(df_one['date'] == '2015') | (df_one['date'] == '1990')]
  df_one.sort_values('value', ascending=False, inplace=True)
  countrylist = df_one.country.unique().tolist()
  for country in countrylist:
      x_val = df_one[df_one['country'] == country].date.tolist()
      y_val =  df_one[df_one['country'] == country].value.tolist()
      graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
      )

  layout_one = dict(title = 'Change in Hectares Arable Land <br> per Person 1990 to 2015',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=1990, dtick=25),
                yaxis = dict(title = 'Hectares'),
                )

  # second chart code
  graph_two = []
  df_one.sort_values('value', ascending=False, inplace=True)
  df_one = df_one[df_one['date'] == '2015'] 

  graph_two.append(
      go.Bar(
      x = df_one.country.tolist(),
      y = df_one.value.tolist(),
      )
  )

  layout_two = dict(title = 'Hectares Arable Land per Person in 2015',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Hectares per person'),
                )


  # third chart code
  graph_three = []
  df_three = pd.DataFrame(data_frames[1])
  df_three = df_three[(df_three['date'] == '2015') | (df_three['date'] == '1990')]

  # df = pd.read_csv('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_clean.csv')
  df_three.sort_values('value', ascending=False, inplace=True)
  for country in countrylist:
      x_val = df_three[df_three['country'] == country].date.tolist()
      y_val =  df_three[df_three['country'] == country].value.tolist()
      graph_three.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
      )

  layout_three = dict(title = 'Change in Rural Population <br> (Percent of Total Population)',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=1990, dtick=25),
                yaxis = dict(title = 'Percent'),
                )

  # fourth chart code
  graph_four = []
  df_four_a = pd.DataFrame(data_frames[2])
  df_four_a = df_four_a[['country', 'date', 'value']]
  
  df_four_b = pd.DataFrame(data_frames[3])
  df_four_b = df_four_b[['country', 'date', 'value']]

  df_four = df_four_a.merge(df_four_b, on=['country', 'date'])
  df_four.sort_values('date', ascending=True, inplace=True)
  
  for country in countrylist:
      x_val = df_four[df_four['country'] == country].value_x.tolist()
      y_val = df_four[df_four['country'] == country].value_y.tolist()
      years = df_four[df_four['country'] == country].date.tolist()
      country_label = df_four[df_four['country'] == country].country.tolist()

      text = []
      for country, year in zip(country_label, years):
          text.append(str(country) + ' ' + str(year))

      color_scale = np.linspace(100, 255, len(years))
      print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
      print(color_scale)
      print(years)
      graph_four.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'markers',
          marker=dict(
            color=color_scale),
          text = text,
          name = country,
          textposition = 'top'
          )
      )

  layout_four = dict(title = 'Rural Population versus <br> Forested Area (square km) 1990-2015',
                xaxis = dict(title = 'Rural Population'),
                yaxis = dict(title = 'Forest Area (square km)'),
                )


  # append all charts
  figures = []
  figures.append(dict(data=graph_one, layout=layout_one))
  figures.append(dict(data=graph_two, layout=layout_two))
  figures.append(dict(data=graph_three, layout=layout_three))
  figures.append(dict(data=graph_four, layout=layout_four))

  return figures
