<template>
<div class="container is-half">
	<b-table :data="resorts">
		<template slot-scope="props">
			<b-table-column field="skiResortName" label="Ski Resort" sortable>
				<a :href="props.row.resortWebsite">{{props.row.skiResortName}}</a>
			</b-table-column>
			<b-table-column field="region" label="Region">
				<p>{{props.row.region}}</p>
			</b-table-column>
			<b-table-column field="snowConditionLink" label="Conditions">
				<a :href="props.row.snowConditionLink">Conditions</a>
			</b-table-column>
			<b-table-column field="uphillPolicy" label="Has Uphill Policy?" sortable>
				<p>{{props.row.uphillPolicy}}</p>
			</b-table-column>
			<b-table-column field="uphillPolicy" label="Uphill Policy" sortable>
				<div v-if="props.row.uphillPolicy === 'Yes'">
					<a :href="props.row.uphillPolicyLink">Uphill Policy</a>
				</div>
			</b-table-column>
		</template>
	</b-table>
</div>
</template>

<script>
const RESORTS = [
  {
    "skiResortName": "49 Degrees Mountain Resort",
    "resortWebsite": "https://www.ski49n.com/",
    "latLong": "48.3011315,-117.5647559",
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Nov",
    "closingMonth": "May",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "May",
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
    "region": "PNW",
    "openingMonth": "Dec",
    "closingMonth": "April",
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
    "region": "PNW",
    "openingMonth": "Jan",
    "closingMonth": "April",
    "snowConditionLink": "https://skitheloup.com/conditions/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://skitheloup.com/mountain-safety/",
    "facebookLink": "https://www.facebook.com/LoupLoupBasin/",
    "twitterLink": "",
    "avalancheForecaster": "NWAC",
    "avalancheForecasterLink": "https://www.nwac.us/"
  },
  {
    "skiResortName": "Bogus Basin",
    "resortWebsite": "https://bogusbasin.org/",
    "latLong": "43.764086,-116.1201264",
    "region": "Rocky",
    "openingMonth": "Dec",
    "closingMonth": "Mar",
    "snowConditionLink": "https://bogusbasin.org/the-mountain/overview/conditions-webcams/",
    "uphillPolicy": "Yes",
    "uphillPolicyLink": "https://bogusbasin.org/restrictions-policies/#uphill",
    "facebookLink": "https://www.facebook.com/BogusBasinIdaho",
    "twitterLink": "https://twitter.com/bogusbasin",
    "avalancheForecaster": "IPAC",
    "avalancheForecasterLink": "https://www.idahopanhandleavalanche.org/"
  }
]

export default {
	name: 'HelloWorld',
	data () {
		return {
			resorts: RESORTS
		}
	}
}
</script>
