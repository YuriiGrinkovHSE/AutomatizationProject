document.getElementById("cityOpt").addEventListener("change", function() {
    if (this.value === "Москва") {
      document.getElementById("MskDistrictOpt").hidden = false;
      document.getElementById("spbDistrictOpt").hidden = true;

    } else {
        document.getElementById("MskDistrictOpt").hidden = true;
        document.getElementById("spbDistrictOpt").hidden = false;
    }
  });

document.getElementById("buildingType").addEventListener("change", function() {
    if (this.value === "Школа") {
      document.getElementById("schoolOpts").style.visibility = 'visible';
      document.getElementById("hospitalOpts").style.visibility = 'hidden';
    } else {
      document.getElementById("schoolOpts").style.visibility = 'hidden';
      document.getElementById("hospitalOpts").style.visibility = 'visible';
    }
  });

document.getElementById("ranger").innerText = document.getElementById("c").value;
document.getElementById("c").addEventListener("change", function() {
    document.getElementById("ranger").innerText = this.value;
  });