"""
Blender Animation Copy Script
Usage: 
1. Select the bones you want to copy animation for (in Pose Mode)
2. Run this script
3. It will copy animation from selected bones to all other actions
Note: It will only really work for repeating animations that have same amount of keyframes (which is the case for most of the weapon aiming animations in Sven Coop)
"""

import bpy

armature_name = "sven_model_skeleton"
source_action_name = 'ref_aim_onehanded_blend01'

target_bones = [b.name for b in bpy.context.selected_pose_bones]
print(target_bones)

armature = bpy.context.scene.objects[armature_name]

area = bpy.context.area
old_type = area.type
area.type = 'DOPESHEET_EDITOR'

for bone_name in target_bones:
    armature.animation_data.action.groups[bone_name].select = True
    bpy.ops.action.clickselect(channel=True)

bpy.ops.action.copy()

for action in bpy.data.actions:
    armature.animation_data.action = action
    bpy.ops.anim.keyframe_insert_menu(type='WholeCharacterSelected')
    bpy.ops.action.paste(offset='START', merge='OVER_RANGE_ALL')

area.type = old_type 