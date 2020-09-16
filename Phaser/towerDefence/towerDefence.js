var config = {
    type: Phaser.AUTO,
    parent: 'content',
    width: 640,
    height: 512,
    scene: {
        key: 'main',
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

var graphics;
var path;

function preload() {
    //load game assets (enemy and turret atlas)
    this.load.atlas('sprites', 'assets/spritesheet.png', 'assets/spirtesheet.json');
    this.load.image('bullet', 'assets/bullet.png');
}

function create() {
    //graphics element for visualisation
    //not related to path
    var graphics = this.add.graphics();

    //path of enemies
    //parameters are start x and y of path
    path = this.add.pah(96, -32);
    path.lineTo(96, 164);
    path.lineTo(480, 164);
    path.lineTo(480, 544);

    graphics.lineStyle(3, 0xffffff, 1);

    //visualise path
    path.draw(graphics);


}

function update() {

}