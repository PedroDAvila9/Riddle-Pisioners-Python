# Success Probability with the Video Strategy

This is a Python code that implements a strategy to calculate the success probability in an experiment based on boxes and prisoners. The code uses the random module to shuffle the boxes and the matplotlib.pyplot module to display a bar chart showing the percentage of success and failure.
Code Execution

 ## To run the code, follow these steps:

    Make sure you have Python installed on your system.
    Copy the code and paste it into a file with the .py extension, for example, success_probability.py.
    Open a terminal or command prompt and navigate to the directory where the .py file is saved.
    Run the following command to execute the code: python success_probability.py.

The result will be displayed in the terminal or command prompt, and the bar chart will be opened in a new window.

## Code Explanation

   1. The code starts by importing the random and matplotlib.pyplot modules.
   2. Then, a function named verify() is defined, which is responsible for executing the experiment for each prisoner and checking if the strategy is successful.
   3. Inside the verify() function, the boxes list is copied to the copied_boxes variable to avoid modifying the original list.
   4. The random.shuffle() function is used to shuffle the copied_boxes list, representing the distribution of passwords in the boxes.
   5. A loop is started to represent each prisoner in the experiment.
   7. The box variable is initially set to the current prisoner number.
   8. Another loop is started, where the box variable is updated to represent the new box that the prisoner will switch to, according to the strategy.
   9. If the chosen box is equal to the prisoner's number, it means that the prisoner has found their password correctly, and the loop is broken.
   10. If the loop is completed without breaking, it means that the prisoner did not find their password, and the verify() function returns 0.
   11. Outside the prisoner loop, the verify() function is called multiple times (as defined by the value of the sim variable) to obtain the number of times the strategy was successful.
   12. The number of successful attempts is stored in the win variable.
   13. The success and failure percentages are calculated based on the number of successful attempts and the total number of simulations.
   14. The categories "Success" and "Failure," the corresponding percentages, and the colors for the bar chart are defined.
   15. Using the matplotlib.pyplot module, a bar chart is generated to show the percentage of success and failure.
   16. The chart is displayed with appropriate labels for the x-axis, y-axis, and title.
    Finally, the success probability with the video strategy is printed.

    the strategy was based on this video: https://www.youtube.com/watch?v=iSNsgj1OCLA&t=38s