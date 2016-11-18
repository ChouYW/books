from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import os

def getbookslist(request):
    bookslist = os.listdir(r'downloads')
    return render(request, 'bookslist.html', {'bookslist': bookslist})

def downloadbook(request, filename):
    def fileIterator(filename, chunkSize=512):
        with open('downloads/'+filename) as f:
            while True:
                c = f.read(chunkSize)
                if c:
                    yield c
                else:
                    break
    response = StreamingHttpResponse(fileIterator(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)

    return response
