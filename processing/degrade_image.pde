void draw_degrade(){
  PImage img = createImage(width, height, RGB);
  for (int x = 0; x < width; x ++){
    for (int y = 0; y < height; y++){
      img.set(x, y, color(x, 0, 0));
    }
  }
  image(img,0,0);
}

void inverse_img(){
  PImage img1 = createImage(width, height, RGB);
  PImage img2 = createImage(width, height, RGB);
  for (int i = 0; i < width; i ++){
    for (int j = 0; j < height; j ++){
      print();
    }
  }
}
