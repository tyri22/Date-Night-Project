'use strict';

// need to create function to update the likes and prevent the default
    // first define the function that takes in an evt func funcName(evt){}
    // prevent the default
    // get the venue id
    // fetch the url w venue params
    // update like field on page
    // ^^add event listener on click w function uncalled

// function addLikes() {
//     // evt.preventDefault();
//     console.log("hi")
//     const venueId = document.querySelector('button').id;
//     // let count = 0;
//     alert(venueId)
//     const formImputs = {
//         venue: venueId
//     };
//     fetch('/likes', {
//         method: 'POST',
//         body: JSON.stringify(formInputs),
//         headers: {
//       'Content-Type': 'application/json',
//     },
//     }) 
//         .then(response => response.text())
//         .then(responseData => {
//             alert(responseData)
//             // document.querySelector('#liked').innerHTML = count + 1;
//         });
// }
// //event listener on form

document.querySelector('button').addEventListener('click', () => {
    const venueId = document.querySelector('button').id;
    
    const formInputs = {
        venue: venueId
    };
    fetch('/likes', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
      'Content-Type': 'application/json',
    },
    }) 
        .then(response => response.text())
        .then(responseData => {
            document.querySelector('#liked').innerHTML = responseData;
        });
}
);


