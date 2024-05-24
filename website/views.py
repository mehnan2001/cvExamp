from django.shortcuts import render


def indexView(request):
    aboutMe = """
    I was born on the 21st of the first month of 2001.
    I have been working with computers since I can remember, 
    and I have been training and working in the field of programming 
    for a long time.
    """
    context = {
        'aboutMe': aboutMe,
        'enName': "Mehdi Kargar",
        'country': "IRAN"
    }
    return render(request, 'index.html', context)