# Youtube Link: 

# Organize objects to display layer in Maya using Python

# importing nessory modules
import pymel.core as pm

# Getting the top level transform node
assemblies = pm.ls(assemblies=True)

# Creating the ignore list.
excludeType = ['persp', 'top', 'side', 'front']

# Empty list created for adding assemblies
finalAssemblies = []

# Looping through all assemblies
for each in assemblies:
	# Checking whether each item is not in exclude list. if avaliable it will be ignored
	if each not in excludeType:
		# Adding each item from list if not avaliable in exclude list
		finalAssemblies.append(each)

# Getting the list of catagories with out duplicates.

# empty list to store catagories
catagory = []

# Looping through final assemblies
for each in finalAssemblies:
	# Splitting the name based on "_"
	typ, col = each.split('_')
	# Adding the typ variable to the list
	catagory.append(typ)
# Removing the duplicates from generated list and assigning as a new variable.
finalCatagory = list(set(catagory))

# Looping through catagory
for eachCatagory in finalCatagory:
	# Creating a new display layer with the each catagory name.
	pm.createDisplayLayer(name=eachCatagory, empty=True)
	# Looping through all final assemblies
	for eachAssembly in finalAssemblies:
		# Checking whether each assembly is starting with catagory name.
		if eachAssembly.startswith(eachCatagory):
			# Adding the assembly to the catagory display layer.
			pm.editDisplayLayerMembers(eachCatagory, eachAssembly)