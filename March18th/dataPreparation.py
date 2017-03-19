import pandas as pd
import pandas_datareader.data as web   # Package and modules for importing data; this code may change depending on pandas version
import datetime
import numpy as np


def getDataForSymbol(sym, start, end):
    df = web.DataReader(sym, "yahoo", start, end) # returns a dataframe
    type(df)
    return df

def getDataForSymbolList(symList, start, end):
    D = {}
    for sym in symList:
        D[sym] = getDataForSymbol(sym, start, end)
    return D

def formatForTraining(data, start, end, daysPerSet, gap=0):
    total = 0
    for i in range(len(data)):
        total += len(data[i]) // (daysPerSet + gap + 1)
    arr = np.zeros((total, 6 * daysPerSet))
    setIdx = 0
    for i in range(len(data)):
        numSets = len(data[i]) // (daysPerSet + gap + 1)
        for j in range(numSets):
            for k in range(daysPerSet):
                idx = setIdx * 6 * daysPerSet 
                arr[idx] = data[i][j * (daysPerSet + gap + 1) + k]["High"]
                arr[idx+1] = data[i][j * (daysPerSet + gap + 1) + k]["Low"]
                arr[idx+2] = data[i][j * (daysPerSet + gap + 1) + k]["Open"]
                arr[idx+3] = data[i][j * (daysPerSet + gap + 1) + k]["Close"]
                arr[idx+4] = data[i][j * (daysPerSet + gap + 1) + k]["Adj. Close"]
                arr[idx+5] = data[i][j * (daysPerSet + gap + 1) + k]["High"]
            setIdx+=1
    return arr

loadTest = False

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()
 
L = ["PIH","SHLM","ACTG","AKAO","ADMS","AAAP","AEHR","AGYS","ATSG","AMRI","ALJJ","ALQA","SWIN","AMBA","AETI","CRMT","IBUY","ANDAR","ABAC","AMAT","ARDM","APLP","ARTX","ASNA","ALOT","ACFC","ATRI","ADP","AHPAU","AZRX","BLDP","OZRK","BHACW","BBBY","BGCP","BLRX","BSTC","BBRY","BLBD","BNCN","BPFHP","BLIN","BRKS","CHRW","CLMS","CALA","CPLA","CAPN","CSII","CRTN","CBIO","CDW","CLLS","CSFL","CRNT","CFCOU","CHKP","CMRX","CNIT","IMOS","CMCT","CZFC","CLRO","CNV","CGNX","COLB","CHUBK","CGEN","CFMS","CFRX","CORT","COUP","CRAY","XRDC","CTIC","CVV","CONE","DRIOW","DWSN","DENN","DXTR","DRAD","DISH","DORM","DXPE","EWBC","EBAYL","EDIT","ERI","CAPX","ECPG","ENOC","EGT","ESPR","EVK","EXFO","EZPW","FARO","FGEN","FITBI","BUSE","FFBC","FIBK","FPA","FVC","FTGC","FTC","FAD","CARZ","QTEC","FYC","FUNC","FLKS","FLXS","FORR","FRAN","FSBW","FSNN","GALTU","GENC","GNTX","GIGA","GOODP","GBLI","ACTX","ALTY","GOGL","GPIAW","GPP","GSIT","GURE","HBK","HRMNU","HWBK","HEBT","HTBK","HIHO","HFBL","HRZN","HTGM","HBANP","IBKC","ICUI","INFO","IMNP","IBCP","INNL","INSG","IART","LINK","ISIL","ISBC","DFVS","IRDMB","FALN","EWZS","QAT","IGOV","XXIA","JXSB","JAZZ","WYIG","KALU","KMPH","KGJI","KLREU","KLIC","LAMR","LE","LPTX","LMAT","LBTYA","BATRK","LCUT","LECO","LOB","CNCR","LMNX","MBVX","MNGA","LOAN","MRLN","MAT","MGRC","MDVX","MTSL","MMSI","MGEE","MVIS","MDXG","MITK","MNTA","MSDI","MSBF","MYOS","NSSC","NGHCN","NWLI","NCIT","NETE","NDRM","NEWS","EGOV","NSYS","NWFL","NUAN","NVDA","OBSV","ODP","OSBCP","ONSIZ","OPXAW","OSUR","OACQW","OTTW","PFIN","PPBI","PANL","PKOH","PAVMW","PDFS","PNNT","PRCP","PGLC","PICO","PLUG","PLKI","PSIX","PFI","PUI","KBWB","USLB","VRIG","PRGX","PSC","PRPH","PRTO","PULM","QGEN","QDEL","RADA","RAND","RDI","REPH","RNST","REFR","REXX","RVSB","ROSG","RUTH","SBRAP","SASR","SMIT","SHIP","SNFCA","SENEB","SREV","SHPG","SWIR","SLAB","SVA","SLMBP","SLRC","SPHS","SONA","DWFI","FUND","SBLKL","STLRU","BANX","SCMP","SPWR","SPRT","SYNL","SYPR","TNDM","AMTD","TELL","TSRA","TGTX","DXYN","FITS","NAVG","YORW","TSBK","TISA","TWMC","TRVN","TRNC","TTMI","TRCB","ULBI","UBCP","UBFO","UVSP","VALX","VIGI","VTWV","VBLT","TVIX","VRSN","VSAT","CSF","VKTX","VRTU","VYGR","WFBI","WCST","WBB","WHLRW","WLTW","AGND","GULF","WWD","WVFC","XGTIW","YIN","ZG","ZUMZ"]
if loadTest:
    L2 = []
    for sym in L:
        if len(sym) < 5 and sym[0] == "A":
            print(sym)
            L2.append(web.DataReader(sym, "yahoo", start, end))
# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
apple = web.DataReader("AAPL", "yahoo", start, end)
 
type(apple)

#print(apple.head())
#print("Size:\n", apple.count())

numberDays = 10

trainingData = np.random.random((1, numberDays * 6))
trainingOutputs = np.random.random((1, 1))

for i in range(numberDays):
    trainingData[0][i * 6] = apple["Open"][i]
    trainingData[0][i * 6 + 1] = apple["Close"][i]
    trainingData[0][i * 6 + 2] = apple["High"][i]
    trainingData[0][i * 6 + 3] = apple["Low"][i]
    trainingData[0][i * 6 + 4] = apple["Volume"][i]
    trainingData[0][i * 6 + 5] = apple["Adj Close"][i]
i += 1
trainingOutputs[0][0] = apple["Close"][i]
