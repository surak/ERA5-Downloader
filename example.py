#!/usr/bin/env python3
import cdsapi
c = cdsapi.Client()

c.retrieve("reanalysis-era5-pressure-levels",
{
"variable": "temperature",
"pressure_level": "1000",
"product_type": "reanalysis",
"date": "2008-01-01",
"time": "12:00",
"format": "grib"
},
"download.grib")
