from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
    """
    This view expects data via GET in order to create an instance
    of the form. This data consists of the url and title of an image
    from an external website and will be provided via GET by the JS
    tool.
    If the form is submitted, it checks whether it is valid. If the
    form data is valid, create Image instance, but prevent saving.
    Assign the current user to the new image object.
    Save the image object to db.
    Create a success message.
    """
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign cuttent user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})
