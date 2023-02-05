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
    Choice("La croyance en un chef unique !", +1, [
        "Croire en Balur a fait avancer le monde dans la bonne direction.",
        "Vive Balur !", "Que serions-nous devenus sans Balur ?",
        "Balur n'a pas fait grand chose pour nous.",
        "Est-ce que Balur a vraiment fait avancer le monde ?",
        "Balur a fait avancer le monde, mais il a aussi fait beaucoup de mal."]),
    Choice("Seul la guerre peut guider le monde", -2, [
        "La guerre est la seule façon de progresser.",
        "La guerre est une erreur.",
        "Seul les forts survivent.",
        "Le pacifisme crée juste des couteaux sous la gorge."]),
    Choice("Croyons en des textes et non des hommes", +3, [
        "L'Homme est un être faillible.",
        "Des lois dures permettent de maintenir l'ordre.",
        "Les lois sont faites pour être respectées.",
        "Croire en des textes nous aidera à avancer ?"]),
]

Free_Will : List[Choice] = [
    Choice("La pensée libre nous permettra de progresser", +3, [
        "La pensée libre a permis de faire avancer le monde.",
        "La pensée libre est le rouage de la société.",
        "Laisser les gens penser par eux-mêmes nous a permis de progresser",
        "La libre pensée de certains devrait être interdite !",
        "Une seule pensée devrait être autorisée !"]),
    Choice("Une pensée unique pour tous !", -2, [
        "Penser par soi-même n'amène qu'au malheur",
        "Une seule pensée pour un monde meilleur",
        "Seule la pensée des dirigeants est la bonne",
        "J'aimerai penser par moi-même, mais je veux aussi vivre",
        "Que faire si je ne veux pas suivre la pensée unique ?"]),
    Choice("Une idéologie forcée, pour mieux contrôler", -4, [
        "Pourquoi devrions nous penser par nous-mêmes ?",
        "L'idéologie, c'est ce qui pense à votre place.",
        "L'idéologie est la seule chose qui nous permet de vivre.",
        "Mieux vaut être un esclave heureux qu'un maître malheureux.",
        "Faisons confiance à nos dirigeants, ils savent ce qu'ils font !"]),
]

Freedom : List[Choice] = [
    Choice("La liberté est un droit fondamental", +3, [
        "La liberté est un droit fondamental.",
        "La liberté des uns s'arrête où commence celle des autres.",
        "La liberté commence où l'ignorance finit.",
        "La liberté est le droit de faire ce que les lois permettent.",
        "Soyons libre, soyons ignorant !",
        "Ne laissons pas les autres nous faire du mal, mais ne soyons pas le mal qui atteint les autres"]),
    Choice("La liberté est dangereuse", +1, [
        "La liberté est dangereuse",
        "L'Homme est un loup pour l'Homme",
        "Toutes les guerres sont civiles, car c'est toujours l'Homme contre l'Homme qui répend son propre sang",
        "Ne ne sommes pas libre et nous le serons jamais !",
        "Le monde est une prison dont on ne peut s'échapper"]),
    Choice("La liberté est un choix", -1, [
        "La liberté est un choix.",
        "La liberté n'est pas l'absence d'engagement, mais la capacité de choisir.",
        "Nos décisions mennent à des actes, nos actes, à notre destin",
        "La liberté est un choix, mais elle est aussi un fardeau",
        "Sommes nous vraiment maître de notre destin ? Si ce dernier se résume à la mort"])
]

Love : List[Choice] = [
    Choice("En amour, rien ne se finit que de très près...", +2, [
        "Le désir est l'essence de la vie.",
        "Vous ne pouvez pas vivre sans amour.",
        "Aimer c'est tout donner, et se donner soi-même.",
        "Le bonheur c'est la vie. Vivre s'est aimer.",
        "Par amour, vous pouvez tout faire, y laisser votre vie."]),
    Choice("L'amour est dangeureux", -2, [
        "Vous n'avez pas besoin d'amour pour vivre",
        "L'amour est une illusion, une illusion qui nous fait souffrir.",
        "L'amour n'est pas fait pour nous rendre heureux. Je crois qu'il est fait pour nous révéler dans quelle mesure nous avons la force de souffrir et de supporter.",
        "Rien n'est plus dangereux que l'amour, car il nous rend vulnérables.",
        "Zut, j'ai oublié de prendre mon anti-dépresseur ce matin."]),
    Choice("L'amour, c'est moi", + 4, [
        "L'amour est une expérience unique, et vous êtes unique.",
        "Le seul amour qui vaille est celui que vous donnez à vous-même.",
        "Regardez-vous dans le miroir, vous êtes magnifique.",
        "La seule personne qui vous aime vraiment, c'est vous.",
        "S'aimer soi-même, c'est le début d'une belle histoire d'amour qui durera éternellement."])
]

Death : List[Choice] = [
    Choice("La mort est un cadeau que vous ouvrez chaque soir.", -10, [
        "Une vie donnée sera toujours reprise. Quand ? Personne ne le sait.",
        "La vie est un cadeau empoisonné donné par la mère à la naissance, elle s'accompagnera toujours de la mort.",
        "Chaque jour, chaque heure, chaque minute, chaque seconde et c'est la mort qui nous attend.",
        "Il n'y a de bien dans la vie que l'espérance d'une autre vie.",
        "La mort est le dernier acte de votre vie, la terre est le premier acte de votre mort."]),
    Choice("La vie est un cadeau que vous ouvrez chaque matin.", +10, [
        "La vie est comme une commande de pizza, vous ne savez pas ce que vous allez recevoir, mais vous savez que vous allez aimer.",
        "Vivez, si m’en croyez, n’attendez à demain : Cueillez dès aujourd’hui les roses de la vie.",
        "Vous savez apprécier la vie, vous savez en profiter, vous savez en profiter...",
        "Croquez une pomme, croquez la vie. Goutez à ses saveurs, à ses couleurs, à ses odeurs.",
        "La vie est un cadeau dont vous êtes le protecteur."]),
    Choice("La mort n'est rien...", -20, [
        "La mort n'est rien : je suis seulement passé, dans la pièce à côté.",
        "Donnez-moi le nom que vous m'avez toujours donné.",
        "Continuez à rire de ce qui nous faisait rire ensemble.",
        "La vie signifie tout ce qu'elle a toujours été. Le fil n'est pas coupé.",
        "Je ne suis pas loin, juste de l'autre côté du chemin."])
]


Themes = [
    Theme("Qui croire ?",
        "Il y a longtemps, les hommes se sont réunis pour savoir vers qui se tourner. Un homme Balur s'est proposé pour les guider, d'autres voulaient la guerre, d'autres voulaient des lois. Quel choix aurions-nous dû faire ?",
        Believe),
    Theme("La pensée unique",
        "Chaque pensée est différente mais certaines pensées amménent au désastre. Devrions nous laisser les gens penser par eux-mêmes ou devrions nous leur imposer une pensée unique ?",
        Free_Will),
    Theme("La liberté",
        "La liberté est un droit fondamental, mais elle peut aussi être dangereuse. Devrions nous laisser les gens faire ce qu'ils veulent ou devrions nous les contrôler ?",
        Freedom),
    Theme("L'amour",
        "L'amour est un sentiment qui peut nous rendre tout aussi heureux, que malheureux... Souvenez-vous de ce que vous avez vécu, de ce que vous avez vu, de ce que vous avez ressenti.",
        Love),
    Theme("La mort",
        "La vie, la mort... La frontière est mince. La mort est un mystère, mais elle est aussi une réalité. Que devrions nous faire ?",
        Death)
]