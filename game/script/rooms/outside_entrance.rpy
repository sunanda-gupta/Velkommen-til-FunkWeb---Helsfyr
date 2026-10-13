screen map_button():
    zorder 100
    button:
        xpos 20
        ypos 20
        padding (12, 8)
        background "#342e57"
        hover_background "#fab63a"
        action Show("map_screen")
        text "🗺 Kart" color "#ffffff" size 24 hover_color "#342e57"

label outside_entrance:
    show screen map_button     
    scene expression Transform("images/bg/helsfyr_panorama_sol.webp", fit="cover", align=(0.5, 0.5)) with fade
    pause 1.8
    scene expression Transform("images/bg/inngangsparti_helsfyr_panorama_sol.webp", fit="cover", align=(0.5, 0.5)) with fade
    
    "Velkommen til FunkWeb på Helsfyr Panorama!"
    "I dette spillet skal du bli kjent med lokalene våre, menneskene som jobber her, og rommene du kan bruke."
    "Klikk deg rundt for å utforske."

    menu:
        "Velkommen inn":
            jump reception
