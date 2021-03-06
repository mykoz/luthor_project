
# coding: utf-8

# In[1]:

import requests
import urlparse
import os
import pickle
from bs4 import BeautifulSoup
import urllib2
import re
from datetime import datetime
from dateutil.parser import *


# In[2]:

url = 'http://www.imdb.com/title/tt1430607/'
#http://www.imdb.com/search/title?genres=animation&title_type=feature&sort=moviemeter,asc

response = requests.get(url)


# In[2]:

def get_imdb_soup(url):
    response = requests.get(url)
    page = response.text
    return BeautifulSoup(page) #for some reason cannot get attributes (ie.title,a,div) from prettify
    


# In[29]:

numtitles = 4191

def iterurl(num_titles):
    i = 1
    urlist = ['http://www.imdb.com/search/title?genres=animation&sort=moviemeter,asc&start=1&title_type=feature']
    urlfront = "http://www.imdb.com/search/title?genres=animation&sort=moviemeter,asc&start="
    urlback = "&title_type=feature"
    while i < num_titles:
        i += 50
        url = urlfront+str(i)+urlback
        if i > (num_titles-40):
            break
        urlist.append(url)
    return urlist
        
#imdb_base_url_list = iterurl(numtitles)
#imdb_base_url_list


# In[7]:

# Pickling functions
def pickle_it(data, filename):
    with open(filename, "wb") as picklefile:
        pickle.dump(data, picklefile)

def load_pickle(filename):
    with open(filename, "rb") as picklefile: 
        return pickle.load(picklefile)


# In[641]:

def get_imdb_links(baseurl):
    basesoup = get_imdb_soup(baseurl)
    mvlinklist = []
    for a in basesoup.find_all('a'):
        if ('/title/tt' in a['href']) & (len(a['href']) == 17):
            mvlinklist.append(a['href'])
    return list(set(mvlinklist))

#get_imdb_links(base_url)


# In[ ]:




# In[4]:

