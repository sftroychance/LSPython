# Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will certainly be involved. Each race has a certain worth when battling against others. On the side of good we have the following races, with their associated worth:

# Hobbits: 1
# Men: 2
# Elves: 3
# Dwarves: 3
# Eagles: 4
# Wizards: 10
# On the side of evil we have:

# Orcs: 1
# Men: 2
# Wargs: 2
# Goblins: 2
# Uruk Hai: 3
# Trolls: 5
# Wizards: 10
# Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

# Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side wins.

# Input:
# The function will be given two parameters. Each parameter will be a string of multiple integers separated by a single space. Each string will contain the count of each race on the side of good and evil.

# The first parameter will contain the count of each race on the side of good in the following order:

# Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
# The second parameter will contain the count of each race on the side of evil in the following order:

# Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
# All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.

def good_vs_evil(good, evil):
    WORTH = {
        'hobbits': 1,
        'men': 2,
        'elves': 3,
        'dwarves': 3,
        'eagles': 4,
        'wizards': 10,
        'orcs': 1,
        'wargs': 2,
        'goblins': 2,
        'uruk_hai': 3,
        'trolls': 5
    }

    hobbits, men, elves, dwarves, eagles, wizards = [int(x) for x in good.split()]

    good_score = (
        hobbits * WORTH['hobbits']
        + men * WORTH['men']
        + elves * WORTH['elves']
        + dwarves * WORTH['dwarves']
        + eagles * WORTH['eagles']
        + wizards * WORTH['wizards']
    )

    orcs, men, wargs, goblins, uruk_hai, trolls, wizards = [int(x) for x in evil.split()]

    evil_score = (
        orcs * WORTH['orcs']
        + men * WORTH['men']
        + wargs * WORTH['wargs']
        + goblins * WORTH['goblins']
        + uruk_hai * WORTH['uruk_hai']
        + trolls * WORTH['trolls']
        + wizards * WORTH['wizards']
    )

    result = 'Battle Result: '

    if evil_score > good_score:
        result += 'Evil eradicates all trace of Good'
    elif good_score > evil_score:
        result += 'Good triumphs over Evil'
    else:
        result += 'No victor on this battle field'

    return result


print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
