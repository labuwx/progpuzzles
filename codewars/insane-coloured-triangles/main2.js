function triangle(row)
{
  var n = row.length;

  var res = 0;
  for (var i = 0; i < n; i++) {
    var c;
    switch (row[i]) {
      case 'R': c = 0; break;
      case 'G': c = 1; break;
      default: c = 2; break;
    }
    /*var cc = row[i];
    if (cc === 'R') {
      c = 0;
    } else if (cc === 'G') {
      c = 1;
    } else {
      c = 2;
    }*/
    if (c !== 0) {
      var nn = n - 1;
      var kk = i;
      
      var r = 1;
      var dn, dk, sc;
      while(kk !== 0) {
        dn = nn % 3;
        dk = kk % 3;
    
        if (dn < dk) {
          r = 0;
          break;
        }
        else if (dn !== dk && dk !== 0) {
          r *= 2;
        }
    
        nn = (nn/3>>0);
        kk = (kk/3>>0);
      }      
      
      res += c * r; 
    }
  }
  res %= 3

  if (n % 2 === 0)
    res = (3 - res) % 3;

  switch (res) {
    case 0: return 'R'; break;
    case 1: return 'G'; break;
    case 2: return 'B'; break;
  }
}
