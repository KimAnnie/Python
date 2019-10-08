
# coding: utf-8

# In[1]:


from geometry.area.circle import circle_area
circle_area(3)

from geometry.area.rectangle import rectangle_area
rectangle_area(3,2)

from geometry.area.square import square_area
square_area(5)

from geometry.area.triangles import triangles_area
triangles_area(3,4)

print("\n")

from geometry.surface_area.cube import cube_surface_area
cube_surface_area(3)

from geometry.surface_area.cuboid import cuboid_surface_area
cuboid_surface_area(3,4,5)

from geometry.surface_area.cylinder import cylinder_surface_area
cylinder_surface_area(3,5)

from geometry.surface_area.sphere import sphere_surface_area
sphere_surface_area(3)

print("\n")

from geometry.volume.cube import cube_volume
cube_volume(3)

from geometry.volume.cuboid import cuboid_volume
cuboid_volume(3,6,8)

from geometry.volume.cylinder import cylinder_volume
cylinder_volume(3,10)

from geometry.volume.sphere import sphere_volume
sphere_volume(7)

