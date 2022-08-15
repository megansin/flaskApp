function deleteClothing(clothingId) {
    fetch("/delete-clothing", {
      method: "POST",
      body: JSON.stringify({ clothingId: clothingId }),
    }).then((_res) => {
      window.location.href = "/closet";
    });
  }