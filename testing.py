from DataModelDict import DataModelDict as DM
import atomman as am

# Load dummy input
inputdict = DM('input.json')

# Build fcc unit cell
box = am.Box.cubic(3.2)
atoms = am.Atoms(pos=[[0.0, 0.0, 0.0], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0]])
ucell = am.System(atoms=atoms, box=box, scale=True)

# Modify system
system = ucell.supersize(3, 3, 3)

# Dump to json
system.dump('system_model', f='system.json', format='json')