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

