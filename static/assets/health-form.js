$(document).ready(function () {

    if (h_type == 'self') {
        $("#myself").removeClass('hide')
        $("#family").addClass('hide')

        $(".family-btn").removeClass('active')
        $(".myself-btn").addClass('active')
    } else if (h_type == 'family') {
        $("#family").show();
    } else if (h_type == 'parents') {
        $("#parents").show();

        $("#parents").removeClass('hide')
        $("#family").addClass('hide')
        $(".family-btn").removeClass('active')
        $(".parents-btn").addClass('active')
    } else {
        $('#main-tab2').show();
    }
    var select_init = {
        placeholder: 'Select City',
        containerCssClass: 'form-control',
        allowClear: true,
        tags: "true",
    };
    $(".select2").select2(select_init);

    //reset select2 on loading page
    //$(".city").val(null).trigger('change');
    //reset page form fields on loading page
    $('.health-search-form')[0].reset();


    $(".price-range").click(function(e){
        e.preventDefault();
        $('.price-range').removeClass('active');
        $(this).addClass('active');
        $(this).closest("form").find("[name='price_range']").val($(this).val());
        $(this).closest('form').find('.see-plan').addClass('success-btn')
        
    });

    
    /**/
    $('.myself-btn').click(function (event) {
        /* Act on the event */

        $(this).addClass('active');
        $('.family-btn, .parents-btn').removeClass('active');

        $('#myself').addClass('show').removeClass('hide');
        $('#family, #parents').addClass('hide').removeClass('show');


        $("input[name='health_for_type']").val("Myself");
    });
    $('.family-btn').click(function (event) {
        /* Act on the event */
        $(this).addClass('active');
        $('.parents-btn, .myself-btn').removeClass('active');

        $('#family').addClass('show').removeClass('hide');
        $('#myself, #parents').addClass('hide').removeClass('show');

        $('#family').show()
        $('#myself, #parents').hide()
       
    });
    $('.parents-btn').click(function (event) {
        $(this).addClass('active');
        $('.family-btn, .myself-btn').removeClass('active');
        /* Act on the event */
        $('#parents').addClass('show').removeClass('hide');
        $('#myself, #family').addClass('hide').removeClass('show');

    

        $("input[name='health_for_type']").val("Parents");
    });
    // 
    $('.self-city').on('change', function(){
        if ( $('.self-city').val() > 0 ) {
            $(this).closest('.form-group').addClass('focused')
        } else {
            $(this).closest('.form-group').removeClass('focused')
        }
    })

    $('.hsreq-self').on('change', function(){
        if ($('.selfage').val()!='' && $('.selectgender').val()!='' /*&& $('.self-city').val() > 0*/ ) {
            $(this).closest('form').find('.price-range').removeAttr('disabled');
        }
    })
    
    $(".btn-health-search-self").on('click', function () {
        var isValid = true;
        $(".form-select_box").each(function () {
            console.log('==================');
            console.log($(this).children('option:selected').val());
            if ($(this).children('option:selected').val() == ' ') {
                isValid = false;
                $(this).addClass('sel-error');
            } else {
                isValid = true;
                $(this).removeClass('sel-error');
            }
        });
        if (isValid) {           
            $("#health-search-form-self").submit();
        }
        return false;
    });

    $(".btn-health-search-family").on('click', function () {
        var isValid = true;
        $(".form-select_box_family").each(function () {
            console.log('=========FAMILY=========');
            console.log($(this).children('option:selected').val());
            if ($(this).children('option:selected').val() == ' ') {
                isValid = false;
                $(this).addClass('sel-error');
            } else {
                isValid = true;
                $(this).removeClass('sel-error');
            }
        });
        if (isValid) {           
            $("#health-search-form-family").submit();
        }
        return false;
    });

    $(".btn-health-search-parent").on('click', function () {
        var isValid = true;
        $(".form-select_box_parent").each(function () {
            console.log('=========parent=========');
            console.log($(this).children('option:selected').val());
            if ($(this).children('option:selected').val() == ' ') {
                isValid = false;
                $(this).addClass('sel-error');
            } else {
                isValid = true;
                $(this).removeClass('sel-error');
            }
        });
        if (isValid) {           
            $("#health-search-form-parent").submit();
        }
        return false;
    });

    $('.family-city').on('change', function(){
        if ( $('.family-city').val() > 0 ) {
            $(this).closest('.form-group').addClass('focused')
        } else {
            $(this).closest('.form-group').removeClass('focused')
        }
    })
    // hsreq-family
    $('.hsreq-family').on('change', function(){
        if ($('.yourage').val()!='' && $('.yourspousage').val()!='' /*&& $('.family-city').val() > 0*/ ) {
           // $(this).closest('form').find('.price-range').removeAttr('disabled').first().addClass('active');
            //$(this).closest('#family').find('.btn-health-search-family').addClass('success-btn')
            $(this).closest('form').find('.price-range').removeAttr('disabled');
        }
    })

    // $(".kid-selection").each(function (index, element) {
    //     if(index >0){
    //         $(this).addClass('disabled');
    //     }
    // });

    $(document).ready(function(){
        $('#kid-step1').click(function(){
            $(this).addClass('hide')
            $('.kid-selection').removeClass('hide')
        })
    })
    $(document).on('change', ".kid-selection select.child", function (e) {
        //$(this).find('select').focus();
        console.log($(this).val());
        if($(this).val() != ""){
            $(this).closest('.kid-selection').addClass('selected')
                .find('.kid-selection-text').text( $(this).find('option:selected').text() );
                $('#kid-add-btn').addClass('show')
        }
        else{
            $(this).closest('.kid-selection').removeClass('selected')
                .find('.kid-selection-text').text("");
                $('#kid-add-btn').removeClass('show')
        }
        //$(".kid-selection select.child option:first").attr('selected','selected');
    });



    $(".btn-health-search-family").on('click', function () {

        var isValid = true;
        $(".hsreq-family").each(function () {
            if ($(this).val() == '') {
                isValid = false;
                $(this).addClass('sel-error');
            } else {
                isValid = true;
                $(this).removeClass('sel-error');
            }
        });
        if (isValid) {
            var policy_for_txt_a = "";
            var policy_for_txt_c = "";
            var count_a = 0;
            var count_c = 0;
            $(".adult").each(function () {
                if ($(this).val() != '' && $(this).val() != '-1') {
                    count_a += 1;
                }
            });
            policy_for_txt_a = 'Adults (' + count_a + ')';
            $(".child").each(function () {
                if ($(this).val() != '') {
                    count_c += 1;
                }
            });
            if (count_c > 0)
                policy_for_txt_c = 'Children (' + count_c + ')';
            $("#members-family").val(policy_for_txt_a + ',' + policy_for_txt_c);
            mixpanel.track('Health Search Family Form Submitted Succesfully');
            mixpanel.track('Health Search Form Submitted Succesfully');
            fbq('track', 'Search');
            console.log('Health Search Form Submitted Succesfully');
            $("#health-search-form-family").submit();

        }
        return false;
    });

    $('.parent-city').on('change', function(){
        if ( $('.parent-city').val() > 0 ) {
            $(this).closest('.form-group').addClass('focused')
        } else {
            $(this).closest('.form-group').removeClass('focused')
        }
    })
    // 
    $('.hsreq-parents').on('change', function(){
        console.log($('.hsreq-parents').val());
        if ($('.hsreq-parents').val()!='' /*&& $('.parent-city').val() > 0*/ ) {
           // $(this).closest('form').find('.price-range').removeAttr('disabled').first().addClass('active');
           // $(this).closest('#parents').find('.btn-health-search-parent').addClass('success-btn')
           $(this).closest('form').find('.price-range').removeAttr('disabled');
        }
    })
    // $(".btn-health-search-parent").on('click', function () {
    //     var isValid = true;
    //     $(".hsreq-parents").each(function () {
    //         if ($(this).val() == '') {
    //             isValid = false;
    //             $(this).addClass('sel-error');
    //         } else {
    //             isValid = true;
    //             $(this).removeClass('sel-error');
    //         }
    //     });
    //     if (isValid) {
           
    //         $("#health-search-form-parent").submit();

    //     }
    //     return false;
    // });

});


