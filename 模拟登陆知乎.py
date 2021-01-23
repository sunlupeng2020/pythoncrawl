from urllib import request
url = 'https://www.zhihu.com/hot'
headers1 = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'cookie': '_zap=3b939fae-4ca2-4d42-adb7-734613dfbcc5; _xsrf=Z2qnRjy1C0TCdW7QcDKRhMQbn6RNylE8; d_c0="AKATMX-tmRGPTihe-AAY4GSzal0eRhNgimM=|1595150913"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1595064743; _ga=GA1.2.1127984714.1595064744; _gid=GA1.2.1564252886.1595064744; SESSIONID=qa5RHYaZH3W7QJD2mTOYyiJbDmaSweaMWQJQrUxHl9s; JOID=V1odA0KO_FwfZhnMeovHiB_nsV5m-JdhRCJHpyjKyAEgPl-PQsHsSUVtFM576uhIeX_2XOYftcFn8YsJDC0rDjI=; osd=UlASBEuL9lMYbxzGdYzOjRXotldj8phmTSdNqC_DzQsvOVaKSM7rQEBnG8ly7-JHfnbzVukYvMRt_owACSckCTs=; l_n_c=1; r_cap_id="OTdkN2Y2NDY2NjljNDU5MjkwNDFmNTQ0YzU4Y2Y2Yzg=|1595151515|818cfe44ce017c9c1a4f59de19b72257bdacb3d1"; cap_id="ZDVlZjJlYjliOWM1NDY0NDhmODlkODA5ZDU0MjMwOGE=|1595151515|1313df7d23e52dc5692be21efc53c13bc7e39a5e"; l_cap_id="MDliOTNlNGE2MDc4NGZiMWE3ZGZjMDQ1ZWE0NGJiMDk=|1595151515|0cca592bc1c6851bbed814678d6a12a53da96ad4"; n_c=1; atoken=35_gsVRCUhs8Ctvwuu6Mf2P4OF_xrdUZO9pSQd64x0RlMhUWeriS4zWjnptwVKDN5acyQlzl08Pm507LnnsM3xtpo7L_OsNx1MOynB9zA9hYfE; atoken_expired_in=7200; client_id="bzNwMi1qdkJvSW5oa2J3UFdQSEUyOHZ3eUwwbw==|1595151534|d474d0f62bdea2f50ef1b4b9935f8855fa3aac6a"; capsion_ticket="2|1:0|10:1595151534|14:capsion_ticket|44:ZjM3YjA2OTE4N2QwNDI5M2JmMjI3MjljODI4ZTczYmM=|c6f5720be99092fccc9b42ab79e58fae65689d632b1d107ad2a84cd139df0c47"; z_c0="2|1:0|10:1595151683|4:z_c0|92:Mi4xUERQRkZRQUFBQUFBb0JNeGY2MlpFU1lBQUFCZ0FsVk5RMk1CWUFEeDB6U3hGWmpSaFk1bFREaUNocEJ4dFlPOGZn|5566ab41b0234ae200b77c718af3c7eead00464f035eb9d91d73ccb424b3e543"; unlock_ticket="AEBhaFB3hBAmAAAAYAJVTUscFF9MsCItIV-9lbDG9raKH1R43BaaBQ=="; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1595065516; tst=h; KLBRSID=81978cf28cf03c58e07f705c156aa833|1595151688|1595150912; tshl='
}
rq = request.Request(url,headers=headers)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))
