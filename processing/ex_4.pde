float abso(float x){
  return sqrt(x * x);
}


float puissance(float x, int expo){
  float return_val = 1;
  for (int i = 0; i < expo; i++){
    return_val *= x;
  }
  return return_val;
}

float puissance_recur(float x, int expo){
  if (expo == 0){
    return 0;
  }
  else {
    return x * puissance_recur (x, expo - 1);
  }
}

int factoriel(int n){
  int return_val = 1;
  for (int i = 1; i <= n; i ++){
    return_val *= i;
  }
  return return_val;
}

int factoriel_recur(int n){
  if (n == 0) {
    return 1;
  }
  else {
    return n * factoriel_recur(n - 1);
  }
}

void table(int n){
  for (int i = 0; i < 11; i++){
    println(n + " * " + i + " = " + (n * i));
  }
}

void degrade(float r, float g, float b){
  for (float i = 0; i < width; i++){
    stroke((i / 255) * r, (i / 255) * g, (i / 255) * b);
    line(i,0,i,height);
  }
}

void pavage(){
  for (int i = 0; i < (width - 30) / 55; i++){
    for (int j = 0; j < (height - 30) / 55; j++){
      fill(random(0, 255), random(0, 255), random(0, 255));
      rect(15 + 55 * i, 15 + 55 * j, 50, 50);
    }
  }
}

void repeat(char mot, int nombre){
  for (int i = 0; i < nombre; i++){
    println(mot);
  }
}

int randint(int a, int b){
  return int(random(a,b));
}

boolean rectangle(int a, int b, int c){
  return ((a * a == b * b + c * c) || (b * b == a * a + c * c) || (c * c == a * a + b * b));
}
