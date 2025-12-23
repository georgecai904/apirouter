import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import SoraGenStyle, SoraGenProductSeed

# TODO: 配置上游 API 地址
# Please configure the upstream API URL here
UPSTREAM_API_BASE = "https://api.wuyinkeji.com" 

@csrf_exempt
@require_http_methods(["POST"])
def submit(request):
    try:
        # 获取请求参数
        # Assuming parameters are in query string as per "POST /api/sora2/submit?key=..." 
        # But usually POST data is in body. User said "Request params description: prompt, url...".
        # It's ambiguous if they are query params or body.
        # "POST /api/sora2/submit?key=your_key, Request params: prompt..."
        # I will look in both request.GET and request.POST/body.
        # Given it's an API, JSON body is common, or Form data.
        
        # Checking query params for key
        api_key = request.GET.get('key')
        print(api_key)
        if not api_key:
             return JsonResponse({'error': 'Missing API key'}, status=401)

        # Parse body or form data
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        else:
            data = request.POST

        style = data.get('style')
        product_seed = data.get('productSeed')
        user_prompt = data.get('prompt', '')
        
        # Other params
        url = data.get('url')
        aspect_ratio = data.get('aspectRatio', '')
        duration = data.get('duration', '')
        size = data.get('size', '')
        remix_target_id = data.get('remixTargetld', '') # Keeping strictly as user wrote: remixTargetld

        if not style or not product_seed:
            # return JsonResponse({'error': 'Missing style or productSeed'}, status=400)
            pass

        # 1. Get promptA
        prompt_a = ""
        if style:
            try:
                style_obj = SoraGenStyle.objects.get(style=style)
                prompt_a = style_obj.promptA
            except SoraGenStyle.DoesNotExist:
                # return JsonResponse({'error': f'Style not found: {style}'}, status=404)
                prompt_a = ""

        # 2. Get promptB
        prompt_b = ""
        if product_seed:
            try:
                seed_obj = SoraGenProductSeed.objects.get(productSeed=product_seed)
                prompt_b = seed_obj.promptB
            except SoraGenProductSeed.DoesNotExist:
                # return JsonResponse({'error': f'ProductSeed not found: {product_seed}'}, status=404)
                prompt_b = ""

        # 3. Concatenate
        final_prompt = f"""{prompt_a}

{prompt_b}

[SCRIPTS - LOCKED]
{user_prompt}
"""

        # 4. Construct upstream payload
        payload = {
            'prompt': final_prompt,
            'url': url,
            'aspectRatio': aspect_ratio,
            'duration': duration,
            # 'size': size,
            # 'remixTargetld': remix_target_id
        }

        # 5. Forward request
        # User didn't specify upstream endpoint path, assuming similar structure or just base?
        # "Then will request... Request params..."
        # I will assume a hypothetical endpoint for now.
        upstream_url = f"{UPSTREAM_API_BASE}/api/sora2/submit?key={api_key}" 
        
        # Note: In real world, we might need to forward the API key or use a different one.
        # User didn't specify.
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            'Authorization': f'Bearer {api_key}',
        }
        response = requests.post(upstream_url, data=payload, headers=headers)
        
        
        # Return upstream response
        try:
            resp_json = response.json()
        except:
            resp_json = response.text
            
        return JsonResponse({
            'upstream_status': response.status_code,
            'upstream_response': resp_json,
            'processed_params': payload
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def test_panel(request):
    """
    Render the test panel UI with dynamic data options.
    """
    styles = SoraGenStyle.objects.all()
    seeds = SoraGenProductSeed.objects.all()
    
    context = {
        'styles': styles,
        'seeds': seeds,
    }
    return render(request, 'soragen/test_panel.html', context)

@csrf_exempt
@require_http_methods(["GET"])
def detail(request):
    try:
        api_key = request.GET.get('key')
        if not api_key:
             return JsonResponse({'error': 'Missing API key'}, status=401)
             
        detail_id = request.GET.get('id')
        if not detail_id:
            return JsonResponse({'error': 'Missing id'}, status=400)
            
        # Forward request
        upstream_url = f"{UPSTREAM_API_BASE}/api/sora2/detail"
        
        response = requests.get(upstream_url, params={'key': api_key, 'id': detail_id})
        
        try:
            resp_json = response.json()
        except:
            resp_json = response.text
            
        return JsonResponse({
            'upstream_status': response.status_code,
            'upstream_response': resp_json
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
