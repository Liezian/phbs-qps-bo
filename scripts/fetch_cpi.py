import pandas as pd
from fredapi import Fred
import sys
if '../src/api_keys' not in sys.path:
    sys.path.append('../src/api_keys')
from api_keys import fred_api


if __name__ == '__main__':
    fred = Fred(api_key=fred_api)

    # 下载美国CPI数据 (符号 'CPIAUCSL' 是常见的CPI总值)
    cpi_data = fred.get_series('CPIAUCSL',
                           observation_start='10/1/2023',
                           observation_end='11/26/2024')
    cpi_data.columns = ['date', 'cpi']

    # 打印数据
    print(cpi_data.head())

    # 保存到 CSV 文件
    cpi_data.to_csv("../data/us_cpi_data_fred.csv")