function setrg(obj, amembersId) {
    var arss = "";
    $(".ag").each(function () {
        if ($(this).val() && $(this).val() != '-1') {
            arss += ($(this).attr('data-rel') + ":" + $(this).val() + "year,");
        }
        $("input[name='amembers']").val(arss);
    })
}


function setval(obj, amembersId) {
    var ar = "";
    var rar = "";
    $('.ag').attr('data-rel', $(obj).val());

    $(".ag").each(function () {
        if ($(this).val()) {
            ar += ($(this).attr('data-rel') + ":" + $(this).val() + "year,");
        }
        if (ar) {
            $("input[name='amembers']").val(ar);
        }
    });

}

var child_counter = 1;
$("#kid-add-btn").click(function () {

    var imgSrc = $('.imggroupforothers').children('img').attr('src');
 
    if(child_counter <=7 ){
        var kids = $(".kid-selection");
        var currentKid = $(".kid-selection:last-child"); 
        var lastField = currentKid.find("select");
        var intId = (lastField && lastField.length && lastField.data("idx") + 1) || 2;
        var fieldWrapper = $("<div  class=\"kid-selection kid-" + intId + "\"/>");
        var ageSelect = $("<div class=\"label-box\">"+
                          "  <div class=\"label-box-in\">"+
                          "      <div class=\"img imggroup\">" +
                          "           <img src=\""+imgSrc+"\">" +
                          "      </div>" +
                          "      <div class=\"text bluedark semibold\">" +
                          "         <div>" +
                          "              Kid "+intId +
                          "         </div> " +
                          "         <div class=\"kid-selection-text2\">" +
                          "             <span>" +
                          "              Select age " +
                          "             </span>" +
                          "             <i class=\"icofont icofont-caret-down\">" +
                          "             </i>" +
                          "         </div> " +
                          "      </div> " +
                          "      <div class=\"kid-selection-text\"></div>" +
                          "  </div> " +
    " <select name=\"kids\" data-rel=\"Kid " + intId + "\" data-idx=\"" + intId + "\" onchange=\"setrg(this,'amembers-family')\" class=\"form-control ag child\">\n" +
            "                                                                                    <option value=\"\"></option>\n" +
            "                                                                                    <option value=\"0.3\">3 Months</option>\n" +
            "                                                                                    <option value=\"0.6\">6 Months</option>\n" +
            "                                                                                    <option value=\"1\">1 Years</option>\n" +
            "                                                                                    <option value=\"2\">2 Years</option>\n" +
            "                                                                                    <option value=\"3\">3 Years</option>\n" +
            "                                                                                    <option value=\"4\">4 Years</option>\n" +
            "                                                                                    <option value=\"5\">5 Years</option>\n" +
            "                                                                                    <option value=\"6\">6 Years</option>\n" +
            "                                                                                    <option value=\"7\">7 Years</option>\n" +
            "                                                                                    <option value=\"8\">8 Years</option>\n" +
            "                                                                                    <option value=\"9\">9 Years</option>\n" +
            "                                                                                    <option value=\"10\">10 Years</option>\n" +
            "                                                                                    <option value=\"11\">11 Years</option>\n" +
            "                                                                                    <option value=\"12\">12 Years</option>\n" +
            "                                                                                    <option value=\"13\">13 Years</option>\n" +
            "                                                                                    <option value=\"14\">14 Years</option>\n" +
            "                                                                                    <option value=\"15\">15 Years</option>\n" +
            "                                                                                    <option value=\"16\">16 Years</option>\n" +
            "                                                                                    <option value=\"17\">17 Years</option>\n" +
            "                                                                                    <option value=\"18\">18 Years</option>\n" +
            "                                                                                    <option value=\"19\">19 Years</option>\n" +
            "                                                                                    <option value=\"20\">20 Years</option>\n" +
            "                                                                                    <option value=\"21\">21 Years</option>\n" +
            "                                                                            </select>");
                          "  </div> "
    
        var removeButton = $("<a id=\"remove\" class=\"button remove\"><i class=\"fas fa-times\" data-toggle=\"tooltip\" title=\"Remove Child\"></i> </a>");
        removeButton.click(function () {
            child_counter--;
             console.log(child_counter);
             $(this).prev('select').prop('selectedIndex',0).trigger( "change" );
            setrg($(this).prev('select'),'amembers-family');
                if(child_counter >1){
                    $(this).parent().prev('.kid-selection').removeClass("hide-remove");
                    
                }
                $(this).parent().remove();
            
        });
        if(child_counter >1){
        $(".kid-selection").addClass('hide-remove');
        }
        fieldWrapper.append(ageSelect);
        fieldWrapper.append(removeButton);
        $(".kids-selection").append(fieldWrapper);
        
        child_counter++;
    }

    

    if(child_counter >=4){
        $(this).addClass('hide');
    }

    console.log(child_counter);
    
});