// розділ Розподіл ступеня ризику субєктів господарювання

//$(document).ready(function() { // ця структура говорить про те що цей код виконуються після відпрацювання шаблону
//	var form = $('#form_choosing_criteria');
//	console.log(form);
//	form.on('submit', function(e){  // e - довільна назва функції (від event)
//	    e.preventDefault();  // preventDefault()не дозволяє автоматично оновлювати форму
//        console.log('123');
//        var nmb = $('#number').val(); // викликаємо val (велью) по id number з темплейту
//        console.log(nmb);
//	})
	var form = $('#form_choosing_criteria_my');
	console.log(form);
	form.on('submit', function(e){  // e - довільна назва функції (від event)
	    e.preventDefault();  // preventDefault()не дозволяє автоматично оновлювати форму
        var is_main = $('#is_main').val(); // викликаємо val (велью) по id number з темплейту
        console.log(is_main);
	})

});





////	додаємо функцію яка передає дані через аджакс для видалення елементів корзини, як зі скрипта так із сторінки корзини
//     function cartUpdating(product_id, nmb, is_delete){
//
//		 var data = {};  // data - це перемінна  (інформація), що буде надсилатися у корзину
//// у data необхідно додати id товару і його кількість:
//         data.product_id = product_id;
//		 data.nmb = nmb;
//		 var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val(); // ці дві строчки додають csrf запит, що треба джанго для проведдення постзапиту
//		 data["csrfmiddlewaretoken"] = csrf_token; // записується у формі у product.html
//
//        if (is_delete){
//            data["is_delete"] = true;
//        }
//
//        // адреса на яку надсилається постзапит
//         var url = form.attr("action"); // треба писати url так, щоб він зчитувався з атрибуту action на формі у product.html
//
//		 console.log(data)
////	додаємо функцію ajax перед відображенням записів у корзині для того, щоб дані у корзину надходили післі обробки через
//// для передачі даних із замовлення на бекенд через ajax записується:
////       тепер іде безпосередньо ajax:
//            $.ajax({
//                 url: url,      // адреса постзапита
//                 type: 'POST',
//                 data: data,
//                 cache: true,
//                 success: function (data) { // спрацьовує у разі успіху
//                     console.log("OK");
//                     console.log(data.products_total_nmb );
//// для відображення кількості товарів у корзині у () на id products_total_nmb у файлі navbar.html пишемо:
//// if пишемо для того, щоб відображення було тільки тоді коли у корзині є щось:
//                     if (data.products_total_nmb || data.products_total_nmb == 0){
//                        $('#cart_total_nmb').text("("+data.products_total_nmb+")");
//    //з вьюхи у ордерс виводимо у консоль дані зі словника, який ми заповнюємо для оптимізації записів у корзині
//                        console.log(data.products);
//
//// цим кодом adjax видаляє усі попередні записи з таблиці і післяцього переходить до формування списку товарів у корзині пишемо:
//                         $('.cart-item ul').html("");
//
////для проходження по списку (data.products), що виводиться у консолі пишемо:
////функція проходиться по кожному обєкту у списку k- його порядковий номер v-сам обєкт:
//                         $.each(data.products, function(k, v){
//// для додавання даних безпоеседеньо у корзину необхідно  використати функцію append
//// додаємо v. до кожної перемінної для відпрацювання функції $.each  вище.
//                            $('.cart-item ul').append('<li>' + v.product_name+' X'+ v.nmb+' UAH'+ v.price_per_item+''+
//                            '<a class="delete-item" href="" data-product_id="'+v.id+'"> x </a>' + // закоментували хрестик для можливості видалення товару через сторінку корзини у навбарі
//                            '</li>');
//                            });
//
//                  }
//             },
//             error: function() {        // спрацьовує у разі помилки
//                 console.log("error")
//             }
//         })
//
//    }
//
//	form.on('submit', function(event){
//		event.preventDefault();
//		console.log('123');
//		var nmb = $('#number').val()
//		console.log(nmb);
//		var submit_btn = $('#submit_btn');
//		var product_id = submit_btn.data("product_id");
//		var product_name = submit_btn.data("product_name");
//		var product_price = submit_btn.data("product_price");
//		console.log(product_id);
//		console.log(product_name);
//		console.log(product_price);
//
//		cartUpdating(product_id, nmb, is_delete=false)
//    });
//
//
////  частина коду, що описує дії при натисканні чи наведенні курсору на корзину для її появи на екрані
//
//    function showing_cart (){}
//
//	$('.cart-container').on('click', function(event){
//		event.preventDefault();
//		$('.cart-item').removeClass('hidden');
//	});
//	$('.cart-container').mouseover (function(){
//		$('.cart-item').removeClass('hidden');
//	});
//	$('.cart-container').mouseout (function(){
//		$('.cart-item').addClass('hidden');
//	});
//
//// для того, щоб спрацьовувах X у кінці корзини для видалення елементів з коризини пишеться додатково:
//	$(document).on('click', '.delete-item', function(event) {
//		event.preventDefault();
//		product_id = $(this).data("product_id")
//		nmb = 0;
//		cartUpdating(product_id, nmb, is_delete=true)
//	});
//
//// функція для підрахунку повної суми замовлення у корзині:
//    function calculatingCartAmount(){
//        var total_order_amount = 0;
//        $('.total-product-in-cart-amount').each(function() {        // проходимо по кожній сумі замовлення у корзині і доодаємо усі значення
//            total_order_amount += parseFloat($(this).text());          // parseInt функція, що преображає текст у числа, для їх успішного додавання
//        });
//
//        $('#total_order_amount').text(total_order_amount.toFixed(2));          // вписуємо отриманий результат у те місце де вказане id,
//    };
//
//
//    $(document).on('change', ".product-in-cart-nmb", function(){
//        var current_nmb = $(this).val();
//        console.log(current_nmb);
//        var current_tr = $(this).closest('tr');
//        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
//        console.log(current_price);
//        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
//        console.log(total_amount);
//        current_tr.find('.total-product-in-cart-amount').text(total_amount);
//
//        calculatingCartAmount();
//    });
//
//    calculatingCartAmount();
//});


