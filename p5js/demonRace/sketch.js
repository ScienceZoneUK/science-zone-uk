let demonCage = [];

function setup() {
  createCanvas(windowHeight, 400);

  for (let i = 0; i < 1000; i++) {
    let dPosX = random(30);
    let dPosY = random(400);
    demon = new Demon(dPosX, dPosY);
    demonCage.push(demon);
  }
}

function draw() {
  background(220,20);
  demonCage.forEach((demon) => {
    demon.drawDemon();
  });
}

class Demon {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.velX = random(6);
  }

  drawDemon() {
    circle((this.x += this.velX), this.y, 20);
  }
}
