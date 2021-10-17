<div align="center">
<h1 align="center"> 
    Astronomy Picture of the Day 
</h1>
<hr />
<br />

<p>{{ picture.date }}</p>
{% if picture.media_type == "image" %}
    <img src="{{ picture.image_file.url }}">

{% elif picture.media_type == "video" %}
    <iframe src="{{ picture.video_url }}"></iframe>
{% endif %}

<p>
    {{ picture.explanation }}
</p>


<a href="/{{ previous_date }}">Prev</a>

<a href="/{{ next_day }}">Next</a>