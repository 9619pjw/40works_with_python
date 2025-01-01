import pandas as pd

df = pd.DataFrame([["홍길동", "1900.01.02", "2021-0001"],
                    ["김민준", "1900.05.06", "2021-0002"],
                    ["김철수", "2000.08.08", "2021-0003"],
                    ["김영희", "2000.09.09", "2021-0004"],
                    ["이서준", "2010.10.10", "2021-0005"],
                    ["장다인", "2017.12.12", "2021-0006"]])

print(df)

# 데이터프레임 xlsx로 저장
df.to_excel(r'12. Certificate with Auto\CertificateList.xlsx', index=False, header=False)