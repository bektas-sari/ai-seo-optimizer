document.addEventListener("DOMContentLoaded", function() {
    // Form elements
    const form = document.querySelector("form");
    const textarea = document.querySelector(".content-input");
    const submitBtn = document.querySelector(".submit-btn");
    const btnText = document.querySelector(".btn-text");
    const spinner = document.querySelector(".loading-spinner");
    const charCounter = document.querySelector(".char-counter");

    // Character counter functionality
    if (textarea && charCounter) {
        function updateCounter() {
            const text = textarea.value;
            const charCount = text.length;
            const wordCount = text.trim() === "" ? 0 : text.trim().split(/\s+/).length;
            charCounter.textContent = `Characters: ${charCount} | Words: ${wordCount}`;
        }

        textarea.addEventListener("input", updateCounter);
        updateCounter(); // Initial count
    }

    // Auto-resize textarea
    if (textarea) {
        textarea.addEventListener("input", function() {
            this.style.height = "