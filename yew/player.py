from dataclasses import dataclass

import requests

from yew import HISCORES_URL, USER_AGENT


@dataclass
class Skill:
    rank: int
    level: int
    xp: int


SKILLS = [
    "Overall",
    "Attack",
    "Defence",
    "Strength",
    "Hitpoints",
    "Ranged",
    "Prayer",
    "Magic",
    "Cooking",
    "Woodcutting",
    "Fletching",
    "Fishing",
    "Firemaking",
    "Crafting",
    "Smithing",
    "Mining",
    "Herblore",
    "Agility",
    "Thieving",
    "Slayer",
    "Farming",
    "Runecraft",
    "Hunter",
    "Construction",
]


@dataclass
class Activity:
    rank: int
    score: int


ACTIVITIES = [
    "League Points",
    "Deadman Points",
    "Bounty Hunter - Hunter",
    "Bounty Hunter - Rogue",
    "Bounty Hunter (Legacy) - Hunter",
    "Bounty Hunter (Legacy) - Rogue",
    "Clue Scrolls (all)",
    "Clue Scrolls (beginner)",
    "Clue Scrolls (easy)",
    "Clue Scrolls (medium)",
    "Clue Scrolls (hard)",
    "Clue Scrolls (elite)",
    "Clue Scrolls (master)",
    "LMS - Rank",
    "PvP Arena - Rank",
    "Soul Wars Zeal",
    "Rifts closed",
    "Abyssal Sire",
    "Alchemical Hydra",
    "Artio",
    "Barrows Chests",
    "Bryophyta",
    "Callisto",
    "Calvar'ion",
    "Cerberus",
    "Chambers of Xeric",
    "Chambers of Xeric: Challenge Mode",
    "Chaos Elemental",
    "Chaos Fanatic",
    "Commander Zilyana",
    "Corporeal Beast",
    "Crazy Archaeologist",
    "Dagannoth Prime",
    "Dagannoth Rex",
    "Dagannoth Supreme",
    "Deranged Archaeologist",
    "Duke Sucellus",
    "General Graardor",
    "Giant Mole",
    "Grotesque Guardians",
    "Hespori",
    "Kalphite Queen",
    "King Black Dragon",
    "Kraken",
    "Kree'Arra",
    "K'ril Tsutsaroth",
    "Mimic",
    "Nex",
    "Nightmare",
    "Phosani's Nightmare",
    "Obor",
    "Phantom Muspah",
    "Sarachnis",
    "Scorpia",
    "Scurrius",
    "Skotizo",
    "Spindel",
    "Tempoross",
    "The Gauntlet",
    "The Corrupted Gauntlet",
    "The Leviathan",
    "The Whisperer",
    "Theatre of Blood",
    "Theatre of Blood: Hard Mode",
    "Thermonuclear Smoke Devil",
    "Tombs of Amascut",
    "Tombs of Amascut: Expert Mode",
    "TzKal-Zuk",
    "TzTok-Jad",
    "Vardorvis",
    "Venenatis",
    "Vet'ion",
    "Vorkath",
    "Wintertodt",
    "Zalcano",
    "Zulrah",
]


class PlayerFetcher:
    @staticmethod
    def fetch_player_by_name(name: str):
        url = f"{HISCORES_URL}?player={name}"

        response = requests.get(url, headers={"User-Agent": USER_AGENT}).json()

        player_skills = {}
        player_activities = {}
        for skill in response.get("skills", [{}]):
            player_skills[skill["name"]] = skill
        for activity in response.get("activities", [{}]):
            player_activities[activity["name"]] = activity

        return {"skills": player_skills, "activities": player_activities}


@dataclass
class Player:

    overall: Skill
    attack: Skill
    defence: Skill
    strength: Skill
    hitpoints: Skill
    ranged: Skill
    prayer: Skill
    magic: Skill
    cooking: Skill
    woodcutting: Skill
    fletching: Skill
    fishing: Skill
    firemaking: Skill
    crafting: Skill
    smithing: Skill
    mining: Skill
    herblore: Skill
    agility: Skill
    thieving: Skill
    slayer: Skill
    farming: Skill
    runecraft: Skill
    hunter: Skill
    construction: Skill

    league_points: Activity
    deadman_points: Activity
    bounty_hunter__hunter: Activity
    bounty_hunter__rogue: Activity
    bounty_hunter_legacy__hunter: Activity
    bounty_hunter_legacy__rogue: Activity
    clue_scrolls_all: Activity
    clue_scrolls_beginner: Activity
    clue_scrolls_easy: Activity
    clue_scrolls_medium: Activity
    clue_scrolls_hard: Activity
    clue_scrolls_elite: Activity
    clue_scrolls_master: Activity
    lms__rank: Activity
    pvp_arena__rank: Activity
    soul_wars_zeal: Activity
    rifts_closed: Activity
    abyssal_sire: Activity
    alchemical_hydra: Activity
    artio: Activity
    barrows_chests: Activity
    bryophyta: Activity
    callisto: Activity
    calvarion: Activity
    cerberus: Activity
    chambers_of_xeric: Activity
    chambers_of_xeric__challenge_mode: Activity
    chaos_elemental: Activity
    chaos_fanatic: Activity
    commander_zilyana: Activity
    corporeal_beast: Activity
    crazy_archaeologist: Activity
    dagannoth_prime: Activity
    dagannoth_rex: Activity
    dagannoth_supreme: Activity
    deranged_archaeologist: Activity
    duke_sucellus: Activity
    general_graardor: Activity
    giant_mole: Activity
    grotesque_guardians: Activity
    hespori: Activity
    kalphite_queen: Activity
    king_black_dragon: Activity
    kraken: Activity
    kreearra: Activity
    kril_tsutsaroth: Activity
    mimic: Activity
    nex: Activity
    nightmare: Activity
    phosanis_nightmare: Activity
    obor: Activity
    phantom_muspah: Activity
    sarachnis: Activity
    scorpia: Activity
    scurrius: Activity
    skotizo: Activity
    spindel: Activity
    tempoross: Activity
    the_gauntlet: Activity
    the_corrupted_gauntlet: Activity
    the_leviathan: Activity
    the_whisperer: Activity
    theatre_of_blood: Activity
    theatre_of_blood__hard_mode: Activity
    thermonuclear_smoke_devil: Activity
    tombs_of_amascut: Activity
    tombs_of_amascut__expert_mode: Activity
    tzkalzuk: Activity
    tztokjad: Activity
    vardorvis: Activity
    venenatis: Activity
    vetion: Activity
    vorkath: Activity
    wintertodt: Activity
    zalcano: Activity
    zulrah: Activity

    def __init__(self, username: str):
        player_data = PlayerFetcher.fetch_player_by_name(username)
        skills = player_data.get("skills", {})
        activities = player_data.get("activities", {})

        for skill in SKILLS:
            setattr(
                self,
                skill.lower(),
                Skill(
                    rank=skills.get(skill, {}).get("rank"),
                    level=skills.get(skill, {}).get("level"),
                    xp=skills.get(skill, {}).get("xp"),
                ),
            )
        for activity in ACTIVITIES:
            setattr(
                self,
                activity.lower()
                .replace(" ", "_")
                .replace("'", "")
                .replace("-", "")
                .replace("(", "")
                .replace(")", "")
                .replace(":", "_"),
                Activity(
                    rank=activities.get(activity, {}).get("rank"),
                    score=activities.get(activity, {}).get("score"),
                ),
            )
