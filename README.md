# Tema Python 

Acest repository conține două aplicații Python realizate pentru materia de Python. Proiectele demonstrează utilizarea claselor și moștenirii, lucrul cu fișiere CSV și afișarea datelor sub formă de grafice.

## 1. Cerințe și rulare

### 1.1 Aplicația 1

Fișier: ex1.py

Cerințe:
- Python 3.x (testat cu Python 3.14.0)
- Nu sunt necesare module externe

Rulare:

Varianta 1 – din IDLE:
1. Deschideți IDLE  
2. File → Open → selectați ex1.py  
3. Run → Run Module sau F5  

Varianta 2 – din Command Prompt / Terminal:
1. Deschideți terminalul în folderul unde se află ex1.py  
2. Rulați comanda:
python ex1.py

### 1.2 Aplicația 2

Fișiere:
- ex2.py  
- data.csv  

Cerințe:
- Python 3.x  
- Module externe:
  - pandas  
  - matplotlib  

Instalare module:
pip install pandas  
pip install matplotlib  

Dacă pip nu funcționează:
python -m pip install pandas  
python -m pip install matplotlib  

Fișierele ex2.py și data.csv trebuie să fie în același folder.

Rulare:

Din IDLE:
1. Deschideți IDLE  
2. Deschideți ex2.py  
3. Apăsați F5  

Din Command Prompt / Terminal:
python ex2.py  

Se vor deschide pe rând 3 ferestre cu grafice.

## 2. Descrierea aplicațiilor

### Aplicația 1 – Clase și moștenire

Aplicația este construită în jurul a două clase:
- Employee – clasa de bază  
- Manager – clasa derivată  

Clasa Employee reprezintă un angajat generic. Are o variabilă de clasă empCount care contorizează numărul total de angajați. Constructorul primește numele și salariul și creează un dicționar pentru sarcini. Include metode pentru afișarea datelor, modificarea salariului și gestionarea sarcinilor.

Clasa Manager moștenește Employee și adaugă o variabilă de clasă mgrCount care contorizează managerii, un departament prefixat cu „F25” și o metodă suprascrisă pentru afișare.

În clasa Manager există două variabile de clasă:
X = 16  
Y = 11  

Metoda display_employee() folosește expresia X % 4. Deoarece 16 % 4 = 0, pentru manageri se afișează doar salariul.

Fluxul programului este următorul:
1. Se creează obiecte Employee și Manager  
2. Se afișează angajații  
3. Se afișează managerii  
4. Se afișează numărul total de angajați și manageri  

### Aplicația 2 – Analiza datelor și grafice

Programul folosește bibliotecile pandas și matplotlib. Datele sunt citite din fișierul data.csv.

Graficul 1: Vizualizarea Tuturor Valorilor 

Prima secțiune de cod generează un grafic liniar care include toate înregistrările din coloanele Durata și Puls din setul de date. 

plt.figure(): Inițiază o nouă figură de grafic, asigurând că acest grafic este independent de cele care vor urma. 

plt.plot(df["Durata"], label="Durata") și plt.plot(df["Puls"], label="Puls"): Desenează două serii de date pe același sistem de coordonate. Ambele coloane sunt reprezentate în funcție de indexul lor în DataFrame (axele X și Y sunt etichetate generic). 

plt.title("Toate valorile"), plt.legend(), plt.show(): Setează titlul, afișează legenda pentru a distinge liniile Durata și Puls, și, în final, afișează graficul pe ecran. 

Graficul 2: Vizualizarea Primelor X Valori 

Al doilea grafic vizualizează doar un subset al datelor, definit de primele X înregistrări. 

Determinarea lui X: Valoarea lui X este stabilită dinamic prin calculul lungimii prenumelui "Alexia-Georgiana". 

X = len("Alexia-Georgiana") = 16. 

Selecția Datelor: Se utilizează funcția .head(X) din pandas pe coloanele Durata și Puls pentru a selecta primele 16 valori din fiecare serie. 

df["Durata"].head(X) și df["Puls"].head(X). 

Afișare: Un nou grafic (prin plt.figure()) este generat folosind acest subset. Titlul graficului este formatat dinamic (prin f-string) pentru a indica exact câte valori sunt vizualizate: "Primele 16 valori: Durata și Puls". 

 Graficul 3: Vizualizarea Ultimelor Y Valori 

Ultimul grafic se concentrează pe vizualizarea datelor de la sfârșitul setului, utilizând ultimele Y înregistrări. 

Determinarea lui Y: Valoarea lui Y este stabilită dinamic prin calculul lungimii numelui de familie "Ghimpeteanu". 

Y = len("Ghimpeteanu") = 11. 

Selecția Datelor: Se folosește funcția .tail(Y) din pandas pentru a izola și vizualiza ultimele 11 înregistrări din coloanele Durata și Puls. 

df["Durata"].tail(Y) și df["Puls"].tail(Y). 

Afișare: Se creează o a treia figură de grafic. Titlul indică: "Ultimele 11 valori: Durata și Puls". Ca și în cazurile precedente, plt.show() afișează rezultatul final. 

Prin urmare, codul demonstrează nu doar capacitatea de a încărca și vizualiza date, dar și abilitatea de a lucra cu subseturi dinamice ale datelor (primele X și ultimele Y) bazate pe variabile calculate dinamic (lungimea numelui și prenumelui). 



## Bibliografie

https://chatgpt.com/share/6936d8e2-3090-8006-944f-ee43904e8829  
https://www.w3schools.com/python/pandas/default.asp  
https://www.w3schools.com/python/matplotlib_intro.asp
