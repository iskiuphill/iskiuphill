<template>
<div class="container is-half">
	<b-table :data="resorts">
			<b-table-column field="skiResortName" label="Ski Resort" sortable v-slot="props" searchable>
				<a :href="props.row.resortWebsite">{{props.row.skiResortName}}</a>
			</b-table-column>
			<b-table-column field="region" label="Region" sortable v-slot="props" searchable>
				<p>{{props.row.region}}</p>
			</b-table-column>
			<b-table-column field="snowConditionLink" label="Conditions" v-slot="props">
				<a :href="props.row.snowConditionLink">Conditions</a>
			</b-table-column>
			<b-table-column field="uphillPolicy" label="Has Uphill Policy?" sortable v-slot="props">
				<p>{{props.row.uphillPolicy}}</p>
			</b-table-column>
			<b-table-column field="uphillPolicy" label="Uphill Policy" sortable v-slot="props">
				<div v-if="props.row.uphillPolicy === 'Yes'">
					<a :href="props.row.uphillPolicyLink">Uphill Policy</a>
				</div>
			</b-table-column>
	</b-table>
</div>
</template>

<script>
const RESORTS = [
  {
    "skiResortName": "49 Degrees Mountain Resort",
    "resortWebsite": "https://www.ski49n.com/",
    "latLong": "48.3011315,-117.5647559",
    "region": "WA",
    "snowConditionLink": "https://www.ski49n.com/mountain-info/expanded-conditions",
    "uphillPolicy": "No",
    "uphillPolicyLink": "",
    "facebookLink": "https://www.facebook.com/ski49n/",
    "twitterLink": "https://twitter.com/49DegreesNorth",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Blue Wood",
    "resortWebsite": "http://www.bluewood.com/",
    "latLong": "46.0824903,-117.8533613",
    "region": "WA",
    "snowConditionLink": "https://www.bluewood.com/conditions",
    "uphillPolicy": "No",
    "uphillPolicyLink": "",
    "facebookLink": "https://www.facebook.com/SkiBluewood/",
    "twitterLink": "https://twitter.com/skibluewood",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Crystal Mountain Resort",
    "resortWebsite": "https://www.crystalmountainresort.com/",
    "latLong": "46.9350794,-121.4749631",
    "region": "WA",
    "snowConditionLink": "https://www.crystalmountainresort.com/the-mountain/mountain-report-and-webcams#/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://www.crystalmountainresort.com/the-mountain/mountain-safety/uphill-travel",
    "facebookLink": "https://www.facebook.com/CrystalMountainWashington/",
    "twitterLink": "https://twitter.com/crystalmt",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Mission Ridge",
    "resortWebsite": "https://www.missionridge.com/",
    "latLong": "47.2922486,-120.4008585",
    "region": "WA",
    "snowConditionLink": "missionridge.com/snow-report",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://www.missionridge.com/uphill-policy",
    "facebookLink": "https://www.facebook.com/MissionRidgeSkiAndBoardResort/",
    "twitterLink": "https://twitter.com/skimissionridge",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Mt. Baker Ski Area",
    "resortWebsite": "https://www.mtbaker.us/",
    "latLong": "48.8572999,-121.6709286",
    "region": "WA",
    "snowConditionLink": "https://www.mtbaker.us/snow-report",
    "uphillPolicy": "No",
    "uphillPolicyLink": "",
    "facebookLink": "https://www.facebook.com/mtbakerskiarea/",
    "twitterLink": "https://twitter.com/mtbakerski",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Mt. Spokane Ski & Snowboard Park",
    "resortWebsite": "https://www.mtspokane.com/",
    "latLong": "47.921355,-117.0978843",
    "region": "WA",
    "snowConditionLink": "https://www.mtspokane.com/mountain-conditions/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://www.mtspokane.com/uphill-travel-policy/",
    "facebookLink": "https://www.facebook.com/mtspokane/",
    "twitterLink": "https://twitter.com/mtspokane",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Stevens Pass",
    "resortWebsite": "https://www.stevenspass.com/",
    "latLong": "47.7446164,-121.0908962",
    "region": "WA",
    "snowConditionLink": "https://www.stevenspass.com/the-mountain/mountain-conditions/weather-report.aspx",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://www.stevenspass.com/the-mountain/more-options/mountain-safety.aspx?tc_1=1",
    "facebookLink": "https://www.facebook.com/stevenspass/",
    "twitterLink": "https://twitter.com/StevensPass",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "The Summit at Snoqualmie",
    "resortWebsite": "https://summitatsnoqualmie.com/",
    "latLong": "47.4078416,-121.420087",
    "region": "WA",
    "snowConditionLink": "https://summitatsnoqualmie.com/conditions",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://summitatsnoqualmie.com/uphill-travel",
    "facebookLink": "https://www.facebook.com/summitatsnoqualmie/",
    "twitterLink": "https://twitter.com/SummitSnow411",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "White Pass Ski Resort",
    "resortWebsite": "https://skiwhitepass.com/",
    "latLong": "46.6373512,-121.3935133",
    "region": "WA",
    "snowConditionLink": "https://skiwhitepass.com/snow-report",
    "uphillPolicy": "No",
    "uphillPolicyLink": "",
    "facebookLink": "https://www.facebook.com/SkiWhitePass",
    "twitterLink": "https://twitter.com/WhitePass",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Loup Loup Ski Bowl",
    "resortWebsite": "https://skitheloup.com/",
    "latLong": "48.3943651,-119.9131587",
    "region": "WA",
    "snowConditionLink": "https://skitheloup.com/conditions/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://skitheloup.com/mountain-safety/",
    "facebookLink": "https://www.facebook.com/LoupLoupBasin/",
    "twitterLink": "",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Anthony Lakes Mountain Resort",
    "resortWebsite": "https://anthonylakes.com/",
    "latLong": "44.9628033,-118.2355979",
    "region": "OR",
    "snowConditionLink": "",
    "uphillPolicy": "No",
    "uphillPolicyLink": "",
    facebookLink: "https://www.facebook.com/anthonylakesmountainresort/",
    twitterLink: "",
    avalancheForecaster: "NWAC",
    avalancheForecasterLink: "https://www.nwac.us/"
  },
  {
    skiResortName: "Cooper Spur",
    resortWebsite: "https://www.cooperspur.com/",
    latLong: "45.4252913,-121.592486",
    region: "OR",
    snowConditionLink: "https://www.cooperspur.com/conditions-report/",
    uphillPolicy: "No",
    uphillPolicyLink: "",
    facebookLink: "https://www.facebook.com/CooperSpur/",
    avalancheForecaster: "NWAC",
    avalancheForecasterLink: "https://www.nwac.us/"
  },
  {
    skiResortName: "Hoodoo Ski Area",
    resortWebsite: "https://skihoodoo.com/",
    region: "OR",
    snowConditionLink: "http://skihoodoo.com/the-mountain/mountain-conditions/",
    uphillPolicy: "Yes",
    uphillPolicyLink: "https://skihoodoo.com/faq/",
    avalancheForecaster: "NWAC",
    avalancheForecasterLink: "https://www.nwac.us/"
  },
  {
    skiResortName: "Mt. Ashland",
    resortWebsite: "http://skihoodoo.com/the-mountain/mountain-conditions/",
    region: "OR",
    snowConditionLink: "https://www.mtashland.com/mountain-report/",
    uphillPolicy: "Yes",
    uphillPolicyLink: "https://www.mtashland.com/uphill-use-policy/",
  },
  {
    skiResortName: "Mt. Bachelor",
    resortWebsite: "https://www.mtbachelor.com/",
    region: "OR",
    snowConditionLink: "https://www.mtbachelor.com/conditions-report/",
    uphillPolicy: "Yes",
    uphillPolicyLink: "https://www.mtbachelor.com/info/uphill-travel/"
  },
  {
    skiResortName: "Mt. Hood Meadows",
    resortWebsite: "https://www.skihood.com/",
    region: "OR",
    snowConditionLink: "https://www.skihood.com/en/the-mountain/conditions",
    uphillPolicy: "Yes",
    uphillPolicyLink: "https://www.skihood.com/en/the-mountain/safety/terrain-management"
  },
  {
    skiResortName: "Mt. Hood Skibowl",
    resortWebsite: "http://www.skibowl.com/",
    region: "OR",
    snowConditionLink: "http://www.skibowl.com/winter/mt-hood-weather-conditions",
    uphillPolicy: "No",
    uphillPolicyLink: ""
  },
  {
    skiResortName: "Sprout Springs",
    resortWebsite: "http://www.spoutspringsskiarea.com/",
    region: "OR",
    snowConditionLink: "",
    uphillPolicy: "No",
    uphillPolicyLink: ""
  },
  {
    skiResortName: "Timberline Lodge",
    resortWebsite: "http://www.timberlinelodge.com/",
    region: "OR",
    snowConditionLink: "http://www.timberlinelodge.com/conditions",
    uphillPolicy: "Yes",
    uphillPolicyLink: "http://www.timberlinelodge.com/mountain/safety"
  },
  {
    skiResortName: "Willamette Pass",
    resortWebsite: "http://www.willamettepass.com/",
    region: "OR",
    snowConditionLink: "",
    uphillPolicy: "No",
    uphillPolicyLink: ""
  },
    {
    "skiResortName": "Bogus Basin",
    "resortWebsite": "https://bogusbasin.org/",
    "region": "ID",
    "snowConditionLink": "https://bogusbasin.org/the-mountain/overview/conditions-webcams/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://bogusbasin.org/restrictions-policies/#uphill"
  },
  {
    "skiResortName": "Brundage Mountain Resort",
    "resortWebsite": "https://brundage.com/",
    "region": "ID",
    "snowConditionLink": "https://brundage.com/on-the-mountain/winter/snow-report/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://brundage.com/on-the-mountain/winter/uphill-travel-policy/"
  },
  {
    "skiResortName": "Kelly Canyon Ski Area",
    "resortWebsite": "https://www.skikelly.com/",
    "region": "ID",
    "snowConditionLink": "https://www.skikelly.com/conditions",
    "uphillPolicy": "No",
    "uphillPolicyLink": ""
  },
  {
    "skiResortName": "Lookout Pass Ski Area",
    "resortWebsite": "https://skilookout.com/",
    "region": "ID",
    "snowConditionLink": "https://skilookout.com/snow-report",
    "uphillPolicy": "No",
    "uphillPolicyLink": ""
  },
  {
    "skiResortName": "Magic Mountain Ski Area",
    "resortWebsite": "https://magicmountainresort.com/",
    "region": "ID",
    "snowConditionLink": "https://magicmountainresort.com/mountain/",
    "uphillPolicy": "No",
    "uphillPolicyLink": ""
  },
  {
    "skiResortName": "Pebble Creek Ski Area",
    "resortWebsite": "https://pebblecreekskiarea.com/",
    "region": "ID",
    "snowConditionLink": "https://pebblecreekskiarea.com/trail-map/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://pebblecreekskiarea.com/policies/"
  },
  {
    "skiResortName": "Pomerelle Mountain Resort",
    "resortWebsite": "http://www.pomerelle.com/",
    "region": "ID",
    "snowConditionLink": "http://www.pomerelle.com/conditions/index.htm",
    "uphillPolicy": "No",
    "uphillPolicyLink": ""
  },
  {
    "skiResortName": "Schweitzer",
    "resortWebsite": "https://www.schweitzer.com/",
    "region": "ID",
    "snowConditionLink": "https://www.schweitzer.com/discover/conditions-report/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://www.schweitzer.com/policies/"
  },
  {
    "skiResortName": "Silver Mountain",
    "resortWebsite": "https://www.silvermt.com/",
    "region": "ID",
    "snowConditionLink": "https://www.silvermt.com/conditions",
    "uphillPolicy": "No",
    "uphillPolicyLink": ""
  },
  {
    "skiResortName": "Soldier Mountain Ski Area",
    "resortWebsite": "https://soldiermountain.com/",
    "region": "ID",
    "snowConditionLink": "https://www.onthesnow.com/idaho/soldier-mountain-ski-area/ski-resort.html",
    "uphillPolicy": "No",
    "uphillPolicyLink": ""
  },
  {
    "skiResortName": "Sun Valley",
    "resortWebsite": "https://www.sunvalley.com/",
    "region": "ID",
    "snowConditionLink": "https://www.sunvalley.com/mountain-snow-report",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://www.sunvalley.com/things-to-do/mountain-safety"
  },
  {
    "skiResortName": "Tamarack Resort",
    "resortWebsite": "https://tamarackidaho.com/",
    "region": "ID",
    "snowConditionLink": "https://tamarackidaho.com/about/snow-report",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://tamarackidaho.com/about/mountain-info"
  }
]

export default {
	name: 'Resorts',
	data () {
		return {
			resorts: RESORTS
		}
	}
}
</script>
