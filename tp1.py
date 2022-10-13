# Le Kinh Vi Phung - 20178538
# Cong Long Ren - 20220497
# Date - 16 Mars 2022
# Ce program sert a lancer un jeu de taquin qui se joue en solitaire

import tuiles
import math

largeur = 4 # size of the grid board 
size = 16   # size of each tile

# Procedure printing the coordinate (x,y) of the pixels
def afficherImage(x, y, colormap, image):       
    for j in range(size):
        for i in range(size):
            setPixel(i+size*(x-1),
                     j+size*(y-1),
                     colormap[tuiles.images[image][j][i]])

# Procedure printing the coordinate (x,y) of the tiles
def afficherTuile(x, y, tuile):
    afficherImage(x, y, tuiles.colormap, tuile)
    # print the tile with the designated colour

# Return the coordinates of the tile being clicked on
def attendreClic():
    while True:
        mouse = getMouse()
        sleep(0.01)
      #-------------------------------------#  
        if mouse.button == 1:     # when clicking the left mouse button
            pos = struct(x = mouse.x, y = mouse.y)
            if mouse.x >= 0 and mouse.x <= size-1:
                pos.x = 0
            if mouse.x >= size and mouse.x <= size*2-1:
                pos.x = 1
            if mouse.x >= size*2 and mouse.x <= size*3-1:
                pos.x = 2
            if mouse.x >=size*3 and mouse.x <= size*4-1:
                pos.x = 3
       #-------------------------------------#     
            if mouse.y >= 0 and mouse.y <= size-1:
                pos.y = 0
            if mouse.y >= size and mouse.y <= size*2-1:
                pos.y = 1
            if mouse.y >= size*2 and mouse.y <= size*3-1:
                pos.y = 2
            if mouse.y >= size*3 and mouse.y <= size*4-1:
                pos.y = 3
            
            return pos
        # report the position of the mouse cursor while clicking the button
        
# Function that takes in 1 parameter n being an interger and returns a random
# list length = n
def permutationAleatoire(n):
    randomTab = []
    for i in range(0, n):
        randomTab.append(i)
    
    for index in range(len(randomTab)):
        newIndex = math.ceil(random()*n - 1)
        if newIndex >= index:
            temp = randomTab[index]
            randomTab[index] = randomTab[newIndex]
            randomTab[newIndex] = temp
    
    return randomTab
   
# Find the index of a specific number in a given list
def findIndex(tab, x):
    for index in range(len(tab)):
        if tab[index] == x:
            return index

# Find the position of the blank space given its index
def findVidePos(videIndex):
    if videIndex >= 0 and videIndex <= (largeur-1):
        ypos_0 = 0
    if videIndex >= largeur and videIndex <= (largeur*2-1):
        ypos_0 = 1
    if videIndex >= (largeur*2) and videIndex <= (largeur*3-1):
        ypos_0 = 2
    if videIndex >= (largeur*3) and videIndex <= (largeur*4-1):
        ypos_0 = 3    
    xpos_0 = videIndex - largeur*ypos_0
    return struct(x = xpos_0, y = ypos_0)

# Function that takes in 2 parameters: 
# tab with lenghth n which include all integers from 0 to n-1
# and a integer x from 1 to n-1
# return the element indicating where x is not ordered with tab
def inversions(tab, x):
    count = 0    
    n = findIndex(tab, x)
    for i in range(len(tab)):
        if x > tab[i] and tab[i] > 0 and n < i:
            count += 1
    return count

# Check if the current board is solvable or not
def soluble(tab):
    somme = 0
    rang = 0
    videRang = 0
    for i in range(len(tab)):       
        if len(tab) == 16: # 4*4
            rang = 4
        if len(tab) == 9:  # 3*3
            rang = 3
        if len(tab) == 4:  # 2*2
            rang = 2
        videIndex = findIndex(tab, 0)
        
        if rang%2 == 0:            
            if videIndex >= 0 and videIndex <= (rang-1):
                videRang = 1
            if videIndex >= rang and videIndex <= (rang*2-1):
                videRang  = 2
            if videIndex >= (rang*2) and videIndex <= (rang*3-1):
                videRang  = 3
            if videIndex >= (rang*3) and videIndex <= (rang*4-1):
                videRang  = 4        
               
        somme += inversions(tab, tab[i])  
    
    solubleNum = somme + videRang if rang%2==0 else somme    
    if solubleNum % 2 == 0:
        return True
    else:
        return False    # Proceed to function initiate to reset the taquin
    
# Create a new random solvable board
def initial(largeur):
    solvable = False    
    while not solvable: # If not solvable then reset the taquin
        nouveauTab = permutationAleatoire(largeur*largeur)
        
        if soluble(nouveauTab):
            solvable = True
        else:
            solvable = False
        
    return nouveauTab

# Function returns the solved list of the game
def goal(largeur):
    goalTab = list(range(1, largeur*largeur))
    goalTab.append(0)
    
    return goalTab # To identify if player solved the taquin or not

