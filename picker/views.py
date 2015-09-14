from django import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


from forms import PickForm
from models import Game, Pick, Season

from django.contrib.auth.models import User

import json

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

    def form_invalid(self, form, **kwargs):

        context = self.get_context_data(**kwargs)
        context['error_message'] = form.errors
        
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return self.render_to_response(context)

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


class SeasonListView(ListView):
    model = Season
        
        
class SeasonDetailView(DetailView):
    model = Season
    context_object = 'season'
    
    def get_context_data(self, **kwargs):
        
        season = kwargs['object']
        
        context = super(SeasonDetailView, self).get_context_data(**kwargs)
      
        context['passed_games'] = {}
      
        context['this_weeks_games'] = context['season'].game_set.filter(week=context['season'].current_week)
        
        #If a game has already been played this week, move it to passed games.
        for game in context['this_weeks_games']:
            if not game.pickable:
                
                if not game.week in context['passed_games'].keys():
                    context['passed_games'][game.week] = []
                context['passed_games'][game.week].append(game)
                context['this_weeks_games'] = context['this_weeks_games'].exclude(pk=game.pk)
                
        #Populate passed games
        for game in season.game_set.filter(week__lt=season.current_week):
            if game.week in context['passed_games']:
                context['passed_games'][game.week].append(game)
            else:
                context['passed_games'][game.week] = [game]
        return context
   
class UserDetailView(TemplateView):
    
    template_name='picker/user_detail.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(UserDetailView, self).get_context_data(**kwargs)
        
        context['target_user'] = User.objects.get(pk=kwargs['user_pk'])

        season = Season.objects.get(pk=kwargs['season_pk'])

        context['games_by_week'] = {}
        
        #TODO: move this filter into the model's manager or something
        games = season.game_set.filter(Q(complete=True) | Q(week__lt=season.current_week))
        for game in games:
            pick = game.get_current_pick_by_author(context['target_user'])
            
            if not context['games_by_week'].get(game.week):
                context['games_by_week'][game.week] = [game]
            else:
                context['games_by_week'][game.week].append(game)
                
        return context
        

class GameDetailView(DetailView):
    model = Game
    context_object = 'game'
    
    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        
        game = kwargs['object']

        context['pick_history'] = game.pick_set.all()

        context['away_picks'], context['home_picks'] = game.get_away_home_picks()
        
        if self.request.user.is_authenticated():
            context['my_pick_history'] = game.get_all_picks_by_author(self.request.user)
            context['my_pick'] = game.get_current_pick_by_author(self.request.user)
        
        return context


class PickSubmitView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    template_name = 'picker/pick_submit.html'
    form_class = PickForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        #Make sure the picked team is in the game
        picked_winner = form.cleaned_data['winner']
        picked_game = form.cleaned_data['game']
        
        #Apperiently, returns none if no pick.
        current_pick = picked_game.get_current_pick_by_author(self.request.user)
        
        #If it's a repeat pick, dont' frekin add it...
        if current_pick and current_pick.winner == picked_winner:
            return self.render_to_json_response(form.errors, status=200)
        
        #If the game isn't pickable, return an error.
        if not picked_game.pickable:
            form.add_error("game")
            return self.render_to_json_response(form.errors, status=200)
                
        if picked_winner not in [picked_game.away_team, picked_game.home_team]:
            form.add_error("winner")
            return self.form_invalid(form)
    
        return super(PickSubmitView, self).form_valid(form)
        
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', None)
        
# --Oneshots--
        
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
    season.users.add(user)

    if request.is_ajax():    
        response_data = {}
        response_data['msg'] = 'Added Successfully'
        
        return HttpResponse(
            json.dumps(response_data),
            content_type='application/json',
        )
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@csrf_exempt
def get_picks(request):
    """This provides a way for ajax calls to get the user's own picks"""
    response_data = {}

    user = request.user
    
    games = []
    
    #Only try this if we are asking at least one game.  Otherwise, just return a normal response with no games.
    if request.POST['games']:
        try:
            #I have no clue why, but the brackets are added to this array in the
            #incoming json data.  Oh well, no harm done.
            games = [int(g) for g in request.POST['games'].split(',')] 
        except MultiValueDictKeyError:
            return_thing = request.POST
            return HttpResponse(return_thing, status=400, content_type="application/json")
    
    response_data['picks'] = {}
    
    #Get picks by a list of games
    for game_id in games:

        game = Game.objects.get(id=game_id)
        #except ObjectDoesNotExist:
        pick = game.get_current_pick_by_author(user)
        if pick:
            response_data['picks'][game.id] = pick.winner.id
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")