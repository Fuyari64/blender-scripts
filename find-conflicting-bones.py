import bpy

obj = bpy.context.active_object
assert obj is not None and obj.type == 'MESH', "active object is invalid"
assert bpy.context.mode == 'OBJECT', "invalid mode, pls select OBJECT mode"

mesh = obj.data

group_lookup = {g.index: g.name for g in obj.vertex_groups}
verts = {name: [] for name in group_lookup.values()}
for v in mesh.vertices:
    for g in v.groups:
        verts[group_lookup[g.group]].append(v.index)

vertice_number = 0
found_group = ''
attempted_group = ''
name_list = []
result_list = []
conflict = None
for name in verts.keys():
    conflict = False
    attempted_group = name
    name_list.append(name)
    for vertice_list in list(map(verts.get, name_list)):
        if vertice_list == verts.get(name) or not vertice_list:
            continue
        for v in verts.get(name):
            if v in vertice_list:
                conflict = True
                vertice_number += 1
                found_group = attempted_group
    if conflict == True:
        result_dict = {"Vertex Group": found_group, "Number of Conflicted Vertices": vertice_number}
        result_dict_copy = result_dict.copy()
        result_list.append(result_dict_copy)

print("Showing results for ", obj.name)
print(*result_list, sep='\n')

if len(result_list) == 0:
    print("No conflicts.")
else:
    print("^^^^^ Found conflicts ^^^^^^^")