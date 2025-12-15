def pourw(juga,jugb):
	max1,max2,fill=3,4,2
	print(f"{juga}\t{jugb}")
	if jugb==fill:
		return
	elif jugb==max2:
		pourw(0,juga)
	elif juga==0 and jugb==0:
		pourw(max1,juga)
	elif juga==fill:
		pourw(juga,0)
	elif juga<max1:
		pourw(max1,jugb)
	elif juga<(max2-jugb):
		pourw(0,juga+jugb)
	else:
		pourw(juga-(max2-jugb),max2)
print("juga \t jugb")
pourw(0,0)