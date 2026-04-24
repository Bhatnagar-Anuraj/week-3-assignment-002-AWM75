import maya.cmds as cmds

# Creates a single building outline with a given position and size 
def create_building(name="building", width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a simple building from a cube, placed on the ground plane.

    The building is a single scaled cube whose base sits at ground level
    (y = 0) at the given position.

    Args:
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.

    Returns:
        str: The name of the created building transform node.
    """
    # Creates the building
    building = cmds.polyCube(w=width, h=height, d=depth, n=name)[0]

    x, y, z = position
    # This palces it in on the ground  
    cmds.move(x, y + height / 2.0, z, building)

    return building

# Buildings inside the fenced area
create_building(name="building_#", position=(-8, 0, -6))
create_building(name="building_#",width=4, height=4, depth=3, position=(0, 0, -6))
create_building(name="building_#", height=10, position=(6, 0, -6))

create_building(name="building_#", position=(3, 0, -1))
create_building(name="building_#",width=2, height=5, depth=2, position=(-7, 0, 2))
create_building(name="building_#", height=6, position=(-1, 0, -13))
create_building(name="building_#", height=3, position=(-4, 0, -1.5))
create_building(name="building_#", height=12, position=(-1, 0, 4))

# Tree creation
def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2, position=(0, 0, 0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy.

    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
    x, y, z = position

    # Creates the Tree trunk
    trunk = cmds.polyCylinder(r=trunk_radius, h=trunk_height)[0]
    cmds.move(x, y + trunk_height / 2.0, z, trunk)

    # Creates the canopy above the tree trunk 
    canopy = cmds.polySphere(r=canopy_radius)[0]
    
    # Moves the canopy so its overlapping the tree trunk 
    canopy_y = y + trunk_height + canopy_radius * 0.6
    cmds.move(x, canopy_y, z, canopy)

    # Groups the tree trunk and canopy
    tree = cmds.group(trunk, canopy, name="tree_group")

    return tree
# Trees inside the fenced area
create_tree(position=(5, 0, -12))
create_tree(position=(-4, 0, -6))
create_tree(position=(4, 0, 4))
create_tree(position=(8, 0, 0), trunk_height=3.5, canopy_radius=1.8)


# Fence creation
def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a simple fence made of posts and rails.

    The fence runs along the X axis starting at the given position.

    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
    """
    x, y, z = position
    parts = []

#  Space posts across the fence length evenly
    spacing = length / (post_count - 1)

    for i in range(post_count):
        # Creates the post 
        post = cmds.polyCube(w=0.2, h=height, d=0.2)[0]

        # places the post evenly along the X axis 
        post_x = i * spacing
        cmds.move(post_x, height / 2.0, 0, post)

        parts.append(post)

    # Creates the rails that connect the posts 
    rail = cmds.polyCube(w=length, h=0.2, d=0.2)[0]
    
    # Lowers the rail below the post
    cmds.move(length / 2.0, height * 0.75, 0, rail)

    parts.append(rail)

    # groups the fences together 
    fence_group = cmds.group(parts, name="fence_group")

    # Move fence to world position
    cmds.move(x, y, z, fence_group)

    return fence_group

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

#This creates the parameters that we can call to create several Lamp Posts in a row through out the code. 
def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a street lamp using a cylinder pole and a sphere light.

    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """
    x, y, z = position

    # Create pole at origin and lift so it sits on ground
    pole = cmds.polyCylinder(r=0.1, h=pole_height)[0]
    cmds.move(0, pole_height / 2.0, 0, pole)

    # Create light and place it on top of the pole
    lamp = cmds.polySphere(r=light_radius)[0]
    cmds.move(0, pole_height + light_radius, 0, lamp)

    # Group pole and lamp together
    lamp_group = cmds.group(pole, lamp, name="lamp_group")

    # Move entire lamp to final position
    cmds.move(x, y, z, lamp_group)

    # Create and assign material
    lamp_shader = cmds.shadingNode("lambert", asShader=True)
    cmds.setAttr(lamp_shader + ".color", 1.0, 0.95, 0.6, type="double3")

    cmds.select(lamp)
    cmds.hyperShade(assign=lamp_shader)

    return lamp_group

#These are the several lamps we places in the town
create_lamp_post(position=(5, 0, 9))
create_lamp_post(position=(-10, 0, 5))
create_lamp_post(position=(10, 0, -7))
create_lamp_post(position=(-10, 0, -12))

# Used for the circle placement 
import math


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0), **kwargs):
    """Place objects created by 'create_func' in a circular arrangement.

    This is a higher-order function: it takes another function as an
    argument and calls it repeatedly to place objects around a circle.

    Args:
        create_func (callable): A function from this module (e.g.,
            create_tree) that accepts a 'position' keyword argument
            and returns an object name.
        count (int): Number of objects to place around the circle.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Additional keyword arguments passed to create_func
            (e.g., trunk_height=4).

    Returns:
        list: A list of object/group names created by create_func.
    """
    results = []
    center_x, center_y, center_z = center

    for i in range(count):
        # figure out the angle for each obejct in the circle
        angle = (2 * math.pi / count) * i
        
        # Figures out the coordinates for the x and Z positions 
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        
        # Creates the circle with the proper positions 
        result = create_func(position=(x, center_y, z), **kwargs)
        results.append(result)

    return results

# Circle placements around the town
place_in_circle(create_tree, count=15, radius=30)  
place_in_circle(create_tree, count=8, radius=20)      # ring of trees
place_in_circle(create_lamp_post, count=6, radius=15)  # ring of lamppost
 







 