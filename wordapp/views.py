from django.shortcuts import render

# Create your views here.

def wordhome(request):
    return render(request, 'wordhome.html')

def worddetail(request):
    return render(request, 'worddetail.html')

def wordabout(request):
    return render(request, 'wordabout.html')

def wordresult(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dictionary={}

    for word in words:
        if word in word_dictionary: #words?
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    

    return render(request, 'wordresult.html',{'full': text, 'total':len(words),'dictionary':word_dictionary.items()})

