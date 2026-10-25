[app]

title = Star GPS
package.name = stargps
package.domain = org.stargps

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy,plyer

orientation = portrait
fullscreen = 0

android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

[buildozer]

log_level = 2
warn_on_root = 1
