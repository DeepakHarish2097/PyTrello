let sortable = new Sortable(
    document
        .getElementById("sortableTable")
        .getElementsByTagName("tbody")[0],
    {
        animation: 150,
        onUpdate: function (evt) {
            // Update the row numbers dynamically
            let rows = evt.from.getElementsByTagName("tr");
            for (let i = 0; i < rows.length; i++) {
                rows[i].getElementsByTagName("th")[0].textContent = i + 1;
            }
        },
    }
);