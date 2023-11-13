"""
@Author: 霍格沃兹测试开发学社-西西
@Desc: 更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860
"""
import allure


@allure.description("""
多行描述语：<br/>
这是通过传递字符串参数的方式添加的一段描述语，<br/>
使用的是装饰器 @allure.description
""")
def test_description_provide_string():
    assert True


@allure.description_html("""
<div class="c-span6 c-span-last text-container_18c0Z" aria-hidden="false" aria-label=""><!--165--><p class="title_2e25d" aria-label="标题：读懂中国经济的信心所在" data-click="{rel_type: 'news_title'}"><a style="color:" href="http://www.baidu.com/link?url=OhpkFgpJVN3rutIwcGefbYOZSz7WMW-e4fvkgI7AMPTh_iSZ41O0Srd4U8SSIgFnpNBBNT8Pdw_kAUKX2Y9tH_" target="_blank" aria-label="" tabindex="0"><!--s-slot--><!--168--><em>读懂中国经济的信心所在</em><!--168--><!--/s-slot--></a></p><p class="abs_2flqn c-color-text" aria-label="摘要：人民对中国经济发展的坚定信心从何而来？来自中国经济发展的长期大势、来自中国经济经过了多次“压力测试”、来自于中国经济坚实的底盘。" data-click="{rel_type: 'news_abs'}">
                人民对中国经济发展的坚定信心从何而来？来自中国经济发展的长期大势、来自中国经济经过了多次“压力测试”、来自于中国经济坚实的底盘。
                <a style="color:" href="http://www.baidu.com/link?url=OhpkFgpJVN3rutIwcGefbYOZSz7WMW-e4fvkgI7AMPTh_iSZ41O0Srd4U8SSIgFnpNBBNT8Pdw_kAUKX2Y9tH_" target="_blank" aria-label="" tabindex="0"><!--170--><span class="abs-detail_107zP">详细 &gt;</span><!--170--></a></p><div class="source-wrapper_2yrv2"><a style="color:" href="http://www.baidu.com/link?url=OhpkFgpJVN3rutIwcGefbYOZSz7WMW-e4fvkgI7AMPTh_iSZ41O0Srd4U8SSIgFnpNBBNT8Pdw_kAUKX2Y9tH_" target="_blank" aria-label="" tabindex="0"><!--173--><img class="source-icon_2i7Ku" src="https://gimg3.baidu.com/rel/src=https%3A%2F%2Fpic.rmb.bdstatic.com%2Fbjh%2Fuser%2F59ba8ee7f07b871b55f61ba49feeb777.jpeg%40s_0%2Cw_200&amp;refer=http%3A%2F%2Fwww.baidu.com&amp;app=2010&amp;size=w100&amp;n=0&amp;g=0n&amp;q=100&amp;fmt=auto?sec=1673110800&amp;t=cbea9b6676a3f69eb2ea0333cbff940f" aria-hidden="true" data-click="{rel_type: 'news_site_pic'}"><!--174--><span class="source-title_2Kkq3 c-color-gray" aria-label="来源：人民网" data-click="{rel_type: 'news_site'}">人民网</span><span class="pubtime_2JQQB c-color-gray2" aria-label="发布时间：12小时前" data-click="{rel_type: 'news_time'}">12小时前</span><!--175--><!--173--></a></div><!--171--><!--176--><!--178--><!--179--><!--178--><!--177--><!--176--><!--165--></div>
""")
def test_description_privide_html():
    assert True

def test_description_docstring():
    """
    文档信息放在方法里面，会按照给定的格式展示，不需要额外加<br/> 换行
    直接在测试用例方法中
    通过编写文档注释的方法
    来添加描述。
    :return:
    """
    assert True


@allure.description("""这个描述将被替换""")
def test_dynamic_description():
    assert 42 == int(6 * 7)
    # allure.dynamic.description('这是最终的描述信息')
    allure.dynamic.description_html(''' <div class="title"><a href="/" data-auto-route="true"><img src="https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png" alt="测试人社区" id="site-logo" class="logo-big"></a></div> ''')