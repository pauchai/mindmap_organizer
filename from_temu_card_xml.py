import json

def convert_from_card_dict(card_dict):
    result_list = []
    
    for good_info in card_dict["result"]["cart_list_info"]["goods_sku_list"]:
        
        if good_info["is_selected"]:
            item_info = {}
            item_info["name"] = good_info["base_goods_info"]["goods_name"]
            #item_info["price"] = good_info["base_goods_info"]["price"]
            item_info["price"] = good_info["sku_info"]["sku_price"] / 100
            item_info["thumb_url"] = good_info["base_goods_info"]['thumb_url']
            result_list.append(item_info)
        
    
    return result_list


goods_list  = []
with open("temu_card_example.json", 'r', encoding='utf-8') as fp:
    card_dict = json.load(fp)

    goods_list = convert_from_card_dict(card_dict)
    print(goods_list) 

with open("origi")
for good_info in goods_list:

