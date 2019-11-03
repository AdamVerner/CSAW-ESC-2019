# include <stdio.h>
# include <stdint.h>


int main(){


    for (uint8_t i = 0; i < 255; i++)  // 401
        for (uint8_t j = 0; j < 255; j++) // 402
            for (uint8_t k = 0; k < 255; k++){ // 403
            
                uint8_t center = (i-k*j) % 25 + 45;

              	printf("%x:%x:%x\n", i, j, k);
                
            }
    
        

}
