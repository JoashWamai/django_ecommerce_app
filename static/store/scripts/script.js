$(document).ready(function()
{

    var searchbar=$(".searchbar");
    var form=$(".form")

    $(".fa-search").click(function()
    {
        searchbar.addClass("searchbar-active");
    });
    $(".search-cancel").click(function()
    {
        searchbar.removeClass("searchbar-active");
    });

    $(".fa-user-alt").click(function()
    {
        form.addClass("login-active");
    });
    $(".form-cancel").click(function()
    {
        form.removeClass("login-active").removeClass("sign-up-active");
    });
    $(".sign-up-btn").click(function()
    {
        form.removeClass("login-active").addClass("sign-up-active");
    });
    $(".sign-in-btn").click(function()
    {
        form.addClass("login-active").removeClass("sign-up-active");
    });


    $('#adaptive').lightSlider({
        adaptiveHeight:true,
        item:1,
        slideMargin:0,
        loop:true ,
        speed:1000,
        pause:4000,
        auto:true,
        pauseOnHover:true,
        controls:false
    }); 
    $("#autoWidth").lightSlider({
        autoWidth:true,
        loop:true,
        onSliderLoad:function()
                    {
                        $("#autoWidth").removeClass("cs-hidden");
                    }
    });
    $("#autoWidth2").lightSlider({
        autoWidth:true,
        loop:true,
        controls:true,
        speed:3000,
        pause:2500,
        auto:true,
        pauseOnHover:true,
        onSliderLoad:function()
                    {
                        $("#autoWidth2").removeClass("cs-hidden");
                    }

    });
    $("#autoWidth3").lightSlider({
        autoWidth:true,
        loop:true,
        speed:2100,
        pause:900,
        controls:false,
        auto:true,
        pauseOnHover:false,
        rtl:true,
        onSliderLoad:function()
            {
                $("#autoWidth3").removeClass("cs-hidden");
            }
    });

    $('.new-arrivals').flyto({
          item      : '.product-box',
          target    : '.cart',
          button    : '.fa-shopping-cart'
        });

            /*** ADD TO CART ***/

    var updatebtns = $('.updatecart');

        updatebtns.each(function(){
            $(this).click(function(e){
                e.preventDefault();
                var productId=$(this).data('product');
                var action=$(this).data('action');
                updateCartOrder(productId,action)
            });
        });

        function updateCartOrder(product,action)
        {

            $.ajax({
                method:'POST',
                headers: {'X-CSRFToken': csrftoken},
                url: '/updateItem/',
                dataType:'json',
                data:JSON.stringify({'product':product,'action':action}),
                success: function(response)
                    {
                        console.log(response);
                        location.reload();
                    }

            });
        }

        /*** ADD TO WISHLIST ***/

        var  updatewish = $('.updatewish');

         updatewish.each(function(){
            $(this).click(function(e){
                e.preventDefault();
                var productId=$(this).data('product');
                var action=$(this).data('action');
               updateWish(productId,action)
            });
        });

        function updateWish(product,action)
        {

            $.ajax({
                method:'POST',
                headers: {'X-CSRFToken': csrftoken},
                url: '/updateWishList/',
                dataType:'json',
                data:JSON.stringify({'product':product,'action':action}),
                success: function(response)
                    {
                        console.log(response);
                        location.reload();
                    }

            });
        }

        /*** SEARCH AUTOCOMPLETE ***/

        var search = $('#search');

        search.autocomplete({
            source:"/autocomplete/"
        });

        /*** SEARCH PRODUCT ***/

      var search=$('#search');

      search.keyup(function(e){
         if (e.keyCode == 13)
          {
          var term=search.val();
            searching(term);
          }
      });
      function searching(term)
      {
         $.ajax({
                type:'GET',
                headers: {'X-CSRFToken': csrftoken},
                url: '/search/',
                data:JSON.stringify({'q':term}),
                success: function(response)
                    {
                        console.log(response);
                    },
                  error:function(response)
                      {
                            console.log(response);
                      }

            });
      }

      /** Checkout **/

       $(".checkout-btn").click(function(){
         details={"fname":$("#FirstName").val(),
                "lname":$("#LastName").val(),
                "phone":$("#Telephone").val(),
                "email":$("#Email").val(),
                "county":$("#County").val(),
                "subcounty":$("#SubCounty").val(),
                "town":$("#Town").val()
                };


            $.ajax({
            url:"/checkout/",
            headers: {'X-CSRFToken': csrftoken},
            type:"post",
            data:JSON.stringify(details),
            success:function(response){
                console.log(response.data)
                alert("sucess")},
             error:function(response){
                alert("something went wrong")
                console.log(response)
            }
            });
       });

        /** From Cart to Wish **/

        $("#wish").click(function(){
            productId=$(this).data("product");
             quantity=$(this).data("quantity");

            transferCarttoWish(productId,quantity)
        });

        function transferCarttoWish(productId,quantity)
        {
            $.ajax({
                type:"post",
                url:"/cartToWishlist/",
                headers: {'X-CSRFToken': csrftoken},
                data:JSON.stringify({"productId" : productId,"quantity":quantity}),
                dataType:"json",
                success:function(response){
                    location.reload();
                },
                error:function(response){
                    alert("Error!!");
                }

            })
        }

        /*** From Wishlist to Cart ***/

        $("#cart").click(function(){
            productId=$(this).data("product");
             quantity=$(this).data("quantity");

            transferWishtoCart(productId,quantity)
        });

        function transferWishtoCart(productId,quantity)
        {
            $.ajax({
                type:"post",
                url:"/wishlistToCart/",
                headers: {'X-CSRFToken': csrftoken},
                data:JSON.stringify({"productId" : productId,"quantity":quantity}),
                dataType:"json",
                success:function(response){
                    location.reload();
                },
                error:function(response){
                    alert("Error!!");
                }

            })
        }
});

