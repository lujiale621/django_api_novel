from django.shortcuts import render
from django.http import  HttpResponse
import polls.src.novel1 as nv1
from django.views.generic import View
import json
def index(request):
    print("index")
    return HttpResponse("Hello you're at the polls index")
class dealer():
    def dealres(self,msg):
        ms = {}
        filt = len(str(msg))
        if filt < 20:
            ms['code'] = 0
            ms['message'] = '失败'
        else:
            ms['code'] = 1
            ms['message'] = '成功'
        ms['data'] = msg
        presendmsg = json.dumps(ms, ensure_ascii=False)
        print(presendmsg)
        send = presendmsg.encode('utf-8')
        return send
class NovelSearchBookView(View):
    def get(self,request):
        bookname = request.GET.get('xsname')
        msg=nv1.searchbook(bookname)
        return HttpResponse(dealer().dealres(msg))
class NovelSearchBookDetailView(View):
    def get(self,request):
        url = request.GET.get('xsdetail')
        msg=nv1.bookdetail(url)
        return HttpResponse(dealer().dealres(msg))
class NovelSearchBookContentView(View):
    def get(self,request):
        url = request.GET.get('xscontent')
        msg=nv1.bookcontent(url)
        return HttpResponse(dealer().dealres(msg))
class NovelSearchBookSort(View):
    def get(self,request):
        page = request.GET.get('page')
        xsfenlei= request.GET.get('xsfenlei')
        msg=nv1.booksort('/'+xsfenlei+'/'+page+'/')
        return HttpResponse(dealer().dealres(msg))
class NovelSearchBookRank1(View):
    def get(self,request):
        msg=nv1.book_rank()
        return HttpResponse(dealer().dealres(msg))
class NovelSearchBookRank2(View):
    def get(self,request):
        msg = nv1.book_rank2()
        return HttpResponse(dealer().dealres(msg))
