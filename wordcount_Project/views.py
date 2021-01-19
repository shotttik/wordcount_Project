from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hithere': 'is it me'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'count': len(wordlist),
                                          'sortedwords': sortedwords,
                                          })


def about(request):
    return render(request, 'about.html',)
