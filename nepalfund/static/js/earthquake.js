// JavaScript Document
// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});



setTimeout(function(){

    $('.progress-bar').each(function() {
        var me = $(this);
        var perc = me.attr("aria-valuenow");

        var current_perc = 0;

        var progress = setInterval(function() {
            if (current_perc>=perc) {
                clearInterval(progress);
            } else {
                current_perc +=1;
                me.css('width', (current_perc)+'%');
            }

            

        }, 50);

    });

},300);

/*JS for progress bar
$(document).ready(function() {  
    $(".sidebar-row").click(function() {  
         $(".right-content-progress").css('display', 'block');
         $("#rectangle").css('height', 'auto');     
    });  
});
*/
/*
ar el = document.getElementById('jpt');
el.onclick = open;

function open( )
{
$(document).ready(function() {  
    $(".clickable").click(function() {  
         $(".right-content-progress").css('display', 'block');     
    });  
});
}*/

/*JS for sidebar*/

$(document).ready(function(){
    $('.btn-toggle').click(function(){
    $('.toggle').slideToggle();
    });

    $('.sidebar-toggle').click(function(){
        $('#sidebar').slideToggle();
        $('.menuTrigger').toggleClass('menuToggle');
    });


if (document.documentElement.clientWidth > 768) { 
            $('#scrollable').jScrollPane();
            $(window).resize(function(){
                $('#scrollable').jScrollPane();
            });
        }


$('.close').click(function() {
    $('.alert').hide();
})

var amountScrolled = 100;
var xSeconds = 2000; // 1 second


$(window).scroll(function() {
    if ($(window).scrollTop() > amountScrolled) {
        $('a.crunchify-top').fadeIn('slow');
        setTimeout(function() {
            $('a.crunchify-top').fadeOut('slow');
        }, xSeconds);

    } else {
        $('a.crunchify-top').fadeOut('slow');
    }
});

});
          
/*JS for sidebar ends*/


(function() {
        var e = document.createElement('script');
        e.async = true;e.src = document.location.protocol +'//connect.facebook.net/en_US/all.js#xfbml=1';document.getElementById('fb-root').appendChild(e);
        }());

jQuery(".slideLeftItem").append('<div style="font-size:12px;font-family: arial;width:300px;text-align:right;"></div>');
jQuery("#slideleft tr").hover(function(b){var a=jQuery(this);jQuery("#slideleft tr").not(a).hide();a.css({"z-index":"9999"});a.stop().animate({left:0})},function(b){var a=jQuery(this);a.css({"z-index":"1000"});a.stop().animate({left:-a.outerWidth()});jQuery("#slideleft tr").show()});

