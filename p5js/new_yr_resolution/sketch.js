res1 = "eat less sweets";
res2 = "give maisie and bonnie more work to do";
res3 = "Learn to defend myself against bonnie";
res4 = "Surf more often";
res5 = "IMprove python skills";

function setup() {
  createCanvas(800, 800);
}

function draw() {
  background(255);
  for (let i = 0; i < 5; i++) {
    textSize(40);
    let y = 40*i;
    text(res2, 10, y);
  }
}
