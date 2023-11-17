from statistics import mean

class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            raise Exception("Title can't be changed after initial title set")
        else:
            if isinstance(new_title, str) and len(new_title) != 0:
                self._title = new_title
            else:
                raise Exception("Title must be a non empty string")


    def results(self):
        return [ result for result in Result.all if result.game == self ]

    def players(self):
        my_players = [ result.player for result in Result.all if result.game == self ]
        return list( set( my_players ) )
        
    def average_score(self, player):
        # get all the scores for a player AND for this game
        scores = [ result.score for result in Result.all if result.game == self and result.player == player ]
        # if list is empty return 0 to satisfy edge case
        if not scores:
            return 0
        # otherwise average the list
        # return the average as a number
        return mean( scores )


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            print("Username must be a string between 2 and 16 characters inclusive")

    def results(self):
        return [ result for result in Result.all if result.player == self ]

    def games_played(self):
        my_games = [ result.game for result in Result.all if result.player == self ]
        return list( set( my_games ) )

    def played_game(self, game):
        # true if the game has been played otherwise false
        return game in self.games_played()

    def num_times_played(self, game):
        game_results = [ result.game for result in Result.all if result.player == self and result.game == game ]
        return len(game_results)
    
class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):

        if not hasattr(self, "_score"):

            if isinstance(new_score, int) and 1 <= new_score <= 5000:

                self._score = new_score
            
            else:
                print("Score must be an integer between 1 and 5000")
        else:
            print("Score cannot be changed once set")