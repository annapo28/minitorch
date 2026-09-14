# minitorch
The full minitorch student suite. 


To access the autograder: 

* Module 0: https://classroom.github.com/a/qDYKZff9

For Task 0.5: Visualization:

Parameters used:
- `linear.weight_0_0 = -10.00`
- `linear.weight_1_0 = 0.00`
- `linear.bias_0 = 5.00`

  
<img width="600" height="600" alt="newplot" src="https://github.com/user-attachments/assets/697999f1-99ab-47f6-920a-3d113601af4b" />


* Module 1: https://classroom.github.com/a/6TiImUiy

**Simple:**

<img width="600" height="600" alt="newplot (1)" src="https://github.com/user-attachments/assets/245bd2b2-cb07-4c88-8376-bd40b9d6bdbe" />

<img width="700" height="450" alt="newplot (2)" src="https://github.com/user-attachments/assets/d459a477-1e80-493d-8cb4-38c0c7873852" />

PTS=50, HIDDEN=2, RATE=0.5

```
Epoch  10  loss  32.773397  correct 32
Epoch  20  loss  31.985409  correct 32
Epoch  30  loss  29.498717  correct 32
Epoch  40  loss  24.552395  correct 38
Epoch  50  loss  17.317389  correct 44
Epoch  60  loss  12.243592  correct 46
Epoch  70  loss  8.899290   correct 48
Epoch  80  loss  6.736883   correct 48
Epoch  90  loss  5.399331   correct 48
Epoch  100 loss  4.444174   correct 50
Epoch  150 loss  2.198896   correct 50
Epoch  200 loss  1.376617   correct 50
Epoch  250 loss  0.952229   correct 50
Epoch  300 loss  0.697376   correct 50
Epoch  350 loss  0.533421   correct 50
Epoch  400 loss  0.422375   correct 50
Epoch  450 loss  0.343916   correct 50
Epoch  500 loss  0.286488   correct 50
```

**Diag:**

<img width="600" height="600" alt="newplot (5)" src="https://github.com/user-attachments/assets/a29b1841-10ac-4eef-8744-490602eaf812" />

<img width="700" height="450" alt="newplot (6)" src="https://github.com/user-attachments/assets/57570bc4-9491-425d-9380-15c5ceacafc1" />

PTS=50, HIDDEN=2, RATE=0.5

```
Epoch  10  loss  18.142916  correct 43
Epoch  20  loss  16.103058  correct 43
Epoch  30  loss  13.680009  correct 43
Epoch  50  loss  10.199570  correct 43
Epoch  70  loss  7.844347   correct 43
Epoch  100 loss  5.867325   correct 48
Epoch  120 loss  5.036074   correct 50
Epoch  150 loss  4.167485   correct 50
Epoch  200 loss  3.230811   correct 50
Epoch  250 loss  2.600508   correct 50
Epoch  270 loss  6.348866   correct 47
Epoch  300 loss  3.191575   correct 48
Epoch  350 loss  3.071704   correct 48
Epoch  400 loss  2.695159   correct 48
Epoch  450 loss  2.438028   correct 48
Epoch  500 loss  2.164222   correct 48
```

**Split:**

<img width="600" height="600" alt="newplot (7)" src="https://github.com/user-attachments/assets/f67f7db4-875d-479f-8c45-c81f4b5c9c91" />

<img width="700" height="450" alt="newplot (8)" src="https://github.com/user-attachments/assets/ec1f75f2-5a8a-4d15-b600-f528a26cc619" />

PTS=50, HIDDEN=10, RATE=0.5

```
Epoch  10  loss  33.118318  correct 29
Epoch  50  loss  28.772499  correct 37
Epoch  100 loss  27.848460  correct 35
Epoch  150 loss  24.929378  correct 36
Epoch  200 loss  20.164309  correct 36
Epoch  250 loss  13.353839  correct 43
Epoch  300 loss  8.264381   correct 46
Epoch  350 loss  5.923841   correct 47
Epoch  400 loss  3.593456   correct 50
Epoch  450 loss  1.649926   correct 50
Epoch  500 loss  1.157084   correct 50
```

**Xor:**

<img width="600" height="600" alt="newplot (9)" src="https://github.com/user-attachments/assets/71d17f7a-6695-4606-ab9d-169e9ffd8cba" />

<img width="700" height="450" alt="newplot (10)" src="https://github.com/user-attachments/assets/64703845-668e-443b-99a2-070d211a47bb" />

PTS=50, HIDDEN=10, RATE=0.5

```
Epoch  10  loss  31.590238  correct 31
Epoch  50  loss  23.309250  correct 37
Epoch  100 loss  13.371239  correct 45
Epoch  150 loss  11.856682  correct 46
Epoch  200 loss  14.805272  correct 44
Epoch  250 loss  7.036468   correct 47
Epoch  300 loss  7.113146   correct 47
Epoch  350 loss  6.799923   correct 47
Epoch  400 loss  6.923969   correct 48
Epoch  450 loss  6.523753   correct 48
Epoch  500 loss  7.329450   correct 48
```

Diag