big_link_list = ['/title/tt0126029/', '/title/tt1911658/', '/title/tt2510894/', '/title/tt0107688/', '/title/tt2245084/', '/title/tt2294629/', '/title/tt0435761/', '/title/tt2267968/', '/title/tt1985949/', '/title/tt0398286/', '/title/tt0103639/', '/title/tt0110357/', '/title/tt1490017/', '/title/tt2452042/', '/title/tt0114709/', '/title/tt2096673/', '/title/tt3606756/', '/title/tt0837562/', '/title/tt1690953/', '/title/tt0119282/', '/title/tt0245429/', '/title/tt2974918/', '/title/tt0317705/', '/title/tt1979388/', '/title/tt2277860/', '/title/tt2224026/', '/title/tt0198781/', '/title/tt2262227/', '/title/tt0382932/', '/title/tt0114148/', '/title/tt1772341/', '/title/tt3819668/', '/title/tt2948356/', '/title/tt2709768/', '/title/tt1646971/', '/title/tt1754656/', '/title/tt2293640/', '/title/tt0061852/', '/title/tt1323594/', '/title/tt0120762/', '/title/tt0442933/', '/title/tt2141773/', '/title/tt0892769/', '/title/tt0266543/', '/title/tt0101414/', '/title/tt0372588/', '/title/tt2401878/', '/title/tt1453405/', '/title/tt1049413/', '/title/tt0317219/','/title/tt4643580/', '/title/tt1865505/', '/title/tt0787474/', '/title/tt0118617/', '/title/tt0120855/', '/title/tt1667889/', '/title/tt0120917/', '/title/tt0351283/', '/title/tt0780521/', '/title/tt0065421/', '/title/tt0133240/', '/title/tt1446192/', '/title/tt0097757/', '/title/tt0120623/', '/title/tt0121164/', '/title/tt1001526/', '/title/tt0910970/', '/title/tt2279373/', '/title/tt0358082/', '/title/tt0268380/', '/title/tt4191054/', '/title/tt0029583/', '/title/tt0096283/', '/title/tt0119698/', '/title/tt0116583/', '/title/tt0230011/', '/title/tt0042332/', '/title/tt2872750/', '/title/tt0441773/', '/title/tt0275847/', '/title/tt0347149/', '/title/tt3411432/', '/title/tt0120794/', '/title/tt1217209/', '/title/tt0481499/', '/title/tt0095327/', '/title/tt0096438/', '/title/tt0472033/', '/title/tt0432283/', '/title/tt0327597/', '/title/tt0094625/', '/title/tt0848537/', '/title/tt0448694/', '/title/tt0983193/', '/title/tt1979376/', '/title/tt0120363/', '/title/tt0129167/', '/title/tt0046183/', '/title/tt2357291/', '/title/tt0461770/',
'/title/tt1436562/', '/title/tt1277953/', '/title/tt1691917/', '/title/tt0087544/', '/title/tt0952640/', '/title/tt0876563/', '/title/tt0345950/', '/title/tt3416828/', '/title/tt0116683/', '/title/tt1700841/', '/title/tt0844471/', '/title/tt0070608/', '/title/tt1302011/', '/title/tt0462538/', '/title/tt1192628/', '/title/tt2013293/', '/title/tt0158983/', '/title/tt1985966/', '/title/tt0892782/', '/title/tt3700456/', '/title/tt0298148/', '/title/tt0338348/', '/title/tt0130623/', '/title/tt0978762/', '/title/tt0117705/', '/title/tt0307453/', '/title/tt0055254/', '/title/tt1219342/', '/title/tt0084503/', '/title/tt1705952/', '/title/tt0864835/', '/title/tt0396555/', '/title/tt0053285/', '/title/tt4520988/', '/title/tt0385880/', '/title/tt0138749/', '/title/tt0397892/', '/title/tt0413267/', '/title/tt0451079/', '/title/tt3521164/', '/title/tt0120630/', '/title/tt1482459/', '/title/tt0328880/', '/title/tt0366548/', '/title/tt2386490/', '/title/tt0405296/', '/title/tt1216475/', '/title/tt0082406/', '/title/tt0043274/', '/title/tt0836682/',
'/title/tt1568921/', '/title/tt1142977/', '/title/tt3469046/', '/title/tt1411704/', '/title/tt0034492/', '/title/tt0424095/', '/title/tt1488589/', '/title/tt0076618/', '/title/tt0120587/', '/title/tt1067106/', '/title/tt0371606/', '/title/tt0283426/', '/title/tt0113198/', '/title/tt0453556/', '/title/tt0032455/', '/title/tt0095489/', '/title/tt1231580/', '/title/tt0327084/', '/title/tt0033563/', '/title/tt0389790/', '/title/tt2980706/', '/title/tt0095776/', '/title/tt1860353/', '/title/tt1640718/', '/title/tt0113568/', '/title/tt1821641/', '/title/tt3398268/', '/title/tt0438097/', '/title/tt0423294/', '/title/tt0479952/', '/title/tt0084649/', '/title/tt1185834/', '/title/tt0892791/', '/title/tt2576852/', '/title/tt1615918/', '/title/tt0048280/', '/title/tt0115641/', '/title/tt2865120/', '/title/tt0032910/', '/title/tt1821658/', '/title/tt0243017/', '/title/tt0092067/', '/title/tt0472181/', '/title/tt0181739/', '/title/tt0097814/', '/title/tt1623288/', '/title/tt0104009/', '/title/tt1080016/', '/title/tt0166813/', '/title/tt2850386/',
'/title/tt0173840/', '/title/tt2483260/', '/title/tt1302067/', '/title/tt4955162/', '/title/tt4618398/', '/title/tt0961097/', '/title/tt0405469/', '/title/tt0120913/', '/title/tt1402488/', '/title/tt0400717/', '/title/tt0084237/', '/title/tt1623780/', '/title/tt4155534/', '/title/tt2140203/', '/title/tt0077869/', '/title/tt0088814/', '/title/tt0762125/', '/title/tt1621039/', '/title/tt0249516/', '/title/tt0808417/', '/title/tt0078480/', '/title/tt2017020/', '/title/tt0377981/', '/title/tt0312004/', '/title/tt1762399/', '/title/tt0111419/', '/title/tt0104254/', '/title/tt1462756/', '/title/tt0347618/', '/title/tt0765446/', '/title/tt0100477/', '/title/tt0096787/', '/title/tt0091149/', '/title/tt1735462/', '/title/tt2263944/', '/title/tt0082509/', '/title/tt1430626/', '/title/tt3638012/', '/title/tt0165982/', '/title/tt1449283/', '/title/tt0038969/', '/title/tt0485601/', '/title/tt0443536/', '/title/tt0053882/', '/title/tt0318155/', '/title/tt0344854/', '/title/tt1634003/', '/title/tt3554046/', '/title/tt0057546/', '/title/tt1037226/',
'/title/tt0495596/', '/title/tt0090633/', '/title/tt0328832/', '/title/tt0286244/', '/title/tt0429589/', '/title/tt4116284/', '/title/tt0120800/', '/title/tt0076363/', '/title/tt1217213/', '/title/tt3148834/', '/title/tt4086018/', '/title/tt1625335/', '/title/tt1305591/', '/title/tt1798188/', '/title/tt3336368/', '/title/tt3606752/', '/title/tt1679335/', '/title/tt0108526/', '/title/tt0156887/', '/title/tt0070016/', '/title/tt0465502/', '/title/tt2396224/', '/title/tt2309836/', '/title/tt4450396/', '/title/tt2091256/', '/title/tt0110763/', '/title/tt0381971/', '/title/tt0375568/', '/title/tt0385700/', '/title/tt0131704/', '/title/tt0884726/', '/title/tt0414853/', '/title/tt0092695/', '/title/tt1181840/', '/title/tt0271263/', '/title/tt0312305/', '/title/tt0275277/', '/title/tt0111333/', '/title/tt0243585/', '/title/tt0112453/', '/title/tt0190641/', '/title/tt0092106/', '/title/tt0268397/', '/title/tt0104652/', '/title/tt1185616/', '/title/tt0076929/', '/title/tt1430607/', '/title/tt1384927/', '/title/tt4302938/', '/title/tt2668134/',
'/title/tt0280030/', '/title/tt0090315/', '/title/tt0308353/', '/title/tt3095734/', '/title/tt0851578/', '/title/tt4622340/', '/title/tt2911342/', '/title/tt0101329/', '/title/tt2006753/', '/title/tt0110008/', '/title/tt0070544/', '/title/tt2085930/', '/title/tt3076510/', '/title/tt0166276/', '/title/tt2908228/', '/title/tt0430779/', '/title/tt3763866/', '/title/tt1713496/', '/title/tt3262342/', '/title/tt1639826/', '/title/tt3470600/', '/title/tt0113824/', '/title/tt1816518/', '/title/tt0096866/', '/title/tt3646944/', '/title/tt2914892/', '/title/tt3717532/', '/title/tt4693418/', '/title/tt0347246/', '/title/tt0102802/', '/title/tt3513498/', '/title/tt0134067/', '/title/tt1474276/', '/title/tt0420238/', '/title/tt3655680/', '/title/tt0106364/', '/title/tt0120910/', '/title/tt0213203/', '/title/tt2398241/', '/title/tt0361089/', '/title/tt0299172/', '/title/tt2062622/', '/title/tt0105616/', '/title/tt1213012/', '/title/tt1594972/', '/title/tt0775489/', '/title/tt1107365/', '/title/tt0401233/', '/title/tt1230204/', '/title/tt0068612/',
'/title/tt0337711/', '/title/tt2210479/', '/title/tt0419724/', '/title/tt0092752/', '/title/tt3501062/', '/title/tt1629374/', '/title/tt4624424/', '/title/tt0940657/', '/title/tt3454574/', '/title/tt3576728/', '/title/tt2290828/', '/title/tt0108395/', '/title/tt0216651/', '/title/tt4426464/', '/title/tt1174954/', '/title/tt0169858/', '/title/tt0265632/', '/title/tt0313680/', '/title/tt0063823/', '/title/tt3526408/', '/title/tt0403703/', '/title/tt4075322/', '/title/tt0112389/', '/title/tt0314063/', '/title/tt0085542/', '/title/tt0293416/', '/title/tt0079833/', '/title/tt1753496/', '/title/tt2764892/', '/title/tt3915172/', '/title/tt3386244/', '/title/tt0084509/', '/title/tt1512222/', '/title/tt0808506/', '/title/tt0940656/', '/title/tt0210234/', '/title/tt0104740/', '/title/tt3529198/', '/title/tt0102587/', '/title/tt1646926/', '/title/tt0447854/', '/title/tt0858486/', '/title/tt0047834/', '/title/tt1679332/', '/title/tt0103783/', '/title/tt0386741/', '/title/tt1216516/', '/title/tt0348121/', '/title/tt1487931/', '/title/tt0844993/',
'/title/tt0482603/', '/title/tt3646946/', '/title/tt0220099/', '/title/tt4131800/', '/title/tt0851471/', '/title/tt3633118/', '/title/tt0498351/', '/title/tt2380307/', '/title/tt0330994/', '/title/tt1620449/', '/title/tt1260502/', '/title/tt3874544/', '/title/tt3748918/', '/title/tt3477554/', '/title/tt1488181/', '/title/tt0142236/', '/title/tt0099472/', '/title/tt0038166/', '/title/tt3896100/', '/title/tt0113568/', '/title/tt1791454/', '/title/tt2822672/', '/title/tt0763304/', '/title/tt0983213/', '/title/tt0985058/', '/title/tt2371399/', '/title/tt0820142/', '/title/tt0282120/', '/title/tt3246908/', '/title/tt0118829/', '/title/tt2636124/', '/title/tt1172587/', '/title/tt3656380/', '/title/tt0860907/', '/title/tt0107745/', '/title/tt2403439/', '/title/tt2859246/', '/title/tt0306474/', '/title/tt0479008/', '/title/tt0114108/', '/title/tt4272866/', '/title/tt0235679/', '/title/tt2783020/', '/title/tt0119273/', '/title/tt0041094/', '/title/tt0485323/', '/title/tt2243621/', '/title/tt1764625/', '/title/tt0058230/', '/title/tt0099733/', '/title/tt3759416/',
'/title/tt1817232/', '/title/tt0115509/', '/title/tt1235830/', '/title/tt0289408/', '/title/tt0168856/', '/title/tt1043842/', '/title/tt0098692/', '/title/tt0099878/', '/title/tt0361500/', '/title/tt1839494/', '/title/tt2358911/', '/title/tt1673702/', '/title/tt3181400/', '/title/tt4162910/', '/title/tt0142243/', '/title/tt1947964/', '/title/tt2569136/', '/title/tt0095525/', '/title/tt0339334/', '/title/tt0083951/', '/title/tt1978567/', '/title/tt0095715/', '/title/tt0259974/', '/title/tt0160429/', '/title/tt4250960/', '/title/tt4789650/', '/title/tt2288005/', '/title/tt1235837/', '/title/tt0107692/', '/title/tt3498786/', '/title/tt2981768/', '/title/tt0388473/', '/title/tt1021002/', '/title/tt2097333/', '/title/tt0114563/', '/title/tt2396690/', '/title/tt1596342/', '/title/tt0088678/', '/title/tt4181270/', '/title/tt0142242/', '/title/tt1776196/', '/title/tt1999167/', '/title/tt0142371/', '/title/tt1853614/', '/title/tt0455326/', '/title/tt0323642/', '/title/tt0091584/', '/title/tt0923811/', '/title/tt1795621/', '/title/tt0314166/',
'/title/tt0297753/', '/title/tt3392330/', '/title/tt4644382/', '/title/tt0298337/', '/title/tt0113799/', '/title/tt3028018/', '/title/tt3102994/', '/title/tt2357365/', '/title/tt2261287/', '/title/tt1540148/', '/title/tt0860906/', '/title/tt0031397/', '/title/tt0407121/', '/title/tt3579524/', '/title/tt2591814/', '/title/tt2226178/', '/title/tt1290393/', '/title/tt1483797/', '/title/tt0142241/', '/title/tt0071913/', '/title/tt1822239/', '/title/tt0082009/', '/title/tt0259308/', '/title/tt1350484/', '/title/tt0350194/', '/title/tt0071361/', '/title/tt0107875/', '/title/tt2953022/', '/title/tt0206013/', '/title/tt0086203/', '/title/tt3653650/', '/title/tt0064107/', '/title/tt2322457/', '/title/tt3915174/', '/title/tt2066048/', '/title/tt0386820/', '/title/tt0831888/', '/title/tt1429433/', '/title/tt3433910/', '/title/tt0061931/', '/title/tt0078477/', '/title/tt0039404/', '/title/tt0088885/', '/title/tt0064806/', '/title/tt1891769/', '/title/tt2320924/', '/title/tt0298388/', '/title/tt0486321/', '/title/tt0109791/', '/title/tt0070165/',
'/title/tt0103837/', '/title/tt4427230/', '/title/tt0102813/', '/title/tt1587414/', '/title/tt1321862/', '/title/tt0259929/', '/title/tt1091821/', '/title/tt1546036/', '/title/tt0034091/', '/title/tt0915463/', '/title/tt1407052/', '/title/tt3331846/', '/title/tt1867086/', '/title/tt0830861/', '/title/tt4926026/', '/title/tt0398872/', '/title/tt0069289/', '/title/tt1817721/', '/title/tt1013607/', '/title/tt1979172/', '/title/tt1748032/', '/title/tt1125254/', '/title/tt1381803/', '/title/tt3152592/', '/title/tt1876517/', '/title/tt2368672/', '/title/tt1587157/', '/title/tt4061146/', '/title/tt2085795/', '/title/tt3528906/', '/title/tt3823912/', '/title/tt3921852/', '/title/tt0086489/', '/title/tt0287635/', '/title/tt0291350/', '/title/tt0090065/', '/title/tt0040580/', '/title/tt3901826/', '/title/tt1620981/', '/title/tt3608838/', '/title/tt1047015/', '/title/tt0790799/', '/title/tt0187819/', '/title/tt1160524/', '/title/tt0142237/', '/title/tt2248068/', '/title/tt0099524/', '/title/tt2296935/', '/title/tt2095004/', '/title/tt0142233/',
'/title/tt3477172/', '/title/tt0100281/', '/title/tt0104298/', '/title/tt2404692/', '/title/tt3007600/', '/title/tt0374248/', '/title/tt0073691/', '/title/tt2328718/', '/title/tt1340803/', '/title/tt3858372/', '/title/tt1481363/', '/title/tt0137201/', '/title/tt0193253/', '/title/tt0142239/', '/title/tt0353014/', '/title/tt0142244/', '/title/tt0206367/', '/title/tt1121794/', '/title/tt0475998/', '/title/tt1609138/', '/title/tt1821680/', '/title/tt2457282/', '/title/tt1560489/', '/title/tt1709652/', '/title/tt0038718/', '/title/tt1272051/', '/title/tt4940416/', '/title/tt1460798/', '/title/tt1971466/', '/title/tt0169880/', '/title/tt2073520/', '/title/tt3794204/', '/title/tt0955411/', '/title/tt3431188/', '/title/tt0331314/', '/title/tt0080461/', '/title/tt0142238/', '/title/tt1606636/', '/title/tt0944834/', '/title/tt3422078/', '/title/tt3897080/', '/title/tt1703049/', '/title/tt0142240/', '/title/tt1109488/', '/title/tt0452039/', '/title/tt0322645/', '/title/tt0381348/', '/title/tt2551566/', '/title/tt1719665/', '/title/tt0208298/',
'/title/tt3794354/', '/title/tt2967286/', '/title/tt0368667/', '/title/tt0824696/', '/title/tt1764666/', '/title/tt2243275/', '/title/tt1537481/', '/title/tt0332318/', '/title/tt2114454/', '/title/tt0439533/', '/title/tt0324572/', '/title/tt1753427/', '/title/tt0088748/', '/title/tt0347791/', '/title/tt0057093/', '/title/tt2358913/', '/title/tt0185481/', '/title/tt0259534/', '/title/tt0100912/', '/title/tt3183630/', '/title/tt3897760/', '/title/tt0084458/', '/title/tt0119899/', '/title/tt2871776/', '/title/tt4042820/', '/title/tt0142234/', '/title/tt2709692/', '/title/tt0875609/', '/title/tt1212022/', '/title/tt0163494/', '/title/tt3726220/', '/title/tt0969345/', '/title/tt0065588/', '/title/tt1241721/', '/title/tt0275230/', '/title/tt0120254/', '/title/tt3122122/', '/title/tt1003009/', '/title/tt4016942/', '/title/tt0184041/', '/title/tt3839992/', '/title/tt0086148/', '/title/tt2312262/', '/title/tt4331400/', '/title/tt4442030/', '/title/tt1679681/', '/title/tt0117715/', '/title/tt4125300/', '/title/tt1285305/', '/title/tt3985472/',
'/title/tt0274470/', '/title/tt0765465/', '/title/tt4544468/', '/title/tt1948223/', '/title/tt0076593/', '/title/tt4168188/', '/title/tt0076591/', '/title/tt0419073/', '/title/tt1361336/', '/title/tt1744641/', '/title/tt0792986/', '/title/tt5044760/', '/title/tt0142251/', '/title/tt1056437/', '/title/tt0197633/', '/title/tt4061952/', '/title/tt3837248/', '/title/tt0090799/', '/title/tt0071203/', '/title/tt0149215/', '/title/tt3811918/', '/title/tt1941466/', '/title/tt1049406/', '/title/tt1372301/', '/title/tt0087660/', '/title/tt0131636/', '/title/tt2339505/', '/title/tt1849027/', '/title/tt3885932/', '/title/tt2078523/', '/title/tt0988982/', '/title/tt4489416/', '/title/tt2262345/', '/title/tt1308650/', '/title/tt2943352/', '/title/tt3178174/', '/title/tt4273562/', '/title/tt1433540/', '/title/tt0476680/', '/title/tt0460907/', '/title/tt0498525/', '/title/tt4219130/', '/title/tt0270933/', '/title/tt2162709/', '/title/tt2652476/', '/title/tt3780824/', '/title/tt1856053/', '/title/tt3644570/', '/title/tt3789946/', '/title/tt1715210/',
'/title/tt1086797/', '/title/tt1814809/', '/title/tt0778631/', '/title/tt0103609/', '/title/tt4676508/', '/title/tt0439123/', '/title/tt0082679/', '/title/tt1155650/', '/title/tt3198454/', '/title/tt1429430/', '/title/tt1288461/', '/title/tt3881410/', '/title/tt3017864/', '/title/tt0089984/', '/title/tt0371552/', '/title/tt1485763/', '/title/tt2722786/', '/title/tt0323869/', '/title/tt1343712/', '/title/tt0056700/', '/title/tt0089206/', '/title/tt1065099/', '/title/tt3689910/', '/title/tt1701992/', '/title/tt1206541/', '/title/tt0181627/', '/title/tt2005363/', '/title/tt4054952/', '/title/tt0078780/', '/title/tt0078915/', '/title/tt0084315/', '/title/tt0072882/', '/title/tt3486626/', '/title/tt4657400/', '/title/tt0348060/', '/title/tt1257561/', '/title/tt1220911/', '/title/tt3801316/', '/title/tt3527020/', '/title/tt1674086/', '/title/tt4057916/', '/title/tt0480507/', '/title/tt3011816/', '/title/tt0067280/', '/title/tt4150316/', '/title/tt0168473/', '/title/tt1206585/', '/title/tt2284790/', '/title/tt0094238/', '/title/tt0050987/',
'/title/tt0327660/', '/title/tt0486731/', '/title/tt2328505/', '/title/tt4307880/', '/title/tt2346354/', '/title/tt4306116/', '/title/tt0951333/', '/title/tt0930902/', '/title/tt2400433/', '/title/tt3280730/', '/title/tt1893371/', '/title/tt1703048/', '/title/tt0094269/', '/title/tt1614955/', '/title/tt1226251/', '/title/tt1403983/', '/title/tt4112930/', '/title/tt2323836/', '/title/tt3468298/', '/title/tt4143804/', '/title/tt4428398/', '/title/tt0807703/', '/title/tt4872206/', '/title/tt0094939/', '/title/tt0076119/', '/title/tt1374990/', '/title/tt4688658/', '/title/tt1756873/', '/title/tt0098598/', '/title/tt2190193/', '/title/tt2961890/', '/title/tt1172203/', '/title/tt1709801/', '/title/tt2359269/', '/title/tt0113429/', '/title/tt0084070/', '/title/tt2231208/', '/title/tt0085218/', '/title/tt1690483/', '/title/tt1305678/', '/title/tt1693039/', '/title/tt1384961/', '/title/tt2573198/', '/title/tt0217590/', '/title/tt1785394/', '/title/tt1690470/', '/title/tt1058779/', '/title/tt0073000/', '/title/tt0113234/', '/title/tt0396042/',
'/title/tt2113091/', '/title/tt0420076/', '/title/tt0187781/', '/title/tt0063668/', '/title/tt2160163/', '/title/tt0233691/', '/title/tt1828229/', '/title/tt3075214/', '/title/tt0107289/', '/title/tt1342403/', '/title/tt1739212/', '/title/tt0462699/', '/title/tt2520678/', '/title/tt0395947/', '/title/tt2397461/', '/title/tt0428646/', '/title/tt0098259/', '/title/tt3564806/', '/title/tt3257582/', '/title/tt2630134/', '/title/tt0093743/', '/title/tt1235827/', '/title/tt3740416/', '/title/tt0089877/', '/title/tt0102812/', '/title/tt0060661/', '/title/tt4337072/', '/title/tt1000095/', '/title/tt1453967/', '/title/tt0112545/', '/title/tt1827527/', '/title/tt2397521/', '/title/tt1754650/', '/title/tt0424958/', '/title/tt1754767/', '/title/tt0443771/', '/title/tt0061069/', '/title/tt1119194/', '/title/tt0435286/', '/title/tt1331294/', '/title/tt0142250/', '/title/tt1193627/', '/title/tt1545319/', '/title/tt2572056/', '/title/tt4144206/', '/title/tt1488591/', '/title/tt1355638/', '/title/tt0154587/', '/title/tt1859606/', '/title/tt4590700/',
'/title/tt0830199/', '/title/tt0059855/', '/title/tt2086830/', '/title/tt2155428/', '/title/tt0843358/', '/title/tt1071815/', '/title/tt0106417/', '/title/tt1199779/', '/title/tt2439190/', '/title/tt2555422/', '/title/tt0135037/', '/title/tt0922366/', '/title/tt2077908/', '/title/tt2296777/', '/title/tt0970472/', '/title/tt0125037/', '/title/tt3415692/', '/title/tt0144608/', '/title/tt0970933/', '/title/tt0112513/', '/title/tt2990836/', '/title/tt4460634/', '/title/tt3640382/', '/title/tt0184872/', '/title/tt4838316/', '/title/tt0120733/', '/title/tt0080772/', '/title/tt1018789/', '/title/tt1711533/', '/title/tt1709812/', '/title/tt1243946/', '/title/tt2070831/', '/title/tt0307456/', '/title/tt0083258/', '/title/tt0480082/', '/title/tt4633694/', '/title/tt2375379/', '/title/tt0396659/', '/title/tt3204012/', '/title/tt4383208/', '/title/tt3737650/', '/title/tt3685006/', '/title/tt0049847/', '/title/tt1345450/', '/title/tt2659374/', '/title/tt0488836/', '/title/tt1655413/', '/title/tt0962762/', '/title/tt1537314/', '/title/tt1239462/',
'/title/tt0015532/', '/title/tt3606504/', '/title/tt1105263/', '/title/tt0791188/', '/title/tt1587156/', '/title/tt2361846/', '/title/tt1043748/', '/title/tt1645129/', '/title/tt2374144/', '/title/tt4503906/', '/title/tt1202580/', '/title/tt1050739/', '/title/tt1618450/', '/title/tt0083701/', '/title/tt0092723/', '/title/tt2946582/', '/title/tt2458948/', '/title/tt0074121/', '/title/tt1753729/', '/title/tt0163080/', '/title/tt0372763/', '/title/tt1476250/', '/title/tt2549540/', '/title/tt1134666/', '/title/tt1754177/', '/title/tt3666024/', '/title/tt0892062/', '/title/tt0125058/', '/title/tt0072901/', '/title/tt1734135/', '/title/tt1043852/', '/title/tt0131400/', '/title/tt0054265/', '/title/tt1572781/', '/title/tt0109872/', '/title/tt2651020/', '/title/tt0065106/', '/title/tt0119346/', '/title/tt1352765/', '/title/tt3832326/', '/title/tt1856057/', '/title/tt1095423/', '/title/tt2857458/', '/title/tt0267024/', '/title/tt1984279/', '/title/tt0815096/', '/title/tt0146249/', '/title/tt0095894/', '/title/tt2642226/', '/title/tt3492042/',
'/title/tt0832449/', '/title/tt1371126/', '/title/tt0078349/', '/title/tt0455142/', '/title/tt0090249/', '/title/tt0972542/', '/title/tt0069383/', '/title/tt3079368/', '/title/tt0118138/', '/title/tt1374985/', '/title/tt0243558/', '/title/tt1683981/', '/title/tt0085390/', '/title/tt1677561/', '/title/tt0372238/', '/title/tt0885415/', '/title/tt0166948/', '/title/tt1517216/', '/title/tt0990372/', '/title/tt0122227/', '/title/tt0400771/', '/title/tt0164917/', '/title/tt1179773/', '/title/tt1039902/', '/title/tt2104985/', '/title/tt1407082/', '/title/tt1458172/', '/title/tt0078187/', '/title/tt0047930/', '/title/tt0021025/', '/title/tt3746824/', '/title/tt1869724/', '/title/tt0366621/', '/title/tt1435990/', '/title/tt0268282/', '/title/tt3480110/', '/title/tt1858441/', '/title/tt3918368/', '/title/tt2243469/', '/title/tt3198652/', '/title/tt0493247/', '/title/tt0071448/', '/title/tt1931569/', '/title/tt0029912/', '/title/tt4001614/', '/title/tt1189006/', '/title/tt0109781/', '/title/tt0301083/', '/title/tt4886780/', '/title/tt2918094/',
'/title/tt0146063/', '/title/tt2769896/', '/title/tt2205948/', '/title/tt2050664/', '/title/tt1725969/', '/title/tt3832158/', '/title/tt1891845/', '/title/tt2990702/', '/title/tt2583814/', '/title/tt3691706/', '/title/tt0093207/', '/title/tt3129656/', '/title/tt5004766/', '/title/tt1713548/', '/title/tt1541005/', '/title/tt1068773/', '/title/tt0792992/', '/title/tt0498396/', '/title/tt0088028/', '/title/tt0293849/', '/title/tt0074705/', '/title/tt1560987/', '/title/tt3455204/', '/title/tt2408734/', '/title/tt0229664/', '/title/tt1124374/', '/title/tt1468843/', '/title/tt0091862/', '/title/tt1832471/', '/title/tt0458076/', '/title/tt0460811/', '/title/tt4823776/', '/title/tt1414518/', '/title/tt0304931/', '/title/tt0315000/', '/title/tt0106421/', '/title/tt1621766/', '/title/tt0166090/', '/title/tt0365296/', '/title/tt1695770/', '/title/tt0211653/', '/title/tt0108069/', '/title/tt3630388/', '/title/tt3529342/', '/title/tt1757912/', '/title/tt4633738/', '/title/tt0437198/', '/title/tt0353261/', '/title/tt1037116/', '/title/tt2918988/',
'/title/tt0142248/', '/title/tt0357545/', '/title/tt0473658/', '/title/tt1190545/', '/title/tt2900934/', '/title/tt1042916/', '/title/tt0184005/', '/title/tt0202287/', '/title/tt0119471/', '/title/tt0033727/', '/title/tt2005281/', '/title/tt0052527/', '/title/tt0041823/', '/title/tt0415481/', '/title/tt0814243/', '/title/tt4555266/', '/title/tt0074539/', '/title/tt2948816/', '/title/tt0088334/', '/title/tt2423504/', '/title/tt4831682/', '/title/tt1978599/', '/title/tt4937208/', '/title/tt4715644/', '/title/tt0366922/', '/title/tt1946347/', '/title/tt0416908/', '/title/tt0109277/', '/title/tt2061702/', '/title/tt1891905/', '/title/tt2476096/', '/title/tt3719916/', '/title/tt0021309/', '/title/tt0800096/', '/title/tt2960524/', '/title/tt1148261/', '/title/tt2816044/', '/title/tt4877122/', '/title/tt1907625/', '/title/tt2948372/', '/title/tt0097839/', '/title/tt4501334/', '/title/tt0049367/', '/title/tt1220201/', '/title/tt2048804/', '/title/tt1485096/', '/title/tt4701724/', '/title/tt1254956/', '/title/tt3091272/', '/title/tt0145891/',
'/title/tt0100339/', '/title/tt1563776/', '/title/tt0298903/', '/title/tt0091794/', '/title/tt0498465/', '/title/tt0083931/', '/title/tt2231489/', '/title/tt0070326/', '/title/tt0142666/', '/title/tt2768084/', '/title/tt0310790/', '/title/tt2318440/', '/title/tt0064714/', '/title/tt0419704/', '/title/tt1180304/', '/title/tt2983564/', '/title/tt0208502/', '/title/tt0096869/', '/title/tt1169841/', '/title/tt0384057/', '/title/tt0174834/', '/title/tt1160525/', '/title/tt1087841/', '/title/tt0114556/', '/title/tt0176694/', '/title/tt1735221/', '/title/tt1077274/', '/title/tt0102371/', '/title/tt0122494/', '/title/tt1828224/', '/title/tt1959437/', '/title/tt0179955/', '/title/tt1686865/', '/title/tt1442223/', '/title/tt1230522/', '/title/tt1210117/', '/title/tt2317103/', '/title/tt4971484/', '/title/tt1068997/', '/title/tt0105654/', '/title/tt0491027/', '/title/tt0137204/', '/title/tt4022252/', '/title/tt0277909/', '/title/tt0443123/', '/title/tt1208658/', '/title/tt0240425/', '/title/tt0202239/', '/title/tt1687231/', '/title/tt0085394/',
'/title/tt4663760/', '/title/tt1309184/', '/title/tt0296620/', '/title/tt3306776/', '/title/tt1520368/', '/title/tt0060283/', '/title/tt0811021/', '/title/tt2898632/', '/title/tt3949650/', '/title/tt1600529/', '/title/tt2506858/', '/title/tt0448150/', '/title/tt0119170/', '/title/tt1117392/', '/title/tt4885238/', '/title/tt0119406/', '/title/tt0084881/', '/title/tt0318819/', '/title/tt0388130/', '/title/tt0124770/', '/title/tt3335192/', '/title/tt0827498/', '/title/tt3723780/', '/title/tt1909796/', '/title/tt2953050/', '/title/tt3032300/', '/title/tt2771178/', '/title/tt0083053/', '/title/tt1920885/', '/title/tt4729560/', '/title/tt0473435/', '/title/tt2171416/', '/title/tt4587656/', '/title/tt0280371/', '/title/tt0272226/', '/title/tt0872236/', '/title/tt3433622/', '/title/tt0084060/', '/title/tt0222724/', '/title/tt0091889/', '/title/tt3823116/', '/title/tt1754455/', '/title/tt2938376/', '/title/tt1999132/', '/title/tt4651660/', '/title/tt0079820/', '/title/tt1422651/', '/title/tt1010435/', '/title/tt0302758/', '/title/tt1636780/',
'/title/tt4235644/', '/title/tt2321492/', '/title/tt0133930/', '/title/tt1961324/', '/title/tt0087376/', '/title/tt2317414/', '/title/tt3593726/', '/title/tt0997274/', '/title/tt0076416/', '/title/tt1492806/', '/title/tt1334413/', '/title/tt0792978/', '/title/tt0090667/', '/title/tt4695548/', '/title/tt0158628/', '/title/tt1254656/', '/title/tt0188404/', '/title/tt1340108/', '/title/tt1703953/', '/title/tt0272183/', '/title/tt0061369/', '/title/tt1467299/', '/title/tt1613031/', '/title/tt0815890/', '/title/tt2251275/', '/title/tt0087543/', '/title/tt0075811/', '/title/tt3400214/', '/title/tt4862056/', '/title/tt1146290/', '/title/tt1577113/', '/title/tt3172162/', '/title/tt0459959/', '/title/tt0926036/', '/title/tt0056281/', '/title/tt0203237/', '/title/tt1996223/', '/title/tt0203895/', '/title/tt1468322/', '/title/tt4539114/', '/title/tt0259134/', '/title/tt1690991/', '/title/tt0301082/', '/title/tt0311618/', '/title/tt1691344/', '/title/tt2425618/', '/title/tt1793224/', '/title/tt0306646/', '/title/tt1460738/', '/title/tt0390159/',
'/title/tt1433915/', '/title/tt2194724/', '/title/tt0430377/', '/title/tt3413018/', '/title/tt0253848/', '/title/tt4007068/', '/title/tt2141789/', '/title/tt0109162/', '/title/tt0159509/', '/title/tt0091123/', '/title/tt3951368/', '/title/tt3539988/', '/title/tt0193995/', '/title/tt1018764/', '/title/tt1727860/', '/title/tt0131479/', '/title/tt1283926/', '/title/tt2936864/', '/title/tt1974262/', '/title/tt2380716/', '/title/tt2347782/', '/title/tt3438514/', '/title/tt3138698/', '/title/tt1865364/', '/title/tt0996976/', '/title/tt0067002/', '/title/tt1796564/', '/title/tt1167480/', '/title/tt1885253/', '/title/tt2752656/', '/title/tt0062687/', '/title/tt0278789/', '/title/tt4412240/', '/title/tt1245891/', '/title/tt0101927/', '/title/tt2311880/', '/title/tt0077204/', '/title/tt1071809/', '/title/tt0356577/', '/title/tt0876287/', '/title/tt1520392/', '/title/tt2355921/', '/title/tt0122735/', '/title/tt0066328/', '/title/tt3239148/', '/title/tt0220450/', '/title/tt2073154/', '/title/tt1339302/', '/title/tt0137226/', '/title/tt1651332/',
'/title/tt3595170/', '/title/tt1186365/', '/title/tt0087202/', '/title/tt1584913/', '/title/tt3205010/', '/title/tt3216346/', '/title/tt3261672/', '/title/tt0253729/', '/title/tt0161981/', '/title/tt2066110/', '/title/tt2321555/', '/title/tt4097336/', '/title/tt0067464/', '/title/tt1879017/', '/title/tt0881252/', '/title/tt2077703/', '/title/tt0456980/', '/title/tt0098189/', '/title/tt0969332/', '/title/tt0272101/', '/title/tt3157636/', '/title/tt0293854/', '/title/tt4105584/', '/title/tt1006926/', '/title/tt1720267/', '/title/tt1612776/', '/title/tt4685554/', '/title/tt0399412/', '/title/tt1710994/', '/title/tt0074657/', '/title/tt1844663/', '/title/tt0322177/', '/title/tt0296619/', '/title/tt0482500/', '/title/tt1278060/', '/title/tt3691942/', '/title/tt0203908/', '/title/tt0116728/', '/title/tt0969348/', '/title/tt3401174/', '/title/tt1274275/', '/title/tt2006291/', '/title/tt2234550/', '/title/tt2431934/', '/title/tt0805605/', '/title/tt2948358/', '/title/tt0376995/', '/title/tt0354770/', '/title/tt1395050/', '/title/tt0088983/', '/title/tt0326101/',
'/title/tt0398237/', '/title/tt0087170/', '/title/tt2109131/', '/title/tt4788934/', '/title/tt2047732/', '/title/tt0090961/', '/title/tt1874412/', '/title/tt2343130/', '/title/tt4154982/', '/title/tt4219304/', '/title/tt0053275/', '/title/tt0096842/', '/title/tt3516252/', '/title/tt1855268/', '/title/tt0170181/', '/title/tt3600950/', '/title/tt1194618/', '/title/tt0234458/', '/title/tt0081881/', '/title/tt4788606/', '/title/tt3898504/', '/title/tt4483100/', '/title/tt1087858/', '/title/tt0331711/', '/title/tt1851909/', '/title/tt0138877/', '/title/tt0140648/', '/title/tt1260351/', '/title/tt0117876/', '/title/tt0291559/', '/title/tt1922736/', '/title/tt1217042/', '/title/tt0109553/', '/title/tt0086515/', '/title/tt1990421/', '/title/tt1067920/', '/title/tt3796312/', '/title/tt0117865/', '/title/tt0965649/', '/title/tt1073223/', '/title/tt2131586/', '/title/tt0466405/', '/title/tt2124046/', '/title/tt4440370/', '/title/tt0986361/', '/title/tt0050604/', '/title/tt1401245/', '/title/tt0076931/', '/title/tt1397147/', '/title/tt1576423/',
'/title/tt0802983/', '/title/tt0089943/', '/title/tt0902265/', '/title/tt3394878/', '/title/tt3505298/', '/title/tt2364816/', '/title/tt5039360/', '/title/tt1671584/', '/title/tt2391821/', '/title/tt1381286/', '/title/tt2798620/', '/title/tt2016868/', '/title/tt1058781/', '/title/tt0097638/', '/title/tt0294590/', '/title/tt1838527/', '/title/tt3038052/', '/title/tt0907678/', '/title/tt1860308/', '/title/tt4788602/', '/title/tt1592517/', '/title/tt1385876/', '/title/tt0064961/', '/title/tt4320236/', '/title/tt2408030/', '/title/tt0443232/', '/title/tt0179829/', '/title/tt3500068/', '/title/tt0212112/', '/title/tt1726286/', '/title/tt4517624/', '/title/tt0304072/', '/title/tt0232622/', '/title/tt0202536/', '/title/tt1483849/', '/title/tt1155651/', '/title/tt0469611/', '/title/tt1807978/', '/title/tt0493306/', '/title/tt1842422/', '/title/tt2653882/', '/title/tt0295152/', '/title/tt3854192/', '/title/tt1740055/', '/title/tt0353824/', '/title/tt2240030/', '/title/tt0188506/', '/title/tt0486728/', '/title/tt4109284/', '/title/tt4766420/',
'/title/tt0166350/', '/title/tt0095262/', '/title/tt1282036/', '/title/tt1762364/', '/title/tt0378262/', '/title/tt3332410/', '/title/tt0239096/', '/title/tt1343046/', '/title/tt0307050/', '/title/tt1147513/', '/title/tt2710884/', '/title/tt1442543/', '/title/tt0265018/', '/title/tt1764329/', '/title/tt0382942/', '/title/tt2399537/', '/title/tt0044414/', '/title/tt4717482/', '/title/tt2507174/', '/title/tt0142632/', '/title/tt1578273/', '/title/tt0826570/', '/title/tt0078495/', '/title/tt0399085/', '/title/tt1840372/', '/title/tt1135522/', '/title/tt0079293/', '/title/tt1110630/', '/title/tt0062366/', '/title/tt4531412/', '/title/tt0401559/', '/title/tt4876468/', '/title/tt0295455/', '/title/tt3198316/', '/title/tt1294788/', '/title/tt0498755/', '/title/tt0082478/', '/title/tt0465967/', '/title/tt0150844/', '/title/tt0818257/', '/title/tt0493440/', '/title/tt3661394/', '/title/tt3136634/', '/title/tt2608516/', '/title/tt0238597/', '/title/tt0159568/', '/title/tt0923985/', '/title/tt0780660/', '/title/tt0240034/', '/title/tt2253947/',
'/title/tt4839424/', '/title/tt3615160/', '/title/tt2080337/', '/title/tt0167770/', '/title/tt1527821/', '/title/tt4885958/', '/title/tt0359784/', '/title/tt2402165/', '/title/tt0079475/', '/title/tt0454883/', '/title/tt0186449/', '/title/tt0348059/', '/title/tt0065021/', '/title/tt0268531/', '/title/tt1468321/', '/title/tt0327408/', '/title/tt0289171/', '/title/tt2375629/', '/title/tt0086520/', '/title/tt4008392/', '/title/tt2033933/', '/title/tt0222225/', '/title/tt1245468/', '/title/tt0067749/', '/title/tt0365659/', '/title/tt0059422/', '/title/tt3163844/', '/title/tt0363141/', '/title/tt2400379/', '/title/tt0326143/', '/title/tt3303446/', '/title/tt0090960/', '/title/tt2234530/', '/title/tt1869677/', '/title/tt3189552/', '/title/tt0075011/', '/title/tt1352802/', '/title/tt1183352/', '/title/tt3805158/', '/title/tt0238319/', '/title/tt0051694/', '/title/tt1519467/', '/title/tt0831848/', '/title/tt5006214/', '/title/tt0101583/', '/title/tt0072004/', '/title/tt3663640/', '/title/tt0082892/', '/title/tt2064704/', '/title/tt0138613/',
'/title/tt3845670/', '/title/tt3265080/', '/title/tt1531066/', '/title/tt0211627/', '/title/tt0053261/', '/title/tt2229387/', '/title/tt0135991/', '/title/tt4872166/', '/title/tt2053359/', '/title/tt0218798/', '/title/tt2752584/', '/title/tt1084680/', '/title/tt0457024/', '/title/tt1877646/', '/title/tt0435635/', '/title/tt0146457/', '/title/tt1358989/', '/title/tt1133936/', '/title/tt0110914/', '/title/tt0296281/', '/title/tt0114349/', '/title/tt1206326/', '/title/tt0155858/', '/title/tt0164724/', '/title/tt0262333/', '/title/tt2241287/', '/title/tt4899056/', '/title/tt0385668/', '/title/tt0142193/', '/title/tt4668834/', '/title/tt0091309/', '/title/tt3777936/', '/title/tt0316540/', '/title/tt0811605/', '/title/tt4544278/', '/title/tt0262264/', '/title/tt4697944/', '/title/tt0383224/', '/title/tt1442556/', '/title/tt0322918/', '/title/tt0187687/', '/title/tt0386611/', '/title/tt0100356/', '/title/tt4641828/', '/title/tt4042020/', '/title/tt2499534/', '/title/tt0926156/', '/title/tt0092916/', '/title/tt2630526/', '/title/tt0279487/',
'/title/tt2390309/', '/title/tt0204034/', '/title/tt3562846/', '/title/tt1796657/', '/title/tt0199898/', '/title/tt0114689/', '/title/tt0089793/', '/title/tt2231505/', '/title/tt0480586/', '/title/tt0096209/', '/title/tt2404027/', '/title/tt0377119/', '/title/tt1740684/', '/title/tt2513552/', '/title/tt3197486/', '/title/tt0144681/', '/title/tt0436710/', '/title/tt0086964/', '/title/tt0804905/', '/title/tt3565026/', '/title/tt0456978/', '/title/tt4298990/', '/title/tt2966696/', '/title/tt1515854/', '/title/tt1707786/', '/title/tt4556038/', '/title/tt0090658/', '/title/tt2158855/', '/title/tt2487126/', '/title/tt0093896/', '/title/tt4731008/', '/title/tt4247856/', '/title/tt3073326/', '/title/tt2125634/', '/title/tt0171357/', '/title/tt1080647/', '/title/tt2833788/', '/title/tt0066781/', '/title/tt1458167/', '/title/tt0043410/', '/title/tt1748199/', '/title/tt0258050/', '/title/tt1133935/', '/title/tt2207572/', '/title/tt1636815/', '/title/tt0342853/', '/title/tt2271315/', '/title/tt4249242/', '/title/tt1891939/', '/title/tt0459263/',
'/title/tt3739130/', '/title/tt1264885/', '/title/tt1613055/', '/title/tt0819643/', '/title/tt3740996/', '/title/tt1964540/', '/title/tt0447249/', '/title/tt0237687/', '/title/tt2463742/', '/title/tt3341536/', '/title/tt2491648/', '/title/tt0223391/', '/title/tt1155652/', '/title/tt2304957/', '/title/tt0159511/', '/title/tt1133559/', '/title/tt0300058/', '/title/tt4872210/', '/title/tt0471945/', '/title/tt0238596/', '/title/tt1176453/', '/title/tt0056060/', '/title/tt1843902/', '/title/tt2557868/', '/title/tt3341598/', '/title/tt0093101/', '/title/tt0373210/', '/title/tt3668382/', '/title/tt4714032/', '/title/tt2403867/', '/title/tt4919442/', '/title/tt0400244/', '/title/tt0782679/', '/title/tt0159508/', '/title/tt2321405/', '/title/tt0271527/', '/title/tt0434147/', '/title/tt0997084/', '/title/tt1632477/', '/title/tt0170180/', '/title/tt1672136/', '/title/tt4080760/', '/title/tt0127745/', '/title/tt3774130/', '/title/tt0092218/', '/title/tt3511362/', '/title/tt0884819/', '/title/tt0238595/', '/title/tt2375938/', '/title/tt0875155/',
'/title/tt0206827/', '/title/tt1278099/', '/title/tt1398425/', '/title/tt4766078/', '/title/tt0126189/', '/title/tt1189893/', '/title/tt3714574/', '/title/tt1948563/', '/title/tt0299040/', '/title/tt1744879/', '/title/tt0290738/', '/title/tt0484999/', '/title/tt0994794/', '/title/tt0483706/', '/title/tt2768474/', '/title/tt3687292/', '/title/tt0184596/', '/title/tt0498536/', '/title/tt0242851/', '/title/tt1775313/', '/title/tt0309827/', '/title/tt4218632/', '/title/tt0152066/', '/title/tt0092917/', '/title/tt3345138/', '/title/tt2023519/', '/title/tt0089042/', '/title/tt1039651/', '/title/tt1534332/', '/title/tt0077673/', '/title/tt3413334/', '/title/tt1291055/', '/title/tt0287351/', '/title/tt1532568/', '/title/tt0806139/', '/title/tt1873576/', '/title/tt0213159/', '/title/tt1570984/', '/title/tt0189973/', '/title/tt3324810/', '/title/tt4885924/', '/title/tt1856022/', '/title/tt1632481/', '/title/tt0087026/', '/title/tt0087925/', '/title/tt0081648/', '/title/tt2056785/', '/title/tt0059212/', '/title/tt0295848/', '/title/tt0229557/',
'/title/tt0062466/', '/title/tt3638542/', '/title/tt0102928/', '/title/tt1777620/', '/title/tt3327856/', '/title/tt0346900/', '/title/tt4067378/', '/title/tt0026793/', '/title/tt3749216/', '/title/tt1535430/', '/title/tt0129734/', '/title/tt1677709/', '/title/tt2312208/', '/title/tt3913856/', '/title/tt1920996/', '/title/tt0959324/', '/title/tt0062044/', '/title/tt0338018/', '/title/tt2592484/', '/title/tt0142080/', '/title/tt0308184/', '/title/tt4179512/', '/title/tt3435632/', '/title/tt0202095/', '/title/tt0158568/', '/title/tt0144667/', '/title/tt0185429/', '/title/tt0446701/', '/title/tt2510924/', '/title/tt1155696/', '/title/tt1934331/', '/title/tt1308100/', '/title/tt0802982/', '/title/tt0436070/', '/title/tt1773768/', '/title/tt0204704/', '/title/tt2210498/', '/title/tt0430271/', '/title/tt2404237/', '/title/tt0446958/', '/title/tt3518826/', '/title/tt0079648/', '/title/tt3205434/', '/title/tt2058651/', '/title/tt4283922/', '/title/tt2303898/', '/title/tt2333658/', '/title/tt4162986/', '/title/tt0238938/', '/title/tt1059950/',
'/title/tt2076142/', '/title/tt0205451/', '/title/tt1691454/', '/title/tt1164545/', '/title/tt0374262/', '/title/tt4385912/', '/title/tt2056607/', '/title/tt1552010/', '/title/tt3977982/', '/title/tt0452130/', '/title/tt1082598/', '/title/tt4881456/', '/title/tt0296274/', '/title/tt2330912/', '/title/tt2836400/', '/title/tt0121387/', '/title/tt4909250/', '/title/tt1261390/', '/title/tt0142307/', '/title/tt0124147/', '/title/tt0104604/', '/title/tt3171016/', '/title/tt3147562/', '/title/tt0333215/', '/title/tt0237622/', '/title/tt1638365/', '/title/tt2431032/', '/title/tt4768656/', '/title/tt0264872/', '/title/tt0363277/', '/title/tt0104623/', '/title/tt3505596/', '/title/tt1609486/', '/title/tt2041470/', '/title/tt0929265/', '/title/tt4085184/', '/title/tt3005710/', '/title/tt1734113/', '/title/tt0272299/', '/title/tt0214468/', '/title/tt4628826/', '/title/tt0499525/', '/title/tt0161122/', '/title/tt3956964/', '/title/tt0215919/', '/title/tt0095512/', '/title/tt0097067/', '/title/tt4885726/', '/title/tt0132528/', '/title/tt4809396/',
'/title/tt1415872/', '/title/tt0400817/', '/title/tt4641882/', '/title/tt0382868/', '/title/tt4839422/', '/title/tt0796232/', '/title/tt0218108/', '/title/tt1612318/', '/title/tt4449798/', '/title/tt1844036/', '/title/tt2691524/', '/title/tt0283476/', '/title/tt0132204/', '/title/tt0184881/', '/title/tt3712588/', '/title/tt0250403/', '/title/tt0294448/', '/title/tt1809274/', '/title/tt1726641/', '/title/tt0078287/', '/title/tt0254950/', '/title/tt0093251/', '/title/tt1183707/', '/title/tt0477602/', '/title/tt0112274/', '/title/tt4637028/', '/title/tt1801025/', '/title/tt0219207/', '/title/tt1731145/', '/title/tt0296161/', '/title/tt0239348/', '/title/tt0184748/', '/title/tt0104401/', '/title/tt0140349/', '/title/tt3916346/', '/title/tt0084774/', '/title/tt0300576/', '/title/tt0084564/', '/title/tt3668234/', '/title/tt0140703/', '/title/tt0060651/', '/title/tt0407924/', '/title/tt2411128/', '/title/tt0382114/', '/title/tt3072888/', '/title/tt1914320/', '/title/tt0387162/', '/title/tt4841364/', '/title/tt0159443/', '/title/tt3859060/',
'/title/tt0037731/', '/title/tt3172170/', '/title/tt1776307/', '/title/tt1087860/', '/title/tt1111358/', '/title/tt1391548/', '/title/tt0393510/', '/title/tt4767910/', '/title/tt0225346/', '/title/tt1147525/', '/title/tt0481511/', '/title/tt4666512/', '/title/tt4954660/', '/title/tt0381884/', '/title/tt0081350/', '/title/tt3758702/', '/title/tt0120691/', '/title/tt0426064/', '/title/tt0202416/', '/title/tt1649349/', '/title/tt0347458/', '/title/tt2552322/', '/title/tt3407024/', '/title/tt4970552/', '/title/tt4719118/', '/title/tt1695823/', '/title/tt1546649/', '/title/tt0377008/', '/title/tt2967094/', '/title/tt0100194/', '/title/tt1966448/', '/title/tt1224370/', '/title/tt3509482/', '/title/tt1499213/', '/title/tt4298254/', '/title/tt3203996/', '/title/tt0416873/', '/title/tt4839348/', '/title/tt0089272/', '/title/tt1655431/', '/title/tt3978744/', '/title/tt1345776/', '/title/tt2197822/', '/title/tt0007646/', '/title/tt0296074/', '/title/tt2380534/', '/title/tt0285868/', '/title/tt3338434/', '/title/tt0312941/', '/title/tt0871896/',
'/title/tt0263027/', '/title/tt0291959/', '/title/tt0029583/', '/title/tt4693318/', '/title/tt0291343/', '/title/tt0131650/', '/title/tt3422716/', '/title/tt0380724/', '/title/tt1978398/', '/title/tt2108579/', '/title/tt0311108/', '/title/tt0102184/', '/title/tt3831888/', '/title/tt3884424/', '/title/tt0060926/', '/title/tt2186751/', '/title/tt1756855/', '/title/tt1147517/', '/title/tt0306741/', '/title/tt1663145/', '/title/tt0086857/', '/title/tt2631012/', '/title/tt1233474/', '/title/tt4079954/', '/title/tt1490539/', '/title/tt3210408/', '/title/tt2708602/', '/title/tt0058734/', '/title/tt3222236/', '/title/tt0064552/', '/title/tt2260256/', '/title/tt4199898/', '/title/tt0934870/', '/title/tt1667662/', '/title/tt0297215/', '/title/tt0482925/', '/title/tt2967856/', '/title/tt4794170/', '/title/tt2287867/', '/title/tt3471272/', '/title/tt0223992/', '/title/tt1054491/', '/title/tt1265173/', '/title/tt3097924/', '/title/tt0159510/', '/title/tt0125494/', '/title/tt2160331/', '/title/tt2139689/', '/title/tt1844206/', '/title/tt2408288/', '/title/tt4204096/',
'/title/tt3095020/', '/title/tt2818724/', '/title/tt1147519/', '/title/tt2412064/', '/title/tt2322603/', '/title/tt3123864/', '/title/tt2108529/', '/title/tt0348878/', '/title/tt3465710/', '/title/tt4104140/', '/title/tt2355737/', '/title/tt1880984/', '/title/tt2572208/', '/title/tt1260575/', '/title/tt0167429/', '/title/tt0188535/', '/title/tt4157940/', '/title/tt0387472/', '/title/tt4325060/', '/title/tt1147509/', '/title/tt0331508/', '/title/tt0945355/', '/title/tt0107382/', '/title/tt0295583/', '/title/tt0130847/', '/title/tt0067179/', '/title/tt2108651/', '/title/tt0171199/', '/title/tt1394245/', '/title/tt0306444/', '/title/tt0098426/', '/title/tt0191400/', '/title/tt3174208/', '/title/tt4278144/', '/title/tt0409848/', '/title/tt0088955/', '/title/tt1930432/', '/title/tt0208663/', '/title/tt0149893/', '/title/tt0054631/', '/title/tt4664926/', '/title/tt0056461/', '/title/tt2449630/', '/title/tt2768704/', '/title/tt4773054/', '/title/tt1846607/', '/title/tt4384804/', '/title/tt0096742/', '/title/tt1343089/', '/title/tt0884832/',
'/title/tt0426315/', '/title/tt1636824/', '/title/tt2145759/', '/title/tt0136748/', '/title/tt0418867/', '/title/tt0073814/', '/title/tt4730838/', '/title/tt3896102/', '/title/tt0090834/', '/title/tt4729430/', '/title/tt0287329/', '/title/tt0295966/', '/title/tt2380283/', '/title/tt1636847/', '/title/tt4733194/', '/title/tt1821415/', '/title/tt4168022/', '/title/tt0160558/', '/title/tt2380049/', '/title/tt0430293/', '/title/tt3462678/', '/title/tt4161520/', '/title/tt0215088/', '/title/tt3204020/', '/title/tt1479690/', '/title/tt1801079/', '/title/tt0372871/', '/title/tt1294710/', '/title/tt0443769/', '/title/tt0847478/', '/title/tt3672130/', '/title/tt2450486/', '/title/tt1453242/', '/title/tt4269194/', '/title/tt1863298/', '/title/tt0109422/', '/title/tt0183902/', '/title/tt1702427/', '/title/tt1446716/', '/title/tt0076922/', '/title/tt2322316/', '/title/tt1838731/', '/title/tt0112862/', '/title/tt0397230/', '/title/tt0399778/', '/title/tt0057669/', '/title/tt1863338/', '/title/tt0475722/', '/title/tt0299878/', '/title/tt2078651/',
'/title/tt3702160/', '/title/tt0347701/', '/title/tt1537967/', '/title/tt1726846/', '/title/tt1507283/', '/title/tt1144950/', '/title/tt1692191/', '/title/tt0056125/', '/title/tt0999910/', '/title/tt4208304/', '/title/tt2034832/', '/title/tt0204541/', '/title/tt4997844/', '/title/tt1466078/', '/title/tt0183308/', '/title/tt0371962/', '/title/tt0045040/', '/title/tt0933763/', '/title/tt0364084/', '/title/tt0192803/', '/title/tt2103204/', '/title/tt3837842/', '/title/tt4766102/', '/title/tt3500764/', '/title/tt1927079/', '/title/tt1486648/', '/title/tt4738752/', '/title/tt0161979/', '/title/tt1430622/', '/title/tt0493226/', '/title/tt1279118/', '/title/tt1304591/', '/title/tt1764578/', '/title/tt4599466/', '/title/tt2996126/', '/title/tt2119579/', '/title/tt3094414/', '/title/tt1839647/', '/title/tt1706670/', '/title/tt2332523/', '/title/tt1180335/', '/title/tt1147528/', '/title/tt1382663/', '/title/tt0338176/', '/title/tt3172194/', '/title/tt0208870/', '/title/tt4466894/', '/title/tt4168024/', '/title/tt1869679/', '/title/tt1147523/',
'/title/tt0400900/', '/title/tt0242599/', '/title/tt2258054/', '/title/tt0273772/', '/title/tt0356742/', '/title/tt0145853/', '/title/tt0249817/', '/title/tt2086840/', '/title/tt0377923/', '/title/tt1873575/', '/title/tt1852151/', '/title/tt0419499/', '/title/tt4899044/', '/title/tt3967976/', '/title/tt3688056/', '/title/tt0328327/', '/title/tt2265279/', '/title/tt0274348/', '/title/tt0040215/', '/title/tt1340708/', '/title/tt1718791/', '/title/tt4333478/', '/title/tt0061062/', '/title/tt3843334/', '/title/tt1934243/', '/title/tt0152979/', '/title/tt4494382/', '/title/tt1264071/', '/title/tt3177056/', '/title/tt2772570/', '/title/tt1513762/', '/title/tt2773420/', '/title/tt1607568/', '/title/tt4439784/', '/title/tt1410243/', '/title/tt0062260/', '/title/tt0145721/', '/title/tt4183924/', '/title/tt0412879/', '/title/tt0882987/', '/title/tt0206366/', '/title/tt2742242/', '/title/tt4844146/', '/title/tt0196503/', '/title/tt0145911/', '/title/tt2309979/', '/title/tt4846282/', '/title/tt0099410/', '/title/tt0390350/', '/title/tt3490438/',
'/title/tt1147526/', '/title/tt1492954/', '/title/tt0121431/', '/title/tt2917574/', '/title/tt0104622/', '/title/tt2131626/', '/title/tt2630316/', '/title/tt1566528/', '/title/tt1147511/', '/title/tt4023452/', '/title/tt3712718/', '/title/tt3194482/', '/title/tt1015980/', '/title/tt1679583/', '/title/tt0352988/', '/title/tt0127464/', '/title/tt0819780/', '/title/tt4940426/', '/title/tt0412026/', '/title/tt2876384/', '/title/tt4264554/', '/title/tt4737774/', '/title/tt1010436/', '/title/tt0459109/', '/title/tt2950510/', '/title/tt2193273/', '/title/tt1633171/', '/title/tt1997607/', '/title/tt0264837/', '/title/tt1147522/', '/title/tt1147510/', '/title/tt1051263/', '/title/tt1457604/', '/title/tt2533166/', '/title/tt0359230/', '/title/tt0046300/', '/title/tt4863692/', '/title/tt1484065/', '/title/tt0295437/', '/title/tt1647446/', '/title/tt1890371/', '/title/tt2336326/', '/title/tt0045160/', '/title/tt0233263/', '/title/tt1864227/', '/title/tt3279464/', '/title/tt0093019/', '/title/tt0433375/', '/title/tt2479654/', '/title/tt0347070/',
'/title/tt1884320/', '/title/tt0384923/', '/title/tt3043848/', '/title/tt1894416/', '/title/tt1753493/', '/title/tt0473474/', '/title/tt0470745/', '/title/tt1201992/', '/title/tt1880341/', '/title/tt0185359/', '/title/tt0406546/', '/title/tt2275080/', '/title/tt1132622/', '/title/tt3856638/', '/title/tt1779847/', '/title/tt0124247/', '/title/tt1333039/', '/title/tt0094954/', '/title/tt0164767/', '/title/tt3308710/', '/title/tt0145672/', '/title/tt0279412/', '/title/tt1896759/', '/title/tt1682222/', '/title/tt4083096/', '/title/tt1869678/', '/title/tt1958090/', '/title/tt0260830/', '/title/tt2786258/', '/title/tt0287058/', '/title/tt4597482/', '/title/tt1149379/', '/title/tt0146253/', '/title/tt4472100/', '/title/tt3366430/', '/title/tt2323723/', '/title/tt0119493/', '/title/tt0890889/', '/title/tt0444629/', '/title/tt0122511/', '/title/tt0202393/', '/title/tt3962802/', '/title/tt1147516/', '/title/tt0374574/', '/title/tt4794852/', '/title/tt0222054/', '/title/tt0965409/', '/title/tt1519364/', '/title/tt4586644/', '/title/tt1946502/',
'/title/tt4820102/', '/title/tt3040120/', '/title/tt0442289/', '/title/tt1187005/', '/title/tt4499280/', '/title/tt1623674/', '/title/tt1380078/', '/title/tt1073670/', '/title/tt4049534/', '/title/tt0086538/', '/title/tt1388333/', '/title/tt0101418/', '/title/tt3914362/', '/title/tt1080035/', '/title/tt2709606/', '/title/tt1806784/', '/title/tt2789530/', '/title/tt2403011/', '/title/tt0202452/', '/title/tt0095448/', '/title/tt1247268/', '/title/tt2378443/', '/title/tt2069921/', '/title/tt0829238/', '/title/tt1980102/', '/title/tt0282708/', '/title/tt3234494/', '/title/tt0090244/', '/title/tt0162327/', '/title/tt0195644/', '/title/tt1147508/', '/title/tt1563153/', '/title/tt3555204/', '/title/tt1997552/', '/title/tt0471589/', '/title/tt0234337/', '/title/tt1426379/', '/title/tt0435202/', '/title/tt2457504/', '/title/tt3176926/', '/title/tt1343039/', '/title/tt1147514/', '/title/tt2382412/', '/title/tt1455676/', '/title/tt1641398/', '/title/tt1622560/', '/title/tt0422702/', '/title/tt1714199/', '/title/tt0478787/', '/title/tt0396094/',
'/title/tt0973837/', '/title/tt0245655/', '/title/tt0305179/', '/title/tt0171048/', '/title/tt2201133/', '/title/tt3499158/', '/title/tt1296149/', '/title/tt4209820/', '/title/tt4794734/', '/title/tt3880898/', '/title/tt0313990/', '/title/tt3293426/', '/title/tt2126385/', '/title/tt1147515/', '/title/tt1707688/', '/title/tt4940436/', '/title/tt0406672/', '/title/tt3106916/', '/title/tt0086160/', '/title/tt1098199/', '/title/tt0768189/', '/title/tt1588287/', '/title/tt4184350/', '/title/tt3855406/', '/title/tt2898884/', '/title/tt0769512/', '/title/tt0816640/', '/title/tt0953478/', '/title/tt4982154/', '/title/tt0871971/', '/title/tt1288380/', '/title/tt4912418/', '/title/tt4177856/', '/title/tt4885916/', '/title/tt1319554/', '/title/tt0102954/', '/title/tt3040230/', '/title/tt1400386/', '/title/tt0308577/', '/title/tt0113389/', '/title/tt0309114/', '/title/tt0095431/', '/title/tt2287172/', '/title/tt0402438/', '/title/tt2186404/', '/title/tt0269358/', '/title/tt2057399/', '/title/tt3741670/', '/title/tt4538366/', '/title/tt3714950/',
'/title/tt0326522/', '/title/tt0063852/', '/title/tt2067027/', '/title/tt1137438/', '/title/tt1401255/', '/title/tt1147521/', '/title/tt3435652/', '/title/tt1734178/', '/title/tt1980133/', '/title/tt0829177/', '/title/tt0156463/', '/title/tt0823511/', '/title/tt0332029/', '/title/tt0889170/', '/title/tt4468650/', '/title/tt2118024/', '/title/tt3277512/', '/title/tt0097411/', '/title/tt0030636/', '/title/tt1147518/', '/title/tt1733139/', '/title/tt0356201/', '/title/tt0988142/', '/title/tt3250872/', '/title/tt4487076/', '/title/tt2404375/', '/title/tt3709868/', '/title/tt2766104/', '/title/tt3715848/', '/title/tt2111383/', '/title/tt0415906/', '/title/tt0269112/', '/title/tt0185337/', '/title/tt1147520/', '/title/tt4346600/', '/title/tt1966486/', '/title/tt2350500/', '/title/tt2330832/', '/title/tt2535654/', '/title/tt0161978/', '/title/tt4171600/', '/title/tt4738728/', '/title/tt1316074/', '/title/tt0298109/', '/title/tt2219554/', '/title/tt3818692/', '/title/tt0201183/', '/title/tt0375141/', '/title/tt3158366/', '/title/tt2368783/',
'/title/tt0190270/', '/title/tt1147527/', '/title/tt0249991/', '/title/tt2860742/', '/title/tt0033399/', '/title/tt0189171/', '/title/tt0212261/', '/title/tt2257994/', '/title/tt2506270/', '/title/tt0243136/', '/title/tt3689894/', '/title/tt0295667/', '/title/tt2980596/', '/title/tt1525803/', '/title/tt1371638/', '/title/tt1912530/', '/title/tt0241436/', '/title/tt4656772/', '/title/tt0191563/', '/title/tt1663667/', '/title/tt3791746/', '/title/tt3565744/', '/title/tt0314923/', '/title/tt1657293/', '/title/tt0072316/', '/title/tt2294521/', '/title/tt1231288/', '/title/tt0271042/', '/title/tt1361317/', '/title/tt4258716/', '/title/tt0356362/', '/title/tt1587216/', '/title/tt0127552/', '/title/tt0109057/', '/title/tt3971764/', '/title/tt3072736/', '/title/tt1907648/', '/title/tt1239461/', '/title/tt2241224/', '/title/tt1038033/', '/title/tt2846622/', '/title/tt0296504/', '/title/tt0341601/', '/title/tt0211310/', '/title/tt3454148/', '/title/tt4439950/', '/title/tt2959216/', '/title/tt1844664/', '/title/tt3574822/', '/title/tt2851954/',
'/title/tt4400926/', '/title/tt0263118/', '/title/tt1869458/', '/title/tt0936472/', '/title/tt2837694/', '/title/tt1163842/', '/title/tt5002078/', '/title/tt1825692/', '/title/tt3573796/', '/title/tt3732474/', '/title/tt1691923/', '/title/tt0271719/', '/title/tt0119260/', '/title/tt0276265/', '/title/tt0114425/', '/title/tt1218026/', '/title/tt0295943/', '/title/tt1843957/', '/title/tt0146275/', '/title/tt0164564/', '/title/tt1630606/', '/title/tt0862815/', '/title/tt0208997/', '/title/tt2220674/', '/title/tt4556264/', '/title/tt2170474/', '/title/tt1954687/', '/title/tt2369119/', '/title/tt1436561/', '/title/tt3604664/', '/title/tt0096353/', '/title/tt4126486/', '/title/tt0116114/', '/title/tt0169951/', '/title/tt1550321/', '/title/tt0784145/', '/title/tt1238732/', '/title/tt0238357/', '/title/tt0180585/', '/title/tt1625545/', '/title/tt0416781/', '/title/tt2101491/', '/title/tt1966449/', '/title/tt0215479/', '/title/tt0202463/', '/title/tt2167725/', '/title/tt3210994/', '/title/tt3969864/', '/title/tt0092141/', '/title/tt2296044/',
'/title/tt2761510/', '/title/tt2335908/', '/title/tt0283107/', '/title/tt4731504/', '/title/tt1059944/', '/title/tt4864886/', '/title/tt0177422/', '/title/tt1033485/', '/title/tt0098077/', '/title/tt4001526/', '/title/tt0334890/', '/title/tt0251985/', '/title/tt1822358/', '/title/tt0295608/', '/title/tt2572014/', '/title/tt4165384/', '/title/tt1324057/', '/title/tt0363704/', '/title/tt0156279/', '/title/tt2411590/', '/title/tt4779206/', '/title/tt5004778/', '/title/tt0395970/', '/title/tt1231574/', '/title/tt3343120/', '/title/tt0400652/', '/title/tt0452226/', '/title/tt0178501/', '/title/tt1454032/', '/title/tt4768918/', '/title/tt1199467/', '/title/tt0214867/', '/title/tt1252601/', '/title/tt0325798/', '/title/tt2251513/', '/title/tt0418602/', '/title/tt0287941/', '/title/tt0332410/', '/title/tt0419954/', '/title/tt0191280/', '/title/tt2179678/', '/title/tt3557294/', '/title/tt0093118/', '/title/tt1313120/', '/title/tt0079102/', '/title/tt0334205/', '/title/tt0294677/', '/title/tt3981582/', '/title/tt1316090/', '/title/tt1827386/',
'/title/tt0445683/', '/title/tt0251670/', '/title/tt1977865/', '/title/tt0156945/', '/title/tt1647467/', '/title/tt1947979/', '/title/tt1548621/', '/title/tt2987316/', '/title/tt2545064/', '/title/tt0271510/', '/title/tt0212599/', '/title/tt0312767/', '/title/tt0179657/', '/title/tt2371337/', '/title/tt3508188/', '/title/tt0247061/', '/title/tt1619890/', '/title/tt1538294/', '/title/tt2156981/', '/title/tt0062224/', '/title/tt0830822/', '/title/tt1296563/', '/title/tt0218288/', '/title/tt2384892/', '/title/tt4253212/', '/title/tt0367172/', '/title/tt2627630/', '/title/tt4863768/', '/title/tt0145943/', '/title/tt2133306/', '/title/tt1326140/', '/title/tt1832515/', '/title/tt4354284/', '/title/tt0239494/', '/title/tt0496595/', '/title/tt0147033/', '/title/tt0997248/', '/title/tt2022564/', '/title/tt4253190/', '/title/tt3953388/', '/title/tt2966560/', '/title/tt2566866/', '/title/tt4819166/', '/title/tt3751278/', '/title/tt1336982/', '/title/tt0790735/', '/title/tt4225410/', '/title/tt0252025/', '/title/tt4266688/', '/title/tt0227528/',
'/title/tt4769824/', '/title/tt2180443/', '/title/tt1865375/', '/title/tt1786454/', '/title/tt1160710/', '/title/tt3364946/', '/title/tt2791442/', '/title/tt4936426/', '/title/tt1483748/', '/title/tt4357590/', '/title/tt0090760/', '/title/tt1725007/', '/title/tt3037136/', '/title/tt1826959/', '/title/tt4560966/', '/title/tt0345600/', '/title/tt2657636/', '/title/tt2435154/', '/title/tt1745702/', '/title/tt4994884/', '/title/tt0829187/', '/title/tt0293093/', '/title/tt3741636/', '/title/tt1844665/', '/title/tt1379057/', '/title/tt2306873/', '/title/tt2235575/', '/title/tt0135559/', '/title/tt0190940/', '/title/tt1833743/', '/title/tt0820054/', '/title/tt0142851/', '/title/tt0160775/', '/title/tt4824274/', '/title/tt1308730/', '/title/tt3139310/', '/title/tt0226851/', '/title/tt0055150/', '/title/tt4153828/', '/title/tt1732650/', '/title/tt0127458/', '/title/tt0442247/', '/title/tt0127331/', '/title/tt0284238/', '/title/tt0291046/', '/title/tt1954293/', '/title/tt2321301/', '/title/tt1225899/', '/title/tt4942202/', '/title/tt3154906/',
'/title/tt0151590/', '/title/tt0103178/', '/title/tt4442090/', '/title/tt3159278/', '/title/tt4001642/', '/title/tt0457998/', '/title/tt2042642/', '/title/tt1976589/', '/title/tt2279314/', '/title/tt1776055/', '/title/tt0198602/', '/title/tt4289332/', '/title/tt4513762/', '/title/tt1851873/', '/title/tt4717402/', '/title/tt1660362/', '/title/tt1330053/', '/title/tt3747944/', '/title/tt1753984/', '/title/tt1473336/', '/title/tt0491646/', '/title/tt0442507/', '/title/tt1283286/', '/title/tt0196502/', '/title/tt2732078/', '/title/tt1966450/', '/title/tt0422875/', '/title/tt2033956/', '/title/tt1487280/', '/title/tt4429160/', '/title/tt2390339/', '/title/tt0286565/', '/title/tt0287547/', '/title/tt0352312/', '/title/tt2193271/', '/title/tt1737726/', '/title/tt3635770/', '/title/tt3014376/', '/title/tt0131629/', '/title/tt0258438/', '/title/tt1805326/', '/title/tt1585572/', '/title/tt3969866/', '/title/tt3596856/', '/title/tt1430605/', '/title/tt1214993/', '/title/tt1537726/', '/title/tt4330400/', '/title/tt0115581/', '/title/tt4367562/',
'/title/tt3454108/', '/title/tt1754233/', '/title/tt1287507/', '/title/tt1920939/', '/title/tt1147524/', '/title/tt0062616/', '/title/tt2164058/', '/title/tt0218606/', '/title/tt4108588/', '/title/tt0366606/', '/title/tt0431684/', '/title/tt1987649/', '/title/tt1268854/', '/title/tt4851798/', '/title/tt0488584/', '/title/tt4130788/', '/title/tt0142971/', '/title/tt0276226/', '/title/tt3745954/', '/title/tt0187189/', '/title/tt2034122/', '/title/tt3043830/', '/title/tt0427580/', '/title/tt3283754/', '/title/tt0373866/', '/title/tt2231095/', '/title/tt1318849/', '/title/tt2220024/', '/title/tt4361020/', '/title/tt0065544/', '/title/tt2859222/', '/title/tt1521839/', '/title/tt4559258/', '/title/tt1432168/', '/title/tt1171260/', '/title/tt1280036/', '/title/tt3859350/', '/title/tt0274681/', '/title/tt3557580/', '/title/tt0430403/', '/title/tt2368717/', '/title/tt2856874/', '/title/tt4955564/', '/title/tt0406197/', '/title/tt0119450/', '/title/tt0055246/', '/title/tt0020825/', '/title/tt1878842/', '/title/tt0219214/', '/title/tt3712490/',
'/title/tt1753855/', '/title/tt0496296/', '/title/tt0360887/', '/title/tt4278346/', '/title/tt3685268/', '/title/tt0009619/', '/title/tt0204199/', '/title/tt1753757/', '/title/tt0146290/', '/title/tt1147512/', '/title/tt1085759/', '/title/tt4534598/', '/title/tt0184653/', '/title/tt0160869/', '/title/tt0299619/', '/title/tt0291061/', '/title/tt0127470/', '/title/tt2189738/', '/title/tt0208252/', '/title/tt0212114/', '/title/tt1101040/', '/title/tt0844353/', '/title/tt1989523/', '/title/tt0188992/', '/title/tt3758690/', '/title/tt1887784/', '/title/tt2836354/', '/title/tt2993424/', '/title/tt0158658/', '/title/tt0291727/', '/title/tt1872871/', '/title/tt2238140/', '/title/tt1135485/', '/title/tt2234345/', '/title/tt0220053/', '/title/tt2609556/', '/title/tt0092167/', '/title/tt3747852/', '/title/tt3950710/', '/title/tt0209086/', '/title/tt2027211/', '/title/tt1826687/', '/title/tt0284075/', '/title/tt0232686/', '/title/tt4461370/', '/title/tt4500214/', '/title/tt0486893/', '/title/tt1690442/', '/title/tt0451769/', '/title/tt4132834/',
'/title/tt3984234/', '/title/tt0216859/', '/title/tt0065434/', '/title/tt0205281/', '/title/tt3505254/', '/title/tt0220996/', '/title/tt0209394/', '/title/tt1713475/', '/title/tt2343633/', '/title/tt3665916/', '/title/tt3415332/', '/title/tt0131472/', '/title/tt0774530/', '/title/tt1508662/', '/title/tt0286468/', '/title/tt0038541/', '/title/tt0063120/', '/title/tt4557900/', '/title/tt0346514/', '/title/tt0336952/', '/title/tt1107334/', '/title/tt1547014/', '/title/tt3249118/', '/title/tt0236421/', '/title/tt0164240/', '/title/tt1865541/', '/title/tt2660104/', '/title/tt0054662/', '/title/tt2460448/', '/title/tt0145710/', '/title/tt2690678/', '/title/tt0066783/', '/title/tt2098658/', '/title/tt1796619/', '/title/tt0127333/', '/title/tt4838278/', '/title/tt0468812/', '/title/tt0932930/', '/title/tt0067286/', '/title/tt0338748/', '/title/tt2887968/', '/title/tt1580005/', '/title/tt0293778/', '/title/tt0059272/', '/title/tt0085483/', '/title/tt0174201/', '/title/tt0476308/', '/title/tt1999166/', '/title/tt3347120/', '/title/tt0174324/',
'/title/tt1190683/', '/title/tt2216582/', '/title/tt0272228/', '/title/tt1786430/', '/title/tt0166721/', '/title/tt0806053/', '/title/tt4942216/', '/title/tt2504572/', '/title/tt3923472/', '/title/tt0115968/', '/title/tt4762698/', '/title/tt0351853/', '/title/tt4587956/', '/title/tt2094154/', '/title/tt4121090/', '/title/tt2378113/', '/title/tt0043163/', '/title/tt1601178/', '/title/tt2233356/', '/title/tt1711005/', '/title/tt4620592/', '/title/tt2010966/', '/title/tt1430628/', '/title/tt0056482/', '/title/tt2353722/', '/title/tt1614343/', '/title/tt1670262/', '/title/tt0146273/', '/title/tt4086028/', '/title/tt1690441/', '/title/tt1988546/', '/title/tt5029776/', '/title/tt0459131/', '/title/tt0126074/', '/title/tt0170134/', '/title/tt1519469/', '/title/tt0405096/', '/title/tt0159387/', '/title/tt1500718/', '/title/tt1160937/', '/title/tt4806378/', '/title/tt3892702/', '/title/tt1492701/', '/title/tt0441319/', '/title/tt2237888/', '/title/tt1708424/', '/title/tt0145694/', '/title/tt1966498/', '/title/tt0211065/', '/title/tt2498062/',
'/title/tt0142636/', '/title/tt1759743/', '/title/tt0226552/', '/title/tt2165561/', '/title/tt2865766/', '/title/tt0126669/', '/title/tt4641736/', '/title/tt0208069/', '/title/tt0454561/', '/title/tt0286578/', '/title/tt0356836/', '/title/tt4832952/', '/title/tt0127332/', '/title/tt0145866/', '/title/tt4776994/', '/title/tt0218170/', '/title/tt1679593/', '/title/tt1454628/', '/title/tt0156411/', '/title/tt0218159/', '/title/tt1803226/', '/title/tt1986206/', '/title/tt2324726/', '/title/tt1827469/', '/title/tt0158113/', '/title/tt0424488/', '/title/tt2194760/', '/title/tt1185646/', '/title/tt1345460/', '/title/tt2291794/', '/title/tt0064560/', '/title/tt2400688/', '/title/tt0876226/', '/title/tt2365574/', '/title/tt0092054/', '/title/tt0204365/', '/title/tt0979942/', '/title/tt3715846/', '/title/tt0250406/', '/title/tt3407994/', '/title/tt3895474/', '/title/tt4815784/', '/title/tt1740147/', '/title/tt3887158/', '/title/tt1207645/', '/title/tt0237400/', '/title/tt0295983/', '/title/tt0266462/', '/title/tt0368373/', '/title/tt4871162/',
'/title/tt2075132/', '/title/tt0415052/', '/title/tt0185389/', '/title/tt0222820/', '/title/tt1817230/', '/title/tt1411700/', '/title/tt3466682/', '/title/tt3224156/', '/title/tt4529784/', '/title/tt0277955/', '/title/tt0074631/', '/title/tt1368061/', '/title/tt0408636/', '/title/tt4785642/', '/title/tt1278035/', '/title/tt0131621/', '/title/tt1568836/', '/title/tt2193269/', '/title/tt4733578/', '/title/tt0275876/', '/title/tt4883574/', '/title/tt0124031/', '/title/tt0389076/', '/title/tt0330830/', '/title/tt2046099/', '/title/tt1862489/', '/title/tt0119399/', '/title/tt0163514/', '/title/tt2820354/', '/title/tt2180441/', '/title/tt1996392/', '/title/tt1930285/', '/title/tt0161107/', '/title/tt0063475/', '/title/tt1937337/', '/title/tt0200613/', '/title/tt1984276/', '/title/tt1842364/', '/title/tt0191629/', '/title/tt0431838/', '/title/tt3036576/', '/title/tt1757846/', '/title/tt1849915/', '/title/tt4540620/', '/title/tt0044086/', '/title/tt0250950/', '/title/tt0188530/', '/title/tt0296162/', '/title/tt0145655/', '/title/tt0228064/',
'/title/tt0252095/', '/title/tt3777398/', '/title/tt0312874/', '/title/tt4948104/', '/title/tt0064561/', '/title/tt0388820/', '/title/tt1118683/', '/title/tt3469670/', '/title/tt2265305/', '/title/tt1935913/', '/title/tt1086280/', '/title/tt3916760/', '/title/tt3654180/', '/title/tt0287470/', '/title/tt3758350/', '/title/tt4793326/', '/title/tt0200223/', '/title/tt1844786/', '/title/tt1215847/', '/title/tt1703945/', '/title/tt0412677/', '/title/tt0145779/', '/title/tt1606383/', '/title/tt3833714/', '/title/tt4921074/', '/title/tt0170374/', '/title/tt4410000/', '/title/tt0295950/', '/title/tt0094205/', '/title/tt2794560/', '/title/tt3892682/', '/title/tt0356937/', '/title/tt1351113/', '/title/tt0306849/', '/title/tt4454336/', '/title/tt0041139/', '/title/tt0138069/', '/title/tt3751700/', '/title/tt3883968/', '/title/tt0276319/', '/title/tt1844787/', '/title/tt0829089/', '/title/tt4126926/', '/title/tt3007238/', '/title/tt1937323/', '/title/tt2736876/', '/title/tt0189231/', '/title/tt1059812/', '/title/tt4387006/', '/title/tt2442294/',
'/title/tt1075365/', '/title/tt0824323/', '/title/tt4164722/', '/title/tt0213292/', '/title/tt0230442/', '/title/tt0307237/', '/title/tt2040434/', '/title/tt0036766/', '/title/tt1857883/', '/title/tt0184516/', '/title/tt1189083/', '/title/tt1000758/', '/title/tt4733692/', '/title/tt3861384/', '/title/tt3267466/', '/title/tt2356478/', '/title/tt2380281/', '/title/tt0271872/', '/title/tt0219380/', '/title/tt4651382/', '/title/tt2390267/', '/title/tt0050410/', '/title/tt0206743/', '/title/tt3852432/', '/title/tt0062965/', '/title/tt1454020/', '/title/tt1989574/', '/title/tt4685636/', '/title/tt1268853/', '/title/tt0323469/', '/title/tt0820129/', '/title/tt1260507/', '/title/tt1723025/', '/title/tt0161730/', '/title/tt0022068/', '/title/tt0065364/', '/title/tt0356026/', '/title/tt4522974/', '/title/tt0091880/', '/title/tt0312694/', '/title/tt1660319/', '/title/tt0233001/', '/title/tt0284632/', '/title/tt0129297/', '/title/tt0405474/', '/title/tt2141927/', '/title/tt1671576/', '/title/tt3756580/', '/title/tt2836140/', '/title/tt0278332/',
'/title/tt1407273/', '/title/tt4781308/', '/title/tt1773063/', '/title/tt0335350/', '/title/tt0201190/', '/title/tt0239634/', '/title/tt3804810/', '/title/tt4920290/', '/title/tt1621835/', '/title/tt2700240/', '/title/tt3692090/', '/title/tt4441760/', '/title/tt1711505/', '/title/tt1220673/', '/title/tt0286927/', '/title/tt0351045/', '/title/tt1927094/', '/title/tt0158300/', '/title/tt3433600/', '/title/tt1178592/', '/title/tt1976562/', '/title/tt1539999/', '/title/tt2435400/', '/title/tt1966446/', '/title/tt0014140/', '/title/tt0079258/', '/title/tt2638036/', '/title/tt0110906/', '/title/tt1941509/', '/title/tt0065953/', '/title/tt1636827/', '/title/tt3468304/', '/title/tt3818654/', '/title/tt0217484/', '/title/tt0213268/', '/title/tt2120764/', '/title/tt4568970/', '/title/tt0365510/', '/title/tt2106600/', '/title/tt1821608/', '/title/tt2361155/', '/title/tt0064956/', '/title/tt1661872/', '/title/tt2281336/', '/title/tt0209448/', '/title/tt4415478/', '/title/tt0146361/', '/title/tt2119558/', '/title/tt0219418/', '/title/tt2008534/',
'/title/tt2911406/', '/title/tt3905716/', '/title/tt0212115/', '/title/tt1616179/', '/title/tt4643142/', '/title/tt1630601/', '/title/tt0170095/', '/title/tt5017974/', '/title/tt4691334/', '/title/tt1935890/', '/title/tt4818944/', '/title/tt4557690/', '/title/tt0055439/', '/title/tt0036852/', '/title/tt4522038/', '/title/tt2876446/', '/title/tt4265532/', '/title/tt0217452/', '/title/tt0814296/', '/title/tt0495289/', '/title/tt3973682/', '/title/tt0112946/', '/title/tt0278307/', '/title/tt1127218/', '/title/tt4135650/', '/title/tt0150366/', '/title/tt1189084/', '/title/tt0186721/', '/title/tt0175647/', '/title/tt0145676/', '/title/tt1880287/', '/title/tt0466198/', '/title/tt1836837/', '/title/tt0276073/', '/title/tt1934342/', '/title/tt0145677/', '/title/tt0810043/', '/title/tt0371676/', '/title/tt1814830/', '/title/tt2388212/', '/title/tt1413256/', '/title/tt0829134/', '/title/tt0056294/', '/title/tt4729312/', '/title/tt0146347/', '/title/tt1692083/', '/title/tt2156911/', '/title/tt2846156/', '/title/tt1408117/', '/title/tt0288549/',
'/title/tt0227517/', '/title/tt0016351/', '/title/tt0297455/', '/title/tt2357467/', '/title/tt1164584/', '/title/tt4582100/', '/title/tt0037730/', '/title/tt0339041/', '/title/tt0284184/', '/title/tt3253744/', '/title/tt0353369/', '/title/tt0355692/', '/title/tt0346914/', '/title/tt0190006/', '/title/tt0206353/', '/title/tt3520212/', '/title/tt4875954/', '/title/tt3007766/', '/title/tt0769760/', '/title/tt0217306/', '/title/tt0373818/', '/title/tt1021087/', '/title/tt0090240/', '/title/tt0146010/', '/title/tt1827387/', '/title/tt3014580/', '/title/tt2063773/', '/title/tt0294886/', '/title/tt2147335/', '/title/tt4332764/', '/title/tt0224564/', '/title/tt4298420/', '/title/tt0457341/', '/title/tt2117996/', '/title/tt2079563/', '/title/tt1557519/', '/title/tt0221440/', '/title/tt1189080/', '/title/tt0342701/', '/title/tt1337718/', '/title/tt1171264/', '/title/tt3438478/', '/title/tt3848896/', '/title/tt1459037/', '/title/tt3133172/', '/title/tt1743341/', '/title/tt0344293/', '/title/tt4126876/', '/title/tt3781004/', '/title/tt3844756/',
'/title/tt1756835/', '/title/tt0145899/', '/title/tt0086224/', '/title/tt0166227/', '/title/tt3871940/', '/title/tt0295409/', '/title/tt0810964/', '/title/tt3405166/', '/title/tt0117937/', '/title/tt0300227/', '/title/tt0146349/', '/title/tt4541680/', '/title/tt0781012/', '/title/tt2224477/', '/title/tt3364162/', '/title/tt0494043/', '/title/tt4203832/', '/title/tt0205971/', '/title/tt1806816/', '/title/tt2534642/', '/title/tt4835618/', '/title/tt2022528/', '/title/tt3424100/', '/title/tt1644694/', '/title/tt1593692/', '/title/tt3995732/', '/title/tt0452821/', '/title/tt0218382/', '/title/tt0263826/', '/title/tt0374091/', '/title/tt0259284/', '/title/tt0025137/', '/title/tt2599928/', '/title/tt1876229/', '/title/tt4139506/', '/title/tt4641286/', '/title/tt0419165/', '/title/tt2856442/', '/title/tt1747913/', '/title/tt4488876/', '/title/tt1928341/', '/title/tt4693398/', '/title/tt4001678/', '/title/tt4624814/', '/title/tt0145675/', '/title/tt3924046/', '/title/tt0185757/', '/title/tt0169626/', '/title/tt0217483/', '/title/tt0229834/',
'/title/tt1187007/', '/title/tt0968334/', '/title/tt4920090/', '/title/tt0317444/', '/title/tt4283240/', '/title/tt0133936/', '/title/tt3226634/', '/title/tt2572226/', '/title/tt0368305/', '/title/tt0127030/', '/title/tt0196839/', '/title/tt0208453/', '/title/tt0420173/', '/title/tt1866142/', '/title/tt0209058/', '/title/tt0052067/', '/title/tt1714907/', '/title/tt0039746/', '/title/tt0202977/', '/title/tt0146246/', '/title/tt3140658/', '/title/tt4581522/', '/title/tt3775590/', '/title/tt2658190/', '/title/tt2475772/', '/title/tt0146329/', '/title/tt1950327/', '/title/tt0254957/', '/title/tt1849772/', '/title/tt0156787/', '/title/tt0931283/', '/title/tt0320282/', '/title/tt2114488/', '/title/tt0196911/', '/title/tt2750736/', '/title/tt0386127/', '/title/tt4539628/', '/title/tt2277196/', '/title/tt2572196/', '/title/tt1872160/', '/title/tt0295659/', '/title/tt2827532/', '/title/tt0140832/', '/title/tt1685648/', '/title/tt1754150/', '/title/tt0145671/', '/title/tt0252057/', '/title/tt0259611/', '/title/tt4898124/', '/title/tt1845789/',
'/title/tt0333656/', '/title/tt0146324/', '/title/tt1918789/', '/title/tt3981120/', '/title/tt1615025/', '/title/tt4660628/', '/title/tt3503074/', '/title/tt3914106/', '/title/tt1703076/', '/title/tt3878490/', '/title/tt1189081/', '/title/tt1171265/', '/title/tt0449634/', '/title/tt1686680/', '/title/tt0358013/', '/title/tt0088188/', '/title/tt0355325/', '/title/tt3999322/', '/title/tt3534078/', '/title/tt4204452/', '/title/tt0218938/', '/title/tt3673898/', '/title/tt0173735/', '/title/tt4357142/', '/title/tt0239657/', '/title/tt4613722/', '/title/tt0461603/', '/title/tt0472415/', '/title/tt1830553/', '/title/tt0027712/', '/title/tt4130762/', '/title/tt2858544/', '/title/tt0306133/', '/title/tt1532410/', '/title/tt0116412/', '/title/tt4534480/', '/title/tt2462452/', '/title/tt2856848/', '/title/tt1942927/', '/title/tt3186878/', '/title/tt0274919/', '/title/tt1867067/', '/title/tt0056318/', '/title/tt1592504/', '/title/tt0037202/', '/title/tt0037222/', '/title/tt0368921/', '/title/tt0146001/', '/title/tt0037729/', '/title/tt3871950/',
'/title/tt0277032/', '/title/tt0065113/', '/title/tt2329968/', '/title/tt1840933/', '/title/tt4642964/', '/title/tt1948614/', '/title/tt0196884/', '/title/tt1032925/', '/title/tt0226373/', '/title/tt1492851/', '/title/tt4109240/', '/title/tt3767066/', '/title/tt2836404/', '/title/tt0406830/', '/title/tt0040013/', '/title/tt4691348/', '/title/tt4613758/', '/title/tt3089632/', '/title/tt0294674/', '/title/tt1319629/', '/title/tt4678116/', '/title/tt0437799/', '/title/tt4318716/', '/title/tt0145927/', '/title/tt1412706/', '/title/tt0281789/', '/title/tt1887672/', '/title/tt0225604/', '/title/tt2120103/', '/title/tt2555494/', '/title/tt1927007/', '/title/tt0099285/', '/title/tt3273260/', '/title/tt3628012/', '/title/tt0311538/', '/title/tt0236451/', '/title/tt0230229/', '/title/tt0145864/', '/title/tt2908488/', '/title/tt2141749/', '/title/tt0143286/', '/title/tt3730256/', '/title/tt2630930/', '/title/tt2383480/', '/title/tt0176697/', '/title/tt0131591/', '/title/tt0884830/', '/title/tt0038149/', '/title/tt0145728/', '/title/tt4714256/',
'/title/tt0129411/', '/title/tt0230426/', '/title/tt1352809/', '/title/tt2889078/', '/title/tt0347319/', '/title/tt3410034/', '/title/tt1386652/', '/title/tt0356936/', '/title/tt3842606/', '/title/tt0310749/', '/title/tt0022855/', '/title/tt1147507/', '/title/tt1492151/', '/title/tt0218169/', '/title/tt0061885/', '/title/tt0419472/', '/title/tt2441426/', '/title/tt0202706/', '/title/tt0217616/', '/title/tt0145646/', '/title/tt0037905/', '/title/tt4135300/', '/title/tt0283962/', '/title/tt2509428/', '/title/tt0145801/', '/title/tt0115592/', '/title/tt4045320/', '/title/tt2128413/', '/title/tt0218384/', '/title/tt0226100/', '/title/tt0145850/', '/title/tt4689936/', '/title/tt0107345/', '/title/tt4571742/', '/title/tt1541057/', '/title/tt3309172/', '/title/tt0311439/', '/title/tt0308220/', '/title/tt0034539/', '/title/tt0176889/', '/title/tt0353803/', '/title/tt0219382/', '/title/tt0037647/', '/title/tt2399527/', '/title/tt0389077/', '/title/tt0207111/', '/title/tt3950500/', '/title/tt0202966/', '/title/tt0156646/', '/title/tt4681974/',
'/title/tt4339226/', '/title/tt0156534/', '/title/tt4002296/', '/title/tt0342179/', '/title/tt0210381/', '/title/tt3004630/', '/title/tt0310111/', '/title/tt2979978/', '/title/tt0378100/', '/title/tt1839567/', '/title/tt0390165/', '/title/tt0086094/', '/title/tt4651380/', '/title/tt0291211/', '/title/tt0295900/', '/title/tt2643796/', '/title/tt0145743/', '/title/tt2007358/', '/title/tt1298836/', '/title/tt0318736/', '/title/tt1757767/', '/title/tt0145654/', '/title/tt4800520/', '/title/tt1650438/', '/title/tt4982156/', '/title/tt3468300/', '/title/tt0014304/', '/title/tt0145888/', '/title/tt0100245/', '/title/tt4164744/', '/title/tt0347318/', '/title/tt0357450/', '/title/tt1458908/', '/title/tt0222783/', '/title/tt1399070/', '/title/tt2644722/', '/title/tt0385141/', '/title/tt0065433/', '/title/tt0120713/', '/title/tt2166109/', '/title/tt0127539/', '/title/tt0240996/', '/title/tt0218418/', '/title/tt3324068/', '/title/tt1174992/', '/title/tt0009469/', '/title/tt3407996/', '/title/tt0078983/', '/title/tt1966447/', '/title/tt0259746/',
'/title/tt1868090/', '/title/tt3668554/', '/title/tt0100737/', '/title/tt0210654/', '/title/tt1158253/', '/title/tt1187013/', '/title/tt0258059/', '/title/tt0204309/', '/title/tt0375148/', '/title/tt2261230/', '/title/tt1956456/', '/title/tt2621194/', '/title/tt0458779/', '/title/tt0021427/', '/title/tt4519530/', '/title/tt2244618/', '/title/tt4877086/', '/title/tt4583796/', '/title/tt1988674/', '/title/tt1047882/', '/title/tt0145735/', '/title/tt1576379/', '/title/tt0298980/', '/title/tt1991145/', '/title/tt0219421/', '/title/tt3912856/', '/title/tt2411156/', '/title/tt4601006/', '/title/tt2861550/', '/title/tt3755716/', '/title/tt0140701/', '/title/tt2714788/', '/title/tt0156816/', '/title/tt0486095/', '/title/tt1158281/', '/title/tt0146285/', '/title/tt3661342/', '/title/tt0390164/', '/title/tt1819706/', '/title/tt0452860/', '/title/tt0356423/', '/title/tt0338178/', '/title/tt0069034/', '/title/tt0203879/', '/title/tt3757838/', '/title/tt1620728/', '/title/tt2305025/', '/title/tt0162329/', '/title/tt2072118/', '/title/tt0100367/',
'/title/tt1857954/', '/title/tt1663150/', '/title/tt2626772/', '/title/tt1379670/', '/title/tt3876928/', '/title/tt0282259/', '/title/tt0304230/', '/title/tt0270598/', '/title/tt0473271/', '/title/tt3342056/', '/title/tt4571702/', '/title/tt1511371/', '/title/tt0129551/', '/title/tt1817290/', '/title/tt0342947/', '/title/tt2919466/', '/title/tt0145658/', '/title/tt1857822/', '/title/tt1473393/', '/title/tt0219231/', '/title/tt0937401/', '/title/tt0111634/', '/title/tt3517948/', '/title/tt0339256/', '/title/tt0040083/', '/title/tt0212116/', '/title/tt0356146/', '/title/tt0230078/', '/title/tt0353358/', '/title/tt3293808/', '/title/tt1401235/', '/title/tt4572342/', '/title/tt0344350/', '/title/tt3912854/', '/title/tt3588478/', '/title/tt0086152/', '/title/tt0015830/', '/title/tt0138067/', '/title/tt0046297/', '/title/tt4562088/', '/title/tt0036853/', '/title/tt1321410/', '/title/tt0496522/', '/title/tt3319148/', '/title/tt0904040/', '/title/tt1948039/', '/title/tt0224175/', '/title/tt4071012/', '/title/tt1711438/', '/title/tt0411189/',
'/title/tt2278518/', '/title/tt3579420/', '/title/tt0156664/', '/title/tt0029851/', '/title/tt0818924/', '/title/tt1858527/', '/title/tt2564760/', '/title/tt3915054/', '/title/tt0356024/', '/title/tt0219777/', '/title/tt0270265/', '/title/tt0244560/', '/title/tt0146129/', '/title/tt2292957/', '/title/tt0244507/', '/title/tt1109651/', '/title/tt3460724/', '/title/tt2413696/', '/title/tt0173406/', '/title/tt4316022/', '/title/tt3859712/', '/title/tt2225362/', '/title/tt3688952/', '/title/tt1369684/', '/title/tt0102560/', '/title/tt1683496/', '/title/tt0100964/', '/title/tt3079670/', '/title/tt5013284/', '/title/tt2130320/', '/title/tt3745490/', '/title/tt0270611/', '/title/tt1942109/', '/title/tt0342153/', '/title/tt0327306/', '/title/tt2931968/', '/title/tt3842620/', '/title/tt2506390/', '/title/tt0157020/', '/title/tt3519512/', '/title/tt0156505/', '/title/tt0348496/', '/title/tt4632916/', '/title/tt2442028/', '/title/tt0373996/', '/title/tt0369308/', '/title/tt1773800/', '/title/tt0354588/', '/title/tt0226978/', '/title/tt0120677/',
'/title/tt0284094/', '/title/tt0238391/', '/title/tt0176405/', '/title/tt0145772/', '/title/tt1788392/', '/title/tt0270510/', '/title/tt3922686/', '/title/tt0156811/', '/title/tt0364491/', '/title/tt1401204/', '/title/tt2343441/', '/title/tt2334592/', '/title/tt1796740/', '/title/tt0105427/', '/title/tt2084012/', '/title/tt4899582/', '/title/tt2327462/', '/title/tt0348495/', '/title/tt0062667/', '/title/tt2403476/', '/title/tt0008840/', '/title/tt0270468/', '/title/tt3852404/', '/title/tt3158482/', '/title/tt3444716/', '/title/tt0259282/', '/title/tt0498519/', '/title/tt1341194/', '/title/tt2510822/', '/title/tt4622576/', '/title/tt0276465/', '/title/tt2666388/', '/title/tt2009504/', '/title/tt3710822/', '/title/tt2070641/', '/title/tt0374552/', '/title/tt0259310/', '/title/tt2320718/', '/title/tt1092581/', '/title/tt2555514/', '/title/tt4653378/', '/title/tt1502811/', '/title/tt0321566/', '/title/tt2575990/', '/title/tt0026156/', '/title/tt0130812/', '/title/tt2400361/', '/title/tt0270251/', '/title/tt3662694/', '/title/tt3656252/',
'/title/tt0270224/', '/title/tt0347317/', '/title/tt4677288/', '/title/tt0037654/', '/title/tt0134187/', '/title/tt0120644/', '/title/tt0131485/', '/title/tt0478788/', '/title/tt1716778/', '/title/tt2058669/', '/title/tt1284996/', '/title/tt0295341/', '/title/tt2317165/', '/title/tt1418201/', '/title/tt2997076/', '/title/tt2281571/', '/title/tt3007608/', '/title/tt0295711/', '/title/tt1532395/', '/title/tt3945666/', '/title/tt0374280/', '/title/tt4123100/', '/title/tt3268404/', '/title/tt1186220/', '/title/tt1245450/', '/title/tt2846426/', '/title/tt1865490/', '/title/tt2878484/', '/title/tt0041606/', '/title/tt1277735/', '/title/tt3776604/', '/title/tt0024840/', '/title/tt0259285/', '/title/tt0196678/', '/title/tt0303318/', '/title/tt0169898/', '/title/tt0183654/', '/title/tt1780834/', '/title/tt0259246/', '/title/tt4837114/', '/title/tt0308717/', '/title/tt0350682/', '/title/tt0041611/', '/title/tt2455354/', '/title/tt0177247/', '/title/tt0270527/', '/title/tt1619815/', '/title/tt0259283/', '/title/tt1245753/', '/title/tt4046308/',
'/title/tt0312821/', '/title/tt0065952/', '/title/tt0335861/', '/title/tt0022874/', '/title/tt0215624/', '/title/tt2188356/', '/title/tt3462802/', '/title/tt1458549/', '/title/tt4087098/', '/title/tt0360790/', '/title/tt1105775/', '/title/tt0494032/', '/title/tt1857791/', '/title/tt1746196/', '/title/tt0146251/', '/title/tt0181884/', '/title/tt3375382/', '/title/tt4531046/', '/title/tt0224087/', '/title/tt4454788/', '/title/tt0353242/', '/title/tt0037834/', '/title/tt0139661/', '/title/tt0399245/', '/title/tt0145755/', '/title/tt0172633/', '/title/tt1303748/', '/title/tt0037203/', '/title/tt4569480/', '/title/tt0347445/', '/title/tt0316846/', '/title/tt0206571/', '/title/tt0041401/', '/title/tt3624632/', '/title/tt3239604/', '/title/tt0061797/', '/title/tt1538477/', '/title/tt0308217/', '/title/tt0961185/', '/title/tt0478450/', '/title/tt0285060/', '/title/tt3579428/', '/title/tt2897368/', '/title/tt0286904/', '/title/tt2089672/', '/title/tt4087962/', '/title/tt0146260/', '/title/tt3505928/', '/title/tt4986230/', '/title/tt1493228/',
'/title/tt0220462/', '/title/tt0316699/', '/title/tt2107737/', '/title/tt4248220/', '/title/tt0226761/', '/title/tt0169899/', '/title/tt1346384/', '/title/tt0109212/', '/title/tt2789674/', '/title/tt3318526/', '/title/tt4670968/', '/title/tt0037322/', '/title/tt0314041/', '/title/tt1606599/', '/title/tt4837182/', '/title/tt0237646/', '/title/tt2750492/', '/title/tt0134774/', '/title/tt0145930/', '/title/tt1112289/', '/title/tt0356726/', '/title/tt4871748/', '/title/tt1176940/', '/title/tt2714780/', '/title/tt2336213/', '/title/tt3652668/', '/title/tt0269788/', '/title/tt0244592/', '/title/tt0230462/', '/title/tt2543538/', '/title/tt4603202/', '/title/tt1286509/', '/title/tt0065435/', '/title/tt3920220/', '/title/tt1843864/', '/title/tt3867870/', '/title/tt0498493/', '/title/tt3645582/', '/title/tt4128402/', '/title/tt1473064/', '/title/tt2490110/', '/title/tt0036850/', '/title/tt1532426/', '/title/tt1974368/', '/title/tt2375039/', '/title/tt3465534/', '/title/tt0276132/', '/title/tt2009445/', '/title/tt0036848/', '/title/tt0039385/',
'/title/tt0310929/', '/title/tt0423316/', '/title/tt0180390/', '/title/tt0145956/', '/title/tt0224114/', '/title/tt0301085/', '/title/tt0240318/', '/title/tt2424520/', '/title/tt3816214/', '/title/tt2234555/', '/title/tt1186219/', '/title/tt0230548/', '/title/tt1971517/', '/title/tt0172535/', '/title/tt2339958/', '/title/tt4898940/', '/title/tt0172922/', '/title/tt0944960/', '/title/tt0270657/', '/title/tt0204600/', '/title/tt0333714/', '/title/tt2932720/', '/title/tt0155288/', '/title/tt3516222/', '/title/tt0145941/', '/title/tt0023648/', '/title/tt0268880/', '/title/tt0270410/', '/title/tt0270237/', '/title/tt1391648/', '/title/tt1315980/', '/title/tt3835438/', '/title/tt4543872/', '/title/tt3329422/', '/title/tt4696626/', '/title/tt2265673/', '/title/tt2231465/', '/title/tt5028140/', '/title/tt1270478/', '/title/tt1396674/', '/title/tt2973542/', '/title/tt3808878/', '/title/tt2756602/', '/title/tt0146311/', '/title/tt1189033/', '/title/tt2819148/', '/title/tt1567370/', '/title/tt0172951/', '/title/tt4007056/', '/title/tt3684412/',
'/title/tt0385907/', '/title/tt4691340/', '/title/tt4991780/', '/title/tt0264438/', '/title/tt3281862/', '/title/tt1784487/', '/title/tt0422446/', '/title/tt0036854/', '/title/tt3495266/', '/title/tt3582072/', '/title/tt2619074/', '/title/tt4735924/', '/title/tt0364458/', '/title/tt0297997/', '/title/tt1957952/', '/title/tt4797286/', '/title/tt0286848/', '/title/tt0146362/', '/title/tt4579020/', '/title/tt4501428/', '/title/tt0497397/', '/title/tt1990284/', '/title/tt1356933/', '/title/tt4126480/', '/title/tt1989450/', '/title/tt0145650/', '/title/tt1951234/', '/title/tt0423315/', '/title/tt0037201/', '/title/tt3407982/', '/title/tt2011215/', '/title/tt1171258/', '/title/tt4104962/', '/title/tt4287160/', '/title/tt4424602/', '/title/tt3851982/', '/title/tt3314908/', '/title/tt4525406/', '/title/tt1865354/', '/title/tt4642966/', '/title/tt0156539/', '/title/tt4457910/', '/title/tt3564384/', '/title/tt0259945/', '/title/tt3377744/', '/title/tt0140089/', '/title/tt1710570/', '/title/tt0310117/', '/title/tt4357692/', '/title/tt0212581/',
'/title/tt3255606/', '/title/tt0373184/', '/title/tt2075199/', '/title/tt0379945/', '/title/tt0253870/', '/title/tt1189085/', '/title/tt0270705/', '/title/tt1586540/', '/title/tt2580474/', '/title/tt3484160/', '/title/tt0145875/', '/title/tt0145843/', '/title/tt3215618/', '/title/tt4818942/', '/title/tt0145717/', '/title/tt0284587/', '/title/tt1062381/', '/title/tt4843742/', '/title/tt4806428/', '/title/tt2246727/', '/title/tt0145973/', '/title/tt2428144/', '/title/tt3707390/', '/title/tt3293420/', '/title/tt3159254/', '/title/tt3817058/', '/title/tt4915594/', '/title/tt0334051/', '/title/tt4968090/', '/title/tt0325179/', '/title/tt0380678/', '/title/tt0099911/', '/title/tt1831837/', '/title/tt0196547/', '/title/tt4670000/', '/title/tt1446181/', '/title/tt1189082/', '/title/tt4577440/', '/title/tt4774922/', '/title/tt1787105/', '/title/tt0270409/', '/title/tt4416372/', '/title/tt2505470/', '/title/tt0099748/', '/title/tt0491980/', '/title/tt3864104/', '/title/tt1813344/', '/title/tt3554004/', '/title/tt3866872/', '/title/tt0300105/',
'/title/tt0356147/', '/title/tt0037200/', '/title/tt3615204/', '/title/tt5070094/', '/title/tt0109182/', '/title/tt0356025/', '/title/tt3223948/', '/title/tt4522944/', '/title/tt0176833/', '/title/tt1090343/', '/title/tt0258642/', '/title/tt0338245/', '/title/tt3428188/', '/title/tt5053128/', '/title/tt4280556/', '/title/tt1640109/', '/title/tt5061124/', '/title/tt4814366/', '/title/tt5061302/', '/title/tt1072747/', '/title/tt0387334/', '/title/tt3438202/', '/title/tt2427458/', '/title/tt0234208/', '/title/tt0259206/', '/title/tt1664684/', '/title/tt3605702/', '/title/tt1242464/', '/title/tt1337611/', '/title/tt5014378/', '/title/tt3847328/', '/title/tt4457378/', '/title/tt4464516/', '/title/tt0205740/', '/title/tt0266230/', '/title/tt2146678/', '/title/tt5062520/', '/title/tt4008950/', '/title/tt0036849/', '/title/tt1107335/', '/title/tt1993354/']


