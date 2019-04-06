from uptime import *
def s37uptime():
    uptimebrut = uptime()
    heure = round(uptimebrut/(3600))
    minutes = round((uptimebrut - heure * 3600)/60)
    if minutes < 0:
        heure = heure - 1
        minutes = round((uptimebrut - heure * 3600)/60)
    return (heure, minutes)