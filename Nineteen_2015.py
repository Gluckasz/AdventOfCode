replacements = {}
skip_line = False
data = open("/Users/lukasz/Desktop/Aoc 2015/Nineteen_2015_data.txt", "r")
for line in data:
    if not skip_line:
        if line is not "\n":
            line_split = line.split()
            replacements[line_split[2]] = line_split[0]
        else:
            skip_line = True
    else:
        molecule = line
molecules = set()
for replacement in replacements:
    if replacements[replacement] in molecule:
        find = molecule.find(replacements[replacement])
        new_molecule = molecule[:find] + replacement + molecule[find+len(replacements[replacement]):]
        molecules.add(new_molecule)
        while True:
            find = molecule.find(replacements[replacement], find + 1)
            if find == -1:
                break
            new_molecule = molecule[:find] + replacement + molecule[find+len(replacements[replacement]):]
            molecules.add(new_molecule)
print(len(molecules))
steps = set()
molecule_start ="e"
def all_recipes(molecule_step, step):
    if molecule_step == molecule_start:
        print(step)
    else:
        potential_replacements = list(replacements.keys())
        for replacement in potential_replacements:
            if replacement in molecule_step:
                potential_replacement = replacement
                break
        for replacement in potential_replacements:
            if len(replacement) > len(potential_replacement) and replacement in molecule_step:
                potential_replacement = replacement
        all_recipes(molecule_step.replace(potential_replacement, replacements[potential_replacement], 1), step+1)
molecule_start = 'e'
all_recipes(molecule, 0)
