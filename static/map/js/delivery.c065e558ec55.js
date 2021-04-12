function initMap() {
    // Create the map.
    const uluru = { lat: 34, lng: -117 };
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 9,
      center: uluru, 
      disableDefaultUI: true,
    });

    const userImage = "/static/images/male.svg";
    const user = new google.maps.Marker({
        position: { lat: accountLoc[0], lng: accountLoc[1] },
        map,
        icon: userImage,
    });

    //fix driver image
    const driverImage = "/static/images/car.svg";
    const driver = new google.maps.Marker({
        position: { lat: driverLoc[0], lng: driverLoc[1] },
        map,
        icon: userImage,
    });

    console.log(storeLats);
    console.log(driverLoc);
}
