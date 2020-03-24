import requests
from lxml import etree
from urllib.parse import quote
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}

def searchbook(nr1):  # 输入搜索内容
    try:
        nr1 = quote(nr1.encode('GBK'))
        url = "https://www.x23qb.com/search.php?searchkey=%s" % nr1
        xqq = requests.post(url, headers=header, timeout=10)
        xqq.encoding = 'gbk'
        if xqq.status_code != 200:
            print("code:" + xqq.status_code)
            return ''
        tree = etree.HTML(xqq.text)
        mzz = tree.xpath('//div[@class="d_title"]/h1/text()')
        if mzz != []:
            jjz = tree.xpath('//div[@id="bookintro"]/p[1]/text()')[0]
            jjj = []
            jjj.append(jjz.replace('\xa0\xa0\xa0\xa0', '').strip('&lt;&gt;').replace('\n', ''))
            zt = tree.xpath('//*[@id="count"]/ul/li[3]/span/text()')
            sj = tree.xpath('//*[@id="uptime"]/span/text()')
            mz = tree.xpath('//div[@class="d_title"]/h1/text()')
            fm = tree.xpath('//*[@id="bookimg"]/img/@src')
            zz = tree.xpath('//span[@class="p_author"]/a/text()')
            xq = tree.xpath('//*[@id="ogurl"]/@content')
            zx = tree.xpath('//*[@id="newlist"]/ul[1]/li[1]/a/text()')
            lx = tree.xpath('//*[@id="count"]/ul/li[1]/span/text()')
        else:
            xq = tree.xpath('//*[@id="nr"]/dd[1]/h3/a/@href')
            mz = tree.xpath('//*[@id="nr"]/dd[1]/h3/a/text()')
            fm = tree.xpath('//*[@id="nr"]/dt/a/img/@_src')
            js = tree.xpath('//*[@id="nr"]/dd[3]/text()')
            jjj = []
            for i in js:
                jjj.append(i.replace('\n    ', '').strip().replace('\n', ''))
            zx = tree.xpath('//dd[@class="book_other"]/a/text()')
            sj = tree.xpath('//span[@class="uptime"]/text()')
            zz = tree.xpath('//*[@id="wrapper"]/div/div/div/div/p[1]/span[2]/text()')
            lx = tree.xpath('//dd[@class="book_other"]/span[1]/text()')
            zt = tree.xpath('//*[@id="nr"]/dd[2]/span[2]/text()')
        z6 = []
        for (i, o, p, z, x, c, l, u) in zip(mz, xq, fm, jjj, zx, sj, lx, zt):
            z6.append(
                {'name': i, 'url':  o, 'cover': p, 'introduce': z, 'time': c, 'num': x, 'tag': l, 'status': u})
        sult={}
        sult['list']=z6
        return sult
    except:
        return ''
def bookdetail (url):#给页面地址，解出所有章名和地址
  try:
    tt = []
    xqq = requests.get(url,headers=header,timeout=10)
    xqq.encoding='gbk'
    if xqq.status_code != 200:
        print("code:" + xqq.status_code)
        return ''
    tree = etree.HTML(xqq.text)
    mz = tree.xpath('//*[@id="chapterList"]/li/a/text()')
    js = tree.xpath('//*[@id="chapterList"]/li/a/@href')
    jjz = tree.xpath('//div[@id="bookintro"]/p[1]/text()')[0]
    jj = jjz.replace('\xa0\xa0\xa0\xa0','').strip('&lt;&gt;').replace('\n','')
    zt = tree.xpath('//*[@id="count"]/ul/li[3]/span/text()')[0]
    sj = tree.xpath('//*[@id="uptime"]/span/text()')[0]
    mzz = tree.xpath('//div[@class="d_title"]/h1/text()')[0]
    fm = tree.xpath('//*[@id="bookimg"]/img/@src')[0]
    zz = tree.xpath('//span[@class="p_author"]/a/text()')[0]
    zx = tree.xpath('//*[@id="newlist"]/ul[1]/li[1]/a/text()')[0]
    lx = tree.xpath('//*[@id="count"]/ul/li[1]/span/text()')[0]
    mzjs = {'data':{'time':sj,'status':zt,'introduce':jj,'name':mzz,'cover':fm,'num':zx,'tag':lx,'author':zz}}
    mzjss = []
    for (i,o) in zip(mz,js):
      mzjss.append({'num':i,'url':o})
    mzjs['list']=mzjss
    return mzjs
  except:
    return ''


def bookcontent(urll):  # 给章回地址，进入内容
        try:
            url = "https://www.x23qb.com" + urll
            yss = requests.get(url, headers=header, timeout=10)
            yss.encoding = 'gbk'
            if yss.status_code != 200:
                print("code:" + yss.status_code)
                return ''
            tree = etree.HTML(yss.text)
            nrr = tree.xpath('//*[@class="read-content"]/text()')
            nr = []
            re=[]
            for i in nrr:
                nr.append(i.replace('\n', ''))
            for i in nr:
                if i.replace(' ', '') == '\n' or i == '\n   ' or i.strip() == '':
                    nr.remove(i)
            for i in nr:
                re.append(i.replace('    ', ''))
            bt = tree.xpath('//div[@id="mlfy_main_text"]/h1/text()')[0]
            nrr = {'content': re[1:], 'num': bt}
            return nrr
        except:
            return ''
