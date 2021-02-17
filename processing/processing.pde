
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
  
  line(width / 2, height / 2, mouseX, mouseY);  
}

void mousePressed(){
  //stroke(color(random(0, 255), random(0, 255), random(0, 255)));
  if (mousePressed == LEFT){
    stroke(#ff0000);
  }
  else if (mousePressed == RIGHT) {
    stroke(#00ff00);
  }
}
