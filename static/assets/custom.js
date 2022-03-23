$(document).ready(function () {
    $('select').not('.select-ignore').select2({
        placeholder: "Select a state",
    });


var select2Optionmodel = { width: '100%', placeholder: 'Car Model', containerCssClass: 'form-control' };
var select2Optionvariant = { width: '100%' };

// Loading raw JSON files of a secret gist - https://gist.github.com/ajaxray/32c5a57fafc3f6bc4c430153d66a55f5
var apiUrlmodel = 'data-form/cars/model/:parentId:.json';
var apiUrlvariant = 'data-form/cars/variant/:parentId:.json';



$('#model').select2(select2Optionmodel);
var cascadLoadingmodel = new Select2Cascade($('#brand'), $('#model'), apiUrlmodel, select2Optionmodel);
cascadLoadingmodel.then(function (parent, child, items) {
    console.log(items);
});


$('#variant').select2(select2Optionvariant);
var cascadLoadingvariant = new Select2Cascade($('#model'), $('#variant'), apiUrlvariant, select2Optionvariant);
cascadLoadingvariant.then(function (parent, child, items) {
    console.log(items);
});

});



