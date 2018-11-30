# 询问是否需要对应货币代码
require=input("Do you need the codes to the names?\
(input 'Y' or 'N')")
if require=="Y":
	print('''Code\tName\nAED\tUnited Arab Emirates Dirham\nAFN\tAfghan Afghani\nALL\tAlbanian Lek\nAMD\tArmenian Dram\nANG\tNetherlands Antillean Guilder\nAOA\tAngolan Kwanza\nARS\tArgentine Peso\nAUD\tAustralian Dollar\nAWG\tAruban Florin\nAZN\tAzerbaijani Manat\nBAM\tBosnia-Herzegovina Convertible Mark\nBBD\tBarbadian Dollar\nBDT\tBangladeshi Taka\nBGN\tBulgarian Lev\nBHD\tBahraini Dinar\nBIF\tBurundian Franc\nBMD\tBermudan Dollar\nBND\tBrunei Dollar\nBOB\tBolivian Boliviano\nBRL\tBrazilian Real\nBSD\tBahamian Dollar\nBTC\tBitcoin\nBTN\tBhutanese Ngultrum\nBWP\tBotswanan Pula\nBYR\tBelarusian Ruble\nBZD\tBelize Dollar\nCAD\tCanadian Dollar\nCDF\tCongolese Franc\nCHF\tSwiss Franc\nCLF\tChilean Unidad de Fomento\nCLP\tChilean Peso\nCNY\tChinese Yuan\nCOP\tColombian Peso\nCRC\tCosta Rican Colón\nCUC\tCuban Convertible Peso\nCUP\tCuban Peso\nCVE\tCape Verdean Escudo\nCZK\tCzech Republic Koruna\nDJF\tDjiboutian Franc\nDKK\tDanish Krone\nDOP\tDominican Peso\nDZD\tAlgerian Dinar\nEEK\tEstonian Kroon\nEGP\tEgyptian Pound\nERN\tEritrean Nakfa\nETB\tEthiopian Birr\nEUR\tEuro\nFJD\tFijian Dollar\nFKP\tFalkland Islands Pound\nGBP\tBritish Pound Sterling\nGEL\tGeorgian Lari\nGGP\tGuernsey Pound\nGHS\tGhanaian Cedi\nGIP\tGibraltar Pound\nGMD\tGambian Dalasi\nGNF\tGuinean Franc\nGTQ\tGuatemalan Quetzal\nGYD\tGuyanaese Dollar\nHKD\tHong Kong Dollar\nHNL\tHonduran Lempira\nHRK\tCroatian Kuna\nHTG\tHaitian Gourde\nHUF\tHungarian Forint\nIDR\tIndonesian Rupiah\nILS\tIsraeli New Sheqel\nIMP\tManx pound\nINR\tIndian Rupee\nIQD\tIraqi Dinar\nIRR\tIranian Rial\nISK\tIcelandic Króna\nJEP\tJersey Pound\nJMD\tJamaican Dollar\nJOD\tJordanian Dinar\nJPY\tJapanese Yen\nKES\tKenyan Shilling\nKGS\tKyrgystani Som\nKHR\tCambodian Riel\nKMF\tComorian Franc\nKPW\tNorth Korean Won\nKRW\tSouth Korean Won\nKWD\tKuwaiti Dinar\nKYD\tCayman Islands Dollar\nKZT\tKazakhstani Tenge\nLAK\tLaotian Kip\nLBP\tLebanese Pound\nLKR\tSri Lankan Rupee\nLKR\tSri Lankan Rupee	\nLRD\tLiberian Dollar	\nLSL\tLesotho Loti	\nLTL\tLithuanian Litas	\nLVL\tLatvian Lats	\nLYD\tLibyan Dinar	\nMAD\tMoroccan Dirham	\nMDL\tMoldovan Leu	\nMGA\tMalagasy Ariary	\nMKD\tMacedonian Denar	\nMMK\tMyanma Kyat	\nMNT\tMongolian Tugrik	\nMOP\tMacanese Pataca	\nMRO\tMauritanian Ouguiya	\nMTL\tMaltese Lira	\nMUR\tMauritian Rupee	\nMVR\tMaldivian Rufiyaa	\nMWK\tMalawian Kwacha	\nMXN\tMexican Peso	\nMYR\tMalaysian Ringgit	\nMZN\tMozambican Metical	\nNAD\tNamibian Dollar	\nNGN\tNigerian Naira	\nNIO\tNicaraguan Córdoba	\nNOK\tNorwegian Krone	\nNPR\tNepalese Rupee	\nNZD\tNew Zealand Dollar	\nOMR\tOmani Rial	\nPAB\tPanamanian Balboa	\nPEN\tPeruvian Nuevo Sol	\nPGK\tPapua New Guinean Kina	\nPHP\tPhilippine Peso	\nPKR\tPakistani Rupee	\nPLN\tPolish Z?oty	\nPYG\tParaguayan Guarani	\nQAR\tQatari Rial	\nRON\tRomanian Leu	\nRSD\tSerbian Dinar	\nRUB\tRussian Ruble	\nRWF\tRwandan Franc	\nSAR\tSaudi Riyal	\nSBD\tSolomon Islands Dollar	\nSCR\tSeychellois Rupee	\nSDG\tSudanese Pound	\nSEK\tSwedish Krona	\nSGD\tSingapore Dollar	\nSHP\tSaint Helena Pound	\nSLL\tSierra Leonean Leone	\nSOS\tSomali Shilling	\nSRD\tSurinamese Dollar	\nSTD\tS?o Tomé and Príncipe Dobra	\nSVC\tSalvadoran Colón	\nSYP\tSyrian Pound	\nSZL\tSwazi Lilangeni	\nTHB\tThai Baht	\nTJS\tTajikistani Somoni	\nTMT\tTurkmenistani Manat	\nTND\tTunisian Dinar	\nTOP\tTongan Pa'anga	\nTRY\tTurkish Lira	\nTTD\tTrinidad and Tobago Dollar	\nTWD\tNew Taiwan Dollar	\nTZS\tTanzanian Shilling	\nUAH\tUkrainian Hryvnia	\nUGX\tUgandan Shilling	\nUSD\tUnited States Dollar	\nUYU\tUruguayan Peso	\nUZS\tUzbekistan Som	\nVEF\tVenezuelan Bolívar Fuerte	\nVND\tVietnamese Dong	\nVUV\tVanuatu Vatu	\nWST\tSamoan Tala	\nXAF\tCFA Franc (BEAC)	\nXAG\tTroy Ounce of Silver	\nXAU\tTroy Ounce of Gold	\nXCD\tEast Caribbean Dollar	\nXDR\tSpecial Drawing Rights	\nXOF\tCFA Franc (BCEAO)	\nXPD\tTroy Ounce of Palladium	\nXPF\tCFP Franc	\nXPT\tTroy Ounce of Platinum	\nYER\tYemeni Rial	\nZAR\tSouth African Rand	\nZMK\tZambian Kwacha (pre-2013)	\nZMW\tZambian Kwacha	\nZWL\tZimbabwean Dollar''')

