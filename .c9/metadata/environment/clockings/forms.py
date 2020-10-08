{"filter":false,"title":"forms.py","tooltip":"/clockings/forms.py","undoManager":{"mark":42,"position":42,"stack":[[{"start":{"row":0,"column":0},"end":{"row":6,"column":89},"action":"insert","lines":["from django import forms","from .models import PersonalDetails","","class PersonalDetailsForm(forms.ModelForm):","    class Meta:","        model = PersonalDetails","        fields = ('address_1', 'address_2', 'county', 'contact_number', 'personal_email')"],"id":1}],[{"start":{"row":6,"column":89},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":7,"column":0},"end":{"row":7,"column":8},"action":"insert","lines":["        "]},{"start":{"row":7,"column":8},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["    "],"id":3},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":["l"],"id":5}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["c"],"id":6},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":["l"]},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":["a"]},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["s"]},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":[" "],"id":7},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["C"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["l"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["c"],"id":8},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["k"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["i"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["n"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["g"],"id":9},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["n"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["i"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["k"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["c"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"remove","lines":["o"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"remove","lines":["l"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"remove","lines":["C"]}],[{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":[","],"id":10}],[{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":[" "],"id":11},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["C"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["l"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["o"]},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["c"]},{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":["k"]},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["i"]},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["g"],"id":12}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["C"],"id":13},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["l"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["o"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["c"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["k"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["i"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["n"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["g"]}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":16},"action":"insert","lines":["()"],"id":14}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":16},"action":"remove","lines":["()"],"id":15}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["F"],"id":16},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["o"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["r"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["m"]}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":20},"action":"insert","lines":["()"],"id":17}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["f"],"id":18},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["o"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["r"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["m"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["."],"id":19},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["M"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["o"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["d"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["e"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":30},"action":"remove","lines":["Model"],"id":20},{"start":{"row":9,"column":25},"end":{"row":9,"column":34},"action":"insert","lines":["ModelForm"]}],[{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":[":"],"id":21}],[{"start":{"row":9,"column":36},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["c"],"id":23},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["l"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["a"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["s"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":[" "],"id":24},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["M"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["e"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["a"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["t"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"remove","lines":["e"],"id":25},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"remove","lines":["t"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["a"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["t"],"id":26},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":[":"],"id":27}],[{"start":{"row":10,"column":15},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["m"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["o"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["d"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["e"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":[" "],"id":29},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":[" "],"id":30},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["C"]}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["l"],"id":31},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["o"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["c"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["k"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["i"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["n"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["g"]}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":24},"action":"remove","lines":["Clocking"],"id":32},{"start":{"row":11,"column":16},"end":{"row":11,"column":24},"action":"insert","lines":["Clocking"]}],[{"start":{"row":11,"column":24},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":12,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["        "]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["f"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["i"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["e"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["l"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["s"],"id":34}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":[" "],"id":35},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":[" "],"id":36}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":19},"action":"insert","lines":["()"],"id":37}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["o"],"id":38},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["f"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["f"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["i"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["c"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["e"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["r"],"id":39},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["e"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["c"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["i"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["f"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["f"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["o"]}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["o"],"id":40},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["f"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["f"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["i"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["c"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["r"],"id":41}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["e"],"id":42},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["r"],"id":43},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["e"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["c"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["i"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["f"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["f"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["o"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":19},"end":{"row":12,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1602142475098,"hash":"393f720b2ae63fd8f94563760eb3f54370285046"}