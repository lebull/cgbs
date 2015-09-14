from django.contrib import admin

from .models import Game, Team, Pick, Season

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['away_team', 'home_team']}),
        ('Date information', {'fields': ['season','week', 'kickoff_time']}),
        ('Results', {'fields': ['complete', 'away_score', 'home_score']}),
    ]
    
    list_display = ('__unicode__', 'season', 'kickoff_time', 'can_pick', 'get_winner', 'complete')
    
    list_filter = ['week', 'kickoff_time', 'away_team', 'home_team']
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )
    
class PickAdmin(admin.ModelAdmin):
    list_display = ('author', 'winner', 'game', 'timestamp')
    list_filter = ['author']

admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Pick, PickAdmin)
admin.site.register(Season)

# Register your models here.
