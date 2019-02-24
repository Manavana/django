const = renderProduct = ({id, name, image, price}) => (
    `
    <div class="product productNew">
        <a href="/products/${ id }" class="product_link">
            <img src="${ image ? image : '/static/products/images/empty.png' }" alt="${ name }">
        </a>
        <div class="productInfo">
            <p class="vendorCode">
                ${ name|upper }
            </p>
            <div>
                <p class="price">
                    ${ price ? price : 'No value' } &#8381;
                </p>
            </div>
        </div>
    </div>
    `
)