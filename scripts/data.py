import pandas as pd
import plotly.graph_objs as go

def return_figures():

  # first chart code
  graph_one = []
  df = pd.read_csv('data/API_AG.LND.ARBL.HA.PC_DS2_en_csv_v2_clean.csv')
  df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
  countrylist = df.country.unique().tolist()
  for country in countrylist:
      x_val = df[df['country'] == country].year.tolist()
      y_val =  df[df['country'] == country].hectaresarablelandperperson.tolist()
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
  df = pd.read_csv('data/API_AG.LND.ARBL.HA.PC_DS2_en_csv_v2_clean.csv')
  df.sort_values('hectaresarablelandperperson', ascending=False, inplace=True)
  df = df[df['year'] == 2015] 

  graph_two.append(
      go.Bar(
      x = df.country.tolist(),
      y = df.hectaresarablelandperperson.tolist(),
      )
  )

  layout_two = dict(title = 'Hectares Arable Land per Person in 2015',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Hectares per person'),
                )


  # third chart code
  graph_three = []
  df = pd.read_csv('data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_clean.csv')
  df.sort_values('percentrural', ascending=False, inplace=True)
  for country in countrylist:
      x_val = df[df['country'] == country].year.tolist()
      y_val =  df[df['country'] == country].percentrural.tolist()
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
  df_one = pd.read_csv('data/API_SP.RUR.TOTL_DS2_en_csv_v2_9914824_clean.csv')
  df_two = pd.read_csv('data/API_AG.LND.FRST.K2_DS2_en_csv_v2_9910393_clean.csv')

  df = df_one.merge(df_two, on=['country', 'year'])

  for country in countrylist:
      x_val = df[df['country'] == country].variable_x.tolist()
      y_val = df[df['country'] == country].variable_y.tolist()
      year = df[df['country'] == country].year.tolist()
      country_label = df[df['country'] == country].country.tolist()

      text = []
      for country, year in zip(country_label, year):
          text.append(str(country) + ' ' + str(year))

      graph_four.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'markers',
          text = text,
          name = country,
          textposition = 'top'
          )
      )

  layout_four = dict(title = 'Rural Population versus <br> Forested Area (square km)',
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
