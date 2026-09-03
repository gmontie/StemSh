10 a = 0
20 b = 0       
30 FOR i = 1 TO 5 
40   PRINT("=========") 
50   PRINT("   ~~~   i = ", i)
60   FOR j = 1 TO 3 
70     PRINT("b =  j * 2 + b") 
80     PRINT("b = ", j, " * 2 + ", b) 
90     b = j * 2 + b    
100     PRINT("b = ", b)    
110    WAIT 0.33 
120   NEXT     
130   PRINT ("=========") 
140   a = a + b  
150  PRINT ( "a=>> " , a )
160 NEXT 
170 PRINT("=========") 
