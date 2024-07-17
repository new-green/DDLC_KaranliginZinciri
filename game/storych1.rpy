label story_ch1:
    scene black
    play music t2 fadeout 0.5
    show monika 1b zorder 2 at t11

    #Oyuna giriş
    m "Etraf neden siyah?"
    mc "Bekle o zaman"
    scene bg club_day with wipeleft
    show monika 1a zorder 2 at t11
    "Işıkları açmaya gittim ve ışıkları açıp Monika'nın karşısına oturdum"
    mc "Işıkları açtım. Daha iyi oldu mu?"
    m "Evet! Daha iyi oldu. Bugün ne anlatacaksın [player]"

    #Hikaye kahramanları Anlatım
    mc "Bugün bir hikaye anlatacağım. Hikayenin adı 'Karanlığın Zinciri'."
    m "Anlat bakalım. Merak ettim."
    show monika 5a zorder 1 at h11
    m "Bu arada DokiTale Discord sunucusuna, xKetum, goddessaquasama, korayxby, the.ro3wy teşekkür ederim. Ana menü'de 'Credit' tuşuna basıldığında tam metini görebilirsiniz."
    show monika 1b zorder 1 at t11
    mc "Neyse devam edelim."
    mc "Hikâyeye başlayalım mı?"
    m "Evet."
    show monika 1j zorder 1 at t11
    mc "Önce karakterleri tanıtalım."

    #Sayori
    scene bg corridor with wipeleft
    show sayori 1a zorder 2 at t21
    mc "Bu Sayori. Grubun 'Neşeli' suratıdır. Genelde hep sıcakkanlı davranır. Her zaman güler yüzlüdür. "
    mc "Merhaba Sayori!"
    s 1x "Merhabaa!"
    hide sayori
    scene bg corridor with wipeleft

    #Natsuki
    show natsuki 5a zorder 1 at t22
    mc "Bu Natsuki. Grubun 'Korkusuz' denilebilecek tatlı bir üyedir."
    n 5r "Heeey! Ben tatlı değilim."
    mc "Tatlısın bir kere."
    m "Ehhhhh--{w=0.1}{nw}"
    hide natsuki 5r
    scene bg corridor with wipeleft

    #Yuri
    mc "Son olarak Yuri"
    show yuri 2q zorder 1 at t11 
    y "M{w=0.05}-M{w=0.05}-Merhaba!"
    mc "Merhaba Yuri!"
    mc "Bu ise Yuri. Grubun 'Utangaç' üyesi. Kendisi kitap kurdudur. Yanında sürekli çakı taşır."
    y 4a "Bu{w=0.05}-Bu doğru değil!"
    y "Ya{w=0.05}-Yalan söyleme!"
    hide yuri

    #Monika ile ufak bir sohbet/atışma
    show monika 2b zorder 1 at t11
    m "Karakterleri anlatman bittiysen hikâyeye devam edelim."
    mc "Evet bitti.{w=1.2}{nw}"
    m 2a "O zaman devam et."
    scene black with wipeleft
    hide monika
    stop music

    #Hikaye başlangıç
    show sayori 1a zorder 3 at h31
    mc "Sayori...{w=0.3}"
    show natsuki 1a zorder 3 at h32
    mc "Natsuki...{w=0.3}"
    show yuri 1a zorder 3 at h33
    mc "Ve Yuri...{w=0.3}"
    play music t4 fadeout 1.0
    hide sayori
    hide yuri
    hide natsuki
    mc "Bu üç arkadaş lise yıllarında arkadaşlıkları şekillenmiş ve güçlü bir sevgi bağı ile bağlanmışlardır."
    show bg afternoon_residential_day with wipeleft
    mc "Bu üç arkadaş bir gün neden kapatıldığı bilinmeyen bir okulun yanından geçerler."
    show natsuki 1a zorder 3 at h33
    n 1a "Burası babannemin eski okuluymuş. Bi ara buraya girelim mi? Hem burası uzun zamandır kullanılmamış. Bir problem olmaz bence."
    mc "Sayori çok heyecenlı şekilde:"
    show sayori 1a zorder 3 at h11
    s "Neden olmasın! Bize de eğlence çıkar!"
    show yuri 1b zorder 1 at h31
    y "Çok iyi olabilir. {w=0.7}Heyecenımızın yanında dikkatli de olmamız gerekir."
    mc "Yuri haklıydı. Başlarına aldıkları beladan habersizlerdi."
    mc "Natsuki alaycı söylemle:"
    n "Ama şöyle bir şey duydum var ki bu okula girenler tekrar çıkamıyormuş."
    show sayori 1c zorder 4 at h11
    s 1a "Güzel şaka Natsuki!!"
    mc "Yuri sesi hafif titreyerek"
    y 3n "Y-{w=0.2}Ya girmesek mi?"
    mc "Natsuki kahkağa atmaya başlar:"
    n 1z "HAHAHAHA! Şaka yaptım böyle bir şeye kim inanır ki."
    mc "Yuri sakinleşir ama haladaha korkmaktadır."
    show natsuki 1a

    #Monika araya dahil olur.
    scene bg club_day with wipeleft
    show monika 1a zorder 1 at h11
    m "Akıllı Yuri."
    mc "Evet akıllı."
    hide monika 1a
    scene bg afternoon_residential_day with wipeleft

    #Hikaye devam eder.
    mc "Evine yaklaştığını gören Natsuki Sayoriye seslenerek söyle der"
    show natsuki 1b zorder 1 at h11
    n "Sayori!"
    show sayori 1c zorder 1 at h33
    s "Efendiiim!"
    n 3a "Burası senin ev değil mi?"
    s 1a "AA eve gelmişiz."
    s "Ben burdan eve geçiyorum. Size görüşürüzzz!"
    hide sayori with moveoutright
    n "Görüşürüz"
    show yuri 1b zorder 1 at h31 
    y "Görüşürüz Sayori!"
    mc "Yalnız kalan ikili öylesine ettikleri bir sohbetten sonra Natsuki şöyle bir soru sorar."
    n  "Ne zaman gideceğimizi kararlaştırmadık."
    y 1a "Haftaya bugün gece saatlerinde gidelim mi?"
    mc "Natsuki göğüsünü kabartarak"
    n 5d "Olur neden olmasın."
    y "Sayoriyi bilgilendirmeyi unutmayalım."
    n 3a "Eve gidince ararım."
    y "Ailemize nasıl bir yalan uyduracağız?"
    n "Sayorinin ailesi 1 haftalığına evde olmayacakmış galiba. Ailemize 'Sayorilerde yatıya kalacağız.' deriz"
    y "Eve gidince arar sorarız."
    mc "Evine yaklaştığını gören Yuri Natsukiye doğru dönerek:"
    y "Benim evime de yaklaşmışız. Ben burdan evime geçeğim."
    n "Tamam görüşürüz o zaman."
    y "Görüşürüz."
    hide yuri with moveoutleft
    mc "Yalnız kalan Natsuki adımlarını hızlandırarak eve daha hızlı gitmeye çalışır ve evine hızlıca ulaşır."
    scene bg natsuki_bedroom with wipeleft_scene
    mc  "Sayoriyi aramak için telefonu alır ve Sayoriyi arar."
    show natsuki nf11 zorder 1 at t31
    n "Sayoriyi arayalım unutmadan."
    play music ringing
    mc "Telefonu eline alır ve Sayoriyi arar."
    play music t5
    n nf1btk "Hey Sayori!"
    show bg natandsayori_bedroom with wipeleft
    show sayori sp1atk zorder 1 at t33
    s "Efendim."
    n nf1atk "Biz okula girmek için haftaya bugünü düşündük. Sana uygun mudur?"
    s "Olur! Benim için uygundur. Zaten ailem de yok."
    n "Güzel. Birde şöyle birşey var.{w=0.2} Biz ailemizden izin alabilmek için 'Sayoride yatıya kalacağız. Zaten ailesi de evde değil.' diye bahane uydurduk."
    n "Sence de uygun mudur?"
    s "Olur! Problem olmaz."
    s "Sence evden neler götürmeliyiz?"
    n "Bilmem. {w=0.3}Fener falan götürürüz herhalde."
    s "Olabilir suda alırız. Şöyle birşey var.{w=0.2} Ailenizden birisi gelirse ne olacak?"
    n nf2atk "Kimse senin evini bilmiyor ki. Bize biraz uzak olduğun için. Okula en yakın sensin ama ne hikmetse en geç sen geliyorsun."
    s "Doğruuu!" 
    s "Birşey olmaz o zaman!"
    n nf1atk "Tamam o zaman yarın dışarıya geliyor musun?"
    s "Bugün Cuma'ydı dimi?"
    n "Evet?"
    s "Evet! Gelebilirim."
    n "Tamam o zaman! Görüşürüz!"
    s "Görüşürüz."
    hide natsuki
    hide sayori
    show black with wipeleft
    mc "Ertesi gün Sayori, Yuri ve Natsuki buluşurlar."
    mc "Okula girdiklerinde nelerle karşılaşabileceklerini tartışırlar."

    #Monika tekrar araya dahil olur. 
    play music t3g fadein 1.0
    scene bg club_day with wipeleft
    show monika 1a zorder 1 at h11
    m "Natsuki'nin haraketleri biraz fazla heycanlı gibi."
    mc "Biraz ya."
    mc "Tezcanlı diyelim."
    hide monika 1a
    show bg restorant with wipeleft
    
    #Hikayeye devam eder
    show natsuki 3ba zorder 1 at t11
    play music t2 fadeout 0.5
    n "Haftaya Cuma çok eğlenceli olacak."
    mc "Yuri hafif korkarak"
    show yuri 4ba zorder 1 at h33
    y "Bi-{w=0.1}Bilemiyorum."
    mc "Natsuki Yuri ile alay ederek."
    n "Haha! Korkuyorsun dimi?"
    mc "Yuri, Natsuki'nin alay ettiğini anladı. Bu yüzden Yuri Natsukiye hafif bağırarak."
    show yuri 2br zorder 1 at h33
    y "Natsuki! Sen korkmuyorsun sanki."
    mc "Natsuki koktuğunu belli etmeden bir şekilde cevap veriyor."
    n 5bf "Kork-{w=0.3}Korkmuyorum."
    mc "Herkes gibi o da korkuyor ama belli etmemeye çalışıyor. Başarılıda oluyor."
    mc "O sırada herşeyden habersiz mutlu mutlu içeceğinden yudumlayan Sayori olaya sakince katılmaya çalışıyor."
    show sayori 2ba zorder 1 at h31
    s "Olay ne?"
    n "Boşver..."
    mc "Sayori mutlu şekilde"
    s 4ba "Pekiiii!"
    mc "Natsuki ve Yuri Sayori için iç çekerek."
    ny "Gerizekalı!"
    show natsuki 1ba zorder 1 at t11
    show yuri 2ba zorder 1 at t33
    s 3bj "Heeey!"
    n 3by "Bugün geziyor muyuz kızlar?"
    show sayori 1bs zorder 1 at h31
    show yuri 1bd zorder 1 at h33 
    sy "Eveeet!"
    scene black with wipeleft
    mc "Gün boyu alışveriş merkezinde gezerler. Çılgınlar gibi eğlenirler ve günü öyle bitirirler."
    mc "Terk edilmiş okula girecekleri bir anlığına akıllarından çıkar bu üçlü grubumuzun."
    show bg afternoon_residential_day with wipeleft_scene
    show sayori 1ba zorder 1 at t11
    s "Bayağı eğlendik yine akşam ettik."
    show yuri 1ba zorder 1 at t33
    y "Değdi ama."
    show natsuki 1by zorder 1 at t31
    n "Eğlendik."
    n 1bk "Pazartesi okula geliyormusunuz?"
    show yuri 1bw zorder 1 at t33
    show sayori 1bj zorder 1 at t11
    sy "Maalesef."
    s 4bs "Ama Cuma günü büyük gün."
            
    #Monika araya tekrar girer
    play music t3g fadein 1.0
    scene bg club_day with wipeleft 
    show monika 1a zorder 1 at h11
    m 1j "Sayoriyide kaybettik."
    mc "O da heyecanlı."
    mc "Yuriyide kaybedeceğiz."
    m "Göreceğiz."
    hide monika 1a
    show bg afternoon_residential_day with wipeleft
    stop music

    #Hikaye devam eder
    play sound t2 fadein 1.5
    show yuri 1ba zorder 1 at t33
    show natsuki 1by zorder 1 at t31
    show sayori 1ba zorder 1 at t11
    mc "Natsuki ve Yuri heyecanlı şekilde."
    show yuri 3bd zorder 1 at h33
    show natsuki 4bz zorder 1 at h31
    ny "Eveeet!"
    s "Bugün çok gezdik. Evlere gidelim."
    ny "Evet gidelim."
    scene black with wipeleft_scene
    mc "Sayori, Yuri ve Natsuki evlerine heyecanlı şekilde dönerler."
    mc "Hafta içini gerçekten sıkıcı geçiren arkadaşlarımız cuma gününü iple çekmektedir."
    mc "Terk edilmiş okula girilmesine son 2 gün kala Sayori Natsukiyi arar ve Sayori uykudan yeni kaldırılmış Natsuki ile konuşmaya çalışır."
    show bg natandsayori_bedroom
    show sayori sp1atk zorder 1 at t33
    s "Hey Natsuki!"
    show natsuki nf2wtk zorder 1 at t31 
    n "Ne var!"
    s "Yanımıza powerbank alalım mı?"
    n "O ne?"
    s "Powerbank?"
    s "Uyuyor muydun?"
    n "Evet!"
    s "O zaman bize gel."
    n "Nee?"
    s "Bize geeel!"
    n "Tamam bekle."
    hide natsuki with moveoutleft
    mc "Der ve kapıyı kapatır."
    hide sayori
    show bg house with wipeleft
    mc "Sayori üstünü değiştirir ve Natsukiyi dışarıda bekler."
    show sayori 2br zorder 1 at t22
    mc "Natsuki 10 dakika sonra gelir ver Natsukiye bağırır."
    s "Natsukiiiii!"
    show natsuki 1bb zorder 1 at h21
    n "Bana yemek vericeksin!"  
    s 2bi "Tamam ya! Eve yeni geldin."
    s "Eve geçelim veririz."
    s 1bh "Ayrıca niye kızıyorsun."
    hide sayori
    n "Sana-{nw}"
    mc "Natsuki sözünü bitirmeden eve girer ve mecburen Natsuki de eve girer."
    show bg kitchen with wipeleft
    show sayori 1bh zorder 1 at h22
    s 1bi "Al sana yemek."
    n 1bi "Sa-{w=0.8}Sağol."
    mc "Natsuki 10 dakika sonra yemeğini bitirir ve Sayoriye dönerek."
    n 5bc "Yemek için teşekkür ederim."
    mc "Ve ardından."
    n 4ba "Çantayı hazırladın mı?"
    s 4bq "O yüzden evimdesin."
    n 4bg "Do-{w=0.3}Doğru..."
    s "Benim odama çıkalım orada hazılayalım."
    n "Olur."
    scene sayori_bedroom with wipeleft_scene
    show sayori 4bo zorder 1 at h21
    s "OOO."
    s 4bc "Çantaya ne koyucağız."
    show natsuki 4bb zorder 1 at h22
    n "Pil, fener, powerbank, su ve telefonlar."
    s 4ba "Hepsi var bir tek su yok."
    n 4ba "Su bizde var"
    show sayori 4bc zorder 1 at h21
    stop music
    play music t4 fadein 1.0
    s "Mükemmel. Ben powerbank'i şarja koyarım. Sonra çantaya atarız"
    n "Yuri nerede?"
    s "Çağırmadım."
    n "Tamam o zaman."
    scene black
    mc "Biraz eğlendikten sonra Natsuki saatin farkına varır."
    scene bg sayori_bedroom with wipeleft
    show natsuki 4bd zorder 1 at t11
    n "Saat geç olacak. Beni aramaları istemiyorum. Ben yavaştan eve geçeyim."
    show sayori 4ba zorder 1 at h21
    show natsuki 4ba zorder 1 at t22
    s "Tamam o zaman. Seni yolcu edeyim."
    n 4bc "Olur."
    mc "Sayori Natsukiyi kapıdan yolcu eder." 
    show bg house with wipeleft    
    s "Yarın okulda görüşürüz."
    n "Görüşürüz!"
    scene black with wipeleft
    mc "Sayori Natsukiyi yolcu ettikten sonra içeri girer ve sadece rasgele şeylerle uğraşır."
    mc "Ertesi gün okula giderler ve son kalan günler öylece geçer gider."
    pause 2.0
    mc "Ve Cuma günü gelip çatar. Sayori Natsuki ve Yuri'nin beklediği o gün. Sayori ve Natsuki koridorda karşılaşırlar."
    scene corridor with wipeleft
    show sayori 4c zorder 1 at h21
    show natsuki 5a zorder 1 at h22
    s "Yuri nerede?"
    n "Bilemiyorum."

$ Beta = True
$ Demo = True
$ Full_Story = False