from mylib import shell

def send_notify(msg="empty-msg", urgency="normal", time=1000):
    command = " ".join([
        f"notify-send '{msg}'",
        "" if time == "STAY" else f"-t {time}",
        f"-u {urgency}"
    ])

    shell.run( command )

def normal( msg="empty-msg", time=1000 ):
    send_notify( msg, "normal", time)

def error( msg="empty-msg", time=1000):
    send_notify( msg, "critical", time)

def low( msg="empty-msg", time=1000):
    send_notify( msg, "low", time )


def send_dunst(title="empty-title", body="", time=1000, urgency="normal", icon="", notify_id=""):
    args = [
        "dunstify",
        f"'{ title }'",
        f"'{ body }'" if body else "",
        "" if time == "STAY" else f"-t {time}",
        f"-u {urgency}",
        f"-i {icon}" if icon else "",
        f"-r {notify_id}" if notify_id else ""
    ]

    command = " ".join( args )

    shell.run( command )

VOL_NOTIFICATION_ID=99
SONG_NOTIFICATION_ID=99

def vol( msg, icon ):
    send_dunst(msg, "", 1000, "normal", icon, VOL_NOTIFICATION_ID)

def song( msg, icon ):
    send_dunst(msg, "", 2000, "normal", icon, SONG_NOTIFICATION_ID)
