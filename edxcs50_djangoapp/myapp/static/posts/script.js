//  Start with first post
let counter = 1;

// Load posts 20 at a time
const quantity = 20;

// When DOM loads, render the first 20 posts
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of posts
function load() {

    // Set start and end post numbers, and uodate counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add posts
    fetch(`/hello/posts?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            data.posts.forEach(add_post);
        })
}

// Add a new post with given contents to DOM
function add_post(contents) {

    // Create new post
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `${contents}  <button class='hide'>Hide</button>`;

    // Add post to DOM
    document.querySelector('#posts').append(post);
};

// If hide button is clicked, delete the post
document.addEventListener('click', e => {

    // Find what was clicked on:
    const element = e.target;

    // Check if the user clicked on a hide button
    if (element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'running'
        element.parentElement.addEventListener('animationend', () => {
            element.parentElement.remove()
        })
    }
})
