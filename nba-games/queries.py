# Sources database

CREATE_TABLE_SOURCES = '''
    CREATE TABLE sources (
    id TEXT NOT NULL PRIMARY KEY,
    summary_source TEXT,
    stats_source TEXT)
'''

INSERT_INTO_SOURCES = '''
    INSERT INTO sources VALUES (
    :id,
    :summary_source,
    :stats_source)
'''

COLUMNS_SOURCES = [
    'id',
    'summary_source',
    'stats_source',
]

INSERT_INTO_SOURCES_DICT = {key: None for key in COLUMNS_SOURCES}

# ----------------------------------------------------------------

# Games database

CREATE_TABLE_GAMES = '''CREATE TABLE games (
    game_id TEXT NOT NULL PRIMARY KEY,
    event TEXT,
    season INTEGER,
    date TEXT,
    status TEXT,
    home_team TEXT,
    away_team TEXT,
    home_score INTEGER,
    away_score INTEGER,
    home_2PA INTEGER,
    away_2PA INTEGER,
    home_2PM INTEGER,
    away_2PM INTEGER,
    home_3PA INTEGER,
    away_3PA INTEGER,
    home_3PM INTEGER,
    away_3PM INTEGER,
    home_FTA INTEGER,
    away_FTA INTEGER,
    home_FTM INTEGER,
    away_FTM INTEGER,
    home_OREB INTEGER,
    away_OREB INTEGER,
    home_DREB INTEGER,
    away_DREB INTEGER,
    home_AST INTEGER,
    away_AST INTEGER,
    home_BLK INTEGER,
    away_BLK INTEGER,
    home_STL INTEGER,
    away_STL INTEGER,
    home_TOV INTEGER,
    away_TOV INTEGER,
    home_PF INTEGER,
    away_PF INTEGER,
    home_odds REAL,
    away_odds REAL)
    '''

INSERT_INTO_GAMES = '''INSERT INTO games VALUES (
    :game_id,
    :event,
    :season,
    :date,
    :status,
    :home_team,
    :away_team,
    :home_score,
    :away_score,
    :home_2PA,
    :away_2PA,
    :home_2PM,
    :away_2PM,
    :home_3PA,
    :away_3PA,
    :home_3PM,
    :away_3PM,
    :home_FTA,
    :away_FTA,
    :home_FTM,
    :away_FTM,
    :home_OREB,
    :away_OREB,
    :home_DREB,
    :away_DREB,
    :home_AST,
    :away_AST,
    :home_BLK,
    :away_BLK,
    :home_STL,
    :away_STL,
    :home_TOV,
    :away_TOV,
    :home_PF,
    :away_PF,
    :home_odds,
    :away_odds)
    '''

COLUMNS_GAMES = [
    'game_id',
    'event',
    'season',
    'date',
    'status',
    'home_team',
    'away_team',
    'home_score',
    'away_score',
    'home_2PA',
    'away_2PA',
    'home_2PM',
    'away_2PM',
    'home_3PA',
    'away_3PA',
    'home_3PM',
    'away_3PM',
    'home_FTA',
    'away_FTA',
    'home_FTM',
    'away_FTM',
    'home_OREB',
    'away_OREB',
    'home_DREB',
    'away_DREB',
    'home_AST',
    'away_AST',
    'home_BLK',
    'away_BLK',
    'home_STL',
    'away_STL',
    'home_TOV',
    'away_TOV',
    'home_PF',
    'away_PF',
    'home_odds',
    'away_odds',
]

INSERT_INTO_GAMES_DICT = {key: None for key in COLUMNS_GAMES}
