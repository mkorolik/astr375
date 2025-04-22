# astr375
final project for astr375: exoplanets

results and brief notes on the results in analysis.ipynb

I made exoplanet models in MESA to study the effect of the mass accretion rate on planet evolution. All of the models had the same intial radius (5 RJ). The models had an initial mass of either 1 MJ or 10 MJ. The mass accretion rate varied from 1e-7 MJ/year to 1e-9 MJ/year. This lower accretion rate failed to converge for the models because it led to a planet with a radius of less than 1 RJ, which MESA is not well equipped to handle. All of the models ended at the same final mass: 20 MJ. 

I studied the effect of the mass accretion rate on the final planet radius, effective temperature, and luminosity. While it has an effect on all of these properties, the effect on the final radius is much smaller than on the other two properties. Particularly, the tracks had a wide range in effective temperatures, which could allow us to use observations to make predictions about the planets' evolutionary history. 
