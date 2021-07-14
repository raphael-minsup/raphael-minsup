import pyupbit

access = "7u5FpiWxRqV3BTy89EfZnnP2MIVk8nqkxObm9Sq3"          # 본인 값으로 변경
secret = "B44DHANAAe3pgaYb5xbrMr0bz867FiijmSPim0gr"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-NEO"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-LINK"))
print(upbit.get_balance("KRW"))         # 보유 현금 조회