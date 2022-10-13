colormap = [
 struct(r= 0, g= 0, b= 0) # 0 = noir
,struct(r=12, g=12, b=12) # 1 = gris pale
,struct(r=15, g=15, b=15) # 2 = blanc
,struct(r= 8, g= 8, b= 8) # 3 = gris fonce
,struct(r= 0, g= 8, b= 0) # 4 = vert fonce
]

images = [
 [ # 0 = case vide
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 ]
,[ # 1 = tuile "1"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 2 = tuile "2"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 3 = tuile "3"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 4 = tuile "4"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 5 = tuile "5"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 6 = tuile "6"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 7 = tuile "7"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 8 = tuile "8"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 9 = tuile "9"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,4,4,4,4,4,4,1,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 10 = tuile "10"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 11 = tuile "11"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,4,4,1,1,1,1,4,4,1,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 12 = tuile "12"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 13 = tuile "13"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 14 = tuile "14"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
,[ # 15 = tuile "15"
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
 ,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,1,1,1,1,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,1,1,1,1,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,4,4,1,1,4,4,4,4,4,4,1,3,3]
 ,[2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,3]
 ,[2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ,[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
 ]
]