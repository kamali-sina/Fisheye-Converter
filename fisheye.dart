import 'dart:math';
import 'package:image/image.dart' as img;
import 'package:flutter/foundation.dart';

img.Image fisheye(img.Image input) {
  var w = input.width;
  var h = input.height;
  var output = img.Image(w, h);
  for (var i = 0; i < h; i++) {
    for (var j = 0; j < w; j++) {
      var x = j - (w / 2);
      var y = (h - i) - (h / 2);
      var xn = x / (w / 2);
      var yn = y / (h / 2);
      var r = sqrt(pow(xn, 2) + pow(yn, 2));
      var theta = atan2(yn, xn);
      if (r <= 1) {
        var rPrime = (r + (1 - sqrt(1 - pow(r, 2)))) / 2;
        var xnNew = rPrime * cos(theta);
        var ynNew = rPrime * sin(theta);
        var xNew = xnNew * (w / 2);
        var yNew = ynNew * (h / 2);
        var iNew = (h - (yNew + (h / 2))).round();
        var jNew = (xNew + (w / 2)).round();
        output.setPixel(jNew, iNew, input.getPixel(j, i));
      }
    }
  }
  return output;
}
