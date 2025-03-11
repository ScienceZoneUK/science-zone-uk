let mover;
let value = 0;

function setup() {
  createCanvas(400, 400);
  mover = new Mover(100, 30, 5, 10);
}

function draw() {
  background(255);
  let grav = createVector(0,0.9);
  mover.update();
  mover.applyForce(grav);
  mover.edgeDetection();
  mover.show();
  
  // if(mouseIsPressed){
  //   let wind = createVector(10,0);
  //   mover.applyForce(wind)
  // }
  
}




// PHYSICS ENGINE BELOW

class Mover {
  constructor(x, y, r,  mass) {
    this.pos = createVector(x, y);
    this.vel = createVector(0,0);
    this.acc = createVector(0,0);
    this.mass = mass;
    this.radius = r
  }

 

  update() {
    
    // this.vel.limit(2);
    this.vel.add(this.acc);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }
  
  applyForce(force){
    let f = p5.Vector.div(force, this.mass)
    this.acc.add(f);
    
  }

  show() {
    stroke(0);
    fill(175);
    circle(this.pos.x, this.pos.y, this.mass*this.radius);
  }

  edgeDetection() {
if(this.pos.x > width-this.radius){
  this.pos.x = width-this.radius
  this.vel.x *=-1
}else if(this.pos.x < 0 + this.radius){
    this.pos.x = 0 + this.radius
  this.vel.x *=-1
}
    
    if(this.pos.y > height - this.radius){
  this.pos.y = height - this.radius
  this.vel.y *=-1
}else if(this.pos.y < 0 + this.radius ){
    this.pos.y = 0 + this.radius
  this.vel.y *=-1
}
    

}
}
