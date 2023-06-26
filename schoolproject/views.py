# I have created this file -Usama
from django.http import HttpResponse
from django.shortcuts import render
from langdetect import detect

def index(request):
    # pipe line in views
    return render(request, 'index.html')
    

 # analyze functionality
def analyze(request):
    gotext = request.GET.get('text', 'defualt')
    print(gotext)
    removepunc = request.GET.get('removepun', 'off')
    fullcaps = request.GET.get('full_caps', 'off')
    new_line_remover=request.GET.get('new_line_remover','off')
    count_words=request.GET.get('count_words','off')
    count_line=request.GET.get('count_line', 'off')
    lanaguage_detecion=request.GET.get('Language_Detection', 'off')
    extra_space=request.GET.get('extra_space', 'off')
    print(fullcaps)
    print(removepunc)
    print(new_line_remover)
    print(count_words)
    print(count_line)
    print(lanaguage_detecion)
    print(extra_space)
    # logic to remove puctuations
    if removepunc == 'on':
        punctuation = '''.,?!;:"'( )[ ]-.../&@$%#+-=*~|\{ }< >'''
        analyzed_text = ""
        for char in gotext:
            if char not in punctuation:
                analyzed_text = analyzed_text + char

        params = {'purpose': 'remove punctuations',  'analyzed_text' : analyzed_text}
        return render(request, 'analyze.html', params)

    elif (fullcaps == 'on'):
        analyzed_text = ""
        for char in gotext:
            analyzed_text = analyzed_text + char.upper()
        params = {'purpose': 'change to upper case' , 'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)
    
     # logic to remove new line from text
    elif (new_line_remover=='on'):
         analyzed_text=""
         for char in gotext:
             if char !="\n":
                  analyzed_text=analyzed_text+char
         params = {'purpose': 'remove new line' , 'analyzed_text': analyzed_text}  
         return render(request,'analyze.html',params )
    
   # logic to count number of words from passage
    elif (count_words=='on'):
         analyzed_text=""
         count=0
         for char in gotext:
              if char !="\n":
                    analyzed_text=analyzed_text+char
                    count=count+1
         params = {'purpose': 'count words' , 'analyzed_text':count}
         return render(request,'analyze.html',params )
                        
    # logic to count number of lines
    elif(count_line=='on'):
        analyzed_text=""
        count=0
        for char in gotext:
            if char !="\n":
                analyzed_text=analyzed_text+char
            else:
                count=count+1
        params = {'purpose': 'count lines' , 'analyzed_text':count}
        return render(request,'analyze.html',params )
    

    # logic for Language Detection from the text
    elif(lanaguage_detecion=='on'):
        analyzed_text=""
        for char in gotext:
            analyzed_text=analyzed_text+char
        lan=detect(analyzed_text)
        params = {'purpose': 'Language Detection' , 'analyzed_text':lan}
        return render(request,'analyze.html',params )
    
    # logic to remove extra space from the text
    elif(extra_space=='on'):
        analyzed_text=""
        for index , char in enumerate(gotext):
            if gotext[index]==" " and  gotext[index+1]==" ":
                pass
            else:
                 analyzed_text=analyzed_text+char
        params = {'purpose': 'extra space remove' , 'analyzed_text':analyzed_text}
        return render(request,'analyze.html',params )

                   
    else:
        return HttpResponse("error")
        
    