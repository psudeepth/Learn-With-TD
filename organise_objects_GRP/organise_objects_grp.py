# Youtube Link: https://youtu.be/rFIH1yvGYSo

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

# Looping through final catagories
for eachCata in finalCatagory:
	# Creating gropus with catagory name with _GRP as suffix
	cataGRP = pm.group(name='{}_GRP'.format(eachCata), em=True)
	# Looping through final assemblies
	for eachAssmb in finalAssemblies:
		# Checking whether each assembly is starting with catagory name.
		if eachAssmb.startswith(eachCata):
			# Adding the assembly to the specific group
			pm.parent(eachAssmb, cataGRP)
# Clearing the selection
pm.select(cl=True)