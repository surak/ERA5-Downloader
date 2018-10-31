# ERA5-Downloader
A JUBE [http://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/JUBE/JUBE2/_node.html] script for downloading the full ERA5 reanalysis-era5-single-levels dataset from Copernicus [http://www.copernicus.eu]. Note that this might take several months and it WILL outrun your computer's disk space, many many times. A supercomputer or other special way of storing huge amounts of data is required.

You need:

- Jube (see link above)
- Python
- The CDS Api from Copernicus. You can download it with pip:

```
pip install cdsapi
```

## How to run

- Create an account on copernicus, and follow the instructions at [https://cds.climate.copernicus.eu/api-how-to] to install the CDS api key.
- Edit `era5 in order to choose which data you want (each dataset is hundreds of terabytes) 

The possible values for the variables are written as comments, and a default value exists.

- Do a `jube run era5.xml. It will perform a combinatory run of all parameters you chose, and download every combination individually. It will create a datasets/ directory on the place you ran jube from. This will be

```
datasets/2000 (year)
          |----+- 01 (month)
          |    |---- 01 (day)
          |    |---- 02
          |    |---- ....
          |    |---- 31
          |    |
          |    +- 02
....
```

And inside, the file name is `dataset-product_type-variable-year-month-day-hour.filetype`, e.g.: `reanalysis-era5-single-levels-ensemble_mean-100m_u_component_of_wind-2018-01-01-00:00.brig`

If you want to download multiple sets in a single file (e.g. all hours of the day, not 24 files), you can change the way JUBE creates combination. JUBE interprets the commas as a new combination of parameters, so if you have 

```<parameter name="time">'00:00','01:00','02:00','03:00','04:00','05:00'</parameter>```, JUBE will do 6 separate downloads.

If you change this to 
```<parameter name="time" separator="!">'00:00','01:00','02:00'!'03:00','04:00','05:00'</parameter>```, then JUBE will perform only two downloads, as the combination is changed by the separator.