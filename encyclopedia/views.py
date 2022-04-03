from django.shortcuts import render
from .forms import EntryCreateForm
from django.shortcuts import redirect
from .forms import EntryEditForm
from . import util
import random
import markdown2


def index(request):
    q = request.GET.get('q', '')
    entries = util.list_entries()
    if q:
        entries = [e for e in entries if q.lower() in e.lower()]
    if q in entries:
        return redirect('wiki:single-entries', q)
    return render(request, "encyclopedia/index.html", {
                 "entries": entries,
          })

def single_entries(request, title: str):
    content = util.get_entry(title)
    if not content:
        return render(request, 'encyclopedia/error.html', {
            'title': '404, Page Not Found!',
        })
    return render(request, 'encyclopedia/single_entries.html', {
        'title': title,
        'content': markdown2.markdown(content)
    })

def create_entries(request):
    entries = util.list_entries()
    form = EntryCreateForm()
    if request.method == 'POST':
        form = EntryCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            for n in entries:
                if title.casefold() == n.casefold():
                    return render(request, 'encyclopedia/error.html', {
                        'title': f'The entry {title} already exists!'
                    })
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return redirect('wiki:index')
    return render(request, 'encyclopedia/create_entries.html', {
        'form': form,
    })

def edit_entries(request, title: str):
        content = util.get_entry(title)
        if not content:
            return render(request, 'encyclopedia/error.html', {
                'title': '404, Page Not Found!',
            })
        if request.method == 'POST':
            form = EntryEditForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                util.save_entry(title, content)
                return redirect("wiki:single-entries", title)
        return render(request, 'encyclopedia/edit_entries.html', {
            'form': EntryEditForm(initial={'content': content}),
            'title': title
        })

def random_entry(request):
    entries = util.list_entries()
    select_entries = random.choice(entries)
    return redirect('wiki:single-entries', select_entries)

