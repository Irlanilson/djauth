from django.shortcuts import render_to_response
from django.template.context import RequestContext
from djauthapp.models import UserProfile

def home(request):
	profile = None
	if request.user.id:
		profile = UserProfile.objects.get(user = request.user)
	context = RequestContext(request, {'request': request, 'user': request.user, "profile": profile})
	return render_to_response('home.html', context_instance=context)