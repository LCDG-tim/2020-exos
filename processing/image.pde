void symetries(){
  PImage img1 = loadImage("../marmote.jpg");
  int widthe = 512, heighte = 512;
  PImage img2 = symetrie_verticale(img1, widthe, heighte);
  PImage img3 = symetrie_horizontale(img1, widthe, heighte);
  PImage img4 = symetrie_horizontale(img2, widthe, heighte);
  image(img1, 5, 5);
  image(img2, widthe + 20, 5);
  image(img3, 5, heighte + 20);
  image(img4, widthe + 20, heighte + 20);
}

PImage symetrie_horizontale(PImage img, int widthe, int heighte){
  PImage new_img = createImage(widthe, heighte, RGB);
  for (int i = 0; i < widthe; i++){
    for (int j = 0; j < heighte; j++){
      new_img.set(i, j, img.get(i, heighte - 1 - j));
    }
  }
  return new_img;
}

PImage symetrie_verticale(PImage img, int widthe, int heighte){
  PImage new_img = createImage(widthe, heighte, RGB);
  for (int i = 0; i < widthe; i++){
    for (int j = 0; j < heighte; j++){
      new_img.set(i, j, img.get(widthe - 1 - i, j));
    }
  }
  return new_img;
}
