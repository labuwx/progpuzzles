function bc(n, k) {
  var r = 1;
  var dn, dk, sc;
  while(r !==0 && k !== 0) {
    dn = n % 3;
    dk = k % 3;
    
    if (dn < dk) {
      r = 0;
    }
    else if (dn !== dk && dk !== 0) {
        r *= 2;
    }
    
    //n = ~~(n / 3);
    //k = ~~(k / 3);
    n = (n/3>>0);
    k = (k/3>>0);
  }

  return r%3;
}

function triangle(row)
{
  var n = row.length;

  var res = 0;
  for (var i = 0; i < n; i++) {
    var c;
    switch (row[i]) {
      case 'R': c = 0; break;
      case 'G': c = 1; break;
      case 'B': c = 2; break;
    }
    if (c !== 0) 
      res += c * bc(n-1, i); 
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
