# phbs-qps-bo
The 2024 phbs qps,bo

# The URL
[git repository](https://github.com/Liezian/phbs-qps-bo.git)

# Instructions about how to run

1. create your own environment
```
conda create --name ""
```
2. activate your environment
```
conda activate ""
```
3. Install the necessary packages
```
pip install requirements.txt
```

# How to get cpi datas
[Federal Reserve Economic Data](https://fred.stlouisfed.org/) provides detailed U.S. economic data, including the CPI.
Using packages **fredapi==0.5.2** to get US CPI data.

In **src** folder, running **fetch_cpi.py** to get the CPI data, which will be stored in folder named **data**.

# How to get inflation
In **notebooks** folder, running **cpi_inflation.ipynb** to get the last 4 quarters of inflation in the US.