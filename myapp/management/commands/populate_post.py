from typing import Any
from django.core.management.base import BaseCommand
from myapp.models import Control

class Command(BaseCommand):
    help = 'This commands inserts control data.'

    def handle(self, *args: Any, **options: Any):
        Control.objects.all().delete()

        titles=["Whispers of Bloom",
            "Velour Essence",
            "Crystal Dawn",
            "Lunar Petals",
            "Saffron Sky",
            "Mystic Veil",
            "Golden Mirage",
            "Silken Shadow",
            "Velvet Ember",
            "Eternal Whisper",
            "Celeste Noir",
            "Amber Horizon",
            "Moonlit Rose",
            "Aurora Mist",
            "Velour Nights",
            "Pearl Echo",
            "Twilight Bloom",
            "Radiant Solace",
            "Scarlet Veil",
            "Opaline Dream"]

        contents=["In the heart of the ancient forest, where sunlight danced through the leaves, a hidden glade blossomed with flowers of every hue. The air was thick with the scent of jasmine and rose, and the gentle hum of bees filled the space with life. It was a place untouched by time, where nature's beauty reigned supreme.",
            "Beneath the velvet sky, the city lights shimmered like stars fallen to earth. The streets were alive with the sounds of laughter and music, as people danced and celebrated the night. In this urban oasis, dreams were born and stories unfolded, each one more vibrant than the last.",
            "At dawn, the desert came alive with a golden glow, as the first rays of sunlight kissed the dunes. The air was warm and dry, carrying the scent of sage and sand. Amidst this vast expanse, a solitary figure walked, leaving footprints that would soon be erased by the shifting winds.",
            "High in the mountains, where the air was crisp and pure, a hidden lake reflected the sky like a mirror. Surrounded by towering pines and wildflowers, it was a sanctuary for those seeking peace and solitude. The only sounds were the gentle lapping of water and the occasional call of an eagle soaring overhead.",
            "In a quaint village nestled between rolling hills, time seemed to slow down. Cobblestone streets wound their way past charming cottages adorned with blooming window boxes. The aroma of freshly baked bread wafted through the air, inviting passersby to stop and savor the simple pleasures of life.",
            "On a remote island, where turquoise waters met white sandy beaches, a vibrant coral reef teemed with life. Colorful fish darted among the swaying seaweed, while graceful turtles glided through the crystal-clear water. It was a paradise untouched by human hands, where nature's wonders flourished in harmony.",
            "In a bustling marketplace, vibrant fabrics and exotic spices created a sensory feast. The air was filled with the sounds of haggling vendors and lively chatter as people from all walks of life came together to trade goods and stories. It was a melting pot of cultures, where diversity was celebrated and connections were forged.",
            "Amidst a field of lavender under a sky painted with hues of pink and orange, a solitary tree stood tall. Its branches reached towards the heavens, adorned with delicate blossoms that swayed gently in the breeze. It was a symbol of resilience and beauty, standing strong against the passage of time.",
            "In an old library filled with dusty tomes and ancient manuscripts, knowledge awaited those who sought it. The scent of aged paper and leather filled the air as readers lost themselves in worlds both real and imagined. It was a sanctuary for curious minds, where every page turned revealed new adventures.",
            "On a quiet beach at sunset, the sky transformed into a canvas of fiery reds and soft purples. The sound of waves crashing against the shore created a soothing rhythm, while the salty breeze carried the promise of new beginnings. It was a moment of tranquility, where time seemed to stand still.",
            "Beneath the velvet sky, the city lights shimmered like stars fallen to earth. The streets were alive with the sounds of laughter and music, as people danced and celebrated the night. In this urban oasis, dreams were born and stories unfolded, each one more vibrant than the last.",
            "At dawn, the desert came alive with a golden glow, as the first rays of sunlight kissed the dunes. The air was warm and dry, carrying the scent of sage and sand. Amidst this vast expanse, a solitary figure walked, leaving footprints that would soon be erased by the shifting winds.",
            "High in the mountains, where the air was crisp and pure, a hidden lake reflected the sky like a mirror. Surrounded by towering pines and wildflowers, it was a sanctuary for those seeking peace and solitude. The only sounds were the gentle lapping of water and the occasional call of an eagle soaring overhead.",
            "In a quaint village nestled between rolling hills, time seemed to slow down. Cobblestone streets wound their way past charming cottages adorned with blooming window boxes. The aroma of freshly baked bread wafted through the air, inviting passersby to stop and savor the simple pleasures of life.",
            "On a remote island, where turquoise waters met white sandy beaches, a vibrant coral reef teemed with life. Colorful fish darted among the swaying seaweed, while graceful turtles glided through the crystal-clear water. It was a paradise untouched by human hands, where nature's wonders flourished in harmony.",
            "In a bustling marketplace, vibrant fabrics and exotic spices created a sensory feast. The air was filled with the sounds of haggling vendors and lively chatter as people from all walks of life came together to trade goods and stories. It was a melting pot of cultures, where diversity was celebrated and connections were forged.",
            "Amidst a field of lavender under a sky painted with hues of pink and orange, a solitary tree stood tall. Its branches reached towards the heavens, adorned with delicate blossoms that swayed gently in the breeze. It was a symbol of resilience and beauty, standing strong against the passage of time.",
            "In an old library filled with dusty tomes and ancient manuscripts, knowledge awaited those who sought it. The scent of aged paper and leather filled the air as readers lost themselves in worlds both real and imagined. It was a sanctuary for curious minds, where every page turned revealed new adventures.",
            "On a quiet beach at sunset, the sky transformed into a canvas of fiery reds and soft purples. The sound of waves crashing against the shore created a soothing rhythm, while the salty breeze carried the promise of new beginnings. It was a moment of tranquility, where time seemed to stand still.",
            "In the heart of the ancient forest, where sunlight danced through the leaves, a hidden glade blossomed with flowers of every hue. The air was thick with the scent of jasmine and rose, and the gentle hum of bees filled the space with life. It was a place untouched by time, where nature's beauty reigned supreme."]

        img_urls=["https://images.pexels.com/photos/1961792/pexels-photo-1961792.jpeg?cs=srgb&dl=pexels-valeriya-1961792.jpg&fm=jpg",
        "https://images.unsplash.com/photo-1615160460366-2c9a41771b51?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fHBlcmZ1bWUlMjBib3R0bGV8ZW58MHx8MHx8fDA%3D",
        "https://images.pexels.com/photos/1961791/pexels-photo-1961791.jpeg?cs=srgb&dl=pexels-valeriya-1961791.jpg&fm=jpg",
        "https://png.pngtree.com/thumb_back/fh260/background/20241018/pngtree-eau-de-parfum-hd-8k-wallpaper-stock-photographic-image-image_16359989.jpg",
        "https://cdn.pixabay.com/photo/2017/03/14/11/41/perfume-2142824_640.jpg",
        "https://i.pinimg.com/736x/ff/6b/1e/ff6b1e290ab1e0e970e092d9e4c3c802.jpg",
        "https://images.pexels.com/photos/1557980/pexels-photo-1557980.jpeg?cs=srgb&dl=pexels-kdjproductions-1557980.jpg&fm=jpg",
        "https://images.unsplash.com/photo-1523293182086-7651a899d37f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGVyZnVtZSUyMGJvdHRsZXxlbnwwfHwwfHx8MA%3D%3D",
        "https://watermark.lovepik.com/photo/20211121/large/lovepik-dior-perfume-picture_500586716.jpg",
        "https://images3.alphacoders.com/641/641460.jpg",
        "https://cdn.pixabay.com/photo/2021/12/28/16/40/perfume-6899766_640.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkpigFIXztnyE5HDhxeTLfllMQsaMDezcWeg&s",
        "https://5.imimg.com/data5/SELLER/Default/2024/4/411681197/QQ/LW/BX/265737/perfume-spray-fragrance.jpg",
        "https://img.freepik.com/free-vector/perfume-deodorant-bottles-water-splash-with-drops_33099-1657.jpg",
        "https://johnphillips.in/cdn/shop/files/525_6ca56700-635f-462b-96a2-afc328e4894c.jpg?v=1725002588&width=1445",
        "https://t4.ftcdn.net/jpg/12/49/73/91/360_F_1249739164_50W13ZvfGQld43a4nADg1CEKQ7gMOZLu.jpg",
        "https://images.unsplash.com/photo-1708979165880-dd0ff61fa748?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bWVuJTIwcGVyZnVtZXxlbnwwfHwwfHx8MA%3D%3D",
        "https://static.vecteezy.com/system/resources/previews/032/254/252/large_2x/perfume-perfume-perfume-bottle-perfume-bottle-perfume-bottle-hd-wallpaper-ai-generated-free-photo.jpg",
        "https://www.jainperfumers.com/cdn/shop/articles/the-timeless-elegance-of-attar-perfumes-a-journey-through-scent-157499.jpg?v=1727435784&width=1100",
        "https://c4.wallpaperflare.com/wallpaper/60/762/383/glass-perfume-bottle-wallpaper-preview.jpg"]


        for title, content, img_url in zip(titles, contents, img_urls):
            Control.objects.create(title=title, content=content, img_url=img_url)
        self.stdout.write(self.style.SUCCESS('Successfully inserted control data.!'))





    