# In[5]:

big_link_list = list(set(big_link_list))


# In[6]:

len(big_link_list)


# In[11]:

def get_mv_urls(link_list):
    mv_url_list = []
    imdb = 'http://www.imdb.com'
    for mvid in link_list:
        mv_url = imdb+mvid
        mv_url_list.append(mv_url)
    return mv_url_list
    pickle_it(mv_url_list,'mv_url_list.pkl')

#get_mv_urls(big_link_list)


# In[13]:

mv_url_list = load_pickle('mv_url_list.pkl') #USE THIS LIST FOR INDIVIDUAL MOVIE LINKS


# In[15]:

len(mv_url_list)


# In[422]:




# In[423]:




# In[27]:

def get_imdb_header(imdb_soup):
    imdb_header = imdb_soup.title
    return imdb_header
imdb_soup = get_imdb_soup('http://www.imdb.com/title/tt5062520/')
imdb_header = get_imdb_header(imdb_soup)


# In[28]:

imdb_header


# In[17]:

def get_imdb_title(imdb_header):
    header = imdb_header.text
    imdb_title = header.split('(')[0]
    try:
        return imdb_title
    except(ValueError,RuntimeError, TypeError, NameError):
        return None

    
#get_imdb_title(imdb_header)  


# In[18]:

