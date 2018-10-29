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
- Copy the download-era5-jube.xml to another file.
- Edit download-era5-jube.xml to choose which data you want (the whole dataset is hundreds of terabytes).
- Do a `jube run download-era5-jube.xml`. It will perform a combinatory run of all parameters you chose, and download every combination individually.
