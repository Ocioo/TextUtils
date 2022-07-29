# Solution to Exercise 1

from django.http import HttpResponse

def navigator(request):
    a = '''<h1 style="color: rgb(16, 29, 104);" >Personal Navigator</h1>
                        <div style="background-color: rgb(142, 255, 113); color: white; padding: 20px;">
                        <a style="color: rgb(16, 29, 104); text-decoration: none; font-size: 20px;" href="https://www.youtube.com/" target="_blank">YouTube</a><br>
                        <a style="color: rgb(16, 29, 104); text-decoration: none; font-size: 20px;" href="https://www.google.com/" target="_blank">Google</a><br>
                        <a style="color: rgb(16, 29, 104); text-decoration: none; font-size: 20px;" href="https://www.pinterest.com/" target="_blank">Pinterest</a><br>
                        <a style="color: rgb(16, 29, 104); text-decoration: none; font-size: 20px;" href="https://www.twitter.com/" target="_blank">Twitter</a><br>
                        </div>'''
    return HttpResponse(a)