from django.db import models

class Tournament(models.Model):

    name = models.CharField(max_length=200)
    date = models.DateField()
    host = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    owner = models.OneToOneField('Player', related_name='owner')
    public = models.BooleanField()

    class Admin: pass

    def __str__(self):
        return '{0!s}'.format(self.name)

class Team (models.Model):

    team_name = models.CharField(max_length=200)
    tournament = models.ForeignKey(Tournament)
    school = models.ForeignKey('School')
    team_owner = models.ForeignKey('Player', related_name='team_owner')

    def __str__(self):
        return'{0!s} - {1!s}'.format(self.team_name, self.tournament)


class Player(models.Model):

    user = models.OneToOneField(User)

    team = models.ManyToManyField(Team)
    tournament = models.ManyToManyField(Tournament)
    school = models.ForeignKey('School')

    def __str__(self):
        return '{0!s}'.format(self.user.username)

class School(models.Model):

    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    contact_phone = models.CharField(max_length=50)
    address = models.TextField()

    created_by = models.ForeignKey(Player, related_name='created_by')

    def __str__(self):
        return '{0!s}'.format(self.name)

