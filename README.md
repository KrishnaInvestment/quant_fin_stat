# quant_fin_stat
For understanding Quant Math Better

```bash
git clone https://github.com/KrishnaInvestment/quant_fin_stat.git
cd quant_fin_stat
 ```

Get the PV of cash flow
 ```bash

python pv_cash_flow.py # This will use default values
python pv_cash_flow.py --nom_price 1500000 --cou_rate 6.0 --dis_rate 4.5 --duration 4.0 --period 5

```
Period here refers to the number of times interest will be paid per year. If the period is 4, then payments will be made quarterly; if it's 2, then payments will be made semi-annually. 