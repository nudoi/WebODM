import { systems } from '../../classes/Units';

describe('Metric system', () => {
  it('it should display units properly', () => {

    const { metric } = systems;

    const lengths = [
        [1, "1 m"],
        [0.01, "1 cm"],
        [0.0154, "1.5 cm"],
        [0.99, "99 cm"],
        [0.995555, "99.6 cm"],
        [1.01, "1.01 m"],
        [999, "999 m"],
        [1000, "1 km"],
        [1001, "1.001 km"],
        [1000010, "1,000.01 km"],
        [1000012.349, "1,000.01235 km"],
    ];
    
    lengths.forEach(l => {
        expect(metric.length(l[0]).toString()).toBe(l[1]);
    });

    const areas = [
        [1, "1 m²"],
        [9999, "9,999 m²"],
        [10000, "1 ha"],
        [11005, "1.1005 ha"],
        [11005, "1.1005 ha"],
        [999999, "99.9999 ha"],
        [1000000, "1 km²"],
        [1000000000, "1,000 km²"],
        [1000255558, "1,000.25556 km²"]   
    ];

    areas.forEach(a => {
        expect(metric.area(a[0]).toString()).toBe(a[1]);
    });
  })
});

describe('Imperial systems', () => {
  it('it should display units properly', () => {

    const { imperial, imperialUS } = systems;

    const lengths = [
        [1, "3.2808 ft", "3.2808 ft (US)"],
        [0.01, "0.0328 ft", "0.0328 ft (US)"],
        [0.0154, "0.0505 ft", "0.0505 ft (US)"],
        [1609, "5,278.8714 ft", "5,278.8608 ft (US)"],
        [1609.344, "1 mi", "5,279.9894 ft (US)"],
        [1609.3472187, "1 mi", "1 mi (US)"],
        [3218.69, "2 mi", "2 mi (US)"]
    ];
    
    lengths.forEach(l => {
      expect(imperial.length(l[0]).toString()).toBe(l[1]);
      expect(imperialUS.length(l[0]).toString()).toBe(l[2]);
    });

    const areas = [
        [1, "10.76 ft²", "10.76 ft² (US)"],
        [9999, "2.47081 ac", "2.4708 ac (US)"],
        [4046.86, "1 ac", "43,559.86 ft² (US)"],
        [4046.87261, "1 ac", "1 ac (US)"],
        [2587398.1, "639.35999 ac", "639.35744 ac (US)"],
        [2.59e+6, "1 mi²", "1 mi² (US)"]
    ];

    areas.forEach(a => {
      expect(imperial.area(a[0]).toString()).toBe(a[1]);
      expect(imperialUS.area(a[0]).toString()).toBe(a[2]);
    });
  })
});