from osrs.utils.api import fetch_player


class Skill:
    def __init__(self, skill_data) -> None:
        self.rank = skill_data.get("rank") if skill_data.get("rank") != -1 else None
        self.level = skill_data.get("level") if skill_data.get("level") != -1 else None
        self.xp = skill_data.get("xp") if skill_data.get("xp") != -1 else None


class Activity:
    def __init__(self, activity_data) -> None:
        self.rank = (
            activity_data.get("rank") if activity_data.get("rank") != -1 else None
        )
        self.score = (
            activity_data.get("score") if activity_data.get("score") != -1 else None
        )


class Player:
    def __init__(self, name) -> None:
        super().__init__()

        player_data = fetch_player(name)
        skills = player_data.get("skills", {})
        activities = player_data.get("activities", {})

        self.overall = Skill(skills.get("Overall", {}))
        self.attack = Skill(skills.get("Attack", {}))
        self.defence = Skill(skills.get("Defence", {}))
        self.strength = Skill(skills.get("Strength", {}))
        self.hitpoints = Skill(skills.get("Hitpoints", {}))
        self.ranged = Skill(skills.get("Ranged", {}))
        self.prayer = Skill(skills.get("Prayer", {}))
        self.magic = Skill(skills.get("Magic", {}))
        self.cooking = Skill(skills.get("Cooking", {}))
        self.woodcutting = Skill(skills.get("Woodcutting", {}))
        self.fletching = Skill(skills.get("Fletching", {}))
        self.fishing = Skill(skills.get("Fishing", {}))
        self.firemaking = Skill(skills.get("Firemaking", {}))
        self.crafting = Skill(skills.get("Crafting", {}))
        self.smithing = Skill(skills.get("Smithing", {}))
        self.mining = Skill(skills.get("Mining", {}))
        self.herblore = Skill(skills.get("Herblore", {}))
        self.agility = Skill(skills.get("Agility", {}))
        self.thieving = Skill(skills.get("Thieving", {}))
        self.slayer = Skill(skills.get("Slayer", {}))
        self.farming = Skill(skills.get("Farming", {}))
        self.runecraft = Skill(skills.get("Runecraft", {}))
        self.hunter = Skill(skills.get("Hunter", {}))
        self.construction = Skill(skills.get("Construction", {}))

        self.league_points = Activity(activities.get("League Points"))
        self.deadman_points = Activity(activities.get("Deadman Points"))
        self.bounty_hunter_hunter = Activity(activities.get("Bounty Hunter - Hunter"))
        self.bounty_hunter_rogue = Activity(activities.get("Bounty Hunter - Rogue"))
        self.bounty_hunter_legacy_hunter = Activity(
            activities.get("Bounty Hunter (Legacy) - Hunter")
        )
        self.bounty_hunter_legacy_rogue = Activity(
            activities.get("Bounty Hunter (Legacy) - Rogue")
        )
        self.clue_scrolls_all = Activity(activities.get("Clue Scrolls (all)"))
        self.clue_scrolls_beginner = Activity(activities.get("Clue Scrolls (beginner)"))
        self.clue_scrolls_easy = Activity(activities.get("Clue Scrolls (easy)"))
        self.clue_scrolls_medium = Activity(activities.get("Clue Scrolls (medium)"))
        self.clue_scrolls_hard = Activity(activities.get("Clue Scrolls (hard)"))
        self.clue_scrolls_elite = Activity(activities.get("Clue Scrolls (elite)"))
        self.clue_scrolls_master = Activity(activities.get("Clue Scrolls (master)"))
        self.lms_rank = Activity(activities.get("LMS - Rank"))
        self.pv_p_arena_rank = Activity(activities.get("PvP Arena - Rank"))
        self.soul_wars_zeal = Activity(activities.get("Soul Wars Zeal"))
        self.rifts_closed = Activity(activities.get("Rifts closed"))
        self.abyssal_sire = Activity(activities.get("Abyssal Sire"))
        self.alchemical_hydra = Activity(activities.get("Alchemical Hydra"))
        self.artio = Activity(activities.get("Artio"))
        self.barrows_chests = Activity(activities.get("Barrows Chests"))
        self.bryophyta = Activity(activities.get("Bryophyta"))
        self.callisto = Activity(activities.get("Callisto"))
        self.calvarion = Activity(activities.get("Calvar'ion"))
        self.cerberus = Activity(activities.get("Cerberus"))
        self.chambers_of_xeric = Activity(activities.get("Chambers of Xeric"))
        self.chambers_of_xeric_challenge_mode = Activity(
            activities.get("Chambers of Xeric: Challenge Mode")
        )
        self.chaos_elemental = Activity(activities.get("Chaos Elemental"))
        self.chaos_fanatic = Activity(activities.get("Chaos Fanatic"))
        self.commander_zilyana = Activity(activities.get("Commander Zilyana"))
        self.corporeal_beast = Activity(activities.get("Corporeal Beast"))
        self.crazy_archaeologist = Activity(activities.get("Crazy Archaeologist"))
        self.dagannoth_prime = Activity(activities.get("Dagannoth Prime"))
        self.dagannoth_rex = Activity(activities.get("Dagannoth Rex"))
        self.dagannoth_supreme = Activity(activities.get("Dagannoth Supreme"))
        self.deranged_archaeologist = Activity(activities.get("Deranged Archaeologist"))
        self.duke_sucellus = Activity(activities.get("Duke Sucellus"))
        self.general_graardor = Activity(activities.get("General Graardor"))
        self.giant_mole = Activity(activities.get("Giant Mole"))
        self.grotesque_guardians = Activity(activities.get("Grotesque Guardians"))
        self.hespori = Activity(activities.get("Hespori"))
        self.kalphite_queen = Activity(activities.get("Kalphite Queen"))
        self.king_black_dragon = Activity(activities.get("King Black Dragon"))
        self.kraken = Activity(activities.get("Kraken"))
        self.kreearra = Activity(activities.get("Kree'Arra"))
        self.kril_tsutsaroth = Activity(activities.get("K'ril Tsutsaroth"))
        self.mimic = Activity(activities.get("Mimic"))
        self.nex = Activity(activities.get("Nex"))
        self.nightmare = Activity(activities.get("Nightmare"))
        self.phosanis_nightmare = Activity(activities.get("Phosani's Nightmare"))
        self.obor = Activity(activities.get("Obor"))
        self.phantom_muspah = Activity(activities.get("Phantom Muspah"))
        self.sarachnis = Activity(activities.get("Sarachnis"))
        self.scorpia = Activity(activities.get("Scorpia"))
        self.scurrius = Activity(activities.get("Scurrius"))
        self.skotizo = Activity(activities.get("Skotizo"))
        self.spindel = Activity(activities.get("Spindel"))
        self.tempoross = Activity(activities.get("Tempoross"))
        self.the_gauntlet = Activity(activities.get("The Gauntlet"))
        self.the_corrupted_gauntlet = Activity(activities.get("The Corrupted Gauntlet"))
        self.the_leviathan = Activity(activities.get("The Leviathan"))
        self.the_whisperer = Activity(activities.get("The Whisperer"))
        self.theatre_of_blood = Activity(activities.get("Theatre of Blood"))
        self.theatre_of_blood_hard_mode = Activity(
            activities.get("Theatre of Blood: Hard Mode")
        )
        self.thermonuclear_smoke_devil = Activity(
            activities.get("Thermonuclear Smoke Devil")
        )
        self.tombs_of_amascut = Activity(activities.get("Tombs of Amascut"))
        self.tombs_of_amascut_expert_mode = Activity(
            activities.get("Tombs of Amascut: Expert Mode")
        )
        self.tz_kazuk = Activity(activities.get("TzKal-Zuk"))
        self.tz_tojad = Activity(activities.get("TzTok-Jad"))
        self.vardorvis = Activity(activities.get("Vardorvis"))
        self.venenatis = Activity(activities.get("Venenatis"))
        self.vetion = Activity(activities.get("Vet'ion"))
        self.vorkath = Activity(activities.get("Vorkath"))
        self.wintertodt = Activity(activities.get("Wintertodt"))
        self.zalcano = Activity(activities.get("Zalcano"))
        self.zulrah = Activity(activities.get("Zulrah"))