#  主函数部分
# 输入变量
currency_from=input("currency_from:")
currency_to=input("currency_to:")
amount_from=input("amount_from:")
# 引入urlopen函数
from urllib.request import urlopen

# 定义生成URL文本的函数
def url(currency_from,currency_to,amount_from):
	return f"http://cs1110.cs.cornell.edu/\
2016fa/a1server.php?\
from={currency_from}\
&to={currency_to}\
&amt={amount_from}"
# 定义对字节流处理的函数
def convert(docstr):
	docstr=str(docstr)[2:-1]
	if "true" in docstr:
		docstr=docstr.replace("true","True")
	elif "false" in docstr:
		docstr=docstr.replace("false","False")
		#将字符串转化为字典
	return eval(docstr)

# 定义 exchange 函数
def exchange(currency_from,currency_to,amount_from):	
	#生成URL文本
	URL=url(currency_from,currency_to,amount_from)

	#用URL获取来自网站的字节流
	doc=urlopen(URL)
	docstr=doc.read()

	#处理字节流
	docdic=convert(docstr)
	
	#若输入形式正确
	if docdic["success"]==True:
		#用键“to”获取值
		value=docdic["to"]
		#将值中的数字与字母分离，获取数字
		to_list=(value.split())
		#将数字从字符串转为浮点数
		return float(to_list[0])
	#若输入形式错误
	else:
		#用键“error”获取错误原因
		error=docdic["error"]
		return error

result=exchange(currency_from,currency_to,amount_from)
print(result)


# 测试函数部分
#测试是否生成了正确的URL文本
def test_url():
	assert(url("USD","EUR","2.5")==\
"http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5")
#测试是否成功将字符串转换为字典
def test_convert():
	assert(convert(\
b'{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')\
=={'from': '2.5 United States Dollars', 'to': '2.1589225 Euros', 'success': True, 'error': ''})
def test_convert_to_dict():	
	assert(type(convert(\
b'{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : True, "error" : "" }')\
==dict))
#测试两组正确数据的输出
def test_exchange1():
	assert(exchange("USD","EUR","2.5")==2.1589225)
def test_exchange2():
	assert(exchange("CNY","JPY","10")==162.57643642095)
#测试一组错误数据的输出
def test_exchange3():
	assert(exchange("YUAN","JPY","10")=="Source currency code is invalid.")

def test_all():
	test_url()
	test_convert()
	test_convert_to_dict()
	test_exchange1()
	test_exchange2()
	test_exchange3()
	print("All tests passed")
test_all()