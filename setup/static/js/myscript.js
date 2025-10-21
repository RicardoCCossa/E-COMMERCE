// Aumentar quantidade
$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    var productRow = $(this).closest(".row.mb-4");

    $.ajax({
        type: "GET",
        url: "/pluscart/",
        data: { prod_id: id },
        success: function (data) {
            // Atualiza a quantidade
            eml.innerText = data.quantity;

            // Atualiza o total geral
            document.getElementById("totalamount").innerText = data.totalamount + " MT";

            // Atualiza o subtotal do produto (opcional)
            var priceElement = productRow.find(".text-success.fw-bold");
            if (priceElement.length > 0) {
                let itemPrice = parseFloat(priceElement.data("price"));
                priceElement.text((itemPrice * data.quantity).toFixed(2) + " MT");
            }
        },
        error: function () {
            alert("⚠️ Erro ao atualizar quantidade.");
        }
    });
});


// Diminuir quantidade
$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    var productRow = $(this).closest(".row.mb-4");

    $.ajax({
        type: "GET",
        url: "/minuscart/",
        data: { prod_id: id },
        success: function (data) {
            if (data.quantity > 0) {
                eml.innerText = data.quantity;
            } else {
                // Remove o item da página
                productRow.fadeOut(300, function () { $(this).remove(); });
            }

            // Atualiza o total geral
            document.getElementById("totalamount").innerText = data.totalamount + " MT";

            // Atualiza subtotal do produto
            var priceElement = productRow.find(".text-success.fw-bold");
            if (priceElement.length > 0) {
                let itemPrice = parseFloat(priceElement.data("price"));
                priceElement.text((itemPrice * data.quantity).toFixed(2) + " MT");
            }
        },
        error: function () {
            alert("⚠️ Erro ao atualizar quantidade.");
        }
    });
});


// Remover produto
$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var productRow = $(this).closest(".row.mb-4");

    $.ajax({
        type: "GET",
        url: "/removecart/",
        data: { prod_id: id },
        success: function (data) {
            productRow.fadeOut(300, function () {
                $(this).remove();
                document.getElementById("totalamount").innerText = data.totalamount + " MT";
            });
        },
        error: function () {
            alert("⚠️ Erro ao remover produto.");
        }
    });
});
