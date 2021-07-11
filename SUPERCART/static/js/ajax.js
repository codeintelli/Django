// $('.plus-cart').click(function () {
//     console.log('plus clicked')
//     let id = $(this).attr("pid").toString();
//     var eml = this.parentNode.children[2]
//     console.log(id)
//     $.ajax({
//         type: 'GET',
//         url: '/pluscart',
//         data: {
//             prod_id: id
//         },
//         success: function (data) {
//             console.log(data);
//             eml.innerText = data.quantity
//         }

//     })
// })