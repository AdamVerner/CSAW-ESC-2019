void challengeFunction(char *password) {
  int i;
  char local_28 [8];
  bool correct;
  
  local_28[0] = 1;
  local_28[1] = 2;
  local_28[2] = 1;
  local_28[3] = 2;
  local_28[4] = 1;
  local_28[5] = 2;
  local_28[6] = 1;
  local_28[7] = 2;
  correct = true;
  i = 0;

  while (i < 8) {
    if ((password[i] - 0x30 ^ 3) != local_28[i]) {
      correct = false;
    }
    i++;
  }

  if (correct) {
    puts("Great Job! The flag is what you entered");
  }
}

