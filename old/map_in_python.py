import pygal

wm = pygal.maps.world.World()
wm.title = "Ukraine"
wm.add('Europe', ['ua'])
wm.add('Europe/Asia', ['ru'])

wm.render_to_file('ukraine.svg')