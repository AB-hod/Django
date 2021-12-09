from django.shortcuts import render
from django.http import JsonResponse
import calendar
from calendar import HTMLCalendar

from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Bindll
# from .utils import get_plot
def search_result(request):
	if request.method == "POST":
		ChemSearched = request.POST.get('ChemSearched')
		tarname = Bindll.objects.filter(targetnameassignedbycuratorordatasource__contains=ChemSearched).exclude(ki_nm__isnull=True , ki_nm__exact='<')[:10]
		kdtarname = Bindll.objects.filter(targetnameassignedbycuratorordatasource__contains=ChemSearched).filter(ki_nm__isnull=True).exclude(kd_nm__isnull=True)[:50]
		Ictarname = Bindll.objects.filter(targetnameassignedbycuratorordatasource__contains=ChemSearched).filter(ki_nm__isnull=True).filter(kd_nm__isnull=True).exclude(ic50_nm__isnull=True)[:50]

		
		# x = [x.ki_nm for x in tarname]
		# y = [y.bindingdbligandname for y in tarname]
		# chart = get_plot(x,y)

		return JsonResponse(request, 'Search/search_result.html',
			{'ChemSearched':ChemSearched,'tarname':tarname,'kdtarname':kdtarname, 'Ictarname':Ictarname})
	else:
		return JsonResponse(request, 'Search/search_result.html',{})


def home(request):
	now = datetime.now()
	current_year = now.year

	return render(request,'Search/home.html',{"current_year": current_year,})

