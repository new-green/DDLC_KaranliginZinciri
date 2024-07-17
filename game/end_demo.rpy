label end_demo:
    #Demo burada biter.
    scene bg club_day with wipeleft 
    show monika 5a zorder 1 at h11
    play music zil fadein 0.5
    stop music
    play music t2
    m "Tüh zil çaldı."
    mc "40 dakika ne ara doldu ya."
    m "Yapçak birşey yok."
    m "Daha sonra devam edersin."
    mc "Aynen."
    mc "Şimdilik sınıflara dönelim."
    m "Tamam."
    m "Daha sonra görüşürüz."
    mc "Görüşürüz."
    m "Bu arada credit sayfasına bakmayı unutmayın."
    mc "Evet oraya da bakın."
    hide monika with wipeleft
    "Sınıftan öylece ayrılırız ve sınıflara döneriz."
    "Dersten sonra aynı yere dönmek için işaret yaparım ve öylece sınıfa gideriz."

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return