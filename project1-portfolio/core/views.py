from django.shortcuts import render, HttpResponse
# Create your views here.


# html_base = """
# <h1>Welcome</h1>
# <ul>
# <li><a href="/">Home</a></li>
# <li><a href="/about-me">About</a></li>
# <li><a href="/portfolio">Portfolio</a></li>
# <li><a href="/contact">Contact</a></li>
# </ul>
# """

# logic execute when user make requests in our website
def home(request):

  # html_response = "<h1>Hola mundo</h1>"

  # for i in range(10):
  #   html_response += "%s %s %s" % ("<h2>Portada ", str(i), "</h2>")
  
  # return HttpResponse(html_base + html_response)
  return render(request, "core/home.html")
  

def about(request):

  # return HttpResponse(html_base + "<h1>About</h1>")
  return render(request, "core/about.html")



def portfolio(request):

  # return HttpResponse(html_base + "<h1>Portfolio</h1>")
  return render(request, "core/portfolio.html")


def contact(request):

  # return HttpResponse(html_base + "<h1>Contact</h1>")
  return render(request, "core/contact.html")
