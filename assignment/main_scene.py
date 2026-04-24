import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]


# Buildings inside the fenced area
create_building(name="building_#", position=(-8, 0, -6))
create_building(name="building_#",width=4, height=4, depth=3, position=(0, 0, -6))
create_building(name="building_#", height=10, position=(6, 0, -6))

create_building(name="building_#", position=(3, 0, -1))
create_building(name="building_#",width=2, height=5, depth=2, position=(-7, 0, 2))
create_building(name="building_#", height=6, position=(-1, 0, -13))
create_building(name="building_#", height=3, position=(-4, 0, -1.5))
create_building(name="building_#", height=12, position=(-1, 0, 4))

# Trees inside the fenced area
create_tree(position=(5, 0, -12))
create_tree(position=(-4, 0, -6))
create_tree(position=(4, 0, 4))
create_tree(position=(8, 0, 0), trunk_height=3.5, canopy_radius=1.8)

#This creates the entraces in the front of the town 
create_fence(position=(-15, 0, 13))
create_fence(position=(5, 0, 13))

#This is the rest of the fenced off area. 

fenceL = create_fence(length=30, post_count=16, position=(-30, 0, -2))
# Rotate fence to form the left side boundary
cmds.rotate(0, 90, 0, fenceL)
#THis builds the back of the fences around the town. 
create_fence(length=30, post_count=16, position=(-15, 0, -17))
# Right boundary fence
fenceR = create_fence(length=30, post_count=16, position=(0, 0, -2))
cmds.rotate(0, 90, 0, fenceR)

#These are the several lamps we places in the town
create_lamp_post(position=(5, 0, 9))
create_lamp_post(position=(-10, 0, 5))
create_lamp_post(position=(10, 0, -7))
create_lamp_post(position=(-10, 0, -12))

# Circle placements around the town
place_in_circle(create_tree, count=15, radius=30)  
place_in_circle(create_tree, count=8, radius=20)      # ring of trees
place_in_circle(create_lamp_post, count=6, radius=15)  # ring of lamppost
 
# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
