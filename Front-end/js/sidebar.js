document.addEventListener("DOMContentLoaded", () => {
  const openBtn = document.getElementById("open-sidebar-btn");
  const closeBtn = document.getElementById("close-sidebar-btn");
  const sidebar = document.getElementById("mobile-sidebar");
  const sidebarLinks = document.querySelectorAll(".sidebar-link");

 
  openBtn.addEventListener("click", () => {
    sidebar.classList.add("is-open");
    document.body.classList.add("no-scroll"); 
  });

  
  const closeSidebar = () => {
    sidebar.classList.remove("is-open");
    document.body.classList.remove("no-scroll");
  };

  
  closeBtn.addEventListener("click", closeSidebar);

  
  sidebarLinks.forEach((link) => {
    link.addEventListener("click", closeSidebar);
  });

  
  document.addEventListener("click", (e) => {
    if (
      sidebar.classList.contains("is-open") &&
      !sidebar.contains(e.target) &&
      !openBtn.contains(e.target)
    ) {
      closeSidebar();
    }
  });

  
});