def get_imdb_year(imdb_header):
    header = imdb_header.text
    year = re.findall(r'\d+', header)
    try:
        imdb_year = int(year[0])
        return imdb_year
    except(ValueError, RuntimeError, TypeError, NameError, IndexError):
        return None
        
    
#get_imdb_year(imdb_header)


# In[20]:

def get_imdb_budget(soup):
        divs = [x.text for x in mv_soup.find_all('div')]
        try:    
            for s in divs:
                start = 'Budget:'
                end = ' '
                result = re.findall('%s(.*)%s' % (start, end), s)
                for n in result:
                    regex = re.compile(r'\d+(?:,\d+)*')
                    bgt = re.findall(regex,n)
                    budget =[x.replace(',','') for x in bgt]
                    budint =[int(b) for b in budget]
                return budint[0]
        except(ValueError, RuntimeError, TypeError, NameError):
            return None
                    
                

#get_imdb_budget(mv_soup)      


# In[21]:

def get_imdb_openingwknd(soup):
        divs = [x.text for x in mv_soup.find_all('div')]
        for s in divs:
            start = 'Opening Weekend:'
            end = ' '
            result = re.findall('%s(.*)%s' % (start, end), s)
            for n in result:
                regex = re.compile(r'\d+(?:,\d+)*')
                opnwknd = re.findall(regex,n)
                openwknd =[x.replace(',','') for x in opnwknd]
                openingwknd =[int(b) for b in openwknd]
        try:
            return openingwknd[0]
        except(ValueError, RuntimeError, TypeError, NameError):
            pass
                    
                

