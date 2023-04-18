from machine import ADC, Pin
import time

# ROWS
R1 = 18
R2 = 17
R3 = 19
R4 = 16
R5 = 14
R6 = 26
R7 = 15
R8 = 13

#COLUMNS
C1 = 12
C2 = 20
C3 = 21
C4 = 11
C5 = 22
C6 = 10
C7 = 9
C8 = 8


ldr = machine.ADC(27)

pin_r1 = Pin(R1, mode=Pin.OUT)
pin_r2 = Pin(R2, mode=Pin.OUT)
pin_r3 = Pin(R3, mode=Pin.OUT)
pin_r4 = Pin(R4, mode=Pin.OUT)
pin_r5 = Pin(R5, mode=Pin.OUT)
pin_r6 = Pin(R6, mode=Pin.OUT)
pin_r7 = Pin(R7, mode=Pin.OUT)
pin_r8 = Pin(R8, mode=Pin.OUT)

pin_c1 = Pin(C1, mode=Pin.OUT)
pin_c2 = Pin(C2, mode=Pin.OUT)
pin_c3 = Pin(C3, mode=Pin.OUT)
pin_c4 = Pin(C4, mode=Pin.OUT)
pin_c5 = Pin(C5, mode=Pin.OUT)
pin_c6 = Pin(C6, mode=Pin.OUT)
pin_c7 = Pin(C7, mode=Pin.OUT)
pin_c8 = Pin(C8, mode=Pin.OUT)


rows = [pin_r1, pin_r2, pin_r3, pin_r4, pin_r5, pin_r6, pin_r7, pin_r8]
cols = [pin_c1, pin_c2, pin_c3, pin_c4, pin_c5, pin_c6, pin_c7, pin_c8]


def light_all():
    for p in rows:
        p.value(1)

    for p in cols:
        p.value(0)
        
def turn_off_all():
    for p in rows:
        p.value(0)

    for p in cols:
        p.value(0)

turn_off_all()

row = 0


ldr_vals = []

def run_rows():

    turn_off_all()
    time.sleep(1)

    for i in range(len(cols)):
        
        print(f'Turning on: cols[{i}]')
        
        cols[i].value(0)
        turn_off_all()
        rows[i].value(1)
        
        print(f'Reading LDR values: {ldr.read_u16()}')
        
        ldr_val = ldr.read_u16()
        ldr_vals.append(ldr_val)
        
        time.sleep(1)
        
    turn_off_all()
    

turn_off_all()


for i in range(len(rows)):    
    for j in range(len(cols)):

        for r in rows:
            r.value(0)
            
        rows[i].value(1)

        for c in cols:
            c.value(1)

        cols[j].value(0)
        ldr_val = ldr.read_u16()
        print(ldr_val)
        ldr_vals.append(ldr_val)
        time.sleep(0.5)
        cols[j].value(1)

        time.sleep(0.5)

arrs = []

for i, c in enumerate(ldr_vals):
    if i % 8 == 0:
        arrs.append(ldr_vals[i:i+8])
        
#print('Contents of ldr_vals[]: ', ldr_vals)
print(arrs)
print('Number of values: ', len(ldr_vals))

