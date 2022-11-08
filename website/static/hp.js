//************************************************
//********** HEADER FILL COLOR (SCROLL) **********
//************************************************

$(window).on("scroll", function() {
	var masterH,
		headerH = $("header").height(),
        scroll = $(window).scrollTop(),
		h, factor,
		initOpacity = 0;

	masterH = $(".hp-banners").innerHeight();

	h = masterH - headerH;
    factor = ((scroll / h) * (1 - initOpacity)) + initOpacity

    if(factor > 0)
        $("header").removeClass("transparent");
    else
        $("header").addClass("transparent");

    if(scroll / h < 1) {
        $("header span.bg").css("opacity", factor);
    } else {
		$("header span.bg").css("opacity", 1);
    }
});

$(window).on("load", function() {
    $(window).trigger("scroll");
});


//************************************
//********** BANNERS SLIDER **********
//************************************

$(".hp-banners .slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 9000,
    pauseOnHover: false,
    speed: 1000,
    fade: false,
    arrows: true,
    prevArrow: $(".hp-banners .prev"),
    nextArrow: $(".hp-banners .next"),
});