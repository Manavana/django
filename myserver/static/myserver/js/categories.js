const = renderCategory = ({id, name}) => (
    `
    <li class="product productNew">
        <a href="/categories/${ id }" class="product_link">
            ${ name|upper }
        </a>
    </li>
    `
)