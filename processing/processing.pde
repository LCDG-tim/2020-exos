
void setup(){
  size(1100, 1100);
  background(#000000);
  stroke(color(random(0, 255), random(0, 255), random(0, 255)));
  //grille();
  //draw_stars(7);
  //de();
  //affiche_de();
  //grille_undefined();
  //pavage();
  //draw_degrade();
  //symetries();
}


void draw(){
  if (!mousePressed){
    stroke(color(random(0, 255), random(0, 255), random(0, 255)));
  }
  line(width / 2, height / 2, mouseX, mouseY);
}

void mousePressed(){
  if (mouseButton == LEFT){
    stroke(#ff0000);
  }
  else if (mouseButton == RIGHT) {
    stroke(#00ff00);
  }
}
