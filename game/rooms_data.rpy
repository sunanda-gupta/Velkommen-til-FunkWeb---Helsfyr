## ============================================================
## INTERAKTIVT KART — Spill9: Velkommen til FunkWeb Helsfyr
## ============================================================
## Legg disse filene i game/-mappen:
##   rooms_data.rpy      ← denne filen
##   screens_map.rpy     ← kart- og romskjermer
##   images/minimap.png  ← plankartet (1280×905)
##   images/map_marker.png
##   images/rooms/*.jpg  ← rombilde per retning
##
## Kall  show screen map_screen  fra script.rpy der du vil at
## kartet skal dukke opp (f.eks. i en meny eller etter intro).
## ============================================================

init python:

    rooms = {

        ## ── Åpne arbeidsområder ──────────────────────────────────────

        "aft_kandidater": {
            "name": "AFT-kandidaters arbeidsplass",
            "map_pos": (78, 160, 590, 235),
            "default_facing": "south",
            "views": {
                "north": "images/rooms/aft_kandidater_north.jpg",
                "east":  "images/rooms/aft_kandidater_east.jpg",
                "south": "images/rooms/aft_kandidater_south.jpg",
                "west":  "images/rooms/aft_kandidater_west.jpg",
            },
            "exits": {
                "south": "samtalerom_7",
                "west":  "lko_omradet",
            },
        },

        "lko_omradet": {
            "name": "LKO-området",
            "map_pos": (0, 355, 236, 195),
            "default_facing": "east",
            "views": {
                "north": "images/rooms/lko_omradet_north.jpg",
                "east":  "images/rooms/lko_omradet_east.jpg",
            },
            "exits": {
                "east":  "aft_kandidater",
                "south": "aft_veileder",
            },
        },

        ## ── Øvre kluster av rom ──────────────────────────────────────

        "samtalerom_7": {
            "name": "Samtale rom 7",
            "map_pos": (355, 360, 113, 130),
            "default_facing": "west",
            "views": {
                "west": "images/rooms/samtalerom_7_west.jpg",
            },
            "exits": {
                "north": "aft_kandidater",
                "east":  "samtalerom_8",
                "south": "rom_6",
            },
        },

        "samtalerom_8": {
            "name": "Samtale rom 8",
            "map_pos": (468, 360, 148, 130),
            "default_facing": "west",
            "views": {
                "west": "images/rooms/samtalerom_8_west.jpg",
            },
            "exits": {
                "west":  "samtalerom_7",
                "east":  "lager",
                "south": "rom_5",
            },
        },

        "lager": {
            "name": "Lager",
            "map_pos": (616, 360, 65, 130),
            "default_facing": "west",
            "views": {},
            "exits": {
                "west":  "samtalerom_8",
                "south": "rom_4",
            },
        },

        ## ── Nedre kluster (rom 4–6) ──────────────────────────────────

        "rom_6": {
            "name": "Rom 6",
            "map_pos": (355, 490, 90, 115),
            "default_facing": "east",
            "views": {
                "east": "images/rooms/rom_6_east.jpg",
            },
            "exits": {
                "north": "samtalerom_7",
                "east":  "rom_5",
            },
        },

        "rom_5": {
            "name": "Rom 5",
            "map_pos": (445, 490, 80, 115),
            "default_facing": "south",
            "views": {
                "south": "images/rooms/rom_5_south.jpg",
            },
            "exits": {
                "north": "samtalerom_8",
                "west":  "rom_6",
                "east":  "rom_4",
            },
        },

        "rom_4": {
            "name": "Rom 4",
            "map_pos": (525, 490, 80, 115),
            "default_facing": "west",
            "views": {},
            "exits": {
                "north": "lager",
                "west":  "rom_5",
                "east":  "kjoekken",
            },
        },

        ## ── Kjøkken og servicezone ───────────────────────────────────

        "kjoekken": {
            "name": "Kjøkken",
            "map_pos": (680, 455, 140, 115),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/kjoekken_north.jpg",
                "west":  "images/rooms/kjoekken_west.jpg",
            },
            "exits": {
                "west":  "rom_4",
                "east":  "toalett",
                "south": "sosial_sone",
            },
        },

        "toalett": {
            "name": "Toalett",
            "map_pos": (820, 480, 60, 90),
            "default_facing": "west",
            "views": {
                "west": "images/rooms/toalett_west.jpg",
            },
            "exits": {
                "west":  "kjoekken",
                "east":  "hc_toalett",
            },
        },

        "hc_toalett": {
            "name": "HC Toalett",
            "map_pos": (880, 460, 95, 110),
            "default_facing": "west",
            "views": {},
            "exits": {
                "west":  "toalett",
                "east":  "inngangsparti",
            },
        },

        "inngangsparti": {
            "name": "Inngangsparti",
            "map_pos": (975, 440, 185, 130),
            "default_facing": "west",
            "views": {
                "north": "images/rooms/inngangsparti_north.jpg",
                "east":  "images/rooms/inngangsparti_east.jpg",
                "south": "images/rooms/inngangsparti_south.jpg",
                "west":  "images/rooms/inngangsparti_west.jpg",
            },
            "exits": {
                "west":  "hc_toalett",
                "south": "samtalerom_1",
            },
        },

        ## ── AFT-veileder og nødutgang ────────────────────────────────

        "aft_veileder": {
            "name": "AFT-veileder kontor",
            "map_pos": (0, 565, 230, 195),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/aft_veileder_north.jpg",
                "east":  "images/rooms/aft_veileder_east.jpg",
            },
            "exits": {
                "north": "lko_omradet",
                "east":  "noedutgang",
            },
        },

        "noedutgang": {
            "name": "Nødutgang",
            "map_pos": (230, 595, 130, 70),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/noedutgang_north.jpg",
            },
            "exits": {
                "west":  "aft_veileder",
                "east":  "joergen_sondre",
            },
        },

        ## ── Kontorer (nedre korridor) ────────────────────────────────

        "joergen_sondre": {
            "name": "Jørgen og Sondres kontor",
            "map_pos": (358, 620, 145, 135),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/joergen_sondre_north.jpg",
                "west":  "images/rooms/joergen_sondre_west.jpg",
            },
            "exits": {
                "west":  "noedutgang",
                "east":  "hans_tore",
            },
        },

        "hans_tore": {
            "name": "Hans Tores kontor",
            "map_pos": (503, 620, 110, 135),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/hans_tore_north.jpg",
                "west":  "images/rooms/hans_tore_west.jpg",
            },
            "exits": {
                "west":  "joergen_sondre",
                "east":  "laila",
            },
        },

        "laila": {
            "name": "Lailas kontor",
            "map_pos": (613, 620, 100, 135),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/laila_north.jpg",
            },
            "exits": {
                "west":  "hans_tore",
                "east":  "sosial_sone",
            },
        },

        ## ── Sosial sone og møterom ───────────────────────────────────

        "sosial_sone": {
            "name": "Sosial sone",
            "map_pos": (680, 600, 220, 130),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/sosial_sone_north.jpg",
                "east":  "images/rooms/sosial_sone_east.jpg",
                "west":  "images/rooms/sosial_sone_west.jpg",
            },
            "exits": {
                "north": "kjoekken",
                "west":  "laila",
                "east":  "moeterom_3",
            },
        },

        "moeterom_3": {
            "name": "Samtale rom 3",
            "map_pos": (897, 615, 95, 145),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/moeterom_3_north.jpg",
            },
            "exits": {
                "west":  "sosial_sone",
                "east":  "moeterom_2",
            },
        },

        "moeterom_2": {
            "name": "Samtale rom 2",
            "map_pos": (992, 615, 85, 145),
            "default_facing": "west",
            "views": {
                "west": "images/rooms/moeterom_2_west.jpg",
            },
            "exits": {
                "west":  "moeterom_3",
                "east":  "samtalerom_1",
            },
        },

        "samtalerom_1": {
            "name": "Samtale rom 1",
            "map_pos": (1077, 600, 185, 165),
            "default_facing": "north",
            "views": {
                "north": "images/rooms/samtalerom_1_north.jpg",
                "west":  "images/rooms/samtalerom_1_west.jpg",
            },
            "exits": {
                "north": "inngangsparti",
                "west":  "moeterom_2",
            },
        },

    }


## ── TILSTAND ──────────────────────────────────────────────────────────────

default current_room    = "inngangsparti"
default current_facing  = "west"
default is_moving       = True


## ── HJELPEFUNKSJONER ──────────────────────────────────────────────────────

init python:

    def room_center(room_id):
        x, y, w, h = rooms[room_id]["map_pos"]
        return (x + w / 2.0, y + h / 2.0)

    def face_or_move(direction):
        global current_room, current_facing, is_moving
        room  = rooms[current_room]
        views = room.get("views", {})
        exits = room.get("exits", {})

        if current_facing == direction and direction in exits:
            target         = exits[direction]
            current_room   = target
            target_views   = rooms[target]["views"]
            current_facing = (direction
                              if direction in target_views
                              else rooms[target]["default_facing"])
            is_moving = True
        elif direction in views:
            current_facing = direction

    def jump_to_room(room_id):
        global current_room, current_facing, is_moving
        current_room   = room_id
        current_facing = rooms[room_id]["default_facing"]
        is_moving      = True
