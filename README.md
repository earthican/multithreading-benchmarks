# multithreading-benchmarks
Data from measuring multithreading performance on my machine

| Machine | OS | OS Version | Processor | # Cores | 
| :--- | ---: | ---: | ---: | ---: | 
| MacBook Pro (Retina, 13-inch, Late 2013) | OS X Yosemite | 10.10.5 | 2.4 GHz Intel Core i5 | 4(?) | 

| Benchmark | # Threads | Elapsed Time | 
| :---- | :---- | ----: | 
| Count 10,000,000 | Single | 00:00:00 | 
| Count 10,000,000 | 8 | 00:01:23 | 
| Count 10,000,000 | 32 | 00:01:12 | 

## What is this?

I am measuring the performance of multithreads on my CPU. This (messy) repository will contain any source code, data, and reports I make during my tests. I hope to run these tests across machines and platforms.

## Why are you doing this?

Just curious to see how the effectiveness of multi threaded programming works under the hood. Nothing fancy here, I'm only implementing very simple and basic benchmarks (for now). Hoping to learn something from this.

## License

MIT
