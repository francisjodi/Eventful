document.querySelectorAll("#categorylist li").forEach(element=>{
  element.addEventListener("click", event=>{
    const url = `/events?category=${element.textContent}`;
    window.location.href = url;
  })
})
