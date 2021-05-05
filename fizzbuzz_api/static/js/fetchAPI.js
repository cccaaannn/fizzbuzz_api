document.addEventListener("DOMContentLoaded", onLoad);
const fizzbuzzDiv = document.getElementById("fizzbuzzDiv");
url = "/api"

async function getFizzBuzz(){
    const response = await fetch(url);
    const data = await response.json();
    return data
}

// async function getFizzBuzz(){
//     const custom_fizzbuzz = JSON.stringify({ 
//         "custom_fizzbuzz":[
//             {"word":"fozz", "divisors":[2]},
//             {"word":"fizz", "divisors":[3]},
//             {"word":"buzz", "divisors":[5]},
//             {"word":"fizzbuzz", "divisors":[3,5]},
//             {"word":"fozzfizz", "divisors":[2,3]},
//             {"word":"fozzbuzz", "divisors":[2,5]},
//             {"word":"fozzfizzbuzz", "divisors":[2,3,5]}
//         ]
//     });

//     const newURL = url + "?&stop=30";

//     const response = await fetch(newURL, {
//         method: "post",
//         body: custom_fizzbuzz,
//         headers: { 
//             "Content-Type": "application/json" 
//         },
//     });

//     const data = await response.json();
//     return data
// }

function onLoad(){
    getFizzBuzz()
    .then((result) => {
        if(result.status === "success"){
            fizzbuzzDiv.innerHTML = result.data;
        }
        else{
            fizzbuzzDiv.innerHTML = result.info;
        }
        
    }).catch((err) => {
        console.log(err);
        fizzbuzzDiv.innerHTML = "api could not fetched";
    });
}
