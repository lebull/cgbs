from django import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from forms import PickForm
from models import Game, Pick, Season

register = template.Library()

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
     
        
class Dashboard(TemplateView):
    template_name='picker/dashboard.html'

    def get_context_data(self):
        context_data = {}
        context_data['recent_picks_list'] = Pick.objects.all()
        return context_data


class SeasonDetailView(DetailView):
    model = Season
    context_object = 'season'
    
    
    def get_context_data(self, **kwargs):
        
        season = kwargs['object']
        
        context = super(SeasonDetailView, self).get_context_data(**kwargs)
      
        context['this_weeks_games'] = context['season'].game_set.filter(week=context['season'].current_week)
        
        context['passed_games'] = {}
        passed_games = []
        
        for game in season.game_set.filter(week__lt=season.current_week):
            if game.week in context['passed_games']:
                context['passed_games'][game.week].append(game)
            else:
                context['passed_games'][game.week] = [game]
        return context
   
 
class GameDetailView(DetailView):
    model = Game
    context_object = 'game'
    
    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        
        game = kwargs['object']

        context['pick_form'] = PickForm(game=game)
        context['all_picks'] = game.pick_set.all()
        context['my_pick_history'] = game.get_all_picks_by_author(self.request.user)
        context['my_pick'] = game.get_current_pick_by_author(self.request.user)
        context['away_picks'], context['home_picks'] = game.get_away_home_picks()
        
        return context
        
    #GetPickCount


class PickSubmitView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    template_name = 'picker/pick_submit.html'
    form_class = PickForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PickSubmitView, self).form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', None)
  
  
@login_required
def join_season(request):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    
    #Try to add the user to the season.
    season_id = request.POST.get('season_id')
    user = request.user

    season = Season.objects.get(pk=season_id)
    season.add_user(user)

    if request.is_ajax():    
        response_data = {}
        response_data['msg'] = 'Added Successfully'
        
        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json',
        )
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))