# Principal procedure of the game
def taquin(largeur):
    setScreenMode(largeur*size, largeur*size)
    tuileTab = initial(largeur)    
    goalTab = goal(largeur)
    videIndex = findIndex(tuileTab, 0) 
    videPos = findVidePos(videIndex) 
    
    index = 0    
    for y in range(1, largeur+1):
        for x in range(1, largeur+1):          
            afficherTuile(x, y, tuileTab[index])
            index += 1
                        
    while True:
        # clicPos and clicIndex are 2 variables returning the position
        # and the index respectively of the tile being clicked on
        clicPos = attendreClic() 
        clicIndex = clicPos.x + largeur*clicPos.y

        # Checking if the tile and the empty square are in the same row or 
        # same column in the board
        if clicPos.x == videPos.x or clicPos.y == videPos.y:          
       #--------------------------------------------------------------------#
           # Checking if the tile and the empty square are next to each other
           # horizontally or vertically. If so, swap their positions
            if clicIndex==videIndex-1 or clicIndex==videIndex-largeur or \
            clicIndex==videIndex+1 or clicIndex==videIndex+largeur:
            
                clicTuile = tuileTab.pop(clicIndex)
                tuileTab.insert(videIndex, clicTuile)
                tuileTab.remove(0)                       
                tuileTab.insert(clicIndex, 0)
        
                afficherTuile(clicPos.x +1, clicPos.y +1, 0)
                afficherTuile(videPos.x +1, videPos.y +1, clicTuile)
            
                videIndex = findIndex(tuileTab, 0)
                videPos = findVidePos(videIndex)
       
       #--------------------------------------------------------------------#
           # Checking if the tile is 1-tile away from the empty square 
           # horizontally or vertically. If so, move the tile, along with   
           # the one next to it to the empty square
            if clicIndex==videIndex-2 or clicIndex==videIndex-largeur*2 or \
            clicIndex==videIndex+2 or clicIndex==videIndex+largeur*2:
          
              #**************************************************#  
                if clicIndex == videIndex - 2:
                          
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuileNext = tuileTab.pop(clicIndex)
                                       
                    tuileTab.insert(clicIndex+1, clicTuile)
                    tuileTab.insert(videIndex, clicTuileNext)

                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x+2, clicPos.y+1, clicTuile)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuileNext)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex)          

              #**************************************************#  
                if clicIndex == videIndex - largeur*2:
                          
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuileNext = tuileTab.pop(clicIndex+largeur-1)
                 
                    tuileTab.insert(clicIndex+largeur-1, clicTuile)
                    tuileTab.insert(videIndex, clicTuileNext)
               
                    tuileTab.remove(0)                       
                    tuileTab.insert(clicIndex, 0)
                         
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x+1, clicPos.y+2, clicTuile)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuileNext)
            
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex)              
              #**************************************************#    
                if clicIndex == videIndex + 2:
                
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuilePrev = tuileTab.pop(clicIndex-1)
                                       
                    tuileTab.insert(clicIndex-1, clicTuile)
                    tuileTab.insert(videIndex, clicTuilePrev)            
                          
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x, clicPos.y+1, clicTuile)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuilePrev)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex) 
              #**************************************************# 
                if clicIndex == videIndex + largeur*2:
                
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuilePrev = tuileTab.pop(clicIndex-largeur)
                                                     
                    tuileTab.insert(clicIndex-largeur, clicTuile)
                    tuileTab.insert(videIndex, clicTuilePrev)
                
                    tuileTab.remove(0)                       
                    tuileTab.insert(clicIndex, 0)               
                                         
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x+1, clicPos.y, clicTuile)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuilePrev)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex) 
        
       #--------------------------------------------------------------------#
           # Checking if the tile is 2-tiles away from the empty square 
           # horizontally or vertically. If so, move the tile, along with   
           # all the tiles next to it to the empty square
            if clicIndex==videIndex-3 or clicIndex==videIndex-largeur*3 or \
            clicIndex==videIndex+3 or clicIndex==videIndex+largeur*3:
              #**************************************************# 
                if clicIndex == videIndex - 3:
                
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuileNext = tuileTab.pop(clicIndex)
                    clicTuileNext_2 = tuileTab.pop(clicIndex)
       
                    tuileTab.insert(clicIndex+1, clicTuile)
                    tuileTab.insert(clicIndex+2, clicTuileNext)
                    tuileTab.insert(videIndex, clicTuileNext_2)
                          
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x+2, clicPos.y+1, clicTuile)
                    afficherTuile(clicPos.x+3, clicPos.y+1, clicTuileNext)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuileNext_2)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex)
              #**************************************************#    
                if clicIndex == videIndex - largeur*3:
                
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuileNext = tuileTab.pop(clicIndex+largeur-1)
                    clicTuileNext_2 = tuileTab.pop(clicIndex+largeur+2)             
                                                     
                    tuileTab.insert(clicIndex+3, clicTuile)
                    tuileTab.insert(clicIndex+7, clicTuileNext)
                    tuileTab.insert(videIndex, clicTuileNext_2)
                    tuileTab.remove(0)                       
                    tuileTab.insert(clicIndex, 0)       
                          
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x+1, clicPos.y+2, clicTuile)
                    afficherTuile(clicPos.x+1, clicPos.y+3, clicTuileNext)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuileNext_2)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex)
           
              #**************************************************# 
                if clicIndex == videIndex + 3:
                
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuilePrev = tuileTab.pop(clicIndex-1)
                    clicTuilePrev_2 = tuileTab.pop(clicIndex-2)
                
                    tuileTab.insert(videIndex, clicTuilePrev_2)
                    tuileTab.insert(clicIndex-2, clicTuilePrev)
                    tuileTab.insert(clicIndex-1, clicTuile)                         
                          
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x, clicPos.y+1, clicTuile)
                    afficherTuile(clicPos.x-1, clicPos.y+1, clicTuilePrev)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuilePrev_2)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex)
           
              #**************************************************#  
                if clicIndex == videIndex + largeur*3:
                
                    clicTuile = tuileTab.pop(clicIndex)
                    clicTuilePrev = tuileTab.pop(clicIndex-largeur)
                    clicTuilePrev_2 = tuileTab.pop(clicIndex-largeur*2)
                
                    tuileTab.insert(videIndex, clicTuilePrev_2)
                    tuileTab.insert(clicIndex-7, clicTuilePrev)
                    tuileTab.insert(clicIndex-3, clicTuile)                                             
                    tuileTab.remove(0)                       
                    tuileTab.insert(clicIndex, 0)
                
                    afficherTuile(clicPos.x+1, clicPos.y+1, 0)
                    afficherTuile(clicPos.x+1, clicPos.y, clicTuile)
                    afficherTuile(clicPos.x+1, clicPos.y-1, clicTuilePrev)
                    afficherTuile(videPos.x+1, videPos.y+1, clicTuilePrev_2)
                
                    videIndex = findIndex(tuileTab, 0)
                    videPos = findVidePos(videIndex)
                   
        else:
            continue
       
      # If the board is solved, alert the message 'Congratulations' and 
      # instruct player click OK to reset the board and restart
        if tuileTab == goalTab:
            sleep(0.01)
            alert('Congratulation! Click OK to reset') # The message
            taquin(largeur) # Reset taquin

            
