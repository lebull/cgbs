from django import template

register = template.Library()

@register.filter
def can_user_pick(value, arg):
    game = value
    user = arg
    return game.can_user_pick(user)

@register.filter
def get_game_pick_by_author(value, arg):
    game = value
    author = arg
    
    
    pick = game.get_current_pick_by_author(author)
    if pick:
        return pick
    else:
        return None

@register.filter
def get_season_user_record(value, arg):
    season = value
    user = arg
    
    record = season.get_user_record(user)
    if record:
        return record
    else:
        return None
    