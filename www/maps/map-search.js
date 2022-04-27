const mapImageTemplate = document.querySelector("[map-image-template]")
const mapsAlignContainer = document.querySelector("[maps-align-container]")
const searchMap = document.querySelector("[search-bar]")

let maps = []

searchMap.addEventListener("input", e => {
  const value = e.target.value.toLowerCase()
  maps.forEach(map => {
    const isVisible =
      map.name.toLowerCase().includes(value)
    map.element.classList.toggle("hidden", !isVisible)
  })
})

fetch("/api/maps.json")
  .then(res => res.json())
  .then(data => {
    maps = data.map(map => {
      const imageBox = mapImageTemplate.content.cloneNode(true).children[0]
      const mapImage = imageBox.querySelector("[img-data]")
      const mapName = imageBox.querySelector("[name-data]")
      //mapImage.textContent = map.image
      mapImage.style.backgroundImage = "url('https://cdn.spco.xyz/zlzs/map-images/" + map.name + ".jpg')"; 
      mapName.textContent = map.name.replaceAll( "_", " ").replace("zs ", "");
      mapsAlignContainer.append(imageBox)
      return { name: map.name, image: map.image, element: imageBox }
    })
  })