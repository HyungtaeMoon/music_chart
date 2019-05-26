from django.shortcuts import render
from django.views.generic import TemplateView

from .models import BugsChart


class ChartListView(TemplateView):
    template_name = 'posts/chart-list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['bugs_chart_list'] = BugsChart.objects.all().order_by('pk').filter(active=True)

        return context_data


chart_list = ChartListView.as_view()
