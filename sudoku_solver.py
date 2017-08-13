#! /usr/bin/python

# 3 x 3 - 362880 combinations
# 9 x 9 - 6,670,903,752,021,072,936,960 combinations
 
import copy
import pdb
 
EVERYTHING_DONE = False
TOTAL_COUNT = 0
 
MATRIX_S = 9
MATRIX_SPLITS = 3
MATRIX = [ [ 0 for _ in range( MATRIX_S ) ] for _ in range( MATRIX_S ) ]
EXISTING_COORDINATES = set()
 
def read_matrix( filepath ):
   
    global MATRIX
   
    MATRIX = []
    lines = open( filepath ).readlines()
    for i in xrange( len(lines) ):
        temp_list = map( int , lines[i].strip().split() )
        for j in xrange( len( temp_list ) ):
            val = temp_list[j]
            if val > 0 :
                EXISTING_COORDINATES.add( (i,j) )
        MATRIX.append( temp_list )
           
            
 
def disp( narr ):
    print '+'+'-'*( MATRIX_S + MATRIX_S +1 )+'+'
    for i,l in enumerate( narr ):
        print '| '+' '.join( map( str , l ) )+' |'
           
    print '+'+'-'*( MATRIX_S + MATRIX_S +1 )+'+'
 
def hori_verti( narr , x , y ):
    val = narr[x][y]
   
    # Horizontal conflict detection
    if narr[x].count( val ) > 1 :
        return False
       
    # Vertical conflict detection
    y_list = list( narr[i][y] for i in xrange( MATRIX_S ) )
    if y_list.count( val ) > 1 :
        return False
       
    return True
   
 
def inmatrix( narr , x , y ):
    val = narr[x][y]
    xmatrix_pos = x/MATRIX_SPLITS
    ymatrix_pos = y/MATRIX_SPLITS
   
    xmatrix_pos = xmatrix_pos * MATRIX_SPLITS
    ymatrix_pos = ymatrix_pos * MATRIX_SPLITS
   
    # Convert the matrix into a list of numbers and then count
    final = []
    for i in xrange( xmatrix_pos , xmatrix_pos + MATRIX_SPLITS ):
        for j in xrange( ymatrix_pos , ymatrix_pos + MATRIX_SPLITS ):
            final.append( narr[i][j] )
   
    if final.count( val ) > 1 :
        return False
       
    return True
   
def test_inmatrix():
    k=1   
    for i in range( 0 , MATRIX_SPLITS ):
        for j in range( 0 , MATRIX_SPLITS ):
            MATRIX[i][j] = k
            k+=1
    MATRIX[0][2] = 2
   
    if inmatrix( MATRIX , 0 , 2 ) == False :
        print 'Works Fine'
   
def start( arr, x , y ):
   
    global EVERYTHING_DONE, TOTAL_COUNT
   
    # Increase x and try with y again if this is hit
    if y >= MATRIX_S:
        x += 1
        y = 0
       
    # Everything is done if this is hit and returning with out
    # further execution
    if x >= MATRIX_S:
        EVERYTHING_DONE = True
        return
   
    # pdb.set_trace()
   
    # Trying all the values in that x,y box
    # If Everything is complete then return and dont proceed  
    
    if (x,y) in EXISTING_COORDINATES:
        start( arr, x , y+1 )
    else:
        for val in range(1, 10):
            arr[x][y] = val
            if hori_verti( arr , x , y ) and inmatrix( arr , x , y ):
                start( arr , x , y+1 )
                if EVERYTHING_DONE:
                    break
                    #TOTAL_COUNT += 1
                    #EVERYTHING_DONE = False
            arr[x][y] = 0
   
 
def main():
    check_copy = copy.deepcopy( MATRIX )
    disp( MATRIX )
    start( MATRIX , 0 , 0 )
    disp( MATRIX )
    if check_copy == MATRIX :
        print '[-]Looks like no solutions was found.'
        print '[-]Please check the input and verify if it is valid.'
 
 
if __name__ == '__main__' :
    filepath = r'sudoku.txt'
    read_matrix( filepath )
    main()
    # print EXISTING_COORDINATES
   
    # print 'Total number of possibilities is {}'.format( TOTAL_COUNT )
      
