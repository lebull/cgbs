from django.shortcuts import render
from django.views.generic import DetailView, ListView

from models import NewsPost

class NewsPostListView(ListView):
    model = NewsPost

class NewsPostDetailView(DetailView):
    model = NewsPost
    context_object = 'post'
    
    """
    def get_context_data(self, **kwargs):
        context = super(NewsPostDetailView, self).get_context_data(**kwargs)
        
        game = kwargs['object']

        context['pick_history'] = game.pick_set.all()

        context['away_picks'], context['home_picks'] = game.get_away_home_picks()
        
        if self.request.user.is_authenticated():
            context['my_pick_history'] = game.get_all_picks_by_author(self.request.user)
            context['my_pick'] = game.get_current_pick_by_author(self.request.user)
        
        return context
    """
#post_detail.__doc__ = date_based.object_detail.__doc__

