void de(){
  float X = random(1,7); 
  float Y = random(1,7);
  int x =int(X);
  int y = int(Y);
  println("le lancer de dés donne " + x + " et " + y);
  if (x == y){
    println(" bravo, vous avez fait un double");
  }
  else {
    println(" perdu");
  }
}

int lancement_de(){
  return int(random(1, 7));
}

void affiche_de(){
  // lancement des dés
  int x = lancement_de();
  int y = lancement_de();
  background(0, 0, 0);
  fill(#ffffff);
  textSize(40);
  text("Lancé de dé", 300, 300);
  text("dé 1 : ", 100, 450);
  stroke(#A2A220);
  rect(270, 400, 70, 70);
  fill(#ff2020);
  text(str(x), 295, 455);
  
  fill(#ffffff);
  text("dé 2 : ", 600, 450);
  stroke(#A2A220);
  rect(770, 400, 70, 70);
  fill(#ff2020);
  text(str(y), 795, 455);
  fill(#ffffff);
  if (x == y){
    text("C'est un double !",300, 800);
    if (x == 6){
      text("Et en plus, un double 6", 300, 550);
    }
  }
  
  else{
    text("Ce n'est pas un double", 300, 550);
  }
}
  
