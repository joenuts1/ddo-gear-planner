import { Component, OnInit } from '@angular/core';

import { EquippedService } from '../equipped.service';
import { GearDbService } from '../gear-db.service';

import { AffixCloud } from '../affix-cloud';

@Component({
  selector: 'app-affix-cloud',
  templateUrl: './affix-cloud.component.html',
  styleUrls: ['./affix-cloud.component.css']
})
export class AffixCloudComponent implements OnInit {
  cloud: AffixCloud;
  workingMap: Map<string, number>;
  savedSet: Set<string>;
  topResults: Array<any>;

  constructor(
    public equipped: EquippedService,
    public gearDB: GearDbService,
  ) { 
    this.workingMap = new Map<string, number>();
    this.savedSet = new Set<string>();
    this.topResults = new Array<any>();

    const gearList = gearDB.getGearList();

    let flatList = [];
    for (const entry of gearList.entries()) {
      flatList = flatList.concat(entry[1]);
    }

    this.cloud = new AffixCloud(flatList);

    const seed = ['Strength', 'Dexterity', 'Intelligence', 'Wisdom', 'Charisma'];
    this.topResults = seed.map(a => [a, 0]);
  }

  ngOnInit() {
  }

  add(affix: string) {
    this.savedSet.add(affix);
    this.equipped.addImportantAffix(affix);

    const map = this.cloud.get(affix);

    this.workingMap = this.cloud.merge(this.workingMap, map);
    for (const entry of this.workingMap) {
      if (this.savedSet.has(entry[0])) {
        this.workingMap.delete(entry[0]);
      }
    }

    this.topResults = Array.from(this.workingMap.entries()).sort((a, b) => b[1] - a[1]).slice(0, 20);
  }

  remove(affix: string) {
    this.savedSet.delete(affix);
    this.equipped.removeImportantAffix(affix);
  }
}
