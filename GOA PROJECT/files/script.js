const myProjects = [
    {
        title: "first project",
        description: "web-page with HTML&CSS",
        image: "https://via.placeholder.com/350x200",
        link: "#"
    },

    {
        title: "js HANGMAN",
        description: "little game created with js",
        image: "https://via.placeholder.com/350x200",
        link: "#"
    },

    {
        title: "py program",
        description: "banl program with python",
        image: "https://via.placeholder.com/350x200",
        link: "#"
    }
];

function displayProjects()  {
    const container = document.getElementById("project-container");

    myProjects.forEach(project => {
        const card = document.createElement("div");
        card.className = "project-card";
        card.innerHTML = `
            <img src="${project.image}" alt="${project.title}">
            <div clas="project-info">
                <h4>${project.title}</h4>
                <p>${project.description}</p>
                <a href="${project.link}" class="btn">click to see</a>
            </div>
        `;
        container.appendChild(card)
    })
}

document.addEventListener("DOMContentLoaded", displayProjects);