```
Epoch  10  loss  12.972246843268922 correct 45
  avg time/epoch so far: 0.0448s
Epoch  50  loss  7.310926756345862 correct 45
  avg time/epoch so far: 0.0457s
Epoch  100  loss  3.9175550700454562 correct 49
  avg time/epoch so far: 0.0485s
Epoch  150  loss  2.6196951268326196 correct 49
  avg time/epoch so far: 0.0455s
Epoch  200  loss  1.9627815120081697 correct 50
  avg time/epoch so far: 0.0435s
Epoch  250  loss  1.575298390896335 correct 50
  avg time/epoch so far: 0.0423s
Epoch  300  loss  1.3170496524763633 correct 50
  avg time/epoch so far: 0.0414s
Epoch  350  loss  1.130570834232976 correct 50
  avg time/epoch so far: 0.0405s
Epoch  400  loss  0.9881893107154824 correct 50
  avg time/epoch so far: 0.0406s
Epoch  450  loss  0.8750045371286221 correct 50
  avg time/epoch so far: 0.0405s
Epoch  500  loss  0.7823009087444074 correct 50
  avg time/epoch so far: 0.0410s

Total time: 20.49s, avg time/epoch: 0.0410s
```

Split

```
Epoch  10  loss  34.582669691330885 correct 34
  avg time/epoch so far: 0.0375s
Epoch  50  loss  34.38028060614135 correct 34
  avg time/epoch so far: 0.0422s
Epoch  100  loss  34.16282684072829 correct 35
  avg time/epoch so far: 0.0406s
Epoch  150  loss  34.01201577686937 correct 35
  avg time/epoch so far: 0.0391s
Epoch  200  loss  33.94296954192315 correct 35
  avg time/epoch so far: 0.0407s
Epoch  250  loss  33.91969240479095 correct 35
  avg time/epoch so far: 0.0435s
Epoch  300  loss  33.90870875632832 correct 34
  avg time/epoch so far: 0.0455s
Epoch  350  loss  33.905875631284495 correct 34
  avg time/epoch so far: 0.0453s
Epoch  400  loss  33.90534074095282 correct 32
  avg time/epoch so far: 0.0443s
Epoch  450  loss  33.90509965741012 correct 32
  avg time/epoch so far: 0.0436s
Epoch  500  loss  33.90502870894615 correct 32
  avg time/epoch so far: 0.0447s

Total time: 22.35s, avg time/epoch: 0.0447s
```

Xor 

```
Epoch  10  loss  32.68867856205831 correct 35
  avg time/epoch so far: 0.3408s
Epoch  50  loss  20.12770289409825 correct 39
  avg time/epoch so far: 0.3096s
Epoch  100  loss  17.38670674824629 correct 41
  avg time/epoch so far: 0.3071s
Epoch  150  loss  14.410135976735013 correct 43
  avg time/epoch so far: 0.3054s
Epoch  200  loss  12.99663006546026 correct 44
  avg time/epoch so far: 0.3040s
Epoch  250  loss  10.302692924014433 correct 45
  avg time/epoch so far: 0.3034s
Epoch  300  loss  17.86782401352321 correct 42
  avg time/epoch so far: 0.3035s
Epoch  350  loss  27.64030348089915 correct 39
  avg time/epoch so far: 0.3038s
Epoch  400  loss  5.229879113848728 correct 49
  avg time/epoch so far: 0.3040s
Epoch  450  loss  9.631913439154568 correct 45
  avg time/epoch so far: 0.3042s
Epoch  500  loss  4.288164120194821 correct 49
  avg time/epoch so far: 0.3038s

Total time: 151.91s, avg time/epoch: 0.3038s
```

* Module 2: https://classroom.github.com/a/0ZHJeTA0
* Module 3: https://classroom.github.com/a/U5CMJec1

Task 3.5:

Simple

```
Epoch  10  loss  27.351249801185162 correct 33
  avg time/epoch so far: 0.0528s
Epoch  50  loss  7.01672338764293 correct 49
  avg time/epoch so far: 0.0462s
Epoch  100  loss  3.1598004700836224 correct 50
  avg time/epoch so far: 0.0461s
Epoch  150  loss  1.93055671396475 correct 50
  avg time/epoch so far: 0.0482s
Epoch  200  loss  1.3630461216930534 correct 50
  avg time/epoch so far: 0.0476s
Epoch  250  loss  1.0305459793912912 correct 50
  avg time/epoch so far: 0.0478s
Epoch  300  loss  0.8137848035650413 correct 50
  avg time/epoch so far: 0.0470s
Epoch  350  loss  0.6641887664091034 correct 50
  avg time/epoch so far: 0.0474s
Epoch  400  loss  0.556278601893604 correct 50
  avg time/epoch so far: 0.0475s
Epoch  450  loss  0.4769898803627563 correct 50
  avg time/epoch so far: 0.0467s
Epoch  500  loss  0.41798514317967517 correct 50
  avg time/epoch so far: 0.0468s

Total time: 23.40s, avg time/epoch: 0.0468s
```
В итоге: 

| Dataset | Hidden | Final loss | Correct | Avg time/epoch |
|---------|--------|-----------|---------|-----------------|
| Simple  | 2      | 3.17      | 49/50   | 0.0384s         |
| Diag    | 2      | 0.42      | 50/50   | 0.0417s         |
| Split   | 2      | 2.74      | 50/50   | 0.0424s         |
| Xor     | 10     | 4.29      | 49/50   | 0.3038s         |



* Module 4: https://classroom.github.com/a/04QA6HZK
* Quizzes: https://classroom.github.com/a/bGcGc12k
