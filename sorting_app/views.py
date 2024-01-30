# views.py
from django.shortcuts import render

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def dashboard_view(request):
    return render(request, 'sorting_app/dashboard.html')

def bubble_sort_view(request):
    if request.method == 'POST':
        arr = list(map(int, request.POST.get('arr').split()))
        bubble_sort(arr)
        return render(request, 'sorting_app/sorted_array.html', {'sorted_arr': arr, 'algorithm': 'Bubble Sort'})
    return render(request, 'sorting_app/sort_form.html', {'algorithm': 'Bubble Sort'})

def selection_sort_view(request):
    if request.method == 'POST':
        arr = list(map(int, request.POST.get('arr').split()))
        selection_sort(arr)
        return render(request, 'sorting_app/sorted_array.html', {'sorted_arr': arr, 'algorithm' : 'Selection Sort'})
    return render(request, 'sorting_app/sort_form.html', {'algorithm': 'Selection Sort'})

def insertion_sort_view(request):
    if request.method == 'POST':
        arr = list(map(int, request.POST.get('arr').split()))
        insertion_sort(arr)
        return render(request, 'sorting_app/sorted_array.html', {'sorted_arr': arr, 'algorithm': 'Insertion Sort'})
    return render(request, 'sorting_app/sort_form.html', {'algorithm': 'Insertion Sort'})