def booksort(detail):
    try:
        url = "https://www.x23qb.com" + detail
        yss = requests.get(url, headers=header, timeout=10)
        yss.encoding = 'gbk'
        if yss.status_code != 200:
            print("code:" + yss.status_code)
            return ''
        tree = etree.HTML(yss.text)
        urls=tree.xpath('//*[@id="sitebox"]/dl/dd[1]/h3/a/@href')
        titles=tree.xpath('//*[@id="sitebox"]/dl/dd[1]/h3/a/text()')
        covers=tree.xpath('//*[@id="sitebox"]/dl/dt/a/img/@_src')
        types=tree.xpath('//*[@id="sitebox"]/dl/dd[2]/span[1]/text()')
        statues=tree.xpath('//*[@id="sitebox"]/dl/dd[2]/span[2]/text()')
        textsizes=tree.xpath('//*[@id="sitebox"]/dl/dd[2]/span[3]/text()')
        lastupdatas=tree.xpath('//*[@id="sitebox"]/dl/dd[4]/a/text()')
        lastupdatalinks=tree.xpath('//*[@id="sitebox"]/dl/dd[4]/a/@href')
        introduces=tree.xpath('//*[@id="sitebox"]/dl/dd[3]/text()')
        updatatimes=tree.xpath('//*[@id="sitebox"]/dl/dd[1]/h3/span/text()')
        sult=[]
        for (url,title,cover,type,statue,textsize,lastupdata,lastupdatalink,introduce,updatatime) in zip(urls,titles,covers,types,statues,textsizes,lastupdatas,lastupdatalinks,introduces,updatatimes):
            sult.append({'url':url,'title':title,'cover':cover,'type':type,'statue':statue,'textsize':textsize,'lastupdata':lastupdata,'lastupdatalink':lastupdatalink,'introduce':introduce,'updatatime':updatatime})
        ret={}
        ret['list']=sult
        return ret
    except:
        return ''
def book_rank():
    try:
        url = "https://www.x23qb.com/paihang.html"
        yss = requests.get(url, headers=header, timeout=5)
        yss.encoding = 'gbk'
        if yss.status_code != 200:
            print("code:"+yss.status_code)
            return ''
        tree = etree.HTML(yss.text)
        block=tree.xpath('//div[contains(@class,"mbottom") or contains(@class,"index_toplist") ]')
        sult=[]
        for res in block:
            sultt = []
            zhits=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/span[1]/text()')
            znums=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/span[2]/text()')
            ztype=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/span[3]/text()')
            zhref=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/a/@href')
            ztitle=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/a/text()')
            yhits=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][2]//li/span[1]/text()')
            ynums=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][2]//li/span[2]/text()')
            ytype=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][2]//li/span[3]/text()')
            yhref = res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][2]//li/a/@href')
            ytitle = res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][2]//li/a/text()')
            thits=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][3]//li/span[1]/text()')
            tnums=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][3]//li/span[2]/text()')
            ttype=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][3]//li/span[3]/text()')
            thref = res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][3]//li/a/@href')
            ttitle = res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][3]//li/a/text()')
            for (zh,zn,zt,zl,ztx,yh,yn,yt,yl,ytx,th,tn,tt,tl,ttx) in zip(zhits,znums,ztype,zhref,ztitle,yhits,ynums,ytype,yhref,ytitle,thits,tnums,ttype,thref,ttitle):
                sultt.append({'z_hit':zh,'z_num':zn,'z_type':zt,'z_href':zl,'z_title':ztx,'y_hit':yh,'y_num':yn,'y_type':yt,'y_href':yl,'y_title':ytx,'t_hit':th,'t_num':tn,'t_type':tt,'t_href':tl,'t_title':ttx})
            sult.append(sultt)
            ase=[]
            for ie in sult:
                ase.append({'ranklist':ie})
            ret = {}
            ret['list'] = ase
        return ret
    except:
        return ''
def book_rank2():
    try:
        url = "https://www.x23qb.com/paihang.html"
        yss = requests.get(url, headers=header, timeout=10)
        yss.encoding = 'gbk'
        if yss.status_code != 200:
            print("code:" + yss.status_code)
            return ''
        tree = etree.HTML(yss.text)
        block=tree.xpath('//div[@id="main"]//div[contains(@class,"toplist")]')[8:]
        sult=[]
        for res in block:
            sultt = []
            zhits=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/span[1]/text()')
            znums=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/span[2]/text()')
            ztype=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/span[3]/text()')
            zhref=res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/a/@href')
            ztitle = res.xpath('.//div[contains(@class,"topbooks") or contains(@class,"topbook")][1]//li/a/text()')

            for (zh,zn,zt,zl,ztitle) in zip(zhits,znums,ztype,zhref,ztitle):
                sultt.append({'z_hit':zh,'z_num':zn,'z_type':zt,'z_href':zl,'z_title':ztitle})
            sult.append(sultt)
            ase = []
            for ie in sult:
                ase.append({'ranklist': ie})
            ret = {}
            ret['list'] = ase
        return ret
    except:
        return ''
if __name__ == '__main__':
    # print(searchbook("系统"))
    # print(bookdetail('https://www.x23qb.com/book/106037/'))
    # print(bookcontent('/book/7936/4247123.html'))
    # print(booksort('/yanqing/1/'))
    print(book_rank())
    print(book_rank2())