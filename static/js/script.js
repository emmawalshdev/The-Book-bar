  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.dropdown-trigger').dropdown();
    $('.tooltipped').tooltip();
    $('#modal1').modal().modal('open');
    $('.modalconfirm').modal().modal('close');

    // CREDIT - Code institute 
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        // set css classes to match materialize valid & invalid classes
        let classValid = { "border-bottom": "1px solid #00acc1", "box-shadow": "0 1px 0 0 #00acc1" };
        let classInvalid = { "border-bottom": "1px solid #e780a3", "box-shadow": "0 1px 0 0 #e780a3" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        // if user is focused within input traverse the DOM
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            // apply valid class again if it is either valid or invalid
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                // else if user leaves the selection & bottom border was not updated to valid class then add invalid class
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(0, 172, 193)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});