#get_imdb_openingwknd(mv_soup)      


# In[22]:

def get_imdb_gross(soup):
        divs = [x.text for x in mv_soup.find_all('div')]
        for s in divs:
            start = 'Gross:'
            end = ' '
            result = re.findall('%s(.*)%s' % (start, end), s)
            for n in result:
                regex = re.compile(r'\d+(?:,\d+)*')
                grs = re.findall(regex,n)
                grss =[x.replace(',','') for x in grs]
                gross =[int(b) for b in grss]
        try:
            return gross[0]
        except(ValueError, RuntimeError, TypeError, NameError):
            return None
                    
                
#get_imdb_gross(mv_soup)      


# In[23]:

def get_imdb_runtime(soup):
    try:
        mvlen = soup.time
        mvtime = mvlen.text
        runtime = re.findall(r'\d+', mvtime)
        imdb_runtime = int(runtime[0])
        return imdb_runtime
    except(ValueError, RuntimeError, TypeError, NameError, AttributeError):
        return None
    
                    
                
#get_imdb_runtime(mv_soup)   


# In[24]:

def get_imdb_releasedate(soup):
    try:
        imdb_releasedate = soup.find(itemprop = 'datePublished')['content']
        #from dateutil.parse import *
        return parse(imdb_releasedate)
    except(ValueError, RuntimeError, TypeError, NameError, KeyError):
        return None
