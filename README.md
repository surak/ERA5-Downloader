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
- Edit download-era5-jube.xml to choose which data you want (the whole dataset is hundreds of terabytes) The possible values for the variables are written as comments, and a default value exists.
- Do a `jube run download-era5-jube.xml`. It will perform a combinatory run of all parameters you chose, and download every combination individually. It will create a datasets/ directory on the place you ran jube from. This will be

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