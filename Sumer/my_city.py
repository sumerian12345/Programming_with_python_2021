# encoding: utf-8

##################################################
# This script shows an example of a header section. This sections is a group of commented lines (lines starting with
# the "#" character) that describes general features of the script such as the type of licence (defined by the
# developer), authors, credits, versions among others
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Michael DiCarlo
# Email: MichaelrDiCarlo@gmail.com
# Status: development
##################################################

# End of header section

city_name = 'Calgary'
city_area = 200000
city_population = 3000
city_density = city_population/city_area

print('The most awesome city is ' + city_name)
print('Population Density is')
print(city_density)

print('Population Density ' + str(city_density) + ' inhabitants per hectare')
