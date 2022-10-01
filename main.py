import pandas as pd

if __name__ == '__main__':
    accStat = pd.concat([pd.read_csv('./2021_account_statements.csv', sep=';'), pd.read_csv('./2022_account_statements.csv', sep=';')])
    accStat = pd.DataFrame(accStat, columns=['Date','Amount','Description','Subject'])
    accStat.fillna('')
    print(accStat)