# Online portfolio optimization
The purpose of providing this software is to provide an open source tool for stock portfolio optimization in financial markets. Due to the limitations of the classic stock portfolio problem, online stock portfolio optimization has been discussed in this software. This tool will offer the possibility of comparing and evaluating different investment methods in the financial markets. This tool can be used in various financial markets and is not limited to the cryptocurrency market.
#### Developers:
<a href="https://www.linkedin.com/in/amir-hossein-ansaripoor-a9543835/?originalSubdomain=au" target="_blank">__Dr. Amir Hossein Ansaripoor__</a>

<a href="https://www.linkedin.com/in/hamed-asgari-18ab89b6/" target="_blank">__Hamed Asgari__</a>

#### Usage
How to use this tool is described below.
First, download the software and install the dependencies using the commands below.
```angular2html
git clone https://github.com/hamedasgari20/online-portfolio-optimization.git
cd online-portfolio-optimization
virtualenv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
#### Fetching required data
The required data can be stored in the data directory with the following command.
```angular2html
from online-portfolio.tools import get_data

# Define parameters
coin_list = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD"]
start_time = '2021-01-01'
end_time = '2021-10-27'
data_source = 'yahoo'

# Fetch data and stores in directory data
get_data(coin_list, start_time,end_time,data_source)

```