# 3.9
# Procedure which conduct all the unit testing for other function and procedure
def testTaquin():
    setScreenMode(16, 16)
    
  #Test for afficherImage() 
    afficherImage(1, 1, tuiles.colormap, 0) 
    assert exportScreen() == '\n'.join(['#000'*16]*16)  
    
  #Test for afficherTuile()
    afficherTuile(1, 1, 0)
    assert exportScreen() == '\n'.join(['#000'*16]*16)
   
  #Test for permutationAleatoire()
    assert permutationAleatoire(0) == []
    assert permutationAleatoire(1) == [0]
    assert permutationAleatoire(2) == [1,0] or [0,1]
    assert permutationAleatoire(3) == [0, 1, 2] or [0, 2, 1] or [1, 0, 2] or \
                                      [1, 2, 0] or [2, 0, 1] or [2, 1, 0]
    assert 0 in permutationAleatoire(9) 
    assert 10 not in permutationAleatoire(9)
    
  #Test for inversions()
    tab = [1,2,3]
    assert inversions(tab, 1) == 0
    assert inversions(tab, 2) == 0
    assert inversions(tab, 3) == 0
    
    tab1 = [3,2,1]
    assert inversions(tab1, 1) == 0
    assert inversions(tab1, 2) == 1
    assert inversions(tab1, 3) == 2

  #Test for soluble()
    tab = []
    assert soluble(tab) == True
    tab1 = [0,0,0,0]
    assert soluble(tab1) == False
    tab2 = [1,2,3,0]
    assert soluble(tab2) == True
    tab3 = [0,1,2,3]
    assert soluble(tab3) == False
    tab4 = [0,1,2,3,4,5,6,7,8]
    assert soluble(tab4) == True
    tab5 = [8,7,6,5,4,3,2,1,0]
    assert soluble(tab5) == True   
    tab6 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    assert soluble(tab6) == False
    tab7 = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    assert soluble(tab7) == False
    
  #Test for initial()
    assert initial(0) == []
    assert initial(1) == [0]
    assert initial(2) == [0, 1, 2, 3] or [0, 1, 3, 2] or [0, 2, 1, 3] or \
    [0, 2, 3, 1] or [0, 3, 1, 2] or [0, 3, 2, 1] or [1, 0, 2, 3] or \
    [1, 0, 3, 2] or [1, 2, 0, 3] or [1, 2, 3, 0] or [1, 3, 0, 2] or \
    [1, 3, 2, 0] or [2, 0, 1, 3] or [2, 0, 3, 1] or [2, 1, 0, 3] or \
    [2, 1, 3, 0] or [2, 3, 1, 0] or [2, 3, 0, 1] or [3, 0, 1, 2] or \
    [3, 0, 2, 1] or [3, 1, 0, 2] or [3, 1, 2, 0] or [3, 2, 0, 1] or \
    [3, 2, 1, 0]
    assert 4 not in initial(2)
    assert 0 in initial(2)
    
    
testTaquin()