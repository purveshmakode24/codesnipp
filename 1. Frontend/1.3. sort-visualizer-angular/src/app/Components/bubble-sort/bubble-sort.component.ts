import { Component, OnInit, ViewChild } from '@angular/core';
import { UIChart } from 'primeng/chart';

@Component({
  selector: 'app-bubble-sort',
  templateUrl: './bubble-sort.component.html',
  styleUrls: ['./bubble-sort.component.scss']
})
export class BubbleSortComponent implements OnInit {
  @ViewChild('chart') chart!: UIChart;

  basicData: any;
  basicOptions: any;
  array: any = [65, 59, 80, 81, 56, 55, 40];
  bkgColor: any = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey'];
  running: boolean = false;
  is_sorted: boolean = false;
  speed: number = 2;

  constructor() {
    this.setChatConfig();
  }

  ngOnInit(): void {
    this.basicData.labels = [...this.array];
    this.basicData.datasets[0].data = [...this.array];
    this.basicData.datasets[0].backgroundColor = [...this.bkgColor];
  }

  play() {
    this.bubbleSort();
  }

  reset() {
    this.is_sorted = false;
    this.basicData.labels = [...this.array];
    this.basicData.datasets[0].data = [...this.array];
    this.basicData.datasets[0].backgroundColor = [...this.bkgColor];
    this.chart.refresh();
  }

  stop() {
    this.running = false;
  }

  async bubbleSort() {
    this.running = true;
    const sleep = (time: any) => {
      return new Promise(resolve => setTimeout(resolve, time))
    }

    let data = this.basicData.datasets[0].data;
    let n = data.length;
    for (let i = 0; i < n; ++i) {
      for (let j = 0; j < n - i - 1; ++j) {
        if (!this.running) {
          break;
        }

        this.basicData.datasets[0].backgroundColor[j] = "red";
        this.basicData.datasets[0].backgroundColor[j + 1] = "red";
        this.chart.refresh();
        await sleep(this.speed * 1000);

        if (this.basicData.datasets[0].data[j] > this.basicData.datasets[0].data[j + 1]) {
          await new Promise((resolve: any) => setTimeout(() => {
            let temp = this.basicData.datasets[0].data[j];
            this.basicData.datasets[0].data[j] = this.basicData.datasets[0].data[j + 1];
            this.basicData.labels[j] = this.basicData.datasets[0].data[j + 1];

            this.basicData.datasets[0].data[j + 1] = temp;
            this.basicData.labels[j + 1] = temp;
            resolve("done");
          }, 500));
        }

        this.basicData.datasets[0].backgroundColor[j] = 'grey';
        this.basicData.datasets[0].backgroundColor[j + 1] = 'grey';
        this.chart.refresh();
      }

      this.basicData.datasets[0].backgroundColor[n - i - 1] = 'green';
      this.chart.refresh();

      if (!this.running) {
        break;
      }
    }

    if (this.running) {
      this.is_sorted = true;
      this.running = false
    } else {
      // stop in the mid of sorting.
      this.reset();
    }
  }

  setChatConfig() {
    this.basicData = {
      labels: [],
      datasets: [
        {
          label: 'My First dataset',
          backgroundColor: [],
          data: []
        }
      ]
    };

    this.basicOptions = {
      plugins: {
        legend: {
          display: false
        },
      }
    }
  }
}
