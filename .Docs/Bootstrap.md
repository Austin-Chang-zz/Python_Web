## bootstrap set up procedure

<details>
  <summary>1. files in templates folder</summary>

  [Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)      
  1.1 find suitable examples  
  1.2 click out the page  
  1.3 use right click on the page to get the bootstrap code  
  1.4 copy the code to vs code  
  1.5 download Compiled CSS and JS  
  [download Compiled CSS and JS](https://getbootstrap.com/docs/5.3/getting-started/download/)  
  1.6 copy the bootstrap.min.css, bootstrap.min.css.map to css folder, and bootstrap.bundle.min.js to js folder  
  1.7 modify the related code, _base.j2 to the right file path with {{  }} jinja format 
  
      <link href="{{url_for('static', filename='css/bootstrap.min.css')}}" rel="stylesheet">     
      <link href="{{url_for('static', filename='css/index.css')}}" rel="stylesheet">      
      <script src="{{url_for('static',filename='js/bootstrap.bundle.min.js')}}"></script>   
  
  
  
  

</details>
<details>
  <summary>2. Flask vs Dash</summary>
  
    Here’s a comparison table of using **Flask** and **Dash** to embed Bootstrap codes, highlighting their pros and cons:

| **Aspect**                  | **Flask with Bootstrap**                                                                                     | **Dash with Bootstrap**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Primary Purpose**         | General-purpose web framework for building full-stack web applications.                                     | Specialized for creating data-driven dashboards and interactive visualizations.                            |
| **Ease of Bootstrap Integration** | Bootstrap can be integrated easily by including the CDN in templates (`HTML/CSS`).                         | Bootstrap can be integrated through Dash Bootstrap Components (DBC) or external stylesheets.               |
| **Flexibility with HTML/CSS** | Full flexibility to write custom HTML/CSS or use Jinja templates with Bootstrap.                           | Dash uses Python to define layouts, but you can use Bootstrap classes via `className`.                     |
| **Support for Components**  | Requires manual coding for Bootstrap components (buttons, cards, modals, etc.).                             | Dash Bootstrap Components library provides ready-to-use Bootstrap components directly in Python.           |
| **Learning Curve**          | Easier for those familiar with standard web development practices (HTML, CSS, JS).                          | Easier for Python developers; no need to learn HTML/CSS deeply for most cases.                             |
| **Responsiveness**          | Fully supports responsive layouts via Bootstrap grid and utilities.                                         | Fully supports responsive layouts using DBC's `Container`, `Row`, and `Col` components.                    |
| **Routing**                 | Flask supports advanced routing and URL patterns with decorators.                                           | Dash has built-in multi-page app support but lacks Flask's routing granularity.                            |
| **JavaScript Support**      | Full control over JavaScript for advanced interactions, including custom scripts.                           | Limited direct JavaScript support; interactivity is managed using Dash callbacks (Python).                 |
| **Use Case**                | Ideal for full-stack web applications with static pages or forms.                                           | Best suited for dashboards, interactive data visualization, and analytics applications.                    |
| **Setup Complexity**        | Requires manual setup of HTML templates and linking Bootstrap files.                                        | Easier to set up with DBC or external stylesheets for predefined components.                               |
| **Performance**             | Faster for static websites or simpler use cases; supports various backend optimizations
</details>
<details>
  <summary>n. ---</summary>
  
    a---
</details>



[]()    
[]()    
