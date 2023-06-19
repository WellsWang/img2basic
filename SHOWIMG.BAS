10 SCREEN 2


100 DIM bili%(1 TO 362)
110 DIM geek%(1 TO 315)
120 DIM text1%(1 TO 267)
130 DIM text2%(1 TO 255)
140 DIM blank%(1 TO 32)

200 DEF SEG = VARSEG(bili%(1))
210 BLOAD "bili.bin", VARPTR(bili%(1))
220 DEF SEG

300 DEF SEG = VARSEG(geek%(1))
310 BLOAD "geek.bin", VARPTR(geek%(1))
320 DEF SEG

400 DEF SEG = VARSEG(text1%(1))
410 BLOAD "text1.bin", VARPTR(text1%(1))
420 DEF SEG

500 DEF SEG = VARSEG(text2%(1))
510 BLOAD "text2.bin", VARPTR(text2%(1))
520 DEF SEG

1000 blank%(1) = 5: blank%(2) = 30
1010 FOR i = 3 TO 32 STEP 1
1020 blank%(i) = 0
1030 NEXT i


5000 s = 5
5010 FOR i = 0 TO 80 STEP s
5020 IF i > 0 THEN PUT (i - s, 50), blank%, PSET: PUT (640 - i, 54), blank%, PSET
5030 PUT (i, 50), bili%, PSET
5040 PUT (440 - i, 54), geek%, PSET
5050 NEXT i

6000 PUT (100, 100), text1%, PSET
6100 PUT (340, 100), text2%, PSET

