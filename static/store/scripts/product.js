$(document).ready(function() {
    $('#gallery').lightSlider({
      gallery:true,
      item:1,
      vertical:true,
      verticalHeight:500,
      vThumbWidth:60,
      thumbItem:7,
      thumbMargin:3,
      slideMargin:0,
      controls:false,
      speed:500
    }); 
     
    $('#relatedProducts').lightSlider({
        autoWidth:true,
        loop:true,
        controls:true,
        keyPress:true,
        onSliderLoad:function()
                    {
                      $("#relatedProducts").removeClass("cs-hidden");
                    }
    });


  });