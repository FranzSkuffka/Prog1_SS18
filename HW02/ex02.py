import re
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

corpus_text = \
    "ENGLAND - Anno Domini 932 Halt ein! Halt! Wer geht dort? Ich " \
    "bin es, Artus, Sohn des Uther Pendragon, vom Schloss Camelot. " \
    "KÃ¶nig der Briten, Sieger Ã¼ber die Sachsen. Herrscher Ã¼ber " \
    "ganz England! Ich kenne bessere Witze. Das bin ich aber, " \
    "und dies ist mein treuer Diener Patsy. Wir reiten quer durch " \
    "das ganze Land, auf der Suche nach Rittern, die mir auf " \
    "meinen Hof in Camelot folgen. Ich muss deinen Herrn und " \
    "Meister sehen. -Wie? Auf einem Pferd geritten? -Ja. -Ihr " \
    "benutzt KokosnÃ¼sse! -Was? Ihr habt zwei leere " \
    "KokosnusshÃ¤lften und die klopft Ihr aneinander. Und? Wir " \
    "reiten, seit der Winterschnee die Lande zu bedecken begann. " \
    "-Durch das KÃ¶nigreich Mercia. -Wo habt ihr die KokosnÃ¼sse " \
    "her? Wir fanden sie. Fandet sie? In Mercia? Die Kokosnuss ist " \
    "eine tropische Frucht. -Was meint Ihr? -Dies ist eine " \
    "gemÃ¤ÃŸigte Klimazone. Die Schwalbe zieht mit der Sonne " \
    "sÃ¼dwÃ¤rts, die Mehlschwalbe, der Kiebitz... mÃ¶gen im Winter " \
    "wÃ¤rmere Gefilde suchen und doch sind sie uns nicht unbekannt. " \
    "-Wollt Ihr sagen, die Kokosnuss wandert? -Keineswegs. Sie " \
    "kÃ¶nnte getragen werden. -Was? Eine Schwalbe trÃ¤gt ne " \
    "Kokosnuss? -Sie kÃ¶nnte sie an der HÃ¼lle packen. Die Frage ist " \
    "nicht, wo sie sie packt, sondern die der " \
    "GewichtsverhÃ¤ltnisse. Ein Vogel mit 150 Gramm trÃ¤gt keine " \
    "500-Gramm Kokosnuss. Das ist unwichtig. Geh und sag deinem " \
    "Herrn, dass Artus aus Camelot hier ist. Um ihre " \
    "Fluggeschwindigkeit zu gewÃ¤hrleisten, muss eine Schwalbe 43 " \
    "Mal pro Sekunde mit den FlÃ¼geln schlagen, stimmts? -Bitte! " \
    "-Habe ich Recht? -Das interessiert mich nicht. - Ne " \
    "afrikanische Schwalbe kann es tragen. O ja! Eine afrikanische " \
    "Schwalbe vielleicht. Aber keine europÃ¤ische. Das meine ich. " \
    "Da stimme ich zu. Wirst du deinen Meister fragen, ob er mich " \
    "an meinen Hof in Camelot begleiten will? Allerdings sind " \
    "afrikanische Schwalben keine ZugvÃ¶gel. -Oh, ja. -Die schaffen " \
    "sowieso keine Kokosnuss. Moment mal! Wenn aber zwei Schwalben " \
    "eine Nuss zusammen trÃ¼gen? -Nein, sie brÃ¤uchten eine Schnur. " \
    "-Ganz einfach. Ein StÃ¼ck Schlingpflanze. -Unter den " \
    "RÃ¼ckenleitfedern? -Warum nicht?"

# Hier kommen Eure LÃ¶sungen der Aufgaben rein. Kommentarzeilen kÃ¶nnen
# wie hier gesetzt werden, indem eine Raute am Anfang der Zeile steht.
# Versucht, auf Englisch zu kommentieren (falls nÃ¶tig) und auch
# englische Variablennamen zu benutzen. Diesen Kommentar dÃ¼rf Ihr
# natÃ¼rlich auch lÃ¶schen, ebenfalls die nÃ¤chste Beispielzeile:

# 1.
corpus_text_cleaned = re.sub('[^\da-zA-Z\s]', '', corpus_text )

# 2. 
def uniq_words(text):
  return len(set(text.lower().split()))

print("Types", uniq_words(corpus_text_cleaned))

# 3
corpus_text_lowered_reversed = corpus_text.lower()[::-1]
print(corpus_text_lowered_reversed)

# 4
to_find = ['reh', 'clown', 'nehcuarb', 'eis']

[print(sub, corpus_text_lowered_reversed.find(sub) != -1) for sub in to_find]

# 5
"""
x = {["Denethor"] , ["Smaug"] , ["Turambar"]}
y = {["Smaug"] , ["Tom Bombadil"] , ["Varda"]}
produces typeerror 'list not hashable'
"""
x = set(["Denethor", "Smaug" , "Turambar"])
y = set(["Smaug", "Tom Bombadil" , "Varda"])

print('common', x.intersection(y))
print('unique', x.symmetric_difference(y))
