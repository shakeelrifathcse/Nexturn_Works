document.getElementById("add-task-btn").addEventListener("click", addTask);

function addTask() {
    const taskInput = document.getElementById("task-input");
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task!");
        return;
    }

    const taskList = document.getElementById("task-list");
    const li = document.createElement("li");

    li.innerHTML = `
        <span>${taskText}</span>
        <button class="delete-btn">Delete</button>
    `;

    li.querySelector("span").addEventListener("click", () => {
        li.querySelector("span").classList.toggle("task-completed");
    });

    li.querySelector(".delete-btn").addEventListener("click", () => {
        taskList.removeChild(li);
    });

    taskList.appendChild(li);
    taskInput.value = ""; // Clear the input field
}
