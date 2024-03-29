// AFRAME.registerComponent("ar-stereo", {
//     init: function() {
//         setTimeout(function() {
//             var vidCam = document.body.lastElementChild;
//             vidCam.setAttribute("id", "arVideo");

//             var camera = document.querySelector("[camera]");
//             var webCamSource = document.createElement("a-entity");
//             webCamSource.setAttribute("geometry", "primitive: plane;");
//             webCamSource.setAttribute("material", "shader: flat; src: #arVideo");
//             webCamSource.setAttribute("position", "0 0 -50");
//             webCamSource.object3D.visible = false;
//             camera.insertBefore(webCamSource, camera.firstChild);
//             document
//                 .querySelector(".a-enter-vr-button")
//                 .addEventListener("clik", () => {
//                     camera.object3D.position.set(0, 0, 0);
//                 });
//             var onResize = () => {
//                 var orientation = window.screen.orientation.angle;
//                 var x = 0;
//                 var y = 0;
//                 if (orientation === 0) {
//                     x = vidCam.offsetWidth / 15; //15
//                     y = vidCam.offsetHeight / 15; //15
//                 } else {
//                     x = vidCam.offsetWidth / 12; //12
//                     y = vidCam.offsetHeight / 12; //12
//                 }
//                 webCamSource.object3D.scale.set(x, y, 1);
//                 //webCamSource.object3D.position.set(0, vidCam.offsetTop/5.8, -50)
//             };
//             onResize();
//             window.addEventListener("resize", onResize);
//             window.addEventListener("orientationchange", onResize);

//             webCamSource.sceneEl.addEventListener("enter-vr", function() {
//                 webCamSource.object3D.visible = true;
//             });
//             webCamSource.sceneEl.addEventListener("exit-vr", function() {
//                 webCamSource.object3D.visible = false;
//             });
//         }, 4000);
//     }
// });
// // Config VR Viewer
// navigator.getVRDisplays().then(function(displays) {
//     var vrDisplay = displays.length && displays[0];
//     if (vrDisplay) {
//         console.log(vrDisplay);
//         vrDisplay.deviceInfo_.viewer.screenLensDistance = 0.044;
//         vrDisplay.deviceInfo_.viewer.fov = 44;
//         vrDisplay.deviceInfo_.viewer.interLensDistance = 0.03;
//         vrDisplay.deviceInfo_.viewer.distortionCoefficients = [0.04, 0.25];
//         // if (sceneEl) { sceneEl.emit('displayconnected', {vrDisplay: vrDisplay}); }
//         // addStereo();
//     }
// });




setTimeout(() => {
    var vidCam = document.body.lastElementChild;
    vidCam.setAttribute('id', 'arVideo');
    var camera = document.querySelector('[camera]');
    webCamSource = document.createElement('a-entity');
    webCamSource.setAttribute('geometry', 'primitive: plane;');
    webCamSource.setAttribute('material', 'shader: flat; src: #arVideo');
    webCamSource.setAttribute('position', '0 0 -50');
    webCamSource.setAttribute('scale', '54 36 1');
    camera.insertBefore(webCamSource, camera.firstChild);
    document.querySelector('.a-enter-vr-button').addEventListener('click', () => {
        camera.object3D.position.set(0, 0, 0)
    })
}, 2000);