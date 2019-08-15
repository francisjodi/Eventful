
// document.querySelectorAll("#collegechoice option").forEach(element=>{
//   element.addEventListener("click", event=>{
//   // url = `/events?college=${choice.textContent}`;
//   console.log(element);
//
//   })
// })
// college = document.querySelectorAll(".college")
// college.forEach(element=>{
//   console.log(element)
// })
// college[0].addEventListener("onclick", e =>{
//   alert(college.textContent);
// })
// document.querySelectorAll(".college").forEach(element=>{
//   element.addEventListener("onclick", event=>{
//     url = `/events?college=${element.textContent}`;
//     alert(url);
//     console.log(url);
//   })
// })
//
// document.querySelector("#searchbtn").addEventListener("onmouseenter", event=>{
//   // window.location.href = url;
//   let choice = document.querySelector("#collegechoice").value;
//   let url = `/events?college=${choice}`;
//   console.log(url);
// })

document.querySelectorAll("#categorylist li").forEach(element=>{
  element.addEventListener("click", event=>{
    const url = `/events?category=${element.textContent}`;
    window.location.href = url;
  })
})

document.querySelector("#jodilinkedin").addEventListener("click", event=>{
  const url =  `https://www.linkedin.com/in/jodi-ann-francis-241a41185/`;
  window.location.href = url;
})

document.querySelector("#heidilinkedin").addEventListener("click", event=>{
  const url =  `https://www.linkedin.com/in/heidi-johnson-66997a190/`;
  window.location.href = url;
})

document.querySelector("#warrenlinkedin").addEventListener("click", event=>{
  const url =  `https://www.linkedin.com/in/warren-lee-75055b15a/`;
  window.location.href = url;
})
//
// document.querySelector("#backbtn").addEventListener("click", event=>{
//   const url = `/addevent`;
//   window.location.href = url;
// })

// document.querySelector("#authorize_button").addEventListener("click", event=>{
  // const url = `/search`;
  // window.location.href = url;
// })