#get_imdb_releasedate(mv_soup)


# In[25]:

def get_imdb_metascore(soup):
    a = soup.find_all('a')[90].text    
    try:
        metascore = int(a.split('/')[0])
        return metascore
    except(RuntimeError, TypeError, NameError,ValueError):
        return None
    

#get_imdb_metascore(mv_soup)


# In[ ]:




# In[ ]:




# In[ ]:




# In[631]:

base_url = 'http://www.imdb.com/search/title?genres=animation&sort=moviemeter,asc&start=1&title_type=feature'


# In[ ]:




# In[633]:

mwsp = get_imdb_soup(base_url)
mv_link_list = []
for a in mwsp.find_all('a'):
    if ('/title/tt' in a['href']) & (len(a['href']) == 17):
        mv_link_list.append(a['href'])
print list(set(mv_link_list))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[756]:

mv_url_id = get_mv_urls(big_link_list) #list of movie url ID's to feed into 
for url in mv_url_id:
    print url


# In[703]:




# In[750]:

# Pickling functions
def pickle_it(data, filename):
    with open(filename, "wb") as picklefile:
        pickle.dump(data, picklefile)

def load_pickle(filename):
    with open(filename, "rb") as picklefile: 
        return pickle.load(picklefile)


# In[702]:

url = 'http://www.imdb.com/title/tt2096673/'


