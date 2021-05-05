## fizzbuzz api
Yes I am serious

---

![GitHub top language](https://img.shields.io/github/languages/top/cccaaannn/fizzbuzz_api?style=flat-square) ![](https://img.shields.io/github/repo-size/cccaaannn/fizzbuzz_api?style=flat-square) [![GitHub license](https://img.shields.io/github/license/cccaaannn/fizzbuzz_api?style=flat-square)](https://github.com/cccaaannn/fizzbuzz_api/blob/master/LICENSE)


### I might not keep this running for obvious reasons.
## [fizz-buzz.xyz](fizz-buzz.xyz)

<br>

### But you can deploy it yourself, even though I don't know why would you want this 🤷🏻‍♂️. (Also check the `fizzbuzz.cfg` file for some customization)
- Install `requirements.txt`
- run `waitress_server.py`
```shell
python waitress_server.py
```

<br>

## API examples

Regular fizzbuzz 1 to 100 with \n's
```
/api
```

```
{
  "data": "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16\n17\nfizz\n19\nbuzz\nfizz\n22\n23\nfizz\nbuzz\n26\nfizz\n28\n29\nfizzbuzz\n31\n32\nfizz\n34\nbuzz\nfizz\n37\n38\nfizz\nbuzz\n41\nfizz\n43\n44\nfizzbuzz\n46\n47\nfizz\n49\nbuzz\nfizz\n52\n53\nfizz\nbuzz\n56\nfizz\n58\n59\nfizzbuzz\n61\n62\nfizz\n64\nbuzz\nfizz\n67\n68\nfizz\nbuzz\n71\nfizz\n73\n74\nfizzbuzz\n76\n77\nfizz\n79\nbuzz\nfizz\n82\n83\nfizz\nbuzz\n86\nfizz\n88\n89\nfizzbuzz\n91\n92\nfizz\n94\nbuzz\nfizz\n97\n98\nfizz\nbuzz", 
  "info": "", 
  "status": "success"
}
```

You can choose start, stop points and convert to_list
```
/api?start=10&stop=50&to_list
```

```
{
  "data": ["buzz", "11", "fizz", "13", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz", "fizz", "22", "23", "fizz", "buzz", "26", "fizz", "28", "29", "fizzbuzz", "31", "32", "fizz", "34", "buzz", "fizz", "37", "38", "fizz", "buzz", "41", "fizz", "43", "44", "fizzbuzz", "46", "47", "fizz", "49", "buzz"], 
  "info": "", 
  "status": "success"
}
```

It is also possible to customize the divisors and words
```javascript
const url = "/api";

async function getFizzBuzzCustom(){
    const custom_fizzbuzz = JSON.stringify({ 
        "custom_fizzbuzz":[
            {"word":"fozz", "divisors":[2]},
            {"word":"fizz", "divisors":[3]},
            {"word":"buzz", "divisors":[5]},
            {"word":"fizzbuzz", "divisors":[3,5]},
            {"word":"fozzfizz", "divisors":[2,3]},
            {"word":"fozzbuzz", "divisors":[2,5]},
            {"word":"fozzfizzbuzz", "divisors":[2,3,5]}
        ]
    });

    const newURL = url + "?&stop=30";

    const response = await fetch(newURL, {
        method: "post",
        body: custom_fizzbuzz,
        headers: { 
            "Content-Type": "application/json" 
        },
    });

    const data = await response.json();
    return data
}
```

```
{
    "data": "1\nfozz\nfizz\nfozz\nbuzz\nfozzfizz\n7\nfozz\nfizz\nfozzbuzz\n11\nfozzfizz\n13\nfozz\nfizzbuzz\nfozz\n17\nfozzfizz\n19\nfozzbuzz\nfizz\nfozz\n23\nfozzfizz\nbuzz\nfozz\nfizz\nfozz\n29\nfozzfizzbuzz",
    "info": "",
    "status": "success"
}
```


