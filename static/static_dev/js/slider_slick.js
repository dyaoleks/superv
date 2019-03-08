  $('.slider').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: false,
	  fade: true,
	  asNavFor: '.slider-nav'
	});
	$('.slider-nav').slick({
      infinite: false,
      slidesToShow: 5,
	  slidesToScroll: 1,
	  asNavFor: '.slider',


	  focusOnSelect: true

  });


