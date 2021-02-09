from jnius import autoclass

# We need a reference to the Java activity running the current
# application, this reference is stored automatically by
# Kivy's PythonActivity bootstrap

# This one works with Pygame
# PythonActivity = autoclass('org.renpy.android.PythonActivity')

# This one works with SDL2
PythonActivity = autoclass('org.kivy.android.PythonActivity')

activity = PythonActivity.mActivity

Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

vibrator.vibrate(10000)  # the argument is in milliseconds
