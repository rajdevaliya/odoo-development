$(document).ready(function () {
    // $("p").click(function(){
    //   $(this).hide();
    // });
    // $("p").mouseenter(function(){
    //     alert("You entered p1!");
    //   });
    // $("p").mouseleave(function(){
    //     alert("Bye! You now leave p1!");
    //   });
    // $("p").mousedown(function(){
    //     alert("Mouse down over p1!");
    //   });
    // $("p").mouseup(function(){
    //     alert("Mouse up over p1!");
    //   });
    // $("input").focus(function(){
    //     $(this).css("background-color", "red");
    //   });

    // $("p").on({
    //     mouseenter: function(){
    //       $(this).css("background-color", "lightgray");
    //     },
    //     mouseleave: function(){
    //       $(this).css("background-color", "lightblue");
    //     },
    //     click: function(){
    //       $(this).css("background-color", "yellow");
    //     }
    //   });
    //   $('#show').hide()
    //   $('#hide').click(function(){
    //     $('p').hide("slow");
    //     $('#hide').hide("slow")
    //     $('#show').show("slow")
    //   })
    //   $('#show').click(function(){
    //     $('p').show("fast");
    //     $('#hide').show("fast");
    //     $('#show').hide("fast")
    //   })
    // $("button").click(function(){
    //     $("p").toggle("slow");
    //   });
    // $("button").click(function(){
    //     $("#div1").fadeTo('fast',0.5);
    //     $("#div3").fadeTo(3000, 0.7);
    //     $("#div2").fadeTo("slow", 0.6);
    //   });
    // $("button").click(function(){
    //     $("div").slideToggle("slow");
    //   });
    // $('button').click(function(){
    //     $('p').css('color', 'red').slideUp('slow').slideDown('slow');
    // })

    // $('#btn1').click(function(){
    //     $('div').append("<p><b>Appending in p</b></p>");
    // })
    // $('#btn2').click(function(){
    //     $('ol').append('<li>item appending in list</li>')
    // })
    // $("li").click(function(){
    //     $(this).hide();
    // })

    $("button").click(function () {
        $("h1, h2, p").toggleClass("blue");
        $("div").toggleClass("important");
    });
});
