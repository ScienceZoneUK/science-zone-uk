# Python Dictionary of Football Teams

## In this workshop we will be creating dictionaries and accessing their data.
### A python dictionary is one of for data structures, it contains ```key:value``` pairs

### Single dictionary
```
afc_bournemouth = {
    "p1": "Jim",
    "p2": "Bob",
    "p3": "Paul",
    "p4": "Xavier",
    "p5": "Lineker",
    "p6": "Gazza",
    }

for player,name in afc_bournemouth.items():
    print(f'{player}:{name}')

#Output
# p1:Jim
# p2:Bob
# p3:Paul
# p4:Xavier
# p5:Lineker
# p6:Gazza
```

### 1lv Nested dictionary
```python
afc_bournemouth = {
    "p1": {"name":"Jim", "position": "cb", "goals":10},
     "p2": {"name":"Bob", "position": "gk", "goals":1},
    "p3": {"name":"Lineker", "position": "st", "goals":100},
    "p4": {"name":"Gazza", "position": "st", "goals":50},

    }

for player,stats in afc_bournemouth.items():
    print(f'{player}')
    for x, y in stats.items():
        print(f'{x}:{y}')
```


### 2lv Nested dictionary
```python
premier_league= {
    "afc_bournemouth" : {
        "p1": {"name":"Jim", "position": "cb", "goals":10},
         "p2": {"name":"Bob", "position": "gk", "goals":1},
        "p3": {"name":"Lineker", "position": "st", "goals":100},
        "p4": {"name":"Gazza", "position": "st", "goals":50},

        },
    "poole_town" : {
        "p1": {"name":"Jim", "position": "cb", "goals":10},
         "p2": {"name":"Bob", "position": "gk", "goals":1},
        "p3": {"name":"Lineker", "position": "st", "goals":100},
        "p4": {"name":"Gazza", "position": "st", "goals":50},

        }

}

for team, players in premier_league.items():
    print(f'{team}')
    for player, stats in players.items():
        print(f'{player}')
        for stats, info in stats.items():
            print(f'{stats}:{info}')
```
        
### Data detective challenge
```python
afc_bournemouth = {
    "Club Info": {
        "Name": "AFC Bournemouth",
        "Founded": 1899,
        "Stadium": "Vitality Stadium",
        "Nickname": "The Cherries",
    },
    "Performance": {
        "League": "Premier League",
        "Best Finish": "9th (2016-17)",
        "Major Trophies": {
            "League Cup": None,
            "FA Cup": None,
            "EFL Championship": "Winners (2014-15)"
        }
    }
}
```


