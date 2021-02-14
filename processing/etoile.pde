
void etoile(int x, int y, int R, int G, int B){
  float angle = 0;
  int longueur = 80;
  float x1 = x - longueur / 2, y1 = y, x2 = x + longueur / 2, y2 = y;
  fill(R, G, B);
  stroke(R, G, B); 
  for (int i = 0; i<5; i++){
    x1 = x2;
    y1 = y2;
    x2 = x1 - cos(3.14 * angle / 180) * longueur;
    y2 = y1 + sin(3.14 * angle / 180) * longueur;
    angle = angle + 2 * (360 / 5);
    line(x1, y1, x2, y2);
  }
}

void draw_stars (int nb){
  for (int i = 1; i <= nb; i++){
    etoile(100 * i, 300, 240, 204, 20);
  }
}
