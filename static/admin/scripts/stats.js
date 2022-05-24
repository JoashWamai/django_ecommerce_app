var config = {
      type: 'doughnut',
      data: {
        datasets: [{
          data: '{{data|safe}}',
          backgroundColor: [
            'red', 'purple', 'blue', 'green', 'yellow','maroon'
          ],
          label: 'Products'
        }],
        labels:'{{ labels|safe }}',
      },
      options: {
        responsive: true
      }
    };

    window.onload = function() {
      var ctx = document.getElementById('piechart').getContext('2d');
      const myChart = new Chart(ctx, config);
    };