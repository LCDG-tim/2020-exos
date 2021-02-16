void grille(){
  stroke(100, 100, 100);
  for(int i = 0; i <= 1001; i = i + 100){
    line(i, 0, i, 1000);
    line(0, i, 1000, i);
  }
}

void grille_undefined(){
  stroke(100, 100, 100);
  for (int i = 0; i <= width; i = i + 100){
    for (int j = 100; j <= height; j = j + 100){
      line(i, 0, i, j);
    }
  }
  for (int i = 0; i <= height; i = i + 100){
    for (int j = 100; j <= width; j = j + 100){
      line(0, i, j, i);
    }
  }
}
