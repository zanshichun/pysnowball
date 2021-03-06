from pysnowball import cons as cons
from pysnowball import token as token
from pysnowball import finance as finance
from pysnowball import realtime as realtime


if __name__ == '__main__':
    token.set_token(cons.SNOW_BALL_TOKEN)
    # print("pankou:\t"+str(realtime.pankou("SH601857")))
    # print("cash_flow:\t"+str(finance.cash_flow("SH601857")))
    # print("balance:\t"+str(finance.balance("SH601857")))
    print("income:\t"+str(finance.income("SH601857")))
    # print("business:\t"+str(finance.business("SH601857")))
    # print("indicator:\t"+str(finance.indicator("SH601857")))