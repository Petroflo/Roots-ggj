@dataclass
Choice:
    choice: str
    era_score: int
    quotes: List[str]
    position = [0, 0]

@dataclass
Theme:
    theme_name: str
    context: str
    choices: List[Choice]

Believe : List[Choice] = [
    Choice("La croyance en un chef unique !", +1, ["Croire en Balur a fait avancer le monde dans la bonne direction.", "Vive Balur !", "Que serions-nous devenus sans Balur ?", "Balur n'a pas fait grand chose pour nous.", "Est-ce que Balur a vraiment fait avancer le monde ?", "Balur a fait avancer le monde, mais il a aussi fait beaucoup de mal."]),
    Choice("Seul la guerre peut guider le monde", -2, ["La guerre est la seule façon de progresser.", "La guerre est une erreur.", "Seul les forts survivent.", "Le pacifisme crée juste des couteaux sous la gorge."]),
    Choice("Croyons en des textes et non des hommes", +3, ["L'Homme est un être faillible.", "Des lois dures permettent de maintenir l'ordre.", "Les lois sont faites pour être respectées.", "Croire en des textes nous aidera à avancer ?"]),
]

Free_Will : List[Choice] = [
    "La pensée libre nous permettra de progresser", +3, ["La pensée libre a permis de faire avancer le monde.", "La pensée libre est le rouage de la société.", "Laisser les gens penser par eux-mêmes nous a permis de progresser", "La libre pensée de certains devrait être interdite !", "Une seule pensée devrait être autorisée !"]
    "Une pensée unique pour tous !", -4, ["Penser par soi-même n'améne qu'au malheur", "Une seule pensée pour un monde meilleur", "Seul la pensée des dirigeants est la bonne", "J'aimerai penser par moi-même, mais je veux aussi vivre", "Que faire si je ne veux pas suivre la pensée unique ?"]

Themes = [
    Theme("Qui croire ?", "Il y a longtemps, les hommes se sont réunis pour savoir vers qui se tourner. Un homme Balur s'est proposé pour les guider, d'autres voulaient la guerre, d'autres voulaient des lois. Quel choix aurions-nous dû faire ?", Believe)
    Theme("La pensée unique", "Chaque pensée est différente mais certaines pensées amménent au désastre. Devrions nous laisser les gens penser par eux-mêmes ou devrions nous leur imposer une pensée unique ?", Free_Will)
]