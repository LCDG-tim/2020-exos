PImage img; // image contenant les animations
PImage sprite; // stockera l'image a afficher
PImage sprites[][]; //tableau des images d'animation
int index=0; // pour se situer dans l'anim. Varie entre 0 et 7
int colonne=0, ligne=0; // coordonnée de l'image ; actuellement 0, 0
int posX=500, posY=300;// position initiale du dragon
int deltaX, deltaY; // décalge en abscisse et en ordonnée entre le dragon et la souris
float angle, proportionDeplacement=0.1; // argument du dragon, angle entre l'axe horizontale de hauteur y = ydragon et la souris
// puissance d'un déplacement

void setup() { 
  size(1000, 600); // taille de l'écran
  frameRate(10); // 10 images/secondes
  img = loadImage("wyvern_vol.png"); // image contenant les animations
  sprites = new PImage[8][8]; // on récupére les images d'animation
  for (int y = 0; y < 8; y++) {
    for (int x = 0; x < 8; x++) {
      sprites[x][y] = img.get(x*256, y*256, 256, 256); // on récupère toutes les images de la wyvern correspondant et on les rentre dans le tableaux
    }
  }
} 
void draw() {
  deltaX=mouseX-posX; // position par rapport à la souris en abscisse
  deltaY=mouseY-posY; // position par rapport à la souris en ordonnée
  if (deltaX!=0){
    angle= (degrees(atan2(deltaY, deltaX))+0); // argument en degrés de la direction du dragon
  }
  else {
    angle=0; // sin atan est incalculable car division par 0, angle est nul
  }
  println(angle); // print vérifictif
  //on cherche le numéro de ligne adéquat selon l'angle entre le dragon et la souris: passage de (-180º,180º) vers (0,7) 
  ligne=(round((angle+180)/360*8))%8;
  if (mousePressed) {
    posX=posX+round(deltaX*proportionDeplacement); // on s'approche de la souris en douceur
    posY=posY+round(deltaY*proportionDeplacement);
  }
  colonne=index%8; // 8 images par animations
  background(255); // on efface l'écran
  image(sprites[colonne][ligne], posX-128, posY-128); // et hop, un dragon
  index++; // image suivante la prochaine fois
}
