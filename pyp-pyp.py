import graphlab as gl
sf = gl.SFrame('https://raw.githubusercontent.com/Kolpashnikova/project2/master/pricesscrapedcopy.csv')

sf['date2'] = sf['date2'].str_to_datetime(str_format='%Y-%m-%d')

gl.canvas.set_target('ipynb')
sf[sf['nrooms']==1].show(view="Heat Map", x="date2", y="ch")

sf[sf['nrooms']==5].show(view="BoxWhisker Plot", x="date_vec", y="ch")

sf[sf['nrooms']==2].show(view="BoxWhisker Plot", x="date_vec", y="ch")

sf.show(view="BoxWhisker Plot", x="zipcode", y="ch")

