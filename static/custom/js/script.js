function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text/plain", event.target.id);
}

function drop(event) {
    event.preventDefault();
    const taskId = event.dataTransfer.getData("text/plain");
    const taskElement = document.getElementById(taskId);

    const droppedColumn = event.target.closest(".column");
    droppedColumn.appendChild(taskElement);
    let task_id = parseInt(taskElement.id.split("-")[1]);
    let stage_id = parseInt(droppedColumn.id.split("-")[1]);
    moveToStage(task_id, stage_id);
}

function addTask() {
    const taskNameInput = document.getElementById("taskName");
    const taskName = taskNameInput.value;

    if (taskName.trim() !== "") {
        const newTask = document.createElement("div");
        newTask.className = "task";
        newTask.draggable = true;
        newTask.id = "task" + Date.now();

        const taskContent = document.createElement("div");
        taskContent.textContent = taskName;

        const taskButton = document.createElement("a");
        taskButton.className = "btn btn-sm btn-secondary";
        taskButton.textContent = "Click me";
        taskButton.href = "https://www.google.com";

        newTask.appendChild(taskContent);
        newTask.appendChild(taskButton);

        newTask.addEventListener("dragstart", drag);

        document.getElementById("todo").appendChild(newTask);

        taskNameInput.value = "";
    }
}

function addColumn() {
    const columnNameInput = document.getElementById("columnName");
    const columnName = columnNameInput.value;

    if (columnName.trim() !== "") {
        const newColumn = document.createElement("div");
        newColumn.className = "column";
        newColumn.id = columnName.toLowerCase().replace(" ", "_");

        const columnHeader = document.createElement("h3");
        columnHeader.textContent = columnName;

        newColumn.appendChild(columnHeader);
        newColumn.ondrop = drop;
        newColumn.ondragover = allowDrop;

        document.getElementById("kanbanBoard").appendChild(newColumn);

        columnNameInput.value = "";
    }
}

function getData() {
    let arrList = [];
    let rows = document
        .getElementById("sortableTable")
        .getElementsByTagName("tbody")[0]
        .getElementsByTagName("tr");
    for (let i = 0; i < rows.length; i++) {
        let row = rows[i].getElementsByTagName("th")[0];
        arrList.push({
            id: row.getAttribute("data-id"),
            value: row.innerHTML,
        });
    }
    return arrList;
}