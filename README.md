 1. Fade In LED

- LED-ul conectat pe pinul GPIO 17 pornește de la intensitate 0% și crește treptat până la intensitate maximă (100%).
- Se folosește PWM (Pulse Width Modulation) pentru a regla luminozitatea LED-ului.
- Codul pornește PWM cu 0% și crește duty cycle în pași de 1%, cu o pauză scurtă între pași pentru efectul de aprindere treptată.

---

2. Fade Out LED

- LED-ul conectat pe pinul GPIO 17 pornește aprins la intensitate maximă (100%) și scade treptat până la 0%, stingându-se.
- De asemenea, folosește PWM pentru a regla luminozitatea în mod gradual.
- Duty cycle scade în pași de 1%, cu o pauză între pași pentru efectul de stingere treptată.

---

3. Semafor Pieton

- Simulează un semafor pentru pietoni și vehicule folosind 4 LED-uri conectate la pinii GPIO 12, 14, 16 și 23.
- Butonul pentru pietoni este conectat pe pinul GPIO 26.
- Semaforul schimbă starea luminilor pentru vehicule și pietoni:
  - Când pietonul apasă butonul, semaforul pietonului se activează și luminile vehiculelor se opresc.
  - Semaforul pietonului intermitent după o perioadă.
  - Apoi revine la starea normală.
- Se poate opri scriptul prin CTRL+C, care face curățenie la pini.