# In[774]:

def get_mv_data(mv_id_list):
    mv_data_list = []
    count = 0
    headlabels = ['Title', 'Year', 'Budget', 'OpeningWkd','Gross','Runtime', 'ReleaseDate','Metascore']
    for mv_urlID in mv_id_list: #iterates through movie id urls
        mv_soup = get_imdb_soup(mv_urlID)
        mv_header = get_imdb_header(mv_soup)
        mv_title = get_imdb_title(mv_header)
        mv_year = get_imdb_year(mv_header)
        mv_budget = get_imdb_budget(mv_soup)
        mv_openingwknd = get_imdb_openingwknd(mv_soup)
        mv_gross = get_imdb_gross(mv_soup)
        mv_runtime = get_imdb_runtime(mv_soup)
        mv_releasedate = get_imdb_releasedate(mv_soup)
        mv_metascore = get_imdb_metascore(mv_soup)
        mv_data_dict = dict(zip(headlabels, [mv_title, mv_year, mv_budget, mv_openingwknd, mv_gross, mv_runtime, mv_releasedate, mv_metascore]))
        count+=1
        mv_data_list.append(mv_data_dict)
        if count%500 == 0 or count%4192==0:
            pickle_it(mv_data_list, 'imdbdata.pkl')
            load_pickle('imdbdata.pkl')
    return mv_data_list


imdb_fulldata = get_mv_data(mv_url_id)


# In[533]:

mv_soup = get_imdb_soup(url)
mv_header = get_imdb_header(mv_soup)
mv_title = get_imdb_title(mv_header)
mv_year = get_imdb_year(mv_header)
mv_budget = get_imdb_budget(mv_soup)
mv_openingwknd = get_imdb_openingwknd(mv_soup)
mv_gross = get_imdb_gross(mv_soup)
mv_runtime = get_imdb_runtime(mv_soup)
mv_releasedate = get_imdb_releasedate(mv_soup)
mv_metascore = get_imdb_metascore(mv_soup)
print mv_header
print mv_title
print mv_year
print mv_budget
print mv_openingwknd
print mv_gross
print mv_runtime
print mv_releasedate
print mv_metascore


# In[ ]:




# In[769]:

len(load_pickle('imdb_data.pkl'))


# In[773]:

load_pickle('imdb_fulldata.pkl')


# In[ ]:




# In[ ]:



