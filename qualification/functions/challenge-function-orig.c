
/* challengeFunction(char*) */

void challengeFunction(char *param_1)

{
  bool bVar1;
  int local_2c;
  uint local_28 [4];
  undefined4 local_18;
  undefined4 local_14;
  undefined4 local_10;
  undefined4 local_c;
  
  local_28[0] = 1;
  local_28[1] = 2;
  local_28[2] = 1;
  local_28[3] = 2;
  local_18 = 1;
  local_14 = 2;
  local_10 = 1;
  local_c = 2;
  bVar1 = true;
  local_2c = 0;
  while (local_2c < 8) {
    if (((int)param_1[(long)local_2c] - 0x30U ^ 3) != local_28[(long)local_2c]) {
      bVar1 = false;
    }
    local_2c = local_2c + 1;
  }
  if (bVar1) {
    puts("Great Job! The flag is what you entered");
  }
  return;
}

