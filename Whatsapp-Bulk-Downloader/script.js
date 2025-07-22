const downloadButtons = Array.from(document.querySelectorAll('div[role="button"][title^="Download"]'));

console.log("Found", downloadButtons.length, "downloadable files");

downloadButtons.forEach((btn, i) => {
  setTimeout(() => {
    console.log("Clicking:", btn.title);
    btn.click();
  }, i * 1500); // 1.5s delay to avoid overwhelming
});