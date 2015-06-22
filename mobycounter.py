original = open('mobydick.txt').read()
txt_split = original.split()
whalecount = 0
mobycount = 0
whitecount = 0
orphancount = 0
whale_forms = ['whale', 'whales','Whale','Whales']
moby_forms = ['moby','Moby']
white_forms = ['white','White','whiteness']
orphan_forms = ['orphan', 'Orphan', 'Orphans', 'orphans', 'orphans.',]

for word in txt_split:
    if word in whale_forms:
        whalecount += 1
    if word in moby_forms:
        mobycount += 1
    if word in white_forms:
        whitecount += 1
    if word in orphan_forms:
        orphancount += 1

print("The whale count is %d\nThe moby count is %d\nThe white count is %d\nThe orphan count is %d" % (whalecount,mobycount,whitecount,orphancount))

