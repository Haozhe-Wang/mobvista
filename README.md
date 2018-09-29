#DATA SCHEME
##介绍
程序实现结构体的合并，将大数据的结构提取出来并根据key来进行合并。实现的源代码为get5.py.其中有一些对error type found的判断就目前来看没有用，是曾经想要标记出有多个结构类型的key所用。可后来取消了对其的标记。
***
以下内容将显示出各种数据的所有数据结构。分别通过json结构输出和通过我自定义的一种格式输出。

***
##输出格式说明
---
###格式一
```
格式一以同级对齐的方式输出。而每个json将被{}所包裹，json中的key单独一行，并以:结尾，而数据类型永远在key下，并列的数据类型表明不同的数据在这个key下存储了不一致的数据类型，而被[]包裹的不同数据类型，表明同一个数据下这个key是一个list型的数据。而空的[]表明这个key下没有数据，就是一个空的list。而有些key有的有数据有的为[]，则不会输出[].同时也存在[[]]，即嵌套的list结构.有些key下的值是list结构和json结构并列，意思就是不同的数据在这个key下，有的为list型，有的为json型.
```
###格式二
```
格式二没有任何空行，是数据合并后的原始输出。因为格式一是根据数据二的基础上，根据视觉需要，进行的输出调整。最大的三个不同是:
**1.数据二没有空行**
**2.数据二可以得知哪些key错在，不同的数据下这个key可能有值也可能为空list的情况**
**3.数据二下的每个key的值都被一个不属于原始值的list所包裹，目的是为了能存放多个不同的数据结构。所以数据二会比数据一多一个外层list**
***
##结构输出
---
###Campaign:
```
 {
 _id :
	 <class 'bson.objectid.ObjectId'>
 campaignId :
	 <class 'bson.int64.Int64'>
 advertiserId :
	 <class 'bson.int64.Int64'>
 name :
	 <class 'str'>
 platform :
	 <class 'bson.int64.Int64'>
 trackingUrl :
	 <class 'str'>
 directUrl :
	 <class 'str'>
 totalBudget :
	 <class 'bson.int64.Int64'>
 dailyBudget :
	 <class 'bson.int64.Int64'>
 dailyNum :
	 <class 'bson.int64.Int64'>
 price :
	 <class 'float'>
 startTime :
	 <class 'bson.int64.Int64'>
 endTime :
	 <class 'bson.int64.Int64'>
 countryCode :
		 [
		 <class 'str'>
		 ]
 status :
	 <class 'bson.int64.Int64'>
 created :
	 <class 'bson.int64.Int64'>
 weight :
	 <class 'bson.int64.Int64'>
 network :
	 <class 'bson.int64.Int64'>
 previewUrl :
	 <class 'str'>
 packageName :
	 <class 'str'>
 campaignType :
	 <class 'bson.int64.Int64'>
 specialType :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 ctype :
	 <class 'bson.int64.Int64'>
 networkCid :
	 <class 'str'>
 agentAd :
	 <class 'bson.int64.Int64'>
 mnc :
	 []
 deviceModel :
		 [
		 <class 'str'>
		 ]
 mobileTraffic :
	 []
 hours :
	 []
 osVersion :
		 [
		 <class 'str'>
		 ]
 osVersionMin :
	 <class 'bson.int64.Int64'>
 osVersionMax :
	 <class 'bson.int64.Int64'>
 appName :
	 <class 'str'>
 appDesc :
	 <class 'str'>
 iconUrl :
	 <class 'str'>
 appSize :
	 <class 'str'>
 appScore :
	 <class 'float'>
 appInstall :
	 <class 'bson.int64.Int64'>
 direct :
	 <class 'bson.int64.Int64'>
 tag :
	 <class 'bson.int64.Int64'>
 adSourceId :
	 <class 'bson.int64.Int64'>
 category :
	 <class 'bson.int64.Int64'>
 publisherId :
	 <class 'bson.int64.Int64'>
 preClick :
	 <class 'bool'>
 frequencyCap :
	 <class 'bson.int64.Int64'>
 updated :
	 <class 'bson.int64.Int64'>
 updatedDate :
	 <class 'str'>
 directPackageName :
	 <class 'str'>
 creative :
		 {
		 campaignId :
			 <class 'bson.int64.Int64'>
		 creativeId :
			 <class 'bson.int64.Int64'>
		 lang :
			 <class 'bson.int64.Int64'>
		 type :
			 <class 'bson.int64.Int64'>
		 width :
			 <class 'bson.int64.Int64'>
		 height :
			 <class 'bson.int64.Int64'>
		 imageSize :
			 <class 'str'>
		 name :
			 <class 'str'>
		 imageUrl :
			 <class 'str'>
		 comment :
			 <class 'str'>
		 creativeCta :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 tag :
			 <class 'bson.int64.Int64'>
		 created :
			 <class 'bson.int64.Int64'>
		 resourceType :
			 <class 'bson.int64.Int64'>
		 mime :
				 [
				 <class 'str'>
				 ]
		 attribute :
			 []
		 templateType :
			 <class 'bson.int64.Int64'>
		 tagCode :
			 <class 'str'>
		 showType :
			 <class 'bson.int64.Int64'>
		 imageSizeId :
			 <class 'bson.int64.Int64'>
		 textVideo :
				 {
				 videoLength :
					 <class 'bson.int64.Int64'>
				 }
				 {
				 videoSize :
					 <class 'bson.int64.Int64'>
				 }
				 {
				 videoResolution :
					 <class 'str'>
				 }
				 {
				 watchMile :
					 <class 'bson.int64.Int64'>
				 }
		 videoUrlEncode :
			 <class 'str'>
		 videoUrl :
			 <class 'str'>
		 }
 imageSize :
		 [
		 <class 'str'>
		 ]
 imageSizeId :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 apkUrl :
	 <class 'str'>
 appWhiteList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 appBlackList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 mobileCode :
		 [
		 <class 'str'>
		 ]
 networkType :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 reduceRuleAdv :
	 []
 landingType :
	 <class 'bson.int64.Int64'>
 sdkPackageName :
	 <class 'str'>
 oriPrice :
	 <class 'float'>
 ctatext :
	 <class 'str'>
 preClickRate :
	 {
	 default :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 version :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 }
 preClickCacheTime :
	 <class 'bson.int64.Int64'>
 excludeRule :
	 {
	 grades :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 includeAppIds :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 excludeAppIds :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 status :
		 <class 'bson.int64.Int64'>
	 type :
		 <class 'bson.int64.Int64'>
	 }
 sdkDetect :
	 {
	 jumpCount :
		 <class 'bson.int64.Int64'>
	 success :
		 <class 'bson.int64.Int64'>
	 }
 budgetFirst :
	 <class 'bool'>
 gaid_idfa_needs :
	 <class 'bson.int64.Int64'>
 cityCode :
		 {
		 IN :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 CN :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 SA :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 BR :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 US :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 FR :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
 tImp :
	 <class 'bson.int64.Int64'>
 advImp :
	 []
 adUrlList :
		 [
		 <class 'str'>
		 ]
 jumpType :
	 <class 'bson.int64.Int64'>
 targetPackageNames :
	 []
 isNoPayment :
	 <class 'bson.int64.Int64'>
 newVersion :
	 <class 'str'>
 bt :
	 {
	 subIds :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
	 percent :
		 <class 'float'>
	 status :
		 <class 'bson.int64.Int64'>
	 }
 contentRating :
	 <class 'bson.int64.Int64'>
 subCategoryId :
	 <class 'bson.int64.Int64'>
 system :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 deviceType :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 inventory :
		 [
		 <class 'str'>
		 ]
 deviceId :
	 <class 'str'>
 btV2 :
	 {
	 subIds :
			 {
			 <class 'int'> :
				 <class 'bson.int64.Int64'>
			 }
	 btClass :
		 {
		 <class 'int'> :
			 {
			 percent :
				 <class 'float'>
				 <class 'bson.int64.Int64'>
			 capMargin :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 vbaConnecting :
	 <class 'bson.int64.Int64'>
 vbaTrackingLink :
	 <class 'str'>
 trafficType :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 inventoryV2 :
	 {
	 type :
		 <class 'bson.int64.Int64'>
	 adnAdtype :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 app_site :
		 []
	 iabCategory :
		 {
		 IAB7 :
				 [
				 <class 'str'>
				 ]
		 IAB1 :
			 []
		 IAB9 :
			 []
		 IAB18 :
			 []
		 IAB20 :
			 []
		 IAB22 :
			 []
		 IAB5 :
			 []
		 IAB6 :
			 []
		 IAB8 :
			 []
		 IAB10 :
			 []
		 IAB16 :
			 []
		 IAB14 :
			 []
		 IAB3 :
			 []
		 IAB12 :
			 []
		 IAB2 :
			 []
		 }
	 }
 userInterest :
	 {
	 ALL :
		 []
	 Shopping :
		 []
	 Beauty :
		 []
	 Food & Drink :
		 []
	 Social :
		 []
	 Travel :
		 []
	 News & Magazines :
		 []
	 Video :
		 []
	 Games :
			 [
			 <class 'str'>
			 ]
	 Entertainment :
		 []
	 Lifestyle :
		 []
	 Music :
		 []
	 Personalization :
		 []
	 Photography :
		 []
	 Productivity :
		 []
	 Tools :
		 []
	 Art & Design :
		 []
	 Communication :
		 []
	 Dating :
		 []
	 Education :
		 []
	 Family :
		 []
	 Health & Fitness :
		 []
	 Sports :
		 []
	 Business :
		 []
	 Finance :
		 []
	 Comics :
		 []
	 Books & Reference :
		 []
	 Sticker :
		 []
	 Events :
		 []
	 Libraries & Demo :
		 []
	 }
 gender :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 ttcCt2 :
	 <class 'bson.int64.Int64'>
 nxAdvName :
	 <class 'str'>
 retargetingDevice :
	 <class 'bson.int64.Int64'>
 sendDeviceidRate :
	 <class 'bson.int64.Int64'>
 blackSubidList :
	 {
	 <class 'int'> :
		 <class 'str'>
	 }
 advOfferName :
	 <class 'str'>
 userAge :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 adSchedule :
	 {
	 -2 :
		 []
	 -1 :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 <class 'int'> :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 }
 osVersionMinV2 :
	 <class 'bson.int64.Int64'>
 osVersionMaxV2 :
	 <class 'bson.int64.Int64'>
 inventoryBlackList :
		 [
		 <class 'str'>
		 ]
 retargetOffer :
	 <class 'bson.int64.Int64'>
 vtaJump :
	 <class 'bson.int64.Int64'>
 blackSubidListV2 :
	 {
	 <class 'int'> :
		 {
		 <class 'int'> :
			 <class 'str'>
		 }
	 }
 btV3 :
	 {
	 subIds :
			 {
			 <class 'int'> :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 packageName :
					 <class 'str'>
				 dspSubIds :
					 []
				 }
			 }
			 {
			 <class 'int'> :
					 {
					 dspSubIds :
							 {
							 <class 'int'> :
									 {
									 rate :
										 <class 'bson.int64.Int64'>
									 }
							 }
					 }
			 }
			 {
			 <class 'int'> :
					 {
					 dspSubIds :
							 {
							 <class 'int'> :
									 {
									 packageName :
										 <class 'str'>
									 }
							 }
					 }
			 }
	 btClass :
		 {
		 <class 'int'> :
			 {
			 percent :
				 <class 'bson.int64.Int64'>
				 <class 'float'>
			 capMargin :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 belongType :
	 <class 'bson.int64.Int64'>
 openType :
	 <class 'bson.int64.Int64'>
 iabCategory :
	 {
	 IAB22 :
		 []
	 IAB1 :
			 [
			 <class 'str'>
			 ]
	 IAB10 :
		 []
	 IAB14 :
		 []
	 IAB20 :
		 []
	 IAB24 :
		 []
	 IAB8 :
		 []
	 IAB17 :
		 []
	 IAB9 :
		 []
	 IAB3 :
		 []
	 IAB2 :
		 []
	 IAB11 :
		 []
	 IAB12 :
		 []
	 IAB19 :
		 []
	 IAB13 :
		 []
	 IAB6 :
		 []
	 IAB5 :
		 []
	 IAB21 :
		 []
	 IAB18 :
		 []
	 IAB15 :
		 []
	 IAB7 :
		 []
	 }
 mInventoryV2 :
	 {
	 type :
		 <class 'bson.int64.Int64'>
	 adnAdtype :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 units :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 iabCategory :
		 {
		 IAB7 :
				 [
				 <class 'str'>
				 ]
		 IAB1 :
			 []
		 IAB9 :
			 []
		 IAB18 :
			 []
		 IAB20 :
			 []
		 IAB22 :
			 []
		 IAB5 :
			 []
		 IAB6 :
			 []
		 IAB8 :
			 []
		 IAB10 :
			 []
		 IAB16 :
			 []
		 IAB14 :
			 []
		 IAB3 :
			 []
		 IAB12 :
			 []
		 IAB2 :
			 []
		 }
	 }
 dailyCap :
	 <class 'bson.int64.Int64'>
 promotionType :
	 <class 'bson.int64.Int64'>
 networkTypeV2 :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 deviceTypeV2 :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 genderV2 :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 userAgeV2 :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 subCategoryV2 :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 subCategoryName :
		 [
		 <class 'str'>
		 ]
 jumpParam :
	 {
	 b2t :
		 <class 'bson.int64.Int64'>
	 b2tStatus :
		 <class 'bson.int64.Int64'>
	 noDeviceId :
		 <class 'bson.int64.Int64'>
	 noDeviceIdStatus :
		 <class 'bson.int64.Int64'>
	 }
 isCampaignCreative :
	 <class 'bson.int64.Int64'>
 detectedSwitch1 :
	 <class 'bson.int64.Int64'>
 detectedSwitch2 :
	 <class 'bson.int64.Int64'>
 reduceRuleV2 :
	 {
	 app :
		 {
		 <class 'int'> :
			 {
			 <class 'int'> :
				 {
				 priority :
					 <class 'bson.int64.Int64'>
				 install :
					 <class 'bson.int64.Int64'>
				 price :
					 <class 'bson.int64.Int64'>
				 status :
					 <class 'bson.int64.Int64'>
				 start :
					 <class 'bson.int64.Int64'>
				 }
			 }
		 }
	 grade :
		 {
		 <class 'int'> :
			 {
			 <class 'int'> :
				 {
				 priority :
					 <class 'bson.int64.Int64'>
				 install :
					 <class 'bson.int64.Int64'>
				 price :
					 <class 'bson.int64.Int64'>
				 status :
					 <class 'bson.int64.Int64'>
				 start :
					 <class 'bson.int64.Int64'>
				 }
			 }
		 }
	 }
 costTotalBudget :
	 <class 'bson.int64.Int64'>
 costDailyBudget :
	 <class 'bson.int64.Int64'>
 costDailyCap :
	 <class 'bson.int64.Int64'>
 source :
	 <class 'bson.int64.Int64'>
 costType :
	 <class 'bson.int64.Int64'>
 preClickSwitch :
	 <class 'bool'>
 endcard :
	 {
	 ALL :
		 {
		 urls :
				 {
				 id :
					 <class 'bson.int64.Int64'>
				 url :
					 <class 'str'>
				 url_v2 :
					 <class 'str'>
				 weight :
					 <class 'bson.int64.Int64'>
				 }
		 status :
			 <class 'bson.int64.Int64'>
		 orientation :
			 <class 'bson.int64.Int64'>
		 videoTemplateUrl :
			 []
		 }
	 <class 'int'> :
		 {
		 urls :
				 {
				 id :
					 <class 'bson.int64.Int64'>
				 url :
					 <class 'str'>
				 url_v2 :
					 <class 'str'>
				 weight :
					 <class 'bson.int64.Int64'>
				 }
		 status :
			 <class 'bson.int64.Int64'>
		 orientation :
			 <class 'bson.int64.Int64'>
		 videoTemplateUrl :
			 None 

		 }
	 }
 btBlackList :
	 {
	 apps :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 status :
		 <class 'bson.int64.Int64'>
	 }
 reduceRule :
	 {
	 app :
		 {
		 <class 'int'> :
			 {
			 priority :
				 <class 'bson.int64.Int64'>
			 install :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 start :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 grade :
		 {
		 <class 'int'> :
			 {
			 priority :
				 <class 'bson.int64.Int64'>
			 install :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 start :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 ttcType :
	 <class 'bson.int64.Int64'>
 configVBA :
	 {
	 useVBA :
		 <class 'bson.int64.Int64'>
	 frequencyCap :
		 <class 'bson.int64.Int64'>
	 status :
		 <class 'bson.int64.Int64'>
	 }
 saBt :
	 <class 'bson.int64.Int64'>
 JUMP_TYPE_CONFIG :
	 {
	 <class 'int'> :
		 <class 'float'>
	 }
 deviceModelV2 :
	 {
	 apple :
			 [
			 <class 'str'>
			 ]
	 }
 appPostList :
	 {
	 include :
			 [
			 <class 'str'>
			 ]
	 exclude :
		 []
	 }
 }
```

```
{'_id': [<class 'bson.objectid.ObjectId'>], 'campaignId': [<class 'bson.int64.Int64'>], 'advertiserId': [<class 'bson.int64.Int64'>], 'name': [<class 'str'>], 'platform': [<class 'bson.int64.Int64'>], 'trackingUrl': [<class 'str'>], 'directUrl': [<class 'str'>], 'totalBudget': [<class 'bson.int64.Int64'>], 'dailyBudget': [<class 'bson.int64.Int64'>], 'dailyNum': [<class 'bson.int64.Int64'>], 'price': [<class 'float'>], 'startTime': [<class 'bson.int64.Int64'>], 'endTime': [<class 'bson.int64.Int64'>], 'countryCode': [[<class 'str'>], []], 'status': [<class 'bson.int64.Int64'>], 'created': [<class 'bson.int64.Int64'>], 'weight': [<class 'bson.int64.Int64'>], 'network': [<class 'bson.int64.Int64'>], 'previewUrl': [<class 'str'>], 'packageName': [<class 'str'>], 'campaignType': [<class 'bson.int64.Int64'>], 'specialType': [[<class 'bson.int64.Int64'>]], 'ctype': [<class 'bson.int64.Int64'>], 'networkCid': [<class 'str'>], 'agentAd': [<class 'bson.int64.Int64'>], 'mnc': [[]], 'deviceModel': [[<class 'str'>]], 'mobileTraffic': [[]], 'hours': [[]], 'osVersion': [[<class 'str'>]], 'osVersionMin': [<class 'bson.int64.Int64'>], 'osVersionMax': [<class 'bson.int64.Int64'>], 'appName': [<class 'str'>], 'appDesc': [<class 'str'>], 'iconUrl': [<class 'str'>], 'appSize': [<class 'str'>], 'appScore': [<class 'float'>], 'appInstall': [<class 'bson.int64.Int64'>], 'direct': [<class 'bson.int64.Int64'>], 'tag': [<class 'bson.int64.Int64'>], 'adSourceId': [<class 'bson.int64.Int64'>], 'category': [<class 'bson.int64.Int64'>], 'publisherId': [<class 'bson.int64.Int64'>], 'preClick': [<class 'bool'>], 'frequencyCap': [<class 'bson.int64.Int64'>], 'updated': [<class 'bson.int64.Int64'>], 'updatedDate': [<class 'str'>], 'directPackageName': [<class 'str'>], 'creative': [{'campaignId': [<class 'bson.int64.Int64'>], 'creativeId': [<class 'bson.int64.Int64'>], 'lang': [<class 'bson.int64.Int64'>], 'type': [<class 'bson.int64.Int64'>], 'width': [<class 'bson.int64.Int64'>], 'height': [<class 'bson.int64.Int64'>], 'imageSize': [<class 'str'>], 'name': [<class 'str'>], 'imageUrl': [<class 'str'>], 'comment': [<class 'str'>], 'creativeCta': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'tag': [<class 'bson.int64.Int64'>], 'created': [<class 'bson.int64.Int64'>], 'resourceType': [<class 'bson.int64.Int64'>], 'mime': [[], [<class 'str'>]], 'attribute': [[]], 'templateType': [<class 'bson.int64.Int64'>], 'tagCode': [<class 'str'>], 'showType': [<class 'bson.int64.Int64'>], 'imageSizeId': [<class 'bson.int64.Int64'>], 'textVideo': [{'videoLength': [<class 'bson.int64.Int64'>]}, {'videoSize': [<class 'bson.int64.Int64'>]}, {'videoResolution': [<class 'str'>]}, {'watchMile': [<class 'bson.int64.Int64'>]}], 'videoUrlEncode': [<class 'str'>], 'videoUrl': [<class 'str'>]}], 'imageSize': [[<class 'str'>]], 'imageSizeId': [[<class 'bson.int64.Int64'>]], 'apkUrl': [<class 'str'>], 'appWhiteList': [[], [<class 'bson.int64.Int64'>]], 'appBlackList': [[<class 'bson.int64.Int64'>], []], 'mobileCode': [[<class 'str'>]], 'networkType': [[<class 'bson.int64.Int64'>]], 'reduceRuleAdv': [[]], 'landingType': [<class 'bson.int64.Int64'>], 'sdkPackageName': [<class 'str'>], 'oriPrice': [<class 'float'>], 'ctatext': [<class 'str'>], 'preClickRate': {'default': [[<class 'bson.int64.Int64'>]], 'version': [[<class 'bson.int64.Int64'>]]}, 'preClickCacheTime': [<class 'bson.int64.Int64'>], 'excludeRule': {'grades': [[<class 'bson.int64.Int64'>], []], 'includeAppIds': [[], [<class 'bson.int64.Int64'>]], 'excludeAppIds': [[<class 'bson.int64.Int64'>], []], 'status': [<class 'bson.int64.Int64'>], 'type': [<class 'bson.int64.Int64'>]}, 'sdkDetect': {'jumpCount': [<class 'bson.int64.Int64'>], 'success': [<class 'bson.int64.Int64'>]}, 'budgetFirst': [<class 'bool'>], 'gaid_idfa_needs': [<class 'bson.int64.Int64'>], 'cityCode': [[], {'IN': [[<class 'bson.int64.Int64'>]]}, {'CN': [[<class 'bson.int64.Int64'>]]}, {'SA': [[<class 'bson.int64.Int64'>]]}, {'BR': [[<class 'bson.int64.Int64'>]]}, {'US': [[<class 'bson.int64.Int64'>]]}, {'FR': [[<class 'bson.int64.Int64'>]]}], 'tImp': [<class 'bson.int64.Int64'>], 'advImp': [[]], 'adUrlList': [[], [<class 'str'>]], 'jumpType': [<class 'bson.int64.Int64'>], 'targetPackageNames': [[]], 'isNoPayment': [<class 'bson.int64.Int64'>], 'newVersion': [<class 'str'>], 'bt': {'subIds': {"<class 'int'>": [<class 'bson.int64.Int64'>]}, 'percent': [<class 'float'>], 'status': [<class 'bson.int64.Int64'>]}, 'contentRating': [<class 'bson.int64.Int64'>], 'subCategoryId': [<class 'bson.int64.Int64'>], 'system': [[<class 'bson.int64.Int64'>]], 'deviceType': [[<class 'bson.int64.Int64'>]], 'inventory': [[<class 'str'>]], 'deviceId': [<class 'str'>], 'btV2': {'subIds': [{"<class 'int'>": [<class 'bson.int64.Int64'>]}, []], 'btClass': {"<class 'int'>": {'percent': [<class 'float'>, <class 'bson.int64.Int64'>], 'capMargin': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}}, 'vbaConnecting': [<class 'bson.int64.Int64'>], 'vbaTrackingLink': [<class 'str'>], 'trafficType': [[<class 'bson.int64.Int64'>]], 'inventoryV2': {'type': [<class 'bson.int64.Int64'>], 'adnAdtype': [[], [<class 'bson.int64.Int64'>]], 'app_site': [[]], 'iabCategory': {'IAB7': [[<class 'str'>]], 'IAB1': [[]], 'IAB9': [[]], 'IAB18': [[]], 'IAB20': [[]], 'IAB22': [[]], 'IAB5': [[]], 'IAB6': [[]], 'IAB8': [[]], 'IAB10': [[]], 'IAB16': [[]], 'IAB14': [[]], 'IAB3': [[]], 'IAB12': [[]], 'IAB2': [[]]}}, 'userInterest': {'ALL': [[]], 'Shopping': [[]], 'Beauty': [[]], 'Food & Drink': [[]], 'Social': [[]], 'Travel': [[]], 'News & Magazines': [[]], 'Video': [[]], 'Games': [[], [<class 'str'>]], 'Entertainment': [[]], 'Lifestyle': [[]], 'Music': [[]], 'Personalization': [[]], 'Photography': [[]], 'Productivity': [[]], 'Tools': [[]], 'Art & Design': [[]], 'Communication': [[]], 'Dating': [[]], 'Education': [[]], 'Family': [[]], 'Health & Fitness': [[]], 'Sports': [[]], 'Business': [[]], 'Finance': [[]], 'Comics': [[]], 'Books & Reference': [[]], 'Sticker': [[]], 'Events': [[]], 'Libraries & Demo': [[]]}, 'gender': [[<class 'bson.int64.Int64'>]], 'ttcCt2': [<class 'bson.int64.Int64'>], 'nxAdvName': [<class 'str'>], 'retargetingDevice': [<class 'bson.int64.Int64'>], 'sendDeviceidRate': [<class 'bson.int64.Int64'>], 'blackSubidList': {"<class 'int'>": [<class 'str'>]}, 'advOfferName': [<class 'str'>], 'userAge': [[<class 'bson.int64.Int64'>]], 'adSchedule': {'-2': [[]], '-1': [[<class 'bson.int64.Int64'>]], "<class 'int'>": [[<class 'bson.int64.Int64'>]]}, 'osVersionMinV2': [<class 'bson.int64.Int64'>], 'osVersionMaxV2': [<class 'bson.int64.Int64'>], 'inventoryBlackList': [[], [<class 'str'>]], 'retargetOffer': [<class 'bson.int64.Int64'>], 'vtaJump': [<class 'bson.int64.Int64'>], 'blackSubidListV2': {"<class 'int'>": {"<class 'int'>": [<class 'str'>]}}, 'btV3': {'subIds': [{"<class 'int'>": {'rate': [<class 'bson.int64.Int64'>], 'packageName': [<class 'str'>], 'dspSubIds': [[]]}}, [], {"<class 'int'>": [{'dspSubIds': [{"<class 'int'>": [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'dspSubIds': [{"<class 'int'>": [{'packageName': [<class 'str'>]}]}]}]}], 'btClass': {"<class 'int'>": {'percent': [<class 'bson.int64.Int64'>, <class 'float'>], 'capMargin': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}}, 'belongType': [<class 'bson.int64.Int64'>], 'openType': [<class 'bson.int64.Int64'>], 'iabCategory': {'IAB22': [[]], 'IAB1': [[], [<class 'str'>]], 'IAB10': [[]], 'IAB14': [[]], 'IAB20': [[]], 'IAB24': [[]], 'IAB8': [[]], 'IAB17': [[]], 'IAB9': [[]], 'IAB3': [[]], 'IAB2': [[]], 'IAB11': [[]], 'IAB12': [[]], 'IAB19': [[]], 'IAB13': [[]], 'IAB6': [[]], 'IAB5': [[]], 'IAB21': [[]], 'IAB18': [[]], 'IAB15': [[]], 'IAB7': [[]]}, 'mInventoryV2': {'type': [<class 'bson.int64.Int64'>], 'adnAdtype': [[], [<class 'bson.int64.Int64'>]], 'units': [[], [<class 'bson.int64.Int64'>]], 'iabCategory': {'IAB7': [[<class 'str'>]], 'IAB1': [[]], 'IAB9': [[]], 'IAB18': [[]], 'IAB20': [[]], 'IAB22': [[]], 'IAB5': [[]], 'IAB6': [[]], 'IAB8': [[]], 'IAB10': [[]], 'IAB16': [[]], 'IAB14': [[]], 'IAB3': [[]], 'IAB12': [[]], 'IAB2': [[]]}}, 'dailyCap': [<class 'bson.int64.Int64'>], 'promotionType': [<class 'bson.int64.Int64'>], 'networkTypeV2': [[<class 'bson.int64.Int64'>]], 'deviceTypeV2': [[<class 'bson.int64.Int64'>]], 'genderV2': [[<class 'bson.int64.Int64'>]], 'userAgeV2': [[<class 'bson.int64.Int64'>]], 'subCategoryV2': [[<class 'bson.int64.Int64'>]], 'subCategoryName': [[<class 'str'>]], 'jumpParam': {'b2t': [<class 'bson.int64.Int64'>], 'b2tStatus': [<class 'bson.int64.Int64'>], 'noDeviceId': [<class 'bson.int64.Int64'>], 'noDeviceIdStatus': [<class 'bson.int64.Int64'>]}, 'isCampaignCreative': [<class 'bson.int64.Int64'>], 'detectedSwitch1': [<class 'bson.int64.Int64'>], 'detectedSwitch2': [<class 'bson.int64.Int64'>], 'reduceRuleV2': {'app': {"<class 'int'>": {"<class 'int'>": {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'price': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}}}, 'grade': {"<class 'int'>": {"<class 'int'>": {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'price': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}}}}, 'costTotalBudget': [<class 'bson.int64.Int64'>], 'costDailyBudget': [<class 'bson.int64.Int64'>], 'costDailyCap': [<class 'bson.int64.Int64'>], 'source': [<class 'bson.int64.Int64'>], 'costType': [<class 'bson.int64.Int64'>], 'preClickSwitch': [<class 'bool'>], 'endcard': {'ALL': {'urls': [{'id': [<class 'bson.int64.Int64'>], 'url': [<class 'str'>], 'url_v2': [<class 'str'>], 'weight': [<class 'bson.int64.Int64'>]}], 'status': [<class 'bson.int64.Int64'>], 'orientation': [<class 'bson.int64.Int64'>], 'videoTemplateUrl': [[]]}, "<class 'int'>": {'urls': [{'id': [<class 'bson.int64.Int64'>], 'url': [<class 'str'>], 'url_v2': [<class 'str'>], 'weight': [<class 'bson.int64.Int64'>]}, []], 'status': [<class 'bson.int64.Int64'>], 'orientation': [<class 'bson.int64.Int64'>], 'videoTemplateUrl': None}}, 'btBlackList': {'apps': [[<class 'bson.int64.Int64'>]], 'status': [<class 'bson.int64.Int64'>]}, 'reduceRule': {'app': {"<class 'int'>": {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}}, 'grade': {"<class 'int'>": {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}}}, 'ttcType': [<class 'bson.int64.Int64'>], 'configVBA': {'useVBA': [<class 'bson.int64.Int64'>], 'frequencyCap': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'saBt': [<class 'bson.int64.Int64'>], 'JUMP_TYPE_CONFIG': {"<class 'int'>": [<class 'float'>]}, 'deviceModelV2': {'apple': [[<class 'str'>], []]}, 'appPostList': {'include': [[<class 'str'>]], 'exclude': [[]]}}
```

---
###App:
```
 {
 _id :
	 <class 'bson.objectid.ObjectId'>
 appId :
	 <class 'bson.int64.Int64'>
	 <class 'int'>
 publisher :
	 {
	 publisherId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 username :
		 <class 'str'>
	 status :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 apiKey :
		 <class 'str'>
	 type :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 mvSourceStatus :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 forceDeviceId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 blockCategory :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 created :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 blockCategoryV2 :
			 [
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'int'>
			 ]
	 }
 app :
	 {
	 appId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 publisherId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 grade :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 name :
		 <class 'str'>
	 platform :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 directMarket :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 campaignType :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 desc :
		 <class 'str'>
	 created :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 status :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 custom :
		 []
	 postback :
		 <class 'str'>
	 postbackUrl :
		 <class 'str'>
	 devinfoEncrypt :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 plct :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 plctb :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 nativexAppId :
		 <class 'str'>
	 nativexApiKey :
		 <class 'str'>
	 applovinSdkKey :
		 <class 'str'>
	 applovinReportKey :
		 <class 'str'>
	 isIncent :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 allowBlend :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 apkChance :
			 {
			 ALL :
				 <class 'int'>
				 <class 'bson.int64.Int64'>
			 }
	 offerPreference :
			 [
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'int'>
			 ]
	 contentPreference :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 btClass :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 category :
		 <class 'str'>
	 iabCategory :
			 [
			 <class 'str'>
			 ]
	 subCategory :
			 [
			 <class 'str'>
			 ]
	 trafficType :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 vtaRelatedUnitId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 vtaRelatedAppId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 rushSetting :
		 {
		 pc :
			 <class 'bson.int64.Int64'>
			 <class 'int'>
		 sdkrush :
			 <class 'bson.int64.Int64'>
			 <class 'int'>
		 }
	 rushUnits :
		 <class 'NoneType'>
			 {
			 <class 'int'> :
				 <class 'int'>
				 <class 'bson.int64.Int64'>
			 }
	 frequencyCap :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 subCategoryV2 :
			 [
			 <class 'str'>
			 ]
	 domain :
		 <class 'str'>
	 domain_verify :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 iabSubCategory :
		 {
		 IAB1 :
				 [
				 <class 'str'>
				 ]
		 IAB2 :
				 [
				 <class 'str'>
				 ]
		 IAB3 :
				 [
				 <class 'str'>
				 ]
		 IAB4 :
				 [
				 <class 'str'>
				 ]
		 IAB5 :
				 [
				 <class 'str'>
				 ]
		 IAB6 :
				 [
				 <class 'str'>
				 ]
		 IAB7 :
				 [
				 <class 'str'>
				 ]
		 IAB8 :
				 [
				 <class 'str'>
				 ]
		 IAB9 :
				 [
				 <class 'str'>
				 ]
		 IAB10 :
				 [
				 <class 'str'>
				 ]
		 IAB11 :
				 [
				 <class 'str'>
				 ]
		 IAB12 :
				 [
				 <class 'str'>
				 ]
		 IAB13 :
				 [
				 <class 'str'>
				 ]
		 IAB14 :
				 [
				 <class 'str'>
				 ]
		 IAB15 :
				 [
				 <class 'str'>
				 ]
		 IAB16 :
				 [
				 <class 'str'>
				 ]
		 IAB17 :
				 [
				 <class 'str'>
				 ]
		 IAB18 :
				 [
				 <class 'str'>
				 ]
		 IAB19 :
				 [
				 <class 'str'>
				 ]
		 IAB20 :
				 [
				 <class 'str'>
				 ]
		 IAB21 :
				 [
				 <class 'str'>
				 ]
		 IAB22 :
				 [
				 <class 'str'>
				 ]
		 IAB23 :
				 [
				 <class 'str'>
				 ]
		 IAB24 :
				 [
				 <class 'str'>
				 ]
		 IAB25 :
				 [
				 <class 'str'>
				 ]
		 IAB26 :
				 [
				 <class 'str'>
				 ]
		 }
	 iabCategoryV2 :
		 {
		 IAB1 :
			 []
		 IAB9 :
			 []
		 IAB18 :
			 []
		 IAB3 :
			 []
		 IAB2 :
			 []
		 IAB22 :
			 []
		 IAB19 :
			 []
		 IAB24 :
			 []
		 IAB11 :
			 []
		 IAB12 :
			 []
		 IAB14 :
			 []
		 IAB10 :
			 []
		 IAB7 :
			 []
		 IAB5 :
			 []
		 IAB6 :
			 []
		 IAB15 :
			 []
		 IAB20 :
			 []
		 IAB13 :
			 []
		 IAB8 :
			 []
		 IAB17 :
			 []
		 }
	 coppa :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 }
 sspCampaignIds :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 allowIp :
		 [
		 <class 'str'>
		 ]
 publisherId :
	 <class 'bson.int64.Int64'>
	 <class 'int'>
 blackList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
 whiteList :
	 []
 postbackM :
	 <class 'bson.int64.Int64'>
 blackPackageNameList :
		 [
		 <class 'str'>
		 ]
 excludeAdvertiserIds :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 campaignFields :
		 [
		 <class 'str'>
		 ]
 excludeSpecialType :
	 []
 updated :
	 <class 'bson.int64.Int64'>
	 <class 'int'>
 updatedDate :
	 <class 'str'>
 rewards :
		 {
		 id :
			 <class 'bson.int64.Int64'>
		 name :
			 <class 'str'>
		 amount :
			 <class 'bson.int64.Int64'>
		 }
 setting :
	 {
	 plct :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 plctb :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 cfb :
		 <class 'bool'>
	 hideVersion :
			 [
			 <class 'str'>
			 ]
	 hideLoad :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 shuffleVersion :
			 [
			 <class 'str'>
			 ]
	 wreq :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 dlct :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 vcct :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 jumpType :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 openType :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 dlrf :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 dlrfct :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 pcct :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 storekit :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 }
 appsetting :
	 {
	 pcto :
		 <class 'bson.int64.Int64'>
	 tcto :
		 <class 'bson.int64.Int64'>
	 pcrn :
		 <class 'bson.int64.Int64'>
	 uplc :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 upmi :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 upaid :
		 <class 'bson.int64.Int64'>
	 n2 :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 n3 :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 n4 :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 tcct :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 t_vba :
			 [
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'float'>
			 ]
	 jumptBw :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 crashCt :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 ats_c :
		 <class 'bson.int64.Int64'>
		 <class 'float'>
	 plc :
		 <class 'bson.int64.Int64'>
	 dut :
		 <class 'bson.int64.Int64'>
	 iex :
		 <class 'bson.int64.Int64'>
	 pctn :
		 <class 'bson.int64.Int64'>
	 strtaRate :
		 <class 'bson.int64.Int64'>
	 ilrf :
		 <class 'bson.int64.Int64'>
	 pf :
		 <class 'bson.int64.Int64'>
	 pb :
		 []
	 pctrl :
		 {
		 full :
			 <class 'bson.int64.Int64'>
		 add :
			 <class 'bson.int64.Int64'>
		 delete :
			 <class 'bson.int64.Int64'>
		 }
	 pmax :
		 <class 'bson.int64.Int64'>
	 adct :
		 <class 'bson.int64.Int64'>
	 dlapk :
		 <class 'bson.int64.Int64'>
	  upaid :
		 <class 'bson.int64.Int64'>
	 httpType :
		 <class 'float'>
	 }
 offsetList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
			 <class 'int'>
		 }
 vbaConf :
	 {
	 vbaClose :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 vbaOption :
			 {
			 request_day :
				 <class 'bson.int64.Int64'>
			 }
			 {
			 install_day :
				 <class 'bson.int64.Int64'>
			 }
			 {
			 install_num :
				 <class 'bson.int64.Int64'>
			 }
	 }
 landingPageVersion :
		 [
		 <class 'str'>
		 ]
 btCampaignIds :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 realPackageName :
	 <class 'str'>
 reduceRule :
	 {
	 priority :
		 <class 'bson.int64.Int64'>
	 install :
		 <class 'bson.int64.Int64'>
	 status :
		 <class 'bson.int64.Int64'>
	 start :
		 <class 'bson.int64.Int64'>
	 }
 reduceRuleV2 :
	 {
	 <class 'int'> :
		 {
		 priority :
			 <class 'bson.int64.Int64'>
		 install :
			 <class 'bson.int64.Int64'>
		 price :
			 <class 'bson.int64.Int64'>
		 status :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'bson.int64.Int64'>
		 }
	 }
 blackPackageList :
		 [
		 <class 'str'>
		 ]
 blackCategoryList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 vtaConfigApp :
	 {
	 US :
		 {
		 status :
			 <class 'bson.int64.Int64'>
		 rate :
			 <class 'bson.int64.Int64'>
		 rule :
			 <class 'bson.int64.Int64'>
		 }
	 ALL :
		 {
		 status :
			 <class 'bson.int64.Int64'>
		 rate :
			 <class 'bson.int64.Int64'>
		 rule :
			 <class 'bson.int64.Int64'>
		 }
	 }
 fillRateApp :
	 {
	 version :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 FR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JP :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 US :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 HK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TW :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 ALL :
		 {
		 PH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 HK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TW :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ID :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 VN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AU :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 US :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KW :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 MY :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 MX :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 NG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 OM :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 QA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 RO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 RU :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ES :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JP :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 DE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 FR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 <class 'int'> :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 blend_traffic :
	 {
	 app :
			 [
			 <class 'str'>
			 ]
	 offer :
		 {
		 <class 'int'> :
				 [
				 <class 'str'>
				 ]
		 }
	 }
 SETTING_CONFIG_API :
	 {
	 plct :
		 <class 'bson.int64.Int64'>
	 }
 JUMP_TYPE_CONFIG_PUBLISHER :
	 {
	 <class 'int'> :
		 <class 'float'>
	 }
 priceAdjustmentApp :
	 <class 'float'>
 JUMP_TYPE_CONFIG :
	 {
	 <class 'int'> :
		 <class 'float'>
	 }
 offerFreCap :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
			 <class 'int'>
		 }
 JUMP_TYPE_CONFIG_PUBLISHER_IOS :
	 {
	 <class 'int'> :
		 <class 'bson.int64.Int64'>
	 }
 offerVbaIntval :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
			 <class 'int'>
		 }
 advVbaIntval :
	 {
	 <class 'int'> :
		 <class 'bson.int64.Int64'>
	 }
 }
```

```
{'_id': [<class 'bson.objectid.ObjectId'>], 'appId': [<class 'bson.int64.Int64'>, <class 'int'>], 'publisher': {'publisherId': [<class 'bson.int64.Int64'>, <class 'int'>], 'username': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>, <class 'int'>], 'apiKey': [<class 'str'>], 'type': [<class 'bson.int64.Int64'>, <class 'int'>], 'mvSourceStatus': [<class 'bson.int64.Int64'>, <class 'int'>], 'forceDeviceId': [<class 'bson.int64.Int64'>, <class 'int'>], 'blockCategory': [[], [<class 'bson.int64.Int64'>]], 'created': [<class 'bson.int64.Int64'>, <class 'int'>], 'blockCategoryV2': [[], [<class 'bson.int64.Int64'>], [<class 'int'>]]}, 'app': {'appId': [<class 'bson.int64.Int64'>, <class 'int'>], 'publisherId': [<class 'bson.int64.Int64'>, <class 'int'>], 'grade': [<class 'bson.int64.Int64'>, <class 'int'>], 'name': [<class 'str'>], 'platform': [<class 'bson.int64.Int64'>, <class 'int'>], 'directMarket': [<class 'bson.int64.Int64'>, <class 'int'>], 'campaignType': [<class 'bson.int64.Int64'>, <class 'int'>], 'desc': [<class 'str'>], 'created': [<class 'bson.int64.Int64'>, <class 'int'>], 'status': [<class 'bson.int64.Int64'>, <class 'int'>], 'custom': [[]], 'postback': [<class 'str'>], 'postbackUrl': [<class 'str'>], 'devinfoEncrypt': [<class 'bson.int64.Int64'>, <class 'int'>], 'plct': [<class 'bson.int64.Int64'>, <class 'int'>], 'plctb': [<class 'bson.int64.Int64'>, <class 'int'>], 'nativexAppId': [<class 'str'>], 'nativexApiKey': [<class 'str'>], 'applovinSdkKey': [<class 'str'>], 'applovinReportKey': [<class 'str'>], 'isIncent': [<class 'bson.int64.Int64'>, <class 'int'>], 'allowBlend': [<class 'bson.int64.Int64'>, <class 'int'>], 'apkChance': [[], {'ALL': [<class 'int'>, <class 'bson.int64.Int64'>]}], 'offerPreference': [[<class 'bson.int64.Int64'>], [], [<class 'int'>]], 'contentPreference': [<class 'bson.int64.Int64'>, <class 'int'>], 'btClass': [<class 'bson.int64.Int64'>, <class 'int'>], 'category': [<class 'str'>], 'iabCategory': [[], [<class 'str'>]], 'subCategory': [[], [<class 'str'>]], 'trafficType': [<class 'bson.int64.Int64'>, <class 'int'>], 'vtaRelatedUnitId': [<class 'bson.int64.Int64'>, <class 'int'>], 'vtaRelatedAppId': [<class 'bson.int64.Int64'>, <class 'int'>], 'rushSetting': {'pc': [<class 'bson.int64.Int64'>, <class 'int'>], 'sdkrush': [<class 'bson.int64.Int64'>, <class 'int'>]}, 'rushUnits': [<class 'NoneType'>, {"<class 'int'>": [<class 'int'>, <class 'bson.int64.Int64'>]}], 'frequencyCap': [<class 'bson.int64.Int64'>, <class 'int'>], 'subCategoryV2': [[], [<class 'str'>]], 'domain': [<class 'str'>], 'domain_verify': [<class 'bson.int64.Int64'>, <class 'int'>], 'iabSubCategory': {'IAB1': [[<class 'str'>]], 'IAB2': [[<class 'str'>]], 'IAB3': [[<class 'str'>]], 'IAB4': [[<class 'str'>]], 'IAB5': [[<class 'str'>]], 'IAB6': [[<class 'str'>]], 'IAB7': [[<class 'str'>]], 'IAB8': [[<class 'str'>]], 'IAB9': [[<class 'str'>]], 'IAB10': [[<class 'str'>]], 'IAB11': [[<class 'str'>]], 'IAB12': [[<class 'str'>]], 'IAB13': [[<class 'str'>]], 'IAB14': [[<class 'str'>]], 'IAB15': [[<class 'str'>]], 'IAB16': [[<class 'str'>]], 'IAB17': [[<class 'str'>]], 'IAB18': [[<class 'str'>]], 'IAB19': [[<class 'str'>]], 'IAB20': [[<class 'str'>]], 'IAB21': [[<class 'str'>]], 'IAB22': [[<class 'str'>]], 'IAB23': [[<class 'str'>]], 'IAB24': [[<class 'str'>]], 'IAB25': [[<class 'str'>]], 'IAB26': [[<class 'str'>]]}, 'iabCategoryV2': {'IAB1': [[]], 'IAB9': [[]], 'IAB18': [[]], 'IAB3': [[]], 'IAB2': [[]], 'IAB22': [[]], 'IAB19': [[]], 'IAB24': [[]], 'IAB11': [[]], 'IAB12': [[]], 'IAB14': [[]], 'IAB10': [[]], 'IAB7': [[]], 'IAB5': [[]], 'IAB6': [[]], 'IAB15': [[]], 'IAB20': [[]], 'IAB13': [[]], 'IAB8': [[]], 'IAB17': [[]]}, 'coppa': [<class 'bson.int64.Int64'>, <class 'int'>]}, 'sspCampaignIds': [[<class 'bson.int64.Int64'>]], 'allowIp': [[<class 'str'>]], 'publisherId': [<class 'bson.int64.Int64'>, <class 'int'>], 'blackList': [[<class 'bson.int64.Int64'>], {"<class 'int'>": [<class 'bson.int64.Int64'>]}], 'whiteList': [[]], 'postbackM': [<class 'bson.int64.Int64'>], 'blackPackageNameList': [[], [<class 'str'>]], 'excludeAdvertiserIds': [[], [<class 'bson.int64.Int64'>]], 'campaignFields': [[], [<class 'str'>]], 'excludeSpecialType': [[]], 'updated': [<class 'bson.int64.Int64'>, <class 'int'>], 'updatedDate': [<class 'str'>], 'rewards': [{'id': [<class 'bson.int64.Int64'>], 'name': [<class 'str'>], 'amount': [<class 'bson.int64.Int64'>]}], 'setting': {'plct': [<class 'bson.int64.Int64'>, <class 'int'>], 'plctb': [<class 'bson.int64.Int64'>, <class 'int'>], 'cfb': [<class 'bool'>], 'hideVersion': [[], [<class 'str'>]], 'hideLoad': [<class 'bson.int64.Int64'>, <class 'int'>], 'shuffleVersion': [[], [<class 'str'>]], 'wreq': [<class 'bson.int64.Int64'>, <class 'int'>], 'dlct': [<class 'bson.int64.Int64'>, <class 'int'>], 'vcct': [<class 'bson.int64.Int64'>, <class 'int'>], 'jumpType': [<class 'bson.int64.Int64'>, <class 'int'>], 'openType': [<class 'bson.int64.Int64'>, <class 'int'>], 'dlrf': [<class 'bson.int64.Int64'>, <class 'int'>], 'dlrfct': [<class 'bson.int64.Int64'>, <class 'int'>], 'pcct': [<class 'bson.int64.Int64'>, <class 'int'>], 'storekit': [<class 'bson.int64.Int64'>, <class 'int'>]}, 'appsetting': {'pcto': [<class 'bson.int64.Int64'>], 'tcto': [<class 'bson.int64.Int64'>], 'pcrn': [<class 'bson.int64.Int64'>], 'uplc': [<class 'bson.int64.Int64'>, <class 'float'>], 'upmi': [<class 'bson.int64.Int64'>, <class 'float'>], 'upaid': [<class 'bson.int64.Int64'>], 'n2': [<class 'bson.int64.Int64'>, <class 'float'>], 'n3': [<class 'bson.int64.Int64'>, <class 'float'>], 'n4': [<class 'bson.int64.Int64'>, <class 'float'>], 'tcct': [<class 'bson.int64.Int64'>, <class 'float'>], 't_vba': [[<class 'bson.int64.Int64'>], [<class 'float'>], []], 'jumptBw': [<class 'bson.int64.Int64'>, <class 'float'>], 'crashCt': [<class 'bson.int64.Int64'>, <class 'float'>], 'ats_c': [<class 'bson.int64.Int64'>, <class 'float'>], 'plc': [<class 'bson.int64.Int64'>], 'dut': [<class 'bson.int64.Int64'>], 'iex': [<class 'bson.int64.Int64'>], 'pctn': [<class 'bson.int64.Int64'>], 'strtaRate': [<class 'bson.int64.Int64'>], 'ilrf': [<class 'bson.int64.Int64'>], 'pf': [<class 'bson.int64.Int64'>], 'pb': [[]], 'pctrl': {'full': [<class 'bson.int64.Int64'>], 'add': [<class 'bson.int64.Int64'>], 'delete': [<class 'bson.int64.Int64'>]}, 'pmax': [<class 'bson.int64.Int64'>], 'adct': [<class 'bson.int64.Int64'>], 'dlapk': [<class 'bson.int64.Int64'>], ' upaid': [<class 'bson.int64.Int64'>], 'httpType': [<class 'float'>]}, 'offsetList': [[], [<class 'bson.int64.Int64'>], {"<class 'int'>": [<class 'bson.int64.Int64'>, <class 'int'>]}], 'vbaConf': {'vbaClose': [<class 'bson.int64.Int64'>, <class 'int'>], 'vbaOption': [[], {'request_day': [<class 'bson.int64.Int64'>]}, {'install_day': [<class 'bson.int64.Int64'>]}, {'install_num': [<class 'bson.int64.Int64'>]}]}, 'landingPageVersion': [[], [<class 'str'>]], 'btCampaignIds': [[], [<class 'bson.int64.Int64'>]], 'realPackageName': [<class 'str'>], 'reduceRule': {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}, 'reduceRuleV2': {"<class 'int'>": {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'price': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}}, 'blackPackageList': [[<class 'str'>], []], 'blackCategoryList': [[], [<class 'bson.int64.Int64'>]], 'vtaConfigApp': {'US': {'status': [<class 'bson.int64.Int64'>], 'rate': [<class 'bson.int64.Int64'>], 'rule': [<class 'bson.int64.Int64'>]}, 'ALL': {'status': [<class 'bson.int64.Int64'>], 'rate': [<class 'bson.int64.Int64'>], 'rule': [<class 'bson.int64.Int64'>]}}, 'fillRateApp': {'version': {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'FR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JP': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'US': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'HK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TW': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}, 'ALL': {'PH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'HK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TW': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ID': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'VN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AU': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'US': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KW': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'MY': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'MX': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'NG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'OM': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'QA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'RO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'RU': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ES': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JP': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'DE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'FR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}, "<class 'int'>": {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}}, 'blend_traffic': {'app': [[<class 'str'>]], 'offer': {"<class 'int'>": [[<class 'str'>]]}}, 'SETTING_CONFIG_API': {'plct': [<class 'bson.int64.Int64'>]}, 'JUMP_TYPE_CONFIG_PUBLISHER': {"<class 'int'>": [<class 'float'>]}, 'priceAdjustmentApp': [<class 'float'>], 'JUMP_TYPE_CONFIG': {"<class 'int'>": [<class 'float'>]}, 'offerFreCap': [[], {"<class 'int'>": [<class 'bson.int64.Int64'>, <class 'int'>]}], 'JUMP_TYPE_CONFIG_PUBLISHER_IOS': {"<class 'int'>": [<class 'bson.int64.Int64'>]}, 'offerVbaIntval': [{"<class 'int'>": [<class 'bson.int64.Int64'>, <class 'int'>]}, []], 'advVbaIntval': {"<class 'int'>": [<class 'bson.int64.Int64'>]}}
```

---
###Creative:
```
 {
 _id :
	 <class 'bson.objectid.ObjectId'>
 campaignId :
	 <class 'bson.int64.Int64'>
 status :
	 <class 'bson.int64.Int64'>
 source :
	 <class 'bson.int64.Int64'>
 packageName :
	 <class 'str'>
 countryCode :
	 <class 'str'>
 sourceCreativeId :
	 <class 'bson.int64.Int64'>
 content :
	 {
	 <class 'int'> :
		 {
		 <class 'int'> :
			 {
			 url :
				 <class 'str'>
			 creativeId :
				 <class 'bson.int64.Int64'>
			 value :
				 <class 'str'>
				 <class 'float'>
			 mime :
				 <class 'str'>
			 attribute :
				 <class 'str'>
			 advCreativeId :
				 <class 'str'>
			 resolution :
				 <class 'str'>
			 videoLength :
				 <class 'bson.int64.Int64'>
			 videoSize :
				 <class 'bson.int64.Int64'>
			 videoResolution :
				 <class 'str'>
			 width :
				 <class 'bson.int64.Int64'>
			 height :
				 <class 'bson.int64.Int64'>
			 videoTruncation :
				 <class 'bson.int64.Int64'>
			 watchMile :
				 <class 'bson.int64.Int64'>
			 bitrate :
				 <class 'bson.int64.Int64'>
			 screenShot :
				 <class 'str'>
			 resourceType :
				 <class 'bson.int64.Int64'>
			 templateType :
				 <class 'bson.int64.Int64'>
			 tagCode :
				 <class 'str'>
			 showType :
				 <class 'bson.int64.Int64'>
			 orientation :
				 <class 'bson.int64.Int64'>
			 minOs :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 updated :
	 <class 'bson.int64.Int64'>
 updatedDate :
	 <class 'str'>
 }
{'_id': [<class 'bson.objectid.ObjectId'>], 'campaignId': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'source': [<class 'bson.int64.Int64'>], 'packageName': [<class 'str'>], 'countryCode': [<class 'str'>], 'sourceCreativeId': [<class 'bson.int64.Int64'>], 'content': {"<class 'int'>": {"<class 'int'>": {'url': [<class 'str'>], 'creativeId': [<class 'bson.int64.Int64'>], 'value': [<class 'str'>, <class 'float'>], 'mime': [<class 'str'>], 'attribute': [<class 'str'>], 'advCreativeId': [<class 'str'>], 'resolution': [<class 'str'>], 'videoLength': [<class 'bson.int64.Int64'>], 'videoSize': [<class 'bson.int64.Int64'>], 'videoResolution': [<class 'str'>], 'width': [<class 'bson.int64.Int64'>], 'height': [<class 'bson.int64.Int64'>], 'videoTruncation': [<class 'bson.int64.Int64'>], 'watchMile': [<class 'bson.int64.Int64'>], 'bitrate': [<class 'bson.int64.Int64'>], 'screenShot': [<class 'str'>], 'resourceType': [<class 'bson.int64.Int64'>], 'templateType': [<class 'bson.int64.Int64'>], 'tagCode': [<class 'str'>], 'showType': [<class 'bson.int64.Int64'>], 'orientation': [<class 'bson.int64.Int64'>], 'minOs': [<class 'bson.int64.Int64'>]}}}, 'updated': [<class 'bson.int64.Int64'>], 'updatedDate': [<class 'str'>]}


Unit:
 {
 _id :
	 <class 'bson.objectid.ObjectId'>
 publisherId :
	 <class 'bson.int64.Int64'>
 publisher :
	 {
	 publisherId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 username :
		 <class 'str'>
	 status :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 apiKey :
		 <class 'str'>
	 type :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 mvSourceStatus :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 forceDeviceId :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 blockCategory :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 blockCategoryV2 :
			 [
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'int'>
			 ]
	 created :
		 <class 'bson.int64.Int64'>
		 <class 'int'>
	 }
 blackPackageNameList :
		 [
		 <class 'str'>
		 ]
 appId :
	 <class 'bson.int64.Int64'>
 app :
	 {
	 appId :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 publisherId :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 grade :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 name :
		 <class 'str'>
	 platform :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 directMarket :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 campaignType :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 desc :
		 <class 'str'>
	 created :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 status :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 custom :
		 []
	 postback :
		 <class 'str'>
	 postbackUrl :
		 <class 'str'>
	 devinfoEncrypt :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 plct :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 plctb :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 nativexAppId :
		 <class 'str'>
	 nativexApiKey :
		 <class 'str'>
	 applovinSdkKey :
		 <class 'str'>
	 applovinReportKey :
		 <class 'str'>
	 isIncent :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 allowBlend :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 apkChance :
			 {
			 ALL :
				 <class 'int'>
				 <class 'bson.int64.Int64'>
			 }
	 offerPreference :
			 [
			 <class 'int'>
			 ]
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 contentPreference :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 btClass :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 category :
		 <class 'str'>
	 iabCategory :
			 [
			 <class 'str'>
			 ]
	 subCategory :
			 [
			 <class 'str'>
			 ]
	 trafficType :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 vtaRelatedUnitId :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 vtaRelatedAppId :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 rushSetting :
		 {
		 pc :
			 <class 'int'>
			 <class 'bson.int64.Int64'>
		 sdkrush :
			 <class 'int'>
			 <class 'bson.int64.Int64'>
		 }
	 rushUnits :
			 {
			 <class 'int'> :
				 <class 'int'>
				 <class 'bson.int64.Int64'>
			 }
		 <class 'NoneType'>
	 frequencyCap :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 subCategoryV2 :
			 [
			 <class 'str'>
			 ]
	 domain :
		 <class 'str'>
	 domain_verify :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 coppa :
		 <class 'int'>
		 <class 'bson.int64.Int64'>
	 iabSubCategory :
			 {
			 IAB1 :
					 [
					 <class 'str'>
					 ]
			 IAB2 :
					 [
					 <class 'str'>
					 ]
			 IAB3 :
					 [
					 <class 'str'>
					 ]
			 IAB4 :
					 [
					 <class 'str'>
					 ]
			 IAB5 :
					 [
					 <class 'str'>
					 ]
			 IAB6 :
					 [
					 <class 'str'>
					 ]
			 IAB7 :
					 [
					 <class 'str'>
					 ]
			 IAB8 :
					 [
					 <class 'str'>
					 ]
			 IAB9 :
					 [
					 <class 'str'>
					 ]
			 IAB10 :
					 [
					 <class 'str'>
					 ]
			 IAB11 :
					 [
					 <class 'str'>
					 ]
			 IAB12 :
					 [
					 <class 'str'>
					 ]
			 IAB13 :
					 [
					 <class 'str'>
					 ]
			 IAB14 :
					 [
					 <class 'str'>
					 ]
			 IAB15 :
					 [
					 <class 'str'>
					 ]
			 IAB16 :
					 [
					 <class 'str'>
					 ]
			 IAB17 :
					 [
					 <class 'str'>
					 ]
			 IAB18 :
					 [
					 <class 'str'>
					 ]
			 IAB19 :
					 [
					 <class 'str'>
					 ]
			 IAB20 :
					 [
					 <class 'str'>
					 ]
			 IAB21 :
					 [
					 <class 'str'>
					 ]
			 IAB22 :
					 [
					 <class 'str'>
					 ]
			 IAB23 :
					 [
					 <class 'str'>
					 ]
			 IAB24 :
					 [
					 <class 'str'>
					 ]
			 IAB25 :
					 [
					 <class 'str'>
					 ]
			 IAB26 :
					 [
					 <class 'str'>
					 ]
			 }
	 iabCategoryV2 :
			 {
			 IAB3 :
				 []
			 IAB2 :
				 []
			 IAB9 :
				 []
			 IAB1 :
				 []
			 IAB18 :
				 []
			 IAB19 :
				 []
			 IAB24 :
				 []
			 IAB11 :
				 []
			 IAB12 :
				 []
			 IAB14 :
				 []
			 IAB10 :
				 []
			 IAB7 :
				 []
			 IAB5 :
				 []
			 IAB6 :
				 []
			 IAB15 :
				 []
			 IAB20 :
				 []
			 IAB13 :
				 []
			 IAB8 :
				 []
			 IAB17 :
				 []
			 IAB22 :
				 []
			 }
	 }
 campaignFields :
		 [
		 <class 'str'>
		 ]
 unitId :
	 <class 'bson.int64.Int64'>
 unit :
	 {
	 unitId :
		 <class 'bson.int64.Int64'>
	 appId :
		 <class 'bson.int64.Int64'>
	 publisherId :
		 <class 'bson.int64.Int64'>
	 name :
		 <class 'str'>
	 fbPlacementId :
		 <class 'str'>
	 myTargetSlotId :
		 <class 'str'>
	 frameNum :
		 <class 'bson.int64.Int64'>
	 adType :
		 <class 'bson.int64.Int64'>
	 orientation :
		 <class 'bson.int64.Int64'>
	 templates :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 refresh :
		 <class 'bson.int64.Int64'>
	 status :
		 <class 'bson.int64.Int64'>
	 preClick :
		 <class 'bool'>
	 pubnativeAppToken :
		 <class 'str'>
	 mobvistaAppId :
		 <class 'bson.int64.Int64'>
	 mobvistaApiKey :
		 <class 'str'>
	 entraImage :
		 <class 'str'>
	 relatedUnitId :
		 <class 'bson.int64.Int64'>
	 redPointShow :
		 <class 'bool'>
	 redPointShowInterval :
		 <class 'bson.int64.Int64'>
	 admobUnitId :
		 <class 'str'>
	 apiRequestNum :
		 <class 'bson.int64.Int64'>
	 apiCacheNum :
		 <class 'bson.int64.Int64'>
	 ttcType :
		 <class 'bson.int64.Int64'>
	 waitingTime :
		 <class 'bson.int64.Int64'>
	 ctaMove :
		 <class 'bson.int64.Int64'>
	 autoOptimize :
		 <class 'bool'>
	 nativexPlacementName :
		 <class 'str'>
	 vct :
		 <class 'bson.int64.Int64'>
	 isIncent :
		 <class 'bson.int64.Int64'>
	 btClass :
		 <class 'bson.int64.Int64'>
	 isServerCall :
		 <class 'bson.int64.Int64'>
	 newFakeRule :
		 <class 'bson.int64.Int64'>
	 grade :
		 <class 'bson.int64.Int64'>
	 adFilter :
		 <class 'bson.int64.Int64'>
	 videoAds :
		 <class 'bson.int64.Int64'>
	 offerwallTypes :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 videoEndType :
		 <class 'bson.int64.Int64'>
	 recallNet :
		 <class 'str'>
	 hang :
		 <class 'bson.int64.Int64'>
	 endcardTemplate :
		 <class 'str'>
	 cookieAchieve :
		 <class 'bson.int64.Int64'>
	 nvTemplate :
		 <class 'bson.int64.Int64'>
	 allAdFilter :
		 {
		 ALL :
			 <class 'bson.int64.Int64'>
		 JP :
			 <class 'bson.int64.Int64'>
		 FR :
			 <class 'bson.int64.Int64'>
		 KR :
			 <class 'bson.int64.Int64'>
		 RU :
			 <class 'bson.int64.Int64'>
		 UK :
			 <class 'bson.int64.Int64'>
		 CN :
			 <class 'bson.int64.Int64'>
		 US :
			 <class 'bson.int64.Int64'>
		 IN :
			 <class 'bson.int64.Int64'>
		 DE :
			 <class 'bson.int64.Int64'>
		 BR :
			 <class 'bson.int64.Int64'>
		 VN :
			 <class 'bson.int64.Int64'>
		 ES :
			 <class 'bson.int64.Int64'>
		 NL :
			 <class 'bson.int64.Int64'>
		 AR :
			 <class 'bson.int64.Int64'>
		 PT :
			 <class 'bson.int64.Int64'>
		 PA :
			 <class 'bson.int64.Int64'>
		 UY :
			 <class 'bson.int64.Int64'>
		 KW :
			 <class 'bson.int64.Int64'>
		 IL :
			 <class 'bson.int64.Int64'>
		 MX :
			 <class 'bson.int64.Int64'>
		 IQ :
			 <class 'bson.int64.Int64'>
		 PR :
			 <class 'bson.int64.Int64'>
		 BD :
			 <class 'bson.int64.Int64'>
		 JO :
			 <class 'bson.int64.Int64'>
		 CM :
			 <class 'bson.int64.Int64'>
		 EC :
			 <class 'bson.int64.Int64'>
		 PY :
			 <class 'bson.int64.Int64'>
		 LA :
			 <class 'bson.int64.Int64'>
		 CO :
			 <class 'bson.int64.Int64'>
		 PE :
			 <class 'bson.int64.Int64'>
		 GT :
			 <class 'bson.int64.Int64'>
		 CL :
			 <class 'bson.int64.Int64'>
		 PH :
			 <class 'bson.int64.Int64'>
		 TH :
			 <class 'bson.int64.Int64'>
		 TR :
			 <class 'bson.int64.Int64'>
		 IT :
			 <class 'bson.int64.Int64'>
		 CA :
			 <class 'bson.int64.Int64'>
		 GB :
			 <class 'bson.int64.Int64'>
		 AT :
			 <class 'bson.int64.Int64'>
		 EG :
			 <class 'bson.int64.Int64'>
		 VE :
			 <class 'bson.int64.Int64'>
		 ID :
			 <class 'bson.int64.Int64'>
		 NG :
			 <class 'bson.int64.Int64'>
		 JM :
			 <class 'bson.int64.Int64'>
		 TW :
			 <class 'bson.int64.Int64'>
		 PK :
			 <class 'bson.int64.Int64'>
		 MY :
			 <class 'bson.int64.Int64'>
		 HK :
			 <class 'bson.int64.Int64'>
		 VI :
			 <class 'bson.int64.Int64'>
		 UG :
			 <class 'bson.int64.Int64'>
		 UA :
			 <class 'bson.int64.Int64'>
		 GR :
			 <class 'bson.int64.Int64'>
		 }
	 }
 myOfferIdList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 adSourceCountry :
		 {
		 AD :
			 <class 'bson.int64.Int64'>
		 ZW :
			 <class 'bson.int64.Int64'>
		 ZM :
			 <class 'bson.int64.Int64'>
		 YE :
			 <class 'bson.int64.Int64'>
		 EH :
			 <class 'bson.int64.Int64'>
		 WF :
			 <class 'bson.int64.Int64'>
		 VG :
			 <class 'bson.int64.Int64'>
		 VN :
			 <class 'bson.int64.Int64'>
		 VE :
			 <class 'bson.int64.Int64'>
		 VU :
			 <class 'bson.int64.Int64'>
		 UZ :
			 <class 'bson.int64.Int64'>
		 UY :
			 <class 'bson.int64.Int64'>
		 VI :
			 <class 'bson.int64.Int64'>
		 UM :
			 <class 'bson.int64.Int64'>
		 US :
			 <class 'bson.int64.Int64'>
		 UK :
			 <class 'bson.int64.Int64'>
		 GB :
			 <class 'bson.int64.Int64'>
		 AE :
			 <class 'bson.int64.Int64'>
		 UA :
			 <class 'bson.int64.Int64'>
		 UG :
			 <class 'bson.int64.Int64'>
		 TV :
			 <class 'bson.int64.Int64'>
		 TC :
			 <class 'bson.int64.Int64'>
		 TM :
			 <class 'bson.int64.Int64'>
		 TR :
			 <class 'bson.int64.Int64'>
		 TN :
			 <class 'bson.int64.Int64'>
		 TT :
			 <class 'bson.int64.Int64'>
		 TO :
			 <class 'bson.int64.Int64'>
		 TK :
			 <class 'bson.int64.Int64'>
		 TG :
			 <class 'bson.int64.Int64'>
		 TL :
			 <class 'bson.int64.Int64'>
		 TH :
			 <class 'bson.int64.Int64'>
		 TZ :
			 <class 'bson.int64.Int64'>
		 TJ :
			 <class 'bson.int64.Int64'>
		 TW :
			 <class 'bson.int64.Int64'>
		 SY :
			 <class 'bson.int64.Int64'>
		 CH :
			 <class 'bson.int64.Int64'>
		 SE :
			 <class 'bson.int64.Int64'>
		 SZ :
			 <class 'bson.int64.Int64'>
		 SJ :
			 <class 'bson.int64.Int64'>
		 SR :
			 <class 'bson.int64.Int64'>
		 SD :
			 <class 'bson.int64.Int64'>
		 LK :
			 <class 'bson.int64.Int64'>
		 ES :
			 <class 'bson.int64.Int64'>
		 SS :
			 <class 'bson.int64.Int64'>
		 GS :
			 <class 'bson.int64.Int64'>
		 ZA :
			 <class 'bson.int64.Int64'>
		 SO :
			 <class 'bson.int64.Int64'>
		 SB :
			 <class 'bson.int64.Int64'>
		 SI :
			 <class 'bson.int64.Int64'>
		 SK :
			 <class 'bson.int64.Int64'>
		 SX :
			 <class 'bson.int64.Int64'>
		 SG :
			 <class 'bson.int64.Int64'>
		 SL :
			 <class 'bson.int64.Int64'>
		 SC :
			 <class 'bson.int64.Int64'>
		 RS :
			 <class 'bson.int64.Int64'>
		 SN :
			 <class 'bson.int64.Int64'>
		 SA :
			 <class 'bson.int64.Int64'>
		 ST :
			 <class 'bson.int64.Int64'>
		 SM :
			 <class 'bson.int64.Int64'>
		 WS :
			 <class 'bson.int64.Int64'>
		 VC :
			 <class 'bson.int64.Int64'>
		 PM :
			 <class 'bson.int64.Int64'>
		 MF :
			 <class 'bson.int64.Int64'>
		 LC :
			 <class 'bson.int64.Int64'>
		 KN :
			 <class 'bson.int64.Int64'>
		 SH :
			 <class 'bson.int64.Int64'>
		 BL :
			 <class 'bson.int64.Int64'>
		 RW :
			 <class 'bson.int64.Int64'>
		 RU :
			 <class 'bson.int64.Int64'>
		 RO :
			 <class 'bson.int64.Int64'>
		 RE :
			 <class 'bson.int64.Int64'>
		 QA :
			 <class 'bson.int64.Int64'>
		 PR :
			 <class 'bson.int64.Int64'>
		 PT :
			 <class 'bson.int64.Int64'>
		 PL :
			 <class 'bson.int64.Int64'>
		 PN :
			 <class 'bson.int64.Int64'>
		 PH :
			 <class 'bson.int64.Int64'>
		 PE :
			 <class 'bson.int64.Int64'>
		 PY :
			 <class 'bson.int64.Int64'>
		 PG :
			 <class 'bson.int64.Int64'>
		 PA :
			 <class 'bson.int64.Int64'>
		 PS :
			 <class 'bson.int64.Int64'>
		 PW :
			 <class 'bson.int64.Int64'>
		 PK :
			 <class 'bson.int64.Int64'>
		 OTH :
			 <class 'bson.int64.Int64'>
		 OM :
			 <class 'bson.int64.Int64'>
		 NO :
			 <class 'bson.int64.Int64'>
		 MP :
			 <class 'bson.int64.Int64'>
		 KP :
			 <class 'bson.int64.Int64'>
		 NF :
			 <class 'bson.int64.Int64'>
		 NU :
			 <class 'bson.int64.Int64'>
		 NG :
			 <class 'bson.int64.Int64'>
		 NE :
			 <class 'bson.int64.Int64'>
		 NI :
			 <class 'bson.int64.Int64'>
		 NZ :
			 <class 'bson.int64.Int64'>
		 NC :
			 <class 'bson.int64.Int64'>
		 NL :
			 <class 'bson.int64.Int64'>
		 NP :
			 <class 'bson.int64.Int64'>
		 NR :
			 <class 'bson.int64.Int64'>
		 NA :
			 <class 'bson.int64.Int64'>
		 NK :
			 <class 'bson.int64.Int64'>
		 MM :
			 <class 'bson.int64.Int64'>
		 MZ :
			 <class 'bson.int64.Int64'>
		 MA :
			 <class 'bson.int64.Int64'>
		 MS :
			 <class 'bson.int64.Int64'>
		 ME :
			 <class 'bson.int64.Int64'>
		 MN :
			 <class 'bson.int64.Int64'>
		 MC :
			 <class 'bson.int64.Int64'>
		 MD :
			 <class 'bson.int64.Int64'>
		 FM :
			 <class 'bson.int64.Int64'>
		 MX :
			 <class 'bson.int64.Int64'>
		 YT :
			 <class 'bson.int64.Int64'>
		 MU :
			 <class 'bson.int64.Int64'>
		 MR :
			 <class 'bson.int64.Int64'>
		 MQ :
			 <class 'bson.int64.Int64'>
		 MH :
			 <class 'bson.int64.Int64'>
		 MT :
			 <class 'bson.int64.Int64'>
		 ML :
			 <class 'bson.int64.Int64'>
		 MV :
			 <class 'bson.int64.Int64'>
		 MY :
			 <class 'bson.int64.Int64'>
		 MW :
			 <class 'bson.int64.Int64'>
		 MG :
			 <class 'bson.int64.Int64'>
		 MK :
			 <class 'bson.int64.Int64'>
		 MO :
			 <class 'bson.int64.Int64'>
		 LU :
			 <class 'bson.int64.Int64'>
		 LT :
			 <class 'bson.int64.Int64'>
		 LI :
			 <class 'bson.int64.Int64'>
		 LY :
			 <class 'bson.int64.Int64'>
		 LR :
			 <class 'bson.int64.Int64'>
		 LS :
			 <class 'bson.int64.Int64'>
		 LB :
			 <class 'bson.int64.Int64'>
		 LV :
			 <class 'bson.int64.Int64'>
		 LA :
			 <class 'bson.int64.Int64'>
		 KG :
			 <class 'bson.int64.Int64'>
		 KW :
			 <class 'bson.int64.Int64'>
		 KR :
			 <class 'bson.int64.Int64'>
		 KI :
			 <class 'bson.int64.Int64'>
		 KE :
			 <class 'bson.int64.Int64'>
		 KZ :
			 <class 'bson.int64.Int64'>
		 JO :
			 <class 'bson.int64.Int64'>
		 JE :
			 <class 'bson.int64.Int64'>
		 JP :
			 <class 'bson.int64.Int64'>
		 JM :
			 <class 'bson.int64.Int64'>
		 IT :
			 <class 'bson.int64.Int64'>
		 IL :
			 <class 'bson.int64.Int64'>
		 IM :
			 <class 'bson.int64.Int64'>
		 IE :
			 <class 'bson.int64.Int64'>
		 IQ :
			 <class 'bson.int64.Int64'>
		 IR :
			 <class 'bson.int64.Int64'>
		 ID :
			 <class 'bson.int64.Int64'>
		 IN :
			 <class 'bson.int64.Int64'>
		 IS :
			 <class 'bson.int64.Int64'>
		 HU :
			 <class 'bson.int64.Int64'>
		 HK :
			 <class 'bson.int64.Int64'>
		 HN :
			 <class 'bson.int64.Int64'>
		 VA :
			 <class 'bson.int64.Int64'>
		 HM :
			 <class 'bson.int64.Int64'>
		 HT :
			 <class 'bson.int64.Int64'>
		 GY :
			 <class 'bson.int64.Int64'>
		 GW :
			 <class 'bson.int64.Int64'>
		 GN :
			 <class 'bson.int64.Int64'>
		 GG :
			 <class 'bson.int64.Int64'>
		 GT :
			 <class 'bson.int64.Int64'>
		 GU :
			 <class 'bson.int64.Int64'>
		 GP :
			 <class 'bson.int64.Int64'>
		 GD :
			 <class 'bson.int64.Int64'>
		 GL :
			 <class 'bson.int64.Int64'>
		 GR :
			 <class 'bson.int64.Int64'>
		 GI :
			 <class 'bson.int64.Int64'>
		 GH :
			 <class 'bson.int64.Int64'>
		 DE :
			 <class 'bson.int64.Int64'>
		 GE :
			 <class 'bson.int64.Int64'>
		 GM :
			 <class 'bson.int64.Int64'>
		 GA :
			 <class 'bson.int64.Int64'>
		 TF :
			 <class 'bson.int64.Int64'>
		 PF :
			 <class 'bson.int64.Int64'>
		 GF :
			 <class 'bson.int64.Int64'>
		 FR :
			 <class 'bson.int64.Int64'>
		 FI :
			 <class 'bson.int64.Int64'>
		 FJ :
			 <class 'bson.int64.Int64'>
		 FO :
			 <class 'bson.int64.Int64'>
		 FK :
			 <class 'bson.int64.Int64'>
		 ET :
			 <class 'bson.int64.Int64'>
		 EE :
			 <class 'bson.int64.Int64'>
		 ER :
			 <class 'bson.int64.Int64'>
		 GQ :
			 <class 'bson.int64.Int64'>
		 SV :
			 <class 'bson.int64.Int64'>
		 EG :
			 <class 'bson.int64.Int64'>
		 EC :
			 <class 'bson.int64.Int64'>
		 DO :
			 <class 'bson.int64.Int64'>
		 DM :
			 <class 'bson.int64.Int64'>
		 DJ :
			 <class 'bson.int64.Int64'>
		 DK :
			 <class 'bson.int64.Int64'>
		 CZ :
			 <class 'bson.int64.Int64'>
		 CY :
			 <class 'bson.int64.Int64'>
		 CW :
			 <class 'bson.int64.Int64'>
		 CU :
			 <class 'bson.int64.Int64'>
		 HR :
			 <class 'bson.int64.Int64'>
		 CI :
			 <class 'bson.int64.Int64'>
		 CR :
			 <class 'bson.int64.Int64'>
		 CK :
			 <class 'bson.int64.Int64'>
		 CD :
			 <class 'bson.int64.Int64'>
		 CG :
			 <class 'bson.int64.Int64'>
		 KM :
			 <class 'bson.int64.Int64'>
		 CO :
			 <class 'bson.int64.Int64'>
		 CC :
			 <class 'bson.int64.Int64'>
		 CX :
			 <class 'bson.int64.Int64'>
		 CN :
			 <class 'bson.int64.Int64'>
		 CL :
			 <class 'bson.int64.Int64'>
		 TD :
			 <class 'bson.int64.Int64'>
		 CF :
			 <class 'bson.int64.Int64'>
		 KY :
			 <class 'bson.int64.Int64'>
		 CV :
			 <class 'bson.int64.Int64'>
		 CA :
			 <class 'bson.int64.Int64'>
		 CM :
			 <class 'bson.int64.Int64'>
		 KH :
			 <class 'bson.int64.Int64'>
		 BI :
			 <class 'bson.int64.Int64'>
		 BF :
			 <class 'bson.int64.Int64'>
		 BG :
			 <class 'bson.int64.Int64'>
		 BN :
			 <class 'bson.int64.Int64'>
		 IO :
			 <class 'bson.int64.Int64'>
		 BR :
			 <class 'bson.int64.Int64'>
		 BV :
			 <class 'bson.int64.Int64'>
		 BW :
			 <class 'bson.int64.Int64'>
		 BA :
			 <class 'bson.int64.Int64'>
		 BQ :
			 <class 'bson.int64.Int64'>
		 BO :
			 <class 'bson.int64.Int64'>
		 BT :
			 <class 'bson.int64.Int64'>
		 BM :
			 <class 'bson.int64.Int64'>
		 BJ :
			 <class 'bson.int64.Int64'>
		 BZ :
			 <class 'bson.int64.Int64'>
		 BE :
			 <class 'bson.int64.Int64'>
		 BY :
			 <class 'bson.int64.Int64'>
		 BB :
			 <class 'bson.int64.Int64'>
		 BD :
			 <class 'bson.int64.Int64'>
		 BH :
			 <class 'bson.int64.Int64'>
		 BS :
			 <class 'bson.int64.Int64'>
		 AZ :
			 <class 'bson.int64.Int64'>
		 AT :
			 <class 'bson.int64.Int64'>
		 AU :
			 <class 'bson.int64.Int64'>
		 AW :
			 <class 'bson.int64.Int64'>
		 AM :
			 <class 'bson.int64.Int64'>
		 AR :
			 <class 'bson.int64.Int64'>
		 AG :
			 <class 'bson.int64.Int64'>
		 AQ :
			 <class 'bson.int64.Int64'>
		 AI :
			 <class 'bson.int64.Int64'>
		 AO :
			 <class 'bson.int64.Int64'>
		 AS :
			 <class 'bson.int64.Int64'>
		 DZ :
			 <class 'bson.int64.Int64'>
		 AL :
			 <class 'bson.int64.Int64'>
		 AF :
			 <class 'bson.int64.Int64'>
		 AX :
			 <class 'bson.int64.Int64'>
		 }
 adSourceData :
		 {
		 adSourceId :
			 <class 'bson.int64.Int64'>
		 status :
			 <class 'bson.int64.Int64'>
		 priority :
			 <class 'bson.int64.Int64'>
		 }
 updated :
	 <class 'int'>
	 <class 'bson.int64.Int64'>
 updatedDate :
	 <class 'str'>
 excludeAdvertiserIds :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 excludeSpecialType :
	 []
 outputType :
	 None 

 adSourceTime :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
 activeAdSources :
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
		 [
			 [
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 <class 'bson.int64.Int64'>
			 ]
		 ]
 setting :
	 {
	 thirdPartyRequestNum :
		 <class 'bson.int64.Int64'>
	 apiRequestNum :
		 <class 'bson.int64.Int64'>
	 apiCacheNum :
		 <class 'bson.int64.Int64'>
	 ttcType :
		 <class 'bson.int64.Int64'>
	 waitingTime :
		 <class 'bson.int64.Int64'>
	 ctaMove :
		 <class 'bson.int64.Int64'>
	 mo :
		 <class 'bson.int64.Int64'>
	 vcn :
		 <class 'bson.int64.Int64'>
	 cbp :
		 <class 'float'>
	 dlnet :
		 <class 'bson.int64.Int64'>
	 autoplay :
		 <class 'bson.int64.Int64'>
	 callbackType :
		 <class 'bson.int64.Int64'>
	 clct :
		 <class 'bson.int64.Int64'>
	 clcq :
		 <class 'bson.int64.Int64'>
	 endScreen :
		 <class 'bson.int64.Int64'>
	 closeButtonDelay :
		 <class 'bson.int64.Int64'>
	 recallNet :
			 [
			 <class 'bson.int64.Int64'>
			 ]
	 readyRate :
		 <class 'bson.int64.Int64'>
	 aqn :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
	 acn :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
	 impt :
		 <class 'bson.int64.Int64'>
	 degradeDisplay :
			 {
			 ALL :
				 <class 'bson.int64.Int64'>
			 }
	 dailyPlayCap :
		 <class 'bson.int64.Int64'>
	 videoSkipTime :
		 <class 'bson.int64.Int64'>
	 videoInteractiveType :
		 <class 'bson.int64.Int64'>
	 orientation :
		 <class 'bson.int64.Int64'>
	 }
 cpcOfferList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 brandOfferList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 offsetList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
			 <class 'int'>
		 }
 vbaConf :
	 {
	 vbaClose :
		 <class 'bson.int64.Int64'>
	 vbaOption :
			 {
			 request_day :
				 <class 'bson.int64.Int64'>
			 }
			 {
			 install_day :
				 <class 'bson.int64.Int64'>
			 }
			 {
			 install_num :
				 <class 'bson.int64.Int64'>
			 }
	 }
 landingPageVersion :
		 [
		 <class 'str'>
		 ]
 virtualReward :
		 {
		 id :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 name :
			 <class 'str'>
		 }
		 {
		 app_id :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 exchange_rate :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 static_reward :
			 <class 'bson.int64.Int64'>
		 }
 callbackUrl :
	 <class 'str'>
 securityKey :
	 <class 'str'>
 power :
	 {
	 autoSwitch :
		 <class 'bson.int64.Int64'>
	 requestNum :
		 <class 'bson.int64.Int64'>
	 requestInterval :
		 <class 'bson.int64.Int64'>
	 cacheTime :
		 <class 'bson.int64.Int64'>
	 referCacheTime :
		 <class 'bson.int64.Int64'>
	 usedTime :
		 <class 'bson.int64.Int64'>
	 waitingTime :
		 <class 'bson.int64.Int64'>
	 offset :
		 <class 'bson.int64.Int64'>
	 broadcast :
		 <class 'bson.int64.Int64'>
	 }
 unitSetting :
	 {
	 tvStart :
		 <class 'float'>
		 <class 'bson.int64.Int64'>
	 tvEnd :
		 <class 'float'>
		 <class 'bson.int64.Int64'>
	 atf :
		 {
		 status :
			 <class 'float'>
		 countries :
				 [
				 <class 'str'>
				 ]
		 }
	 videoSkipResult :
		 <class 'bson.int64.Int64'>
	 }
 preClick :
	 <class 'bool'>
 blackList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 whiteList :
	 []
 subsidyRule :
	 {
	 priority :
		 <class 'bson.int64.Int64'>
	 install :
		 <class 'bson.int64.Int64'>
	 status :
		 <class 'bson.int64.Int64'>
	 start :
		 <class 'bson.int64.Int64'>
	 }
 fakeRule :
	 {
	 install :
		 <class 'bson.int64.Int64'>
	 start :
		 <class 'str'>
	 status :
		 <class 'bson.int64.Int64'>
	 eCPM :
		 <class 'float'>
	 reduceMax :
		 <class 'bson.int64.Int64'>
	 plusMax :
		 <class 'bson.int64.Int64'>
	 amplitude :
		 <class 'bson.int64.Int64'>
	 updated :
		 <class 'str'>
	 }
 fakeRuleV2 :
	 {
	 ALL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
			 <class 'bson.int64.Int64'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 US :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 IN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 JP :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 KR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 VN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AX :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 ID :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TW :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 FR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MX :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 RU :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TH :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GB :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AU :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 IT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 UK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SG :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 DE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MY :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 JO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 ES :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NZ :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NG :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PH :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 ZA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 HK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 QA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 KW :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 OM :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BH :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 EG :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NC :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 IL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 UY :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AS :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 KH :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AF :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 DZ :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AM :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 AZ :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BD :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BB :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BM :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 BG :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CM :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CG :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CW :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CY :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 DK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 DM :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 DO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 EC :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SV :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 FO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GF :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PF :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GY :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 HU :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 IQ :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 LA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 LB :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 LY :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 LT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MG :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MW :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MV :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MQ :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MM :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NP :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NI :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PS :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PY :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 PR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 RE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 RO :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 LC :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 MF :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 VC :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 RS :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SI :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SS :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 LK :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 SR :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 CH :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TZ :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TL :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TT :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 TN :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 UA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 VE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 YE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 IE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 GU :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 NA :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 EE :
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'str'>
		 status :
			 <class 'bson.int64.Int64'>
		 updated :
			 <class 'str'>
		 }
	 }
 fillRateUnit :
	 {
	 ALL :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 FR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ID :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JP :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 RU :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 US :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 DZ :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AU :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BD :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CF :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 MY :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ZA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ES :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 LK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 DE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 VN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 NL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 DK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 HK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 MX :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TW :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AM :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AZ :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CM :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SV :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 GT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 HN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KZ :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 LB :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 NI :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 RO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 VE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 EG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IQ :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UY :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KW :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 EC :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PY :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 LA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BJ :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CY :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 DO :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 GH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 HT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JM :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 KE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 MA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 NG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 QA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 RS :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 GB :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 OM :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AF :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BS :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CI :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 VI :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 GR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 version :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 US :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 <class 'int'> :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 tryNewRate :
	 <class 'float'>
	 <class 'bson.int64.Int64'>
 reduceRule :
	 {
	 impression :
		 <class 'bson.int64.Int64'>
	 click :
		 <class 'bson.int64.Int64'>
	 install :
		 <class 'bson.int64.Int64'>
	 start :
		 <class 'bson.int64.Int64'>
	 priority :
		 <class 'bson.int64.Int64'>
	 status :
		 <class 'bson.int64.Int64'>
	 }
 sspCampaignIds :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 allowIp :
		 [
		 <class 'str'>
		 ]
 postbackM :
	 <class 'bson.int64.Int64'>
 rewards :
		 {
		 id :
			 <class 'bson.int64.Int64'>
		 name :
			 <class 'str'>
		 amount :
			 <class 'bson.int64.Int64'>
		 }
 endcard :
	 {
	 urls :
			 {
			 id :
				 <class 'bson.int64.Int64'>
			 url :
				 <class 'str'>
			 weight :
				 <class 'bson.int64.Int64'>
			 }
	 status :
		 <class 'bson.int64.Int64'>
	 orientation :
		 <class 'bson.int64.Int64'>
	 videoTemplateUrl :
			 {
			 id :
				 <class 'bson.int64.Int64'>
			 url :
				 <class 'str'>
			 url_zip :
				 <class 'str'>
			 weight :
				 <class 'bson.int64.Int64'>
			 }
	 }
 JUMP_TYPE_CONFIG_PUBLISHER :
	 {
	 <class 'int'> :
		 <class 'float'>
	 }
 appsetting :
		 {
		 pcto :
			 <class 'bson.int64.Int64'>
		 tcto :
			 <class 'bson.int64.Int64'>
		 pcrn :
			 <class 'bson.int64.Int64'>
		 uplc :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 upmi :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 upaid :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 n2 :
			 <class 'bson.int64.Int64'>
			 <class 'float'>
		 n3 :
			 <class 'bson.int64.Int64'>
			 <class 'float'>
		  upaid :
			 <class 'bson.int64.Int64'>
		 t_vba :
				 [
				 <class 'float'>
				 ]
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 httpType :
			 <class 'float'>
		 ats_c :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 jumptBw :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 crashCt :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 n4 :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 tcct :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 storekit :
			 <class 'float'>
		 }
		 {
		 plc :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 dut :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 iex :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 pctn :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 strtaRate :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 ilrf :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 pf :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 pb :
			 []
		 }
		 {
		 pctrl :
				 {
				 full :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 pctrl :
				 {
				 add :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 pctrl :
				 {
				 delete :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 pmax :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 adct :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 dlapk :
			 <class 'bson.int64.Int64'>
		 }
 vtaConfigUnit :
	 {
	 ALL :
		 {
		 status :
			 <class 'bson.int64.Int64'>
		 rate :
			 <class 'bson.int64.Int64'>
		 rule :
			 <class 'bson.int64.Int64'>
		 }
	 }
 offerFreCap :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
 JUMP_TYPE_CONFIG_PUBLISHER_IOS :
	 {
	 <class 'int'> :
		 <class 'bson.int64.Int64'>
	 }
 blend_traffic :
	 {
	 app :
			 [
			 <class 'str'>
			 ]
	 }
 offerVbaIntval :
		 {
		 <class 'int'> :
			 <class 'bson.int64.Int64'>
		 }
 vtaConfigApp :
	 {
	 US :
		 {
		 status :
			 <class 'bson.int64.Int64'>
		 rate :
			 <class 'bson.int64.Int64'>
		 rule :
			 <class 'bson.int64.Int64'>
		 }
	 ALL :
		 {
		 status :
			 <class 'bson.int64.Int64'>
		 rate :
			 <class 'bson.int64.Int64'>
		 rule :
			 <class 'bson.int64.Int64'>
		 }
	 }
 advVbaIntval :
	 {
	 <class 'int'> :
		 <class 'bson.int64.Int64'>
	 }
 btCampaignIds :
	 []
 realPackageName :
	 <class 'str'>
 fillRateApp :
	 {
	 version :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 FR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IT :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 JP :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 US :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 CA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 ALL :
		 {
		 US :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SA :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 AE :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 UK :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 PH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 IN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 ID :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 RU :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 BR :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 TH :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 VN :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 SG :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 <class 'int'> :
		 {
		 ALL :
			 {
			 rate :
				 <class 'bson.int64.Int64'>
			 status :
				 <class 'bson.int64.Int64'>
			 }
		 }
	 }
 blackPackageList :
		 [
		 <class 'str'>
		 ]
 blackCategoryList :
		 [
		 <class 'bson.int64.Int64'>
		 ]
 reduceRuleV2 :
	 {
	 <class 'int'> :
		 {
		 priority :
			 <class 'bson.int64.Int64'>
		 install :
			 <class 'bson.int64.Int64'>
		 price :
			 <class 'bson.int64.Int64'>
		 status :
			 <class 'bson.int64.Int64'>
		 start :
			 <class 'bson.int64.Int64'>
		 }
	 }
 JUMP_TYPE_CONFIG :
	 {
	 <class 'int'> :
		 <class 'float'>
	 }
 }
```

```
{'_id': [<class 'bson.objectid.ObjectId'>], 'publisherId': [<class 'bson.int64.Int64'>], 'publisher': {'publisherId': [<class 'bson.int64.Int64'>, <class 'int'>], 'username': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>, <class 'int'>], 'apiKey': [<class 'str'>], 'type': [<class 'bson.int64.Int64'>, <class 'int'>], 'mvSourceStatus': [<class 'bson.int64.Int64'>, <class 'int'>], 'forceDeviceId': [<class 'bson.int64.Int64'>, <class 'int'>], 'blockCategory': [[], [<class 'bson.int64.Int64'>]], 'blockCategoryV2': [[], [<class 'bson.int64.Int64'>], [<class 'int'>]], 'created': [<class 'bson.int64.Int64'>, <class 'int'>]}, 'blackPackageNameList': [[<class 'str'>], []], 'appId': [<class 'bson.int64.Int64'>], 'app': {'appId': [<class 'int'>, <class 'bson.int64.Int64'>], 'publisherId': [<class 'int'>, <class 'bson.int64.Int64'>], 'grade': [<class 'int'>, <class 'bson.int64.Int64'>], 'name': [<class 'str'>], 'platform': [<class 'int'>, <class 'bson.int64.Int64'>], 'directMarket': [<class 'int'>, <class 'bson.int64.Int64'>], 'campaignType': [<class 'int'>, <class 'bson.int64.Int64'>], 'desc': [<class 'str'>], 'created': [<class 'int'>, <class 'bson.int64.Int64'>], 'status': [<class 'int'>, <class 'bson.int64.Int64'>], 'custom': [[]], 'postback': [<class 'str'>], 'postbackUrl': [<class 'str'>], 'devinfoEncrypt': [<class 'int'>, <class 'bson.int64.Int64'>], 'plct': [<class 'int'>, <class 'bson.int64.Int64'>], 'plctb': [<class 'int'>, <class 'bson.int64.Int64'>], 'nativexAppId': [<class 'str'>], 'nativexApiKey': [<class 'str'>], 'applovinSdkKey': [<class 'str'>], 'applovinReportKey': [<class 'str'>], 'isIncent': [<class 'int'>, <class 'bson.int64.Int64'>], 'allowBlend': [<class 'int'>, <class 'bson.int64.Int64'>], 'apkChance': [[], {'ALL': [<class 'int'>, <class 'bson.int64.Int64'>]}], 'offerPreference': [[<class 'int'>], [<class 'bson.int64.Int64'>], []], 'contentPreference': [<class 'int'>, <class 'bson.int64.Int64'>], 'btClass': [<class 'int'>, <class 'bson.int64.Int64'>], 'category': [<class 'str'>], 'iabCategory': [[], [<class 'str'>]], 'subCategory': [[], [<class 'str'>]], 'trafficType': [<class 'int'>, <class 'bson.int64.Int64'>], 'vtaRelatedUnitId': [<class 'int'>, <class 'bson.int64.Int64'>], 'vtaRelatedAppId': [<class 'int'>, <class 'bson.int64.Int64'>], 'rushSetting': {'pc': [<class 'int'>, <class 'bson.int64.Int64'>], 'sdkrush': [<class 'int'>, <class 'bson.int64.Int64'>]}, 'rushUnits': [{"<class 'int'>": [<class 'int'>, <class 'bson.int64.Int64'>]}, <class 'NoneType'>], 'frequencyCap': [<class 'int'>, <class 'bson.int64.Int64'>], 'subCategoryV2': [[], [<class 'str'>]], 'domain': [<class 'str'>], 'domain_verify': [<class 'int'>, <class 'bson.int64.Int64'>], 'coppa': [<class 'int'>, <class 'bson.int64.Int64'>], 'iabSubCategory': [{'IAB1': [[<class 'str'>]], 'IAB2': [[<class 'str'>]], 'IAB3': [[<class 'str'>]], 'IAB4': [[<class 'str'>]], 'IAB5': [[<class 'str'>]], 'IAB6': [[<class 'str'>]], 'IAB7': [[<class 'str'>]], 'IAB8': [[<class 'str'>]], 'IAB9': [[<class 'str'>]], 'IAB10': [[<class 'str'>]], 'IAB11': [[<class 'str'>]], 'IAB12': [[<class 'str'>]], 'IAB13': [[<class 'str'>]], 'IAB14': [[<class 'str'>]], 'IAB15': [[<class 'str'>]], 'IAB16': [[<class 'str'>]], 'IAB17': [[<class 'str'>]], 'IAB18': [[<class 'str'>]], 'IAB19': [[<class 'str'>]], 'IAB20': [[<class 'str'>]], 'IAB21': [[<class 'str'>]], 'IAB22': [[<class 'str'>]], 'IAB23': [[<class 'str'>]], 'IAB24': [[<class 'str'>]], 'IAB25': [[<class 'str'>]], 'IAB26': [[<class 'str'>]]}, []], 'iabCategoryV2': [{'IAB3': [[]], 'IAB2': [[]], 'IAB9': [[]], 'IAB1': [[]], 'IAB18': [[]], 'IAB19': [[]], 'IAB24': [[]], 'IAB11': [[]], 'IAB12': [[]], 'IAB14': [[]], 'IAB10': [[]], 'IAB7': [[]], 'IAB5': [[]], 'IAB6': [[]], 'IAB15': [[]], 'IAB20': [[]], 'IAB13': [[]], 'IAB8': [[]], 'IAB17': [[]], 'IAB22': [[]]}, []]}, 'campaignFields': [[], [<class 'str'>]], 'unitId': [<class 'bson.int64.Int64'>], 'unit': {'unitId': [<class 'bson.int64.Int64'>], 'appId': [<class 'bson.int64.Int64'>], 'publisherId': [<class 'bson.int64.Int64'>], 'name': [<class 'str'>], 'fbPlacementId': [<class 'str'>], 'myTargetSlotId': [<class 'str'>], 'frameNum': [<class 'bson.int64.Int64'>], 'adType': [<class 'bson.int64.Int64'>], 'orientation': [<class 'bson.int64.Int64'>], 'templates': [[<class 'bson.int64.Int64'>]], 'refresh': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'preClick': [<class 'bool'>], 'pubnativeAppToken': [<class 'str'>], 'mobvistaAppId': [<class 'bson.int64.Int64'>], 'mobvistaApiKey': [<class 'str'>], 'entraImage': [<class 'str'>], 'relatedUnitId': [<class 'bson.int64.Int64'>], 'redPointShow': [<class 'bool'>], 'redPointShowInterval': [<class 'bson.int64.Int64'>], 'admobUnitId': [<class 'str'>], 'apiRequestNum': [<class 'bson.int64.Int64'>], 'apiCacheNum': [<class 'bson.int64.Int64'>], 'ttcType': [<class 'bson.int64.Int64'>], 'waitingTime': [<class 'bson.int64.Int64'>], 'ctaMove': [<class 'bson.int64.Int64'>], 'autoOptimize': [<class 'bool'>], 'nativexPlacementName': [<class 'str'>], 'vct': [<class 'bson.int64.Int64'>], 'isIncent': [<class 'bson.int64.Int64'>], 'btClass': [<class 'bson.int64.Int64'>], 'isServerCall': [<class 'bson.int64.Int64'>], 'newFakeRule': [<class 'bson.int64.Int64'>], 'grade': [<class 'bson.int64.Int64'>], 'adFilter': [<class 'bson.int64.Int64'>], 'videoAds': [<class 'bson.int64.Int64'>], 'offerwallTypes': [[<class 'bson.int64.Int64'>]], 'videoEndType': [<class 'bson.int64.Int64'>], 'recallNet': [<class 'str'>], 'hang': [<class 'bson.int64.Int64'>], 'endcardTemplate': [<class 'str'>], 'cookieAchieve': [<class 'bson.int64.Int64'>], 'nvTemplate': [<class 'bson.int64.Int64'>], 'allAdFilter': {'ALL': [<class 'bson.int64.Int64'>], 'JP': [<class 'bson.int64.Int64'>], 'FR': [<class 'bson.int64.Int64'>], 'KR': [<class 'bson.int64.Int64'>], 'RU': [<class 'bson.int64.Int64'>], 'UK': [<class 'bson.int64.Int64'>], 'CN': [<class 'bson.int64.Int64'>], 'US': [<class 'bson.int64.Int64'>], 'IN': [<class 'bson.int64.Int64'>], 'DE': [<class 'bson.int64.Int64'>], 'BR': [<class 'bson.int64.Int64'>], 'VN': [<class 'bson.int64.Int64'>], 'ES': [<class 'bson.int64.Int64'>], 'NL': [<class 'bson.int64.Int64'>], 'AR': [<class 'bson.int64.Int64'>], 'PT': [<class 'bson.int64.Int64'>], 'PA': [<class 'bson.int64.Int64'>], 'UY': [<class 'bson.int64.Int64'>], 'KW': [<class 'bson.int64.Int64'>], 'IL': [<class 'bson.int64.Int64'>], 'MX': [<class 'bson.int64.Int64'>], 'IQ': [<class 'bson.int64.Int64'>], 'PR': [<class 'bson.int64.Int64'>], 'BD': [<class 'bson.int64.Int64'>], 'JO': [<class 'bson.int64.Int64'>], 'CM': [<class 'bson.int64.Int64'>], 'EC': [<class 'bson.int64.Int64'>], 'PY': [<class 'bson.int64.Int64'>], 'LA': [<class 'bson.int64.Int64'>], 'CO': [<class 'bson.int64.Int64'>], 'PE': [<class 'bson.int64.Int64'>], 'GT': [<class 'bson.int64.Int64'>], 'CL': [<class 'bson.int64.Int64'>], 'PH': [<class 'bson.int64.Int64'>], 'TH': [<class 'bson.int64.Int64'>], 'TR': [<class 'bson.int64.Int64'>], 'IT': [<class 'bson.int64.Int64'>], 'CA': [<class 'bson.int64.Int64'>], 'GB': [<class 'bson.int64.Int64'>], 'AT': [<class 'bson.int64.Int64'>], 'EG': [<class 'bson.int64.Int64'>], 'VE': [<class 'bson.int64.Int64'>], 'ID': [<class 'bson.int64.Int64'>], 'NG': [<class 'bson.int64.Int64'>], 'JM': [<class 'bson.int64.Int64'>], 'TW': [<class 'bson.int64.Int64'>], 'PK': [<class 'bson.int64.Int64'>], 'MY': [<class 'bson.int64.Int64'>], 'HK': [<class 'bson.int64.Int64'>], 'VI': [<class 'bson.int64.Int64'>], 'UG': [<class 'bson.int64.Int64'>], 'UA': [<class 'bson.int64.Int64'>], 'GR': [<class 'bson.int64.Int64'>]}}, 'myOfferIdList': [[], [<class 'bson.int64.Int64'>]], 'adSourceCountry': [{'AD': [<class 'bson.int64.Int64'>], 'ZW': [<class 'bson.int64.Int64'>], 'ZM': [<class 'bson.int64.Int64'>], 'YE': [<class 'bson.int64.Int64'>], 'EH': [<class 'bson.int64.Int64'>], 'WF': [<class 'bson.int64.Int64'>], 'VG': [<class 'bson.int64.Int64'>], 'VN': [<class 'bson.int64.Int64'>], 'VE': [<class 'bson.int64.Int64'>], 'VU': [<class 'bson.int64.Int64'>], 'UZ': [<class 'bson.int64.Int64'>], 'UY': [<class 'bson.int64.Int64'>], 'VI': [<class 'bson.int64.Int64'>], 'UM': [<class 'bson.int64.Int64'>], 'US': [<class 'bson.int64.Int64'>], 'UK': [<class 'bson.int64.Int64'>], 'GB': [<class 'bson.int64.Int64'>], 'AE': [<class 'bson.int64.Int64'>], 'UA': [<class 'bson.int64.Int64'>], 'UG': [<class 'bson.int64.Int64'>], 'TV': [<class 'bson.int64.Int64'>], 'TC': [<class 'bson.int64.Int64'>], 'TM': [<class 'bson.int64.Int64'>], 'TR': [<class 'bson.int64.Int64'>], 'TN': [<class 'bson.int64.Int64'>], 'TT': [<class 'bson.int64.Int64'>], 'TO': [<class 'bson.int64.Int64'>], 'TK': [<class 'bson.int64.Int64'>], 'TG': [<class 'bson.int64.Int64'>], 'TL': [<class 'bson.int64.Int64'>], 'TH': [<class 'bson.int64.Int64'>], 'TZ': [<class 'bson.int64.Int64'>], 'TJ': [<class 'bson.int64.Int64'>], 'TW': [<class 'bson.int64.Int64'>], 'SY': [<class 'bson.int64.Int64'>], 'CH': [<class 'bson.int64.Int64'>], 'SE': [<class 'bson.int64.Int64'>], 'SZ': [<class 'bson.int64.Int64'>], 'SJ': [<class 'bson.int64.Int64'>], 'SR': [<class 'bson.int64.Int64'>], 'SD': [<class 'bson.int64.Int64'>], 'LK': [<class 'bson.int64.Int64'>], 'ES': [<class 'bson.int64.Int64'>], 'SS': [<class 'bson.int64.Int64'>], 'GS': [<class 'bson.int64.Int64'>], 'ZA': [<class 'bson.int64.Int64'>], 'SO': [<class 'bson.int64.Int64'>], 'SB': [<class 'bson.int64.Int64'>], 'SI': [<class 'bson.int64.Int64'>], 'SK': [<class 'bson.int64.Int64'>], 'SX': [<class 'bson.int64.Int64'>], 'SG': [<class 'bson.int64.Int64'>], 'SL': [<class 'bson.int64.Int64'>], 'SC': [<class 'bson.int64.Int64'>], 'RS': [<class 'bson.int64.Int64'>], 'SN': [<class 'bson.int64.Int64'>], 'SA': [<class 'bson.int64.Int64'>], 'ST': [<class 'bson.int64.Int64'>], 'SM': [<class 'bson.int64.Int64'>], 'WS': [<class 'bson.int64.Int64'>], 'VC': [<class 'bson.int64.Int64'>], 'PM': [<class 'bson.int64.Int64'>], 'MF': [<class 'bson.int64.Int64'>], 'LC': [<class 'bson.int64.Int64'>], 'KN': [<class 'bson.int64.Int64'>], 'SH': [<class 'bson.int64.Int64'>], 'BL': [<class 'bson.int64.Int64'>], 'RW': [<class 'bson.int64.Int64'>], 'RU': [<class 'bson.int64.Int64'>], 'RO': [<class 'bson.int64.Int64'>], 'RE': [<class 'bson.int64.Int64'>], 'QA': [<class 'bson.int64.Int64'>], 'PR': [<class 'bson.int64.Int64'>], 'PT': [<class 'bson.int64.Int64'>], 'PL': [<class 'bson.int64.Int64'>], 'PN': [<class 'bson.int64.Int64'>], 'PH': [<class 'bson.int64.Int64'>], 'PE': [<class 'bson.int64.Int64'>], 'PY': [<class 'bson.int64.Int64'>], 'PG': [<class 'bson.int64.Int64'>], 'PA': [<class 'bson.int64.Int64'>], 'PS': [<class 'bson.int64.Int64'>], 'PW': [<class 'bson.int64.Int64'>], 'PK': [<class 'bson.int64.Int64'>], 'OTH': [<class 'bson.int64.Int64'>], 'OM': [<class 'bson.int64.Int64'>], 'NO': [<class 'bson.int64.Int64'>], 'MP': [<class 'bson.int64.Int64'>], 'KP': [<class 'bson.int64.Int64'>], 'NF': [<class 'bson.int64.Int64'>], 'NU': [<class 'bson.int64.Int64'>], 'NG': [<class 'bson.int64.Int64'>], 'NE': [<class 'bson.int64.Int64'>], 'NI': [<class 'bson.int64.Int64'>], 'NZ': [<class 'bson.int64.Int64'>], 'NC': [<class 'bson.int64.Int64'>], 'NL': [<class 'bson.int64.Int64'>], 'NP': [<class 'bson.int64.Int64'>], 'NR': [<class 'bson.int64.Int64'>], 'NA': [<class 'bson.int64.Int64'>], 'NK': [<class 'bson.int64.Int64'>], 'MM': [<class 'bson.int64.Int64'>], 'MZ': [<class 'bson.int64.Int64'>], 'MA': [<class 'bson.int64.Int64'>], 'MS': [<class 'bson.int64.Int64'>], 'ME': [<class 'bson.int64.Int64'>], 'MN': [<class 'bson.int64.Int64'>], 'MC': [<class 'bson.int64.Int64'>], 'MD': [<class 'bson.int64.Int64'>], 'FM': [<class 'bson.int64.Int64'>], 'MX': [<class 'bson.int64.Int64'>], 'YT': [<class 'bson.int64.Int64'>], 'MU': [<class 'bson.int64.Int64'>], 'MR': [<class 'bson.int64.Int64'>], 'MQ': [<class 'bson.int64.Int64'>], 'MH': [<class 'bson.int64.Int64'>], 'MT': [<class 'bson.int64.Int64'>], 'ML': [<class 'bson.int64.Int64'>], 'MV': [<class 'bson.int64.Int64'>], 'MY': [<class 'bson.int64.Int64'>], 'MW': [<class 'bson.int64.Int64'>], 'MG': [<class 'bson.int64.Int64'>], 'MK': [<class 'bson.int64.Int64'>], 'MO': [<class 'bson.int64.Int64'>], 'LU': [<class 'bson.int64.Int64'>], 'LT': [<class 'bson.int64.Int64'>], 'LI': [<class 'bson.int64.Int64'>], 'LY': [<class 'bson.int64.Int64'>], 'LR': [<class 'bson.int64.Int64'>], 'LS': [<class 'bson.int64.Int64'>], 'LB': [<class 'bson.int64.Int64'>], 'LV': [<class 'bson.int64.Int64'>], 'LA': [<class 'bson.int64.Int64'>], 'KG': [<class 'bson.int64.Int64'>], 'KW': [<class 'bson.int64.Int64'>], 'KR': [<class 'bson.int64.Int64'>], 'KI': [<class 'bson.int64.Int64'>], 'KE': [<class 'bson.int64.Int64'>], 'KZ': [<class 'bson.int64.Int64'>], 'JO': [<class 'bson.int64.Int64'>], 'JE': [<class 'bson.int64.Int64'>], 'JP': [<class 'bson.int64.Int64'>], 'JM': [<class 'bson.int64.Int64'>], 'IT': [<class 'bson.int64.Int64'>], 'IL': [<class 'bson.int64.Int64'>], 'IM': [<class 'bson.int64.Int64'>], 'IE': [<class 'bson.int64.Int64'>], 'IQ': [<class 'bson.int64.Int64'>], 'IR': [<class 'bson.int64.Int64'>], 'ID': [<class 'bson.int64.Int64'>], 'IN': [<class 'bson.int64.Int64'>], 'IS': [<class 'bson.int64.Int64'>], 'HU': [<class 'bson.int64.Int64'>], 'HK': [<class 'bson.int64.Int64'>], 'HN': [<class 'bson.int64.Int64'>], 'VA': [<class 'bson.int64.Int64'>], 'HM': [<class 'bson.int64.Int64'>], 'HT': [<class 'bson.int64.Int64'>], 'GY': [<class 'bson.int64.Int64'>], 'GW': [<class 'bson.int64.Int64'>], 'GN': [<class 'bson.int64.Int64'>], 'GG': [<class 'bson.int64.Int64'>], 'GT': [<class 'bson.int64.Int64'>], 'GU': [<class 'bson.int64.Int64'>], 'GP': [<class 'bson.int64.Int64'>], 'GD': [<class 'bson.int64.Int64'>], 'GL': [<class 'bson.int64.Int64'>], 'GR': [<class 'bson.int64.Int64'>], 'GI': [<class 'bson.int64.Int64'>], 'GH': [<class 'bson.int64.Int64'>], 'DE': [<class 'bson.int64.Int64'>], 'GE': [<class 'bson.int64.Int64'>], 'GM': [<class 'bson.int64.Int64'>], 'GA': [<class 'bson.int64.Int64'>], 'TF': [<class 'bson.int64.Int64'>], 'PF': [<class 'bson.int64.Int64'>], 'GF': [<class 'bson.int64.Int64'>], 'FR': [<class 'bson.int64.Int64'>], 'FI': [<class 'bson.int64.Int64'>], 'FJ': [<class 'bson.int64.Int64'>], 'FO': [<class 'bson.int64.Int64'>], 'FK': [<class 'bson.int64.Int64'>], 'ET': [<class 'bson.int64.Int64'>], 'EE': [<class 'bson.int64.Int64'>], 'ER': [<class 'bson.int64.Int64'>], 'GQ': [<class 'bson.int64.Int64'>], 'SV': [<class 'bson.int64.Int64'>], 'EG': [<class 'bson.int64.Int64'>], 'EC': [<class 'bson.int64.Int64'>], 'DO': [<class 'bson.int64.Int64'>], 'DM': [<class 'bson.int64.Int64'>], 'DJ': [<class 'bson.int64.Int64'>], 'DK': [<class 'bson.int64.Int64'>], 'CZ': [<class 'bson.int64.Int64'>], 'CY': [<class 'bson.int64.Int64'>], 'CW': [<class 'bson.int64.Int64'>], 'CU': [<class 'bson.int64.Int64'>], 'HR': [<class 'bson.int64.Int64'>], 'CI': [<class 'bson.int64.Int64'>], 'CR': [<class 'bson.int64.Int64'>], 'CK': [<class 'bson.int64.Int64'>], 'CD': [<class 'bson.int64.Int64'>], 'CG': [<class 'bson.int64.Int64'>], 'KM': [<class 'bson.int64.Int64'>], 'CO': [<class 'bson.int64.Int64'>], 'CC': [<class 'bson.int64.Int64'>], 'CX': [<class 'bson.int64.Int64'>], 'CN': [<class 'bson.int64.Int64'>], 'CL': [<class 'bson.int64.Int64'>], 'TD': [<class 'bson.int64.Int64'>], 'CF': [<class 'bson.int64.Int64'>], 'KY': [<class 'bson.int64.Int64'>], 'CV': [<class 'bson.int64.Int64'>], 'CA': [<class 'bson.int64.Int64'>], 'CM': [<class 'bson.int64.Int64'>], 'KH': [<class 'bson.int64.Int64'>], 'BI': [<class 'bson.int64.Int64'>], 'BF': [<class 'bson.int64.Int64'>], 'BG': [<class 'bson.int64.Int64'>], 'BN': [<class 'bson.int64.Int64'>], 'IO': [<class 'bson.int64.Int64'>], 'BR': [<class 'bson.int64.Int64'>], 'BV': [<class 'bson.int64.Int64'>], 'BW': [<class 'bson.int64.Int64'>], 'BA': [<class 'bson.int64.Int64'>], 'BQ': [<class 'bson.int64.Int64'>], 'BO': [<class 'bson.int64.Int64'>], 'BT': [<class 'bson.int64.Int64'>], 'BM': [<class 'bson.int64.Int64'>], 'BJ': [<class 'bson.int64.Int64'>], 'BZ': [<class 'bson.int64.Int64'>], 'BE': [<class 'bson.int64.Int64'>], 'BY': [<class 'bson.int64.Int64'>], 'BB': [<class 'bson.int64.Int64'>], 'BD': [<class 'bson.int64.Int64'>], 'BH': [<class 'bson.int64.Int64'>], 'BS': [<class 'bson.int64.Int64'>], 'AZ': [<class 'bson.int64.Int64'>], 'AT': [<class 'bson.int64.Int64'>], 'AU': [<class 'bson.int64.Int64'>], 'AW': [<class 'bson.int64.Int64'>], 'AM': [<class 'bson.int64.Int64'>], 'AR': [<class 'bson.int64.Int64'>], 'AG': [<class 'bson.int64.Int64'>], 'AQ': [<class 'bson.int64.Int64'>], 'AI': [<class 'bson.int64.Int64'>], 'AO': [<class 'bson.int64.Int64'>], 'AS': [<class 'bson.int64.Int64'>], 'DZ': [<class 'bson.int64.Int64'>], 'AL': [<class 'bson.int64.Int64'>], 'AF': [<class 'bson.int64.Int64'>], 'AX': [<class 'bson.int64.Int64'>]}, []], 'adSourceData': [{'adSourceId': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'priority': [<class 'bson.int64.Int64'>]}, []], 'updated': [<class 'int'>, <class 'bson.int64.Int64'>], 'updatedDate': [<class 'str'>], 'excludeAdvertiserIds': [[], [<class 'bson.int64.Int64'>]], 'excludeSpecialType': [[]], 'outputType': None, 'adSourceTime': [[], {"<class 'int'>": [<class 'bson.int64.Int64'>]}], 'activeAdSources': [[[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>]], [], [[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>], [<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>], [<class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>], [<class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>], [<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>], [<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]], [[<class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>, <class 'bson.int64.Int64'>]]], 'setting': {'thirdPartyRequestNum': [<class 'bson.int64.Int64'>], 'apiRequestNum': [<class 'bson.int64.Int64'>], 'apiCacheNum': [<class 'bson.int64.Int64'>], 'ttcType': [<class 'bson.int64.Int64'>], 'waitingTime': [<class 'bson.int64.Int64'>], 'ctaMove': [<class 'bson.int64.Int64'>], 'mo': [<class 'bson.int64.Int64'>], 'vcn': [<class 'bson.int64.Int64'>], 'cbp': [<class 'float'>], 'dlnet': [<class 'bson.int64.Int64'>], 'autoplay': [<class 'bson.int64.Int64'>], 'callbackType': [<class 'bson.int64.Int64'>], 'clct': [<class 'bson.int64.Int64'>], 'clcq': [<class 'bson.int64.Int64'>], 'endScreen': [<class 'bson.int64.Int64'>], 'closeButtonDelay': [<class 'bson.int64.Int64'>], 'recallNet': [[<class 'bson.int64.Int64'>]], 'readyRate': [<class 'bson.int64.Int64'>], 'aqn': {"<class 'int'>": [<class 'bson.int64.Int64'>]}, 'acn': {"<class 'int'>": [<class 'bson.int64.Int64'>]}, 'impt': [<class 'bson.int64.Int64'>], 'degradeDisplay': [{'ALL': [<class 'bson.int64.Int64'>]}, []], 'dailyPlayCap': [<class 'bson.int64.Int64'>], 'videoSkipTime': [<class 'bson.int64.Int64'>], 'videoInteractiveType': [<class 'bson.int64.Int64'>], 'orientation': [<class 'bson.int64.Int64'>]}, 'cpcOfferList': [[], [<class 'bson.int64.Int64'>]], 'brandOfferList': [[], [<class 'bson.int64.Int64'>]], 'offsetList': [[], [<class 'bson.int64.Int64'>], {"<class 'int'>": [<class 'bson.int64.Int64'>, <class 'int'>]}], 'vbaConf': {'vbaClose': [<class 'bson.int64.Int64'>], 'vbaOption': [[], {'request_day': [<class 'bson.int64.Int64'>]}, {'install_day': [<class 'bson.int64.Int64'>]}, {'install_num': [<class 'bson.int64.Int64'>]}]}, 'landingPageVersion': [[], [<class 'str'>]], 'virtualReward': [[], {'id': [<class 'bson.int64.Int64'>]}, {'name': [<class 'str'>]}, {'app_id': [<class 'bson.int64.Int64'>]}, {'exchange_rate': [<class 'bson.int64.Int64'>]}, {'static_reward': [<class 'bson.int64.Int64'>]}], 'callbackUrl': [<class 'str'>], 'securityKey': [<class 'str'>], 'power': {'autoSwitch': [<class 'bson.int64.Int64'>], 'requestNum': [<class 'bson.int64.Int64'>], 'requestInterval': [<class 'bson.int64.Int64'>], 'cacheTime': [<class 'bson.int64.Int64'>], 'referCacheTime': [<class 'bson.int64.Int64'>], 'usedTime': [<class 'bson.int64.Int64'>], 'waitingTime': [<class 'bson.int64.Int64'>], 'offset': [<class 'bson.int64.Int64'>], 'broadcast': [<class 'bson.int64.Int64'>]}, 'unitSetting': {'tvStart': [<class 'float'>, <class 'bson.int64.Int64'>], 'tvEnd': [<class 'float'>, <class 'bson.int64.Int64'>], 'atf': {'status': [<class 'float'>], 'countries': [[<class 'str'>]]}, 'videoSkipResult': [<class 'bson.int64.Int64'>]}, 'preClick': [<class 'bool'>], 'blackList': [[<class 'bson.int64.Int64'>]], 'whiteList': [[]], 'subsidyRule': {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}, 'fakeRule': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'eCPM': [<class 'float'>], 'reduceMax': [<class 'bson.int64.Int64'>], 'plusMax': [<class 'bson.int64.Int64'>], 'amplitude': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'fakeRuleV2': {'ALL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>, <class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'US': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'IN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'JP': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'KR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'VN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AX': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'ID': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TW': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'FR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MX': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'RU': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TH': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GB': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AU': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'IT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'UK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SG': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'DE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MY': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'JO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'ES': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NZ': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NG': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PH': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'ZA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'HK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'QA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'KW': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'OM': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BH': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'EG': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NC': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'IL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'UY': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AS': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'KH': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AF': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'DZ': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AM': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'AZ': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BD': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BB': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BM': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'BG': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CM': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CG': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CW': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CY': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'DK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'DM': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'DO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'EC': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SV': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'FO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GF': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PF': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GY': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'HU': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'IQ': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'LA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'LB': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'LY': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'LT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MG': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MW': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MV': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MQ': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MM': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NP': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NI': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PS': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PY': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'PR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'RE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'RO': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'LC': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'MF': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'VC': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'RS': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SI': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SS': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'LK': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'SR': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'CH': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TZ': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TL': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TT': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'TN': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'UA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'VE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'YE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'IE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'GU': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'NA': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}, 'EE': {'install': [<class 'bson.int64.Int64'>], 'start': [<class 'str'>], 'status': [<class 'bson.int64.Int64'>], 'updated': [<class 'str'>]}}, 'fillRateUnit': {'ALL': {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'FR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ID': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JP': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'RU': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'US': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'DZ': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AU': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BD': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CF': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'MY': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ZA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ES': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'LK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'DE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'VN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'NL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'DK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'HK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'MX': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TW': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AM': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AZ': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CM': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SV': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'GT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'HN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KZ': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'LB': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'NI': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'RO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'VE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'EG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IQ': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UY': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KW': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'EC': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PY': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'LA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BJ': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CY': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'DO': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'GH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'HT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JM': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'KE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'MA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'NG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'QA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'RS': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'GB': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'OM': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AF': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BS': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CI': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'VI': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'GR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}, 'version': {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'US': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}, "<class 'int'>": {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}}, 'tryNewRate': [<class 'float'>, <class 'bson.int64.Int64'>], 'reduceRule': {'impression': [<class 'bson.int64.Int64'>], 'click': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>], 'priority': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'sspCampaignIds': [[<class 'bson.int64.Int64'>]], 'allowIp': [[<class 'str'>]], 'postbackM': [<class 'bson.int64.Int64'>], 'rewards': [{'id': [<class 'bson.int64.Int64'>], 'name': [<class 'str'>], 'amount': [<class 'bson.int64.Int64'>]}, []], 'endcard': {'urls': [{'id': [<class 'bson.int64.Int64'>], 'url': [<class 'str'>], 'weight': [<class 'bson.int64.Int64'>]}, []], 'status': [<class 'bson.int64.Int64'>], 'orientation': [<class 'bson.int64.Int64'>], 'videoTemplateUrl': [{'id': [<class 'bson.int64.Int64'>], 'url': [<class 'str'>], 'url_zip': [<class 'str'>], 'weight': [<class 'bson.int64.Int64'>]}, []]}, 'JUMP_TYPE_CONFIG_PUBLISHER': {"<class 'int'>": [<class 'float'>]}, 'appsetting': [{'pcto': [<class 'bson.int64.Int64'>], 'tcto': [<class 'bson.int64.Int64'>], 'pcrn': [<class 'bson.int64.Int64'>], 'uplc': [<class 'float'>, <class 'bson.int64.Int64'>], 'upmi': [<class 'float'>, <class 'bson.int64.Int64'>], 'upaid': [<class 'float'>, <class 'bson.int64.Int64'>], 'n2': [<class 'bson.int64.Int64'>, <class 'float'>], 'n3': [<class 'bson.int64.Int64'>, <class 'float'>], ' upaid': [<class 'bson.int64.Int64'>], 't_vba': [[<class 'float'>], [<class 'bson.int64.Int64'>], []], 'httpType': [<class 'float'>], 'ats_c': [<class 'float'>, <class 'bson.int64.Int64'>], 'jumptBw': [<class 'float'>, <class 'bson.int64.Int64'>], 'crashCt': [<class 'float'>, <class 'bson.int64.Int64'>], 'n4': [<class 'float'>, <class 'bson.int64.Int64'>], 'tcct': [<class 'float'>, <class 'bson.int64.Int64'>], 'storekit': [<class 'float'>]}, [], {'plc': [<class 'bson.int64.Int64'>]}, {'dut': [<class 'bson.int64.Int64'>]}, {'iex': [<class 'bson.int64.Int64'>]}, {'pctn': [<class 'bson.int64.Int64'>]}, {'strtaRate': [<class 'bson.int64.Int64'>]}, {'ilrf': [<class 'bson.int64.Int64'>]}, {'pf': [<class 'bson.int64.Int64'>]}, {'pb': [[]]}, {'pctrl': [{'full': [<class 'bson.int64.Int64'>]}]}, {'pctrl': [{'add': [<class 'bson.int64.Int64'>]}]}, {'pctrl': [{'delete': [<class 'bson.int64.Int64'>]}]}, {'pmax': [<class 'bson.int64.Int64'>]}, {'adct': [<class 'bson.int64.Int64'>]}, {'dlapk': [<class 'bson.int64.Int64'>]}], 'vtaConfigUnit': {'ALL': {'status': [<class 'bson.int64.Int64'>], 'rate': [<class 'bson.int64.Int64'>], 'rule': [<class 'bson.int64.Int64'>]}}, 'offerFreCap': [{"<class 'int'>": [<class 'bson.int64.Int64'>]}, []], 'JUMP_TYPE_CONFIG_PUBLISHER_IOS': {"<class 'int'>": [<class 'bson.int64.Int64'>]}, 'blend_traffic': {'app': [[<class 'str'>]]}, 'offerVbaIntval': [{"<class 'int'>": [<class 'bson.int64.Int64'>]}, []], 'vtaConfigApp': {'US': {'status': [<class 'bson.int64.Int64'>], 'rate': [<class 'bson.int64.Int64'>], 'rule': [<class 'bson.int64.Int64'>]}, 'ALL': {'status': [<class 'bson.int64.Int64'>], 'rate': [<class 'bson.int64.Int64'>], 'rule': [<class 'bson.int64.Int64'>]}}, 'advVbaIntval': {"<class 'int'>": [<class 'bson.int64.Int64'>]}, 'btCampaignIds': [[]], 'realPackageName': [<class 'str'>], 'fillRateApp': {'version': {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'FR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IT': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'JP': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'US': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'CA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}, 'ALL': {'US': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SA': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'AE': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'UK': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'PH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'IN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'ID': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'RU': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'BR': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'TH': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'VN': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}, 'SG': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}, "<class 'int'>": {'ALL': {'rate': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>]}}}, 'blackPackageList': [[<class 'str'>], []], 'blackCategoryList': [[], [<class 'bson.int64.Int64'>]], 'reduceRuleV2': {"<class 'int'>": {'priority': [<class 'bson.int64.Int64'>], 'install': [<class 'bson.int64.Int64'>], 'price': [<class 'bson.int64.Int64'>], 'status': [<class 'bson.int64.Int64'>], 'start': [<class 'bson.int64.Int64'>]}}, 'JUMP_TYPE_CONFIG': {"<class 'int'>": [<class 'float'>]}}
```

---
###Config:
```
 {
 _id :
	 <class 'bson.objectid.ObjectId'>
 key :
	 <class 'str'>
 value :
		 {
		 version :
			 {
			 unitSize :
				 <class 'str'>
			 imageSize :
				 <class 'str'>
			 imageSizeId :
				 <class 'bson.int64.Int64'>
			 }
		 domain :
			 <class 'str'>
		 format :
			 <class 'str'>
		 }
	 <class 'str'>
		 {
		 <class 'int'> :
			 <class 'float'>
			 <class 'str'>
				 [
				 <class 'str'>
				 ]
			 <class 'bson.int64.Int64'>
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 upal :
			 <class 'float'>
		 }
		 {
		 cfc :
			 <class 'float'>
		 }
		 {
		 getpf :
			 <class 'float'>
		 }
		 {
		 uplc :
			 <class 'float'>
		 }
		 {
		 cfb :
			 <class 'bool'>
		 }
		 {
		 cct :
			 <class 'float'>
		 }
		 {
		 pcs :
			 <class 'bool'>
		 }
		 {
		 pct :
			 <class 'bool'>
		 }
		 {
		 mo :
			 <class 'float'>
		 }
		 {
		 ttct :
			 <class 'float'>
		 }
		 {
		 awttct :
			 <class 'float'>
		 }
		 {
		 dmcr :
			 <class 'float'>
		 }
		 {
		 ncdn :
			 <class 'str'>
		 }
		 {
		 jabts :
			 <class 'bool'>
		 }
		 {
		 jt3r :
			 <class 'float'>
		 }
		 {
		 <class 'int'> :
				 {
				 name :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 append :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 android :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ios :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [subID] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [USER_AAID] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [TIME_STAMP] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [USER_ANDROID_ID] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {advertisingid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {your_clickid_here} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {your_subid_here} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {click_id} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {pubid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {gaid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 android :
			 <class 'float'>
		 }
		 {
		 ios :
			 <class 'float'>
		 }
		 {
		 plct :
			 <class 'float'>
		 }
		 {
		 spct :
			 <class 'float'>
		 }
		 {
		 awct :
			 <class 'float'>
		 }
		 {
		 uct :
			 <class 'float'>
		 }
		 {
		 rurl :
			 <class 'bool'>
		 }
		 {
		 ujds :
			 <class 'bool'>
		 }
		 {
		 n2 :
			 <class 'float'>
		 }
		 {
		 n3 :
			 <class 'float'>
		 }
		 {
		 n2a :
			 <class 'float'>
		 }
		 {
		 n3a :
			 <class 'float'>
		 }
		 {
		 n2b :
			 <class 'float'>
		 }
		 {
		 n3b :
			 <class 'float'>
		 }
		 {
		 abt :
			 <class 'float'>
		 }
		 {
		 getpf_rv :
			 <class 'float'>
		 }
		 {
		 ruct :
			 <class 'float'>
		 }
		 {
		 sfct :
			 <class 'float'>
		 }
		 {
		 <class 'int'> :
				 {
				 priority :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 install :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 start :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {sub_id} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
					 []
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [click_id] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [[clickid]] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 [[pub_subid]] :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {aid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {adid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {user_id} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {sub_1} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {pub_gaid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {pub_idfa} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {pub_aid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {publisher_slot} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {clickId} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {ifa} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {customParam} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {transaction_id} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {idfa} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {publisher_id} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {refid} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {aff_sub} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {advertising_id} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 replace :
						 {
						 {sub} :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 default :
			 <class 'float'>
		 }
		 {
		 min :
			 <class 'float'>
		 }
		 {
		 max :
			 <class 'float'>
		 }
		 {
		 global :
				 {
				 ad_server :
					 <class 'float'>
				 }
		 }
		 {
		 fcat :
			 <class 'bool'>
		 }
		 {
		 omt :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 pcsc :
				 [
				 <class 'float'>
				 ]
		 }
		 {
		 version :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 trueNumDefault :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 trueNumAppwall :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 domainTestPublishers :
				 [
				 <class 'float'>
				 ]
		 }
		 {
		 newUrlSwitch :
			 <class 'bool'>
		 }
		 {
		 IOSABtest :
				 {
				 <class 'int'> :
					 <class 'float'>
				 }
		 }
		 {
		 nativeApp :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 nativeAdvertiser :
				 [
				 <class 'bson.int64.Int64'>
				 ]
		 }
		 {
		 IOSTestConfTotal :
			 <class 'float'>
		 }
		 {
		 IOSTestConfA :
				 {
				 <class 'int'> :
					 <class 'float'>
				 }
		 }
		 {
		 IOSTestConfB :
			 <class 'float'>
		 }
		 {
		 domainTestAgent :
				 [
				 <class 'float'>
				 ]
		 }
		 {
		 trueNumRewardVideo :
			 <class 'float'>
		 }
		 {
		 trueNumFeedsVideo :
			 <class 'float'>
		 }
		 {
		 trueNumOfferwall :
			 <class 'float'>
		 }
		 {
		 trueNumInterstitialSDK :
			 <class 'float'>
		 }
		 {
		 trueNumOnlineVideo :
			 <class 'float'>
		 }
		 {
		 app_offer :
				 {
				 version :
						 [
						 <class 'str'>
						 ]
				 }
		 }
		 {
		 app :
				 {
				 <class 'int'> :
						 [
						 <class 'str'>
						 ]
				 }
		 }
		 {
		 sdkVersionAndroidMax :
			 <class 'str'>
		 }
		 {
		 osVersionAndroidMin :
			 <class 'str'>
		 }
		 {
		 sdkVersionAndroidInclude :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 sdkVersionIosMax :
			 <class 'str'>
		 }
		 {
		 offerList :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 packageList :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 install :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 status :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 start :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 ALL :
			 <class 'float'>
		 }
		 {
		 US :
			 <class 'float'>
		 }
		 {
		 http :
				 {
				 offerwall :
					 <class 'str'>
				 }
		 }
		 {
		 http :
				 {
				 interstitial_sdk :
					 <class 'str'>
				 }
		 }
		 {
		 http :
				 {
				 end_screen :
					 <class 'str'>
				 }
		 }
		 {
		 http :
				 {
				 rewardvideo_end_screen_v2 :
					 <class 'str'>
				 }
		 }
		 {
		 http :
				 {
				 rewardvideo_end_screen :
					 <class 'str'>
				 }
		 }
		 {
		 http :
				 {
				 rewardvideo_end_screen_cdn1 :
					 <class 'str'>
				 }
		 }
		 {
		 http :
				 {
				 rewardvideo_end_screen_cdn2 :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 offerwall :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 interstitial_sdk :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 end_screen :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 rewardvideo_end_screen_v2 :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 rewardvideo_end_screen :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 rewardvideo_end_screen_cdn1 :
					 <class 'str'>
				 }
		 }
		 {
		 https :
				 {
				 rewardvideo_end_screen_cdn2 :
					 <class 'str'>
				 }
		 }
		 {
		 ios_cdn_rate :
			 <class 'float'>
		 }
		 {
		 ios_cdn_country_code :
			 []
		 }
		 {
		 ALL :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ALL :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ALL :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 US :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 US :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 US :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 IN :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 IN :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 IN :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ID :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ID :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ID :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 TW :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 TW :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 TW :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MY :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MY :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MY :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SA :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SA :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SA :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KR :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KR :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KR :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 RU :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 RU :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 RU :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BR :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BR :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BR :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SG :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SG :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SG :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MM :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MM :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MM :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ZA :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ZA :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ZA :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MX :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MX :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MX :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 CA :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 CA :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 CA :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 PH :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 PH :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 PH :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KW :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KW :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KW :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 TR :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 TR :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 TR :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 EG :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 EG :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 EG :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 QA :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 QA :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 QA :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AR :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AR :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AR :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AE :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AE :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AE :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 HU :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 HU :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 HU :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 CO :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 CO :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 CO :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 FI :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 FI :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 FI :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BE :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BE :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BE :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AF :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AF :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 AF :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BH :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BH :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BH :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SO :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SO :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SO :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NG :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NG :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NG :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NO :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NO :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NO :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 LK :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 LK :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 LK :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 YE :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 YE :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 YE :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NZ :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NZ :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 NZ :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MO :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MO :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MO :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MV :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MV :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MV :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MN :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MN :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 MN :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KE :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KE :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 KE :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 IR :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 IR :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 IR :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SD :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SD :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SD :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SY :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SY :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SY :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 GY :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 GY :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 GY :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ET :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ET :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 ET :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SS :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SS :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 SS :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 PF :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 PF :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 PF :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BQ :
				 {
				 status :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BQ :
				 {
				 rate :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 BQ :
				 {
				 rule :
					 <class 'bson.int64.Int64'>
				 }
		 }
		 {
		 apps :
				 [
				 <class 'float'>
				 ]
		 }
		 {
		 device_models :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 countries :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 campaign :
				 {
				 offerId :
					 <class 'str'>
				 }
		 }
		 {
		 campaign :
				 {
				 priceOut :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 appId :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 unitId :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 ip :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 deviceModel :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 idfa :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 gaid :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 osVersion :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 countryCode :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext1 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext2 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext3 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext4 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext5 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext6 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext7 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext8 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext9 :
					 <class 'str'>
				 }
		 }
		 {
		 extra :
				 {
				 ext10 :
					 <class 'str'>
				 }
		 }
		 {
		 campaign :
				 {
				 campaignId :
					 <class 'str'>
				 }
		 }
		 {
		 campaign :
				 {
				 price :
					 <class 'str'>
				 }
		 }
		 {
		 params :
				 {
				 googleAdvertisingId :
					 <class 'str'>
				 }
		 }
		 {
		 app :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 device_mode :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 sdk_version :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 apk_url :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 all :
			 <class 'float'>
		 }
		 {
		 <class 'int'> :
				 {
				 US :
						 {
						 status :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 US :
						 {
						 rate :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 US :
						 {
						 rule :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 status :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 rate :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 rule :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
					 <class 'str'>
				 }
		 }
		 {
		 unit :
				 [
				 <class 'float'>
				 ]
		 }
		 {
		 <class 'int'> :
				 {
				 ma :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 mal :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 nxa :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 mp :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 mi :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 nxi :
					 <class 'str'>
				 }
		 }
		 {
		 appId :
			 <class 'float'>
		 }
		 {
		 unitId :
			 <class 'float'>
		 }
		 {
		 urls :
				 [
					 {
					 id :
						 <class 'bson.int64.Int64'>
					 }
				 ]
		 }
		 {
		 urls :
				 [
					 {
					 url :
						 <class 'str'>
					 }
				 ]
		 }
		 {
		 urls :
				 [
					 {
					 weight :
						 <class 'bson.int64.Int64'>
					 }
				 ]
		 }
		 {
		 orientation :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 videoTemplateUrl :
			 []
		 }
		 {
		 singapore :
			 <class 'float'>
				 [
				 <class 'str'>
				 ]
			 <class 'bson.int64.Int64'>
		 }
		 {
		 frankfurt :
			 <class 'float'>
				 [
				 <class 'str'>
				 ]
			 <class 'bson.int64.Int64'>
		 }
		 {
		 virginia :
			 <class 'float'>
				 [
				 <class 'str'>
				 ]
			 <class 'bson.int64.Int64'>
		 }
		 {
		 -1 :
			 <class 'float'>
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
						 {
						 <class 'int'> :
							 <class 'str'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 include :
						 [
						 <class 'str'>
						 ]
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 exclude :
					 []
				 }
		 }
		 {
		 switch :
			 <class 'float'>
		 }
		 {
		 rand :
			 <class 'float'>
		 }
		 {
		 platform_android :
			 <class 'str'>
		 }
		 {
		 platform_ios :
			 <class 'str'>
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id907394059 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id840127349 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id503451073 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id785385147 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id483693909 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 com_shopee_vn :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 blibli_mobile_commerce :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 com_yandex_browser :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 com_garena_game_kgid :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 com_skout_android :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id911793120 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id1137673647 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 block_config :
				 {
				 dev_package :
						 {
						 id1206761632 :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 SDK_VTA :
				 {
				 android :
						 {
						 version :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 SDK_VTA :
				 {
				 android :
						 {
						 exclude_version :
								 [
								 <class 'float'>
								 ]
						 }
				 }
		 }
		 {
		 SDK_VTA :
				 {
				 ios :
						 {
						 version :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 SDK_VTA :
				 {
				 ios :
						 {
						 exclude_version :
							 []
						 }
				 }
		 }
		 {
		 OS_VERSION_ENDCARD :
				 {
				 android :
						 {
						 version :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 OS_VERSION_ENDCARD :
				 {
				 android :
						 {
						 exclude_version :
							 []
						 }
				 }
		 }
		 {
		 OS_VERSION_ENDCARD :
				 {
				 ios :
						 {
						 version :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 OS_VERSION_ENDCARD :
				 {
				 ios :
						 {
						 exclude_version :
							 []
						 }
				 }
		 }
		 {
		 playable :
				 {
				 android :
						 {
						 version :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 playable :
				 {
				 android :
						 {
						 exclude_version :
							 []
						 }
				 }
		 }
		 {
		 playable :
				 {
				 ios :
						 {
						 version :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 playable :
				 {
				 ios :
						 {
						 exclude_version :
							 []
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 EG :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 EG :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 MX :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 MX :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 DZ :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 DZ :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 AR :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 AR :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 BD :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 BD :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 BO :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 BO :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 DO :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 DO :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 EC :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 EC :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 IQ :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 IQ :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 KZ :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 KZ :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 LY :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 LY :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 MM :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 MM :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 PE :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 PE :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 SD :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 SD :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 VE :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 VE :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 YE :
								 {
								 rate :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 ALL :
						 {
						 YE :
								 {
								 status :
									 <class 'bson.int64.Int64'>
								 }
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
						 {
						 priority :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
						 {
						 install :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
						 {
						 price :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
						 {
						 status :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 <class 'int'> :
						 {
						 start :
							 <class 'bson.int64.Int64'>
						 }
				 }
		 }
		 {
		 id :
			 <class 'bson.int64.Int64'>
		 }
		 {
		 url :
			 <class 'str'>
		 }
		 {
		 url_zip :
			 <class 'str'>
		 }
		 {
		 paused_url :
			 <class 'str'>
		 }
		 {
		 paused_url_zip :
			 <class 'str'>
		 }
		 {
		 rate :
			 <class 'float'>
			 <class 'bson.int64.Int64'>
		 }
		 {
		 def :
			 <class 'float'>
		 }
		 {
		 <class 'int'> :
				 {
				 url :
					 <class 'str'>
				 }
		 }
		 {
		 <class 'int'> :
				 {
				 rate :
						 {
						 <class 'int'> :
							 <class 'float'>
						 }
				 }
		 }
		 {
		 units :
				 [
				 <class 'float'>
				 ]
		 }
		 {
		 domains :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 cndomain :
			 <class 'str'>
		 }
		 {
		 countrys :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 key_int :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 key_float :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 key_string :
			 []
		 }
		 {
		 MPALL :
			 <class 'float'>
		 }
		 {
		 SAALL :
			 <class 'float'>
		 }
		 {
		 search :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 replace :
				 [
				 <class 'str'>
				 ]
		 }
		 {
		 USD_CNY :
			 <class 'str'>
		 }
 updated :
	 <class 'bson.int64.Int64'>
 updatedDate :
	 <class 'str'>
 }
```

```
{'_id': [<class 'bson.objectid.ObjectId'>], 'key': [<class 'str'>], 'value': [{'version': {'unitSize': [<class 'str'>], 'imageSize': [<class 'str'>], 'imageSizeId': [<class 'bson.int64.Int64'>]}, 'domain': [<class 'str'>], 'format': [<class 'str'>]}, <class 'str'>, {"<class 'int'>": [<class 'float'>, <class 'str'>, [<class 'str'>], <class 'bson.int64.Int64'>, [], [<class 'bson.int64.Int64'>]]}, {'upal': [<class 'float'>]}, {'cfc': [<class 'float'>]}, {'getpf': [<class 'float'>]}, {'uplc': [<class 'float'>]}, {'cfb': [<class 'bool'>]}, {'cct': [<class 'float'>]}, {'pcs': [<class 'bool'>]}, {'pct': [<class 'bool'>]}, {'mo': [<class 'float'>]}, {'ttct': [<class 'float'>]}, {'awttct': [<class 'float'>]}, {'dmcr': [<class 'float'>]}, {'ncdn': [<class 'str'>]}, {'jabts': [<class 'bool'>]}, {'jt3r': [<class 'float'>]}, {"<class 'int'>": [{'name': [<class 'str'>]}]}, {"<class 'int'>": [{'append': [<class 'str'>]}]}, {"<class 'int'>": [{'android': [<class 'str'>]}]}, {"<class 'int'>": [{'ios': [<class 'str'>]}]}, {"<class 'int'>": [{'replace': [{'[subID]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'[USER_AAID]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'[TIME_STAMP]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'[USER_ANDROID_ID]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{advertisingid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{your_clickid_here}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{your_subid_here}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{click_id}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{pubid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{gaid}': [<class 'str'>]}]}]}, {'android': [<class 'float'>]}, {'ios': [<class 'float'>]}, {'plct': [<class 'float'>]}, {'spct': [<class 'float'>]}, {'awct': [<class 'float'>]}, {'uct': [<class 'float'>]}, {'rurl': [<class 'bool'>]}, {'ujds': [<class 'bool'>]}, {'n2': [<class 'float'>]}, {'n3': [<class 'float'>]}, {'n2a': [<class 'float'>]}, {'n3a': [<class 'float'>]}, {'n2b': [<class 'float'>]}, {'n3b': [<class 'float'>]}, {'abt': [<class 'float'>]}, {'getpf_rv': [<class 'float'>]}, {'ruct': [<class 'float'>]}, {'sfct': [<class 'float'>]}, {"<class 'int'>": [{'priority': [<class 'bson.int64.Int64'>]}]}, {"<class 'int'>": [{'install': [<class 'bson.int64.Int64'>]}]}, {"<class 'int'>": [{'status': [<class 'bson.int64.Int64'>]}]}, {"<class 'int'>": [{'start': [<class 'bson.int64.Int64'>]}]}, {"<class 'int'>": [{'replace': [{'{sub_id}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [[]]}]}, {"<class 'int'>": [{'replace': [{'[click_id]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'[[clickid]]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'[[pub_subid]]': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{aid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{adid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{user_id}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{sub_1}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{pub_gaid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{pub_idfa}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{pub_aid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{publisher_slot}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{clickId}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{ifa}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{customParam}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{transaction_id}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{idfa}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{publisher_id}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{refid}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{aff_sub}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{advertising_id}': [<class 'str'>]}]}]}, {"<class 'int'>": [{'replace': [{'{sub}': [<class 'str'>]}]}]}, {'default': [<class 'float'>]}, {'min': [<class 'float'>]}, {'max': [<class 'float'>]}, {'global': [{'ad_server': [<class 'float'>]}]}, {'fcat': [<class 'bool'>]}, {'omt': [<class 'bson.int64.Int64'>]}, {'pcsc': [[<class 'float'>]]}, {'version': [<class 'bson.int64.Int64'>]}, {'trueNumDefault': [<class 'bson.int64.Int64'>]}, {'trueNumAppwall': [<class 'bson.int64.Int64'>]}, {'domainTestPublishers': [[<class 'float'>]]}, {'newUrlSwitch': [<class 'bool'>]}, {'IOSABtest': [{"<class 'int'>": [<class 'float'>]}]}, {'nativeApp': [[<class 'bson.int64.Int64'>]]}, {'nativeAdvertiser': [[<class 'bson.int64.Int64'>]]}, {'IOSTestConfTotal': [<class 'float'>]}, {'IOSTestConfA': [{"<class 'int'>": [<class 'float'>]}]}, {'IOSTestConfB': [<class 'float'>]}, {'domainTestAgent': [[<class 'float'>]]}, {'trueNumRewardVideo': [<class 'float'>]}, {'trueNumFeedsVideo': [<class 'float'>]}, {'trueNumOfferwall': [<class 'float'>]}, {'trueNumInterstitialSDK': [<class 'float'>]}, {'trueNumOnlineVideo': [<class 'float'>]}, {'app_offer': [{'version': [[<class 'str'>]]}]}, {'app': [{"<class 'int'>": [[<class 'str'>]]}]}, {'sdkVersionAndroidMax': [<class 'str'>]}, {'osVersionAndroidMin': [<class 'str'>]}, {'sdkVersionAndroidInclude': [[<class 'str'>]]}, {'sdkVersionIosMax': [<class 'str'>]}, {'offerList': [[<class 'str'>]]}, {'packageList': [[<class 'str'>]]}, {'install': [<class 'bson.int64.Int64'>]}, {'status': [<class 'bson.int64.Int64'>]}, {'start': [<class 'bson.int64.Int64'>]}, {'ALL': [<class 'float'>]}, {'US': [<class 'float'>]}, {'http': [{'offerwall': [<class 'str'>]}]}, {'http': [{'interstitial_sdk': [<class 'str'>]}]}, {'http': [{'end_screen': [<class 'str'>]}]}, {'http': [{'rewardvideo_end_screen_v2': [<class 'str'>]}]}, {'http': [{'rewardvideo_end_screen': [<class 'str'>]}]}, {'http': [{'rewardvideo_end_screen_cdn1': [<class 'str'>]}]}, {'http': [{'rewardvideo_end_screen_cdn2': [<class 'str'>]}]}, {'https': [{'offerwall': [<class 'str'>]}]}, {'https': [{'interstitial_sdk': [<class 'str'>]}]}, {'https': [{'end_screen': [<class 'str'>]}]}, {'https': [{'rewardvideo_end_screen_v2': [<class 'str'>]}]}, {'https': [{'rewardvideo_end_screen': [<class 'str'>]}]}, {'https': [{'rewardvideo_end_screen_cdn1': [<class 'str'>]}]}, {'https': [{'rewardvideo_end_screen_cdn2': [<class 'str'>]}]}, {'ios_cdn_rate': [<class 'float'>]}, {'ios_cdn_country_code': [[]]}, {'ALL': [{'status': [<class 'bson.int64.Int64'>]}]}, {'ALL': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'ALL': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'US': [{'status': [<class 'bson.int64.Int64'>]}]}, {'US': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'US': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'IN': [{'status': [<class 'bson.int64.Int64'>]}]}, {'IN': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'IN': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'ID': [{'status': [<class 'bson.int64.Int64'>]}]}, {'ID':f [{'rate': [<class 'bson.int64.Int64'>]}]}, {'ID': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'TW': [{'status': [<class 'bson.int64.Int64'>]}]}, {'TW': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'TW': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'MY': [{'status': [<class 'bson.int64.Int64'>]}]}, {'MY': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'MY': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'SA': [{'status': [<class 'bson.int64.Int64'>]}]}, {'SA': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'SA': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'KR': [{'status': [<class 'bson.int64.Int64'>]}]}, {'KR': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'KR': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'RU': [{'status': [<class 'bson.int64.Int64'>]}]}, {'RU': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'RU': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'BR': [{'status': [<class 'bson.int64.Int64'>]}]}, {'BR': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'BR': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'SG': [{'status': [<class 'bson.int64.Int64'>]}]}, {'SG': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'SG': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'MM': [{'status': [<class 'bson.int64.Int64'>]}]}, {'MM': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'MM': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'ZA': [{'status': [<class 'bson.int64.Int64'>]}]}, {'ZA': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'ZA': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'MX': [{'status': [<class 'bson.int64.Int64'>]}]}, {'MX': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'MX': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'CA': [{'status': [<class 'bson.int64.Int64'>]}]}, {'CA': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'CA': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'PH': [{'status': [<class 'bson.int64.Int64'>]}]}, {'PH': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'PH': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'KW': [{'status': [<class 'bson.int64.Int64'>]}]}, {'KW': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'KW': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'TR': [{'status': [<class 'bson.int64.Int64'>]}]}, {'TR': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'TR': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'EG': [{'status': [<class 'bson.int64.Int64'>]}]}, {'EG': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'EG': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'QA': [{'status': [<class 'bson.int64.Int64'>]}]}, {'QA': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'QA': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'AR': [{'status': [<class 'bson.int64.Int64'>]}]}, {'AR': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'AR': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'AE': [{'status': [<class 'bson.int64.Int64'>]}]}, {'AE': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'AE': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'HU': [{'status': [<class 'bson.int64.Int64'>]}]}, {'HU': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'HU': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'CO': [{'status': [<class 'bson.int64.Int64'>]}]}, {'CO': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'CO': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'FI': [{'status': [<class 'bson.int64.Int64'>]}]}, {'FI': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'FI': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'BE': [{'status': [<class 'bson.int64.Int64'>]}]}, {'BE': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'BE': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'AF': [{'status': [<class 'bson.int64.Int64'>]}]}, {'AF': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'AF': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'BH': [{'status': [<class 'bson.int64.Int64'>]}]}, {'BH': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'BH': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'SO': [{'status': [<class 'bson.int64.Int64'>]}]}, {'SO': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'SO': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'NG': [{'status': [<class 'bson.int64.Int64'>]}]}, {'NG': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'NG': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'NO': [{'status': [<class 'bson.int64.Int64'>]}]}, {'NO': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'NO': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'LK': [{'status': [<class 'bson.int64.Int64'>]}]}, {'LK': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'LK': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'YE': [{'status': [<class 'bson.int64.Int64'>]}]}, {'YE': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'YE': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'NZ': [{'status': [<class 'bson.int64.Int64'>]}]}, {'NZ': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'NZ': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'MO': [{'status': [<class 'bson.int64.Int64'>]}]}, {'MO': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'MO': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'MV': [{'status': [<class 'bson.int64.Int64'>]}]}, {'MV': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'MV': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'MN': [{'status': [<class 'bson.int64.Int64'>]}]}, {'MN': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'MN': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'KE': [{'status': [<class 'bson.int64.Int64'>]}]}, {'KE': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'KE': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'IR': [{'status': [<class 'bson.int64.Int64'>]}]}, {'IR': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'IR': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'SD': [{'status': [<class 'bson.int64.Int64'>]}]}, {'SD': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'SD': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'SY': [{'status': [<class 'bson.int64.Int64'>]}]}, {'SY': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'SY': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'GY': [{'status': [<class 'bson.int64.Int64'>]}]}, {'GY': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'GY': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'ET': [{'status': [<class 'bson.int64.Int64'>]}]}, {'ET': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'ET': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'SS': [{'status': [<class 'bson.int64.Int64'>]}]}, {'SS': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'SS': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'PF': [{'status': [<class 'bson.int64.Int64'>]}]}, {'PF': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'PF': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'BQ': [{'status': [<class 'bson.int64.Int64'>]}]}, {'BQ': [{'rate': [<class 'bson.int64.Int64'>]}]}, {'BQ': [{'rule': [<class 'bson.int64.Int64'>]}]}, {'apps': [[<class 'float'>]]}, {'device_models': [[<class 'str'>]]}, {'countries': [[<class 'str'>]]}, {'campaign': [{'offerId': [<class 'str'>]}]}, {'campaign': [{'priceOut': [<class 'str'>]}]}, {'params': [{'appId': [<class 'str'>]}]}, {'params': [{'unitId': [<class 'str'>]}]}, {'params': [{'ip': [<class 'str'>]}]}, {'params': [{'deviceModel': [<class 'str'>]}]}, {'params': [{'idfa': [<class 'str'>]}]}, {'params': [{'gaid': [<class 'str'>]}]}, {'params': [{'osVersion': [<class 'str'>]}]}, {'params': [{'countryCode': [<class 'str'>]}]}, {'extra': [{'ext1': [<class 'str'>]}]}, {'extra': [{'ext2': [<class 'str'>]}]}, {'extra': [{'ext3': [<class 'str'>]}]}, {'extra': [{'ext4': [<class 'str'>]}]}, {'extra': [{'ext5': [<class 'str'>]}]}, {'extra': [{'ext6': [<class 'str'>]}]}, {'extra': [{'ext7': [<class 'str'>]}]}, {'extra': [{'ext8': [<class 'str'>]}]}, {'extra': [{'ext9': [<class 'str'>]}]}, {'extra': [{'ext10': [<class 'str'>]}]}, {'campaign': [{'campaignId': [<class 'str'>]}]}, {'campaign': [{'price': [<class 'str'>]}]}, {'params': [{'googleAdvertisingId': [<class 'str'>]}]}, {'app': [[<class 'str'>]]}, {'device_mode': [[<class 'str'>]]}, {'sdk_version': [[<class 'str'>]]}, {'apk_url': [[<class 'str'>]]}, {'all': [<class 'float'>]}, {"<class 'int'>": [{'US': [{'status': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{'US': [{'rate': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{'US': [{'rule': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{'ALL': [{'status': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{'ALL': [{'rate': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{'ALL': [{'rule': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{"<class 'int'>": [<class 'str'>]}]}, {'unit': [[<class 'float'>], []]}, {"<class 'int'>": [{'ma': [<class 'str'>]}]}, {"<class 'int'>": [{'mal': [<class 'str'>]}]}, {"<class 'int'>": [{'nxa': [<class 'str'>]}]}, {"<class 'int'>": [{'mp': [<class 'str'>]}]}, {"<class 'int'>": [{'mi': [<class 'str'>]}]}, {"<class 'int'>": [{'nxi': [<class 'str'>]}]}, {'appId': [<class 'float'>]}, {'unitId': [<class 'float'>]}, {'urls': [[{'id': [<class 'bson.int64.Int64'>]}]]}, {'urls': [[{'url': [<class 'str'>]}]]}, {'urls': [[{'weight': [<class 'bson.int64.Int64'>]}]]}, {'orientation': [<class 'bson.int64.Int64'>]}, {'videoTemplateUrl': [[]]}, {'singapore': [<class 'float'>, [<class 'str'>], <class 'bson.int64.Int64'>]}, {'frankfurt': [<class 'float'>, [<class 'str'>], <class 'bson.int64.Int64'>]}, {'virginia': [<class 'float'>, [<class 'str'>], <class 'bson.int64.Int64'>]}, {'-1': [<class 'float'>]}, {"<class 'int'>": [{"<class 'int'>": [{"<class 'int'>": [<class 'str'>]}]}]}, {"<class 'int'>": [{'include': [[<class 'str'>]]}]}, {"<class 'int'>": [{'exclude': [[]]}]}, {'switch': [<class 'float'>]}, {'rand': [<class 'float'>]}, {'platform_android': [<class 'str'>]}, {'platform_ios': [<class 'str'>]}, {'block_config': [{'dev_package': [{'id907394059': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id840127349': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id503451073': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id785385147': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id483693909': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'com_shopee_vn': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'blibli_mobile_commerce': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'com_yandex_browser': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'com_garena_game_kgid': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'com_skout_android': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id911793120': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id1137673647': [<class 'float'>]}]}]}, {'block_config': [{'dev_package': [{'id1206761632': [<class 'float'>]}]}]}, {'SDK_VTA': [{'android': [{'version': [<class 'float'>]}]}]}, {'SDK_VTA': [{'android': [{'exclude_version': [[<class 'float'>]]}]}]}, {'SDK_VTA': [{'ios': [{'version': [<class 'float'>]}]}]}, {'SDK_VTA': [{'ios': [{'exclude_version': [[]]}]}]}, {'OS_VERSION_ENDCARD': [{'android': [{'version': [<class 'float'>]}]}]}, {'OS_VERSION_ENDCARD': [{'android': [{'exclude_version': [[]]}]}]}, {'OS_VERSION_ENDCARD': [{'ios': [{'version': [<class 'float'>]}]}]}, {'OS_VERSION_ENDCARD': [{'ios': [{'exclude_version': [[]]}]}]}, {'playable': [{'android': [{'version': [<class 'float'>]}]}]}, {'playable': [{'android': [{'exclude_version': [[]]}]}]}, {'playable': [{'ios': [{'version': [<class 'float'>]}]}]}, {'playable': [{'ios': [{'exclude_version': [[]]}]}]}, {"<class 'int'>": [{'ALL': [{'EG': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'EG': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'MX': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'MX': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'DZ': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'DZ': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'AR': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'AR': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'BD': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'BD': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'BO': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'BO': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'DO': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'DO': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'EC': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'EC': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'IQ': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'IQ': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'KZ': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'KZ': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'LY': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'LY': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'MM': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'MM': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'PE': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'PE': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'SD': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'SD': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'VE': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'VE': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'YE': [{'rate': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{'ALL': [{'YE': [{'status': [<class 'bson.int64.Int64'>]}]}]}]}, {"<class 'int'>": [{"<class 'int'>": [{'priority': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{"<class 'int'>": [{'install': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{"<class 'int'>": [{'price': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{"<class 'int'>": [{'status': [<class 'bson.int64.Int64'>]}]}]}, {"<class 'int'>": [{"<class 'int'>": [{'start': [<class 'bson.int64.Int64'>]}]}]}, {'id': [<class 'bson.int64.Int64'>]}, {'url': [<class 'str'>]}, {'url_zip': [<class 'str'>]}, {'paused_url': [<class 'str'>]}, {'paused_url_zip': [<class 'str'>]}, {'rate': [<class 'float'>, <class 'bson.int64.Int64'>]}, {'def': [<class 'float'>]}, {"<class 'int'>": [{'url': [<class 'str'>]}]}, {"<class 'int'>": [{'rate': [{"<class 'int'>": [<class 'float'>]}]}]}, {'units': [[<class 'float'>]]}, {'domains': [[<class 'str'>]]}, {'cndomain': [<class 'str'>]}, {'countrys': [[<class 'str'>]]}, {'key_int': [[<class 'str'>]]}, {'key_float': [[<class 'str'>]]}, {'key_string': [[]]}, {'MPALL': [<class 'float'>]}, {'SAALL': [<class 'float'>]}, {'search': [[<class 'str'>]]}, {'replace': [[<class 'str'>]]}, {'USD_CNY': [<class 'str'>]}], 'updated': [<class 'bson.int64.Int64'>], 'updatedDate': [<class 'str'>]}
```

---
###Tabs:
```
{
 _id :
	 <class 'bson.objectid.ObjectId'>
 key :
	 <class 'str'>
 Featured :
	 <class 'str'>
 Games :
	 <class 'str'>
 Apps :
	 <class 'str'>
 EditorsPick :
	 <class 'str'>
 AwesomeApps :
	 <class 'str'>
 YouMayLike :
	 <class 'str'>
 }
```

```
{'_id': [<class 'bson.objectid.ObjectId'>], 'key': [<class 'str'>], 'Featured': [<class 'str'>], 'Games': [<class 'str'>], 'Apps': [<class 'str'>], 'EditorsPick': [<class 'str'>], 'AwesomeApps': [<class 'str'>], 'YouMayLike': [<class 'str'>]}
```
