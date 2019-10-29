#include <stdio.h>
#include <stdint.h>

int main(){

    uint16_t v12, v8;
    int16_t v6;
    
    v12 = 0xACE1;
    for ( int i = 0; i <= 1621; ++i ) {
        v6 = ((signed int)v12 >> 5) ^ ((signed int)v12 >> 3) ^ v12 ^ ((signed int)v12 >> 2);
        v12 = (v6 << 15) | ((signed int)v12 >> 1);
    }

   printf("%i (0x%x)", v12, v12);

    short r144, r143, butt;

    r144 = 0x61;
    r143 = 0x41;
    butt = 0;


   v8 = (16 * butt) | r144 | (r143 << 8) | (butt << 8) & 0xF000;

   printf("%i (0x%x)", v8, v8);

}
