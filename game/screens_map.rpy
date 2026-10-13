## ============================================================
## SKJERMBILDER — Interaktivt kart, Spill9
## ============================================================

## Pulserende markør-animasjon
transform pulse_marker:
    alpha 1.0
    linear 0.5 alpha 0.3
    linear 0.5 alpha 1.0
    repeat

## Retningsknapp-stil
style map_direction_button:
    background "#000000bb"
    hover_background "#333333cc"
    padding (14, 8)

style map_direction_button_text:
    color "#ffffff"
    size 26
    hover_color "#f0c040"

style map_room_title:
    color "#ffffff"
    size 30


## ============================================================
## KARTSKJERMEN — klikk et rom for å gå inn
## ============================================================
screen map_screen():
    tag map

    ## Hvit bakgrunn + kartbilde
    add Solid("#ffffff")
    add "images/minimap.png"

    ## Klikkbare hotspots
    for room_id, room in rooms.items():
        $ rx, ry, rw, rh = room["map_pos"]
        button:
            xpos rx
            ypos ry
            xsize rw
            ysize rh
            background None
            hover_background "#f0c04044"
            action [
                Function(jump_to_room, room_id),
                Hide("map_screen"),
                Show("room_screen"),
            ]
            tooltip room["name"]

    ## «Du er her»-markør
    $ cx, cy = room_center(current_room)
    if is_moving:
        add "images/map_marker.png" at pulse_marker:
            xpos cx  ypos cy  anchor (0.5, 0.5)
        timer 1.8 action SetVariable("is_moving", False)
    else:
        add "images/map_marker.png":
            xpos cx  ypos cy  anchor (0.5, 0.5)

    ## Romnavnlabel
    frame:
        xpos 12  ypos 10
        padding (14, 8)
        background "#000000bb"
        text "📍 [rooms[current_room]['name']]" size 24 color "#ffffff"

    ## Tilbake-knapp (til spillets eget meny/script)
    textbutton "✕ Lukk kart":
        xalign 1.0  xoffset -14  ypos 12
        action Hide("map_screen")
        text_style "map_direction_button_text"
        background "#000000bb"
        padding (14, 8)


## ============================================================
## ROMSKJERMEN — foto av rommet du er i, med retningsknapper
## ============================================================
screen room_screen():
    tag room

    $ room  = rooms[current_room]
    $ views = room.get("views", {})
    $ exits = room.get("exits", {})
    $ img   = views.get(current_facing)

    ## Bakgrunn: romfoto eller mørk fallback
    if img:
        add img xsize 1280 ysize 720 fit "cover"
    else:
        add Solid("#1a1a2e")

    ## Romtittel øverst i midten
    frame:
        xalign 0.5  ypos 16
        padding (20, 10)
        background "#000000bb"
        text "[room['name']]" style "map_room_title"

    ## NORD-knapp (topp-midten)
    if "north" in views or "north" in exits:
        $ n_lbl = ("Gå inn ↑" if current_facing == "north" and "north" in exits else "Se nord ↑")
        button:
            xalign 0.5  ypos 75
            padding (16, 10)
            background "#000000bb"
            hover_background "#333333cc"
            action Function(face_or_move, "north")
            text n_lbl style "map_direction_button_text"

    ## SØR-knapp (bunn-midten)
    if "south" in views or "south" in exits:
        $ s_lbl = ("Gå inn ↓" if current_facing == "south" and "south" in exits else "Se sør ↓")
        button:
            xalign 0.5  yalign 1.0  yoffset -70
            padding (16, 10)
            background "#000000bb"
            hover_background "#333333cc"
            action Function(face_or_move, "south")
            text s_lbl style "map_direction_button_text"

    ## VEST-knapp (venstre midten)
    if "west" in views or "west" in exits:
        $ w_lbl = ("← Gå inn" if current_facing == "west" and "west" in exits else "← Se vest")
        button:
            xpos 18  yalign 0.5
            padding (16, 10)
            background "#000000bb"
            hover_background "#333333cc"
            action Function(face_or_move, "west")
            text w_lbl style "map_direction_button_text"

    ## ØST-knapp (høyre midten)
    if "east" in views or "east" in exits:
        $ e_lbl = ("Gå inn →" if current_facing == "east" and "east" in exits else "Se øst →")
        button:
            xalign 1.0  xoffset -18  yalign 0.5
            padding (16, 10)
            background "#000000bb"
            hover_background "#333333cc"
            action Function(face_or_move, "east")
            text e_lbl style "map_direction_button_text"

    ## Kart-knapp (øverst til høyre)
    button:
        xalign 1.0  xoffset -14  ypos 16
        padding (14, 10)
        background "#000000bb"
        hover_background "#333333cc"
        action [Hide("room_screen"), Show("map_screen")]
        text "🗺 Kart" style "map_direction_button_text"
