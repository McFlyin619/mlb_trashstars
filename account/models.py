from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TEAMS = {
    ('AZ', 'Arizona Diamondbacks'),
    ('ATL','Atlanta Braves'),
    ('BAL','Baltimore Orioles'),
    ('BOS','Boston Red Sox'),
    ('CHW','Chicago White Sox'),
    ('CHC','Chicago Cubs'),
    ('CIN','Cincinnati Reds'),
    ('CLE','Cleveland Indians'),
    ('COL','Colorado Rockies'),
    ('DET','Detroit Tigers'),
    ('HOU','Houston Astros'),
    ('KC','Kansas City Royals'),
    ('LAA','Los Angeles Angels'),
    ('LAD','Los Angeles Dodgers'),
    ('MIA','Miami Marlins'),
    ('MIL','Milwaukee Brewers'),
    ('MIN','Minnesota Twins'),
    ('NYM','New York Mets'),
    ('NYY','New York Yankees'),
    ('OAK','Oakland Athletics'),
    ('PHI','Philadelphia Phillies'),
    ('PIT','Pittsburgh Pirates'),
    ('SD','San Diego Padres'),
    ('SF','San Francisco Giants'),
    ('SEA','Seattle Mariners'),
    ('STL','St. Louis Cardinals'),
    ('TB','Tampa Bay Rays'),
    ('TEX','Texas Rangers'),
    ('TOR','Toronto Blue Jays'),
    ('WAS','Washington Nationals'),
}



class Profile(models.Model):
    web_user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=254, choices=TEAMS, default='SD')

    def __str__(self):
        return self.web_user