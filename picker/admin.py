from django.contrib import admin

from .models import Game, Team, Pick, Season

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['away_team', 'home_team']}),
        ('Date information', {'fields': ['season','week', 'kickoff_time']}),
        ('Results', {'fields': ['complete', 'away_score', 'home_score']}),
    ]
    
    list_display = ('__unicode__', 'season', 'kickoff_time', 'can_pick', 'get_winner')
    
    list_filter = ['away_team', 'home_team', 'week', 'kickoff_time']
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'get_record')
    
class PickAdmin(admin.ModelAdmin):
    list_display = ('author', 'winner', 'game', 'timestamp')

admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Pick, PickAdmin)
admin.site.register(Season)

# Register your models here.
