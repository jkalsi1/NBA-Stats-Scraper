import requests
from bs4 import BeautifulSoup


class Player:
    def __init__(self, name, pos, age, team, pts, reb, ast, blks,stl, gms):
        self.name = name
        self.pos = pos
        self.age = age
        self.team = team
        self.pts = int(pts)
        self.reb = int(reb)
        self.ast = int(ast)
        self.blks = int(blks)
        self.stl = int(stl)
        self.gms = int(gms)

    def __str__(self):
        return self.name + ', Pos.: ' + self.pos + ', Age: ' + self.age + ', Team: ' + self.team + ', Pts: ' + str(self.pts) + ', Rbs: ' + str(self.reb) + ', Ast: ' + str(self.ast) + ', Blks: ' + str(self.blks)  +', Stl: ' + str(self.stl) + ', Games Played: ' + str(self.gms)

def getPlayersList():
    # specify the url
    url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'

    # send a request to the website and retrieve the HTML
    response = requests.get(url)
    html = response.text

    # parse the HTML using Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.title.text)

    players = []


    data = soup.find("table")
    for list in data:
        for item in list:
            try:
                if ('full_table' in item.attrs.get('class')):
                    player = Player(item.contents[1].string, item.contents[2].string,
                                    item.contents[3].string, item.contents[4].string,
                                    item.contents[29].string, item.contents[23].string,
                                    item.contents[24].string, item.contents[26].string, item.contents[25].string,
                                    item.contents[5].string)
                    players.append(player)
            except Exception as e:
                pass


    return players

def getPtsLdr(players):
    players.sort(key=lambda player: player.pts, reverse=True)
    return players[0]


def getRebLdr(players):
    players.sort(key=lambda player: player.reb, reverse=True)
    return players[0]


def getBlkLdr(players):
    players.sort(key=lambda player: player.blks, reverse=True)
    return players[0]


def getAstLdr(players):
    players.sort(key=lambda player: player.ast, reverse=True)
    return players[0]


def getStlLdr(players):
    players.sort(key=lambda player: player.stl, reverse=True)
    return players[0]


def getNoPoints(players):
    return [x for x in players if x.pts == 0]

if __name__=="__main__":
    print("NBA Stat Leaders for the 2024 season:")
    players = getPlayersList()

    pts = getPtsLdr(players)
    reb = getRebLdr(players)
    blk = getBlkLdr(players)
    ast = getAstLdr(players)
    stl = getStlLdr(players)
    print("Points: " + str(pts))
    print("Rebounds: " + str(reb))
    print("Blocks: " + str(blk))
    print("Assists: " + str(ast))
    print("Steals: " + str(stl))

    # print("The players with zero points are: ")
    # for p in getNoPoints(players):
    #     print(p.name)
    exit()