height = input('請輸入身高 : ')
height = int(height)
height = height/100
weight = input('請輸入體重 : ')
BMI = int(weight) / height/height
if BMI < 18.5 :
	print('您的BMI值為 :', BMI,',體重過輕')
elif BMI >= 18.5 and BMI<24:
	print('您的BMI值為 :', BMI,',正常範圍')
elif BMI >= 24 and BMI<27:
	print('您的BMI值為 :', BMI,',異常範圍:過重')
elif BMI >= 27 and BMI<30:
	print('您的BMI值為 :', BMI,',異常範圍:輕度肥胖')
elif BMI >= 30 and BMI<35:
	print('您的BMI值為 :', BMI,',異常範圍:中度肥胖')
else:
	print('您的BMI值為 :', BMI,',異常範圍:重度肥胖')
