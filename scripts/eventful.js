
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
