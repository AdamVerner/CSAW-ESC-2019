# include <stdio.h>

unsigned int poly(unsigned int k,unsigned int *X,unsigned int Y,int len)
{
  int i;
  unsigned int out;
  int j;
  
  j = 0;
  out = *X;
  i = len;
  while (1 < i) {
    j = j + 1;
    out = ((k * out) % 0xfff1 + X[j]) % 0xfff1;
    i = i + -1;
  }
  return (Y + (k * out) % 0xfff1) % 0xfff1;
}


int main(){

unsigned int X3[5];
unsigned int X2[5];
unsigned int X1[5];

X1[0] = 15117;
X1[1] = 53334;
X1[2] = 35833;
X1[3] = 49425;
X1[4] = 33425;
X2[0] = 58020;
X2[1] = 48937;
X2[2] = 62300;
X2[3] = 56547;
X2[4] = 55154;
X3[0] = 54292;
X3[1] = 38788;
X3[2] = 53943;
X3[3] = 38544;
X3[4] = 62042;

int K;
unsigned int Y;

for(int i = 0; i < 256; i++){       /* r.RFID[401 + 0x10] */
	for(int j = 0; j < 256; j++){   /* r.RFID[400 + 0x10] */
			K = i * 0x100 + j;
		for(int k = 0; k < 256; k++){   /* r.keys[32 + 0x10] * 0x101; */
			Y = 257 * k; 
	
		
			if(poly(K, X1, Y, 5) == 50216){
				if (poly(K, X2, Y, 5) == 6902){
					int p = poly(K, X3, Y, 5);
					printf("r.RFID[400 + 0x10] = %d\n", j);
					printf("r.RFID[401 + 0x10] = %d\n", i);
					printf("r.keys[32 + 0x10] = %d\n", k);

					
					printf("r.RFID[402] = %d\n", p&0xff);
					printf("r.RFID[403] = %d\n", p>>8);				 
				}
			}
		}
	}
}

}