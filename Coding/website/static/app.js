//*********************************
//********** TOGGLE MENU **********
//*********************************

$("header .menu-toggle").click(function(e) {
	e.preventDefault();

	$("header").toggleClass("open");
	$("html, body").toggleClass("lock");
});
$(document).click(function(e) {
	if($("header").hasClass("open") && $(e.target).is("header")) {
		$("header").removeClass("open");
		$("html, body").removeClass("lock");
	}
});


//*********************************************
//********** MENU & SIDEBAR SUBMENUS **********
//*********************************************

if($(window).width() > 992) {
	$("header .menu > ul > .sub > *:not(ul)").mouseenter(function(e) {
		e.preventDefault();

		var sub = $(this).closest(".sub"),
			h = sub.find("> ul")[0].scrollHeight;

		if(sub.find(".sub").length > 0) {
			var subsub = sub.find(".sub");
			subsub.find("> ul").each(function() {
				h += $(this)[0].scrollHeight
			})
		}

		if(!sub.hasClass("open") && !sub.hasClass("active")) {
			sub.find("> ul").css("max-height", h);
			sub.addClass("open");
		}
	});

	$("header .menu > ul > .sub").mouseleave(function(e) {
		e.preventDefault();

		var sub = $(this);

		if(sub.hasClass("open") || sub.hasClass("active")) {
			sub.find("> ul").css("max-height", 0);
			sub.removeClass("open");
			sub.removeClass("active");
		}
	});
} else {
	$("header .menu .sub > span").click(function(e) {
		e.preventDefault();

		var sub = $(this).closest(".sub"),
			h = sub.find("> ul")[0].scrollHeight;

		if(!sub.hasClass("open") && !sub.hasClass("active")) {
			sub.find("> ul").css("max-height", h);
			sub.addClass("open");
		} else {
			sub.find("> ul").css("max-height", "");
			sub.removeClass("open");
		}
	});
}


//********************************************
//********** SEARCH FROM VALIDATION **********
//********************************************

$("form[name='search'] button").on("click", function(e) {
	if(!$(this).parents("form").hasClass("open")) {
		e.preventDefault();
		e.stopPropagation();

		$(this).parents("form").addClass("open")

		return false;
	}
});

$("form[name='search']").submit(function() {
    if($(this).find("[name='q']").val() == "")
        return false;

    return true;
});


/***************************************/
/********** LOAD IMAGES ASYNC **********/
/***************************************/

function loadImages() {
    $("img[data-src]").each(function() {
        var src = $(this).data("src");

		$(this).attr("src", src);
		setTimeout(() => {
			$(this).removeAttr("data-src");
		}, 100);
    });
}

$(window).on("load", function() {
    loadImages();
});

//**************************
//********** BLOG **********
//**************************

$(".blog .slider").slick({
	dots: true,
	arrows: false,
	slidesToShow: 1,
	slidesToScroll: 1,
	autoplay: true,
	autoplaySpeed: 5000,
	speed: 1000
});

$(document).on("change", ".blog .filter-container .custom-select", () => {
	filterBlog();
});

$(".pesquisar input[name='pesquisa']").on("keypress", function (e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        filterBlog();
    }
});

$(".pesquisar").on("click", function (e) {
    e.preventDefault();
    if ($(".pesquisar input[name='pesquisa']").val() != "") {
        filterBlog();
    }
});

$(".filter-btn-container a").click(function () {
    $(".filter-container").addClass("lock");
    $("body").addClass("lock");
    $("html").addClass("lock");
});

$(".filter-container .filter-close").click(function () {
    $(".filter-container").removeClass("lock");
    $("body").removeClass("lock");
    $("html").removeClass("lock");
});

$(document).on("click", ".listing-blog .pagination a", function (e) {
    e.preventDefault();
	var page = $(this).attr("page");

	filterBlog (page);
});

$(document).on("click", ".blog .filter-container .custom-select.isSelected .placeholder", (e) => {
	var placeholder = $(e.currentTarget).parents().closest(".col-lg-3").children("select").find("option:first-of-type").html();
	console.log(placeholder);
	$(e.currentTarget).parent().removeClass("isSelected");
	$(e.currentTarget).parent().find(".options-wrapper .options div").removeClass("selected");
	$(e.currentTarget).html(placeholder);
	$(e.currentTarget).parent().removeClass("open");
	filterBlog();
});

function filterBlog (page = "") {
	var archive = $(".blog .filter-container .custom-select[data-name='ano'] .options-wrapper .options div.selected").data("value"),
		category = $(".blog .filter-container .custom-select[data-name='cat'] .options-wrapper .options div.selected").data("value"),
		pesquisa = $(".blog .filter-container .pesquisar input[name='pesquisa']").val(),
		page = (page != "" ? page : $(".blog .listings-blog .pagination li.active a").attr("page"));

	$.ajax({
		type: "POST",
		url: window.location.href,
		data: {
			data: archive,
			categoria: category,
			page: page,
			pesquisa: pesquisa
		},
		success: (response) => {
			var html = $(response),
			listing, listing_html;

			$(html).each(function() {
				if($(this).find(".listing").length > 0){
					listing = $(this).find(".listing");
				}
			});

			if(listing) {
				listing_html = $(listing).html();
				$(".blog .container .listing").html(listing_html);
			}

			$(".filter-container").removeClass("lock");
            $("body").removeClass("lock");
            $("html").removeClass("lock");

            $('html, body').animate({
                scrollTop: ($('.listing-blog').offset().top - 150)
            }, 500);
		}
	});
}