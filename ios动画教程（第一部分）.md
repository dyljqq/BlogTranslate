#iOS动画教程（第一部分）

[英文版 iOS Animation Tutorial: Getting Started](http://www.raywenderlich.com/113674/ios-animation-tutorial-getting-started)

动画是你的iOS用户交互界面的重要组成部分。动画可以将用户的注意力放在改变的事物上，并且给你的UI带来无限的乐趣与闪光点。

![](http://cdn4.raywenderlich.com/wp-content/uploads/2015/09/iOS9_feast_minis_ios_anim-250x250.jpg
)

更重要的是，在扁平化设计的时代，动画是区分你和别的app 应用的一个很重要的方法。

在这篇教程中，你将会学习到怎么样用UIView的动画来完成下面的事情：

* 设置一个很酷的阶段动画
* 创建移动和回退动画
* 调节动画的速度
* 反向和重复动画

这里有很多的材料需要我们接触，但是我保证这些都非常的有趣。所以，准备好接受挑战了吗？？？？

![](http://cdn4.raywenderlich.com/wp-content/uploads/2015/02/001_ChallengeAccepted.png
)

好了 - 是时候去学习动画了。

##入门

首先下载这篇教程的样例工程，[BahamaAir Starter](http://cdn2.raywenderlich.com/wp-content/uploads/2015/09/BahamaAir-Starter.zip),它展示了一个虚构的航空公司的登陆界面 - “巴哈马航空”

在Xcode中编译运行这个工程，你将会看到下面的效果：
![](http://cdn3.raywenderlich.com/wp-content/uploads/2015/02/002_LoginScreen-338x320.png
)

这个app目前并没有做什么事情 - 它仅仅给我展示了一个界面，这个界面有一个标题，两个文本框，以及底部的一个非常友好的按钮。

它也拥有一个好的背景图和四朵云彩。这些云朵在代码中已经和实例连接了。

打开ViewController.swift，并且查看它的代码。在文件的开头，你将会看到已经和视图连接好的实例变量和类变量。在往下看，你可以看到viewDidLoad()中的一点代码，这个函数是用来初始化界面的UI。这个工程已经为你将要展示的动画做好了准备。

经过上面详细的介绍，你无疑已经准备好写一些代码了。

##你的第一个动画

你的第一个任务是当用户打开应用时，表单元素通过动画的形式进入到应用。既然表单在app启动时是可见的，那么你应该在view controller显示的时候将表单移出屏幕。

在viewWillAppear()函数中添加下面的代码:

	heading.center.x  -= view.bounds.width
	username.center.x -= view.bounds.width
	password.center.x -= view.bounds.width
	
上面的代码将每个表单元素移出屏幕的可见区域，就像下图一样：
![](http://cdn4.raywenderlich.com/wp-content/uploads/2015/02/003_FormElements-480x235.png
)

由于上面的代码在视图控制器显示之前执行，那么那些文本框看起来就像根本不存在一样。

编译运行你的程序，以确认文本框元素在屏幕外显示就像你之前预期的一样：
![](http://cdn1.raywenderlich.com/wp-content/uploads/2015/02/004_MovedElements-377x320.png
)

完美（此处应有掌声，啪啪啪） - 现在你可以将那些被隐藏的表单元素用一些炫酷的动画将它们复原。

在viewDidApear()函数加上下面的代码：

	UIView.animateWithDuration(0.5, animations: {
  	self.heading.center.x += self.view.bounds.width
	})
	
通过UIView的类方法animateWithDuration(_:animations:)，你可以给标题加上动画效果。加的动画马上执行，并且持续0.5秒；你通过这个函数的第一个参数来设置动画的持续时间。

它看起来就是这么简单；你在这个函数的闭包中加入的改变都会通过UIKit以动画的形式展示出来。

编译运行你的工程，你会看到你的标题匀速滑进到指定位置，就像下图一样：
![](http://cdn2.raywenderlich.com/wp-content/uploads/2015/02/005_TitleSlide.png
)

剩下的元素你也可以通过上述的方法显示出来。

由于animateWithDuration(_:animations:) 是一个类方法，所以你可以给多个视图加上动画。事实也是，你可以在方法的比保重，给所有你想要的视图加上动画。

在animations的闭包中加上下面的代码：

	self.username.center.x += self.view.bounds.width

再次编译运行你的工程，你可以看到你的用户名的文本框滑到指定的位置。如下图：

![](http://cdn5.raywenderlich.com/wp-content/uploads/2015/02/006_UsernameSlide.png
)

##延迟动画

看见两个视图同时执行动画看起来非常的酷，但是你可能注意到了，这两个视图移动的距离和时间间隔都相同看起来就有那么点僵硬。只有kill-bots（貌似是一种杀人机器人）的移动才会完全的同步。

每个视图的移动都与其他视图相同难道不更酷一点吗？！！！或者我们可以给其中的一个动画延迟一点时间来实现这个效果？

首先移除原来的username的代码：

	UIView.animateWithDuration(0.5, animations: {
  	self.heading.center.x += self.view.bounds.width
  	// self.username.center.x += self.view.bounds.width
	})

然后早viewDidAppear()的底部加上下面的代码：

	UIView.animateWithDuration(0.5, delay: 0.3, options: [], animations: {
  		self.username.center.x += self.view.bounds.width
	}, completion: nil)
	
这次你使用的这个类方法看起来有点似曾相识，但是它有更多的参数，可以让你定制你的动画：

1. duration：动画的持续时间
2. delay:在开始动画前所等待的时间
3. options：一系列的动画选项可以让你定制的动画的很多方面。关于这个参数，你稍后将会学到更多，但是现在你可以认为[]表示没有选项。
4. animations：支持你的动画的闭包表达式。
5. completion：当动画结束时执行的闭包；这个参数通常在你需要执行清除任务或者下一个动画需要在这个动画结束后才能执行时使用。

在上面的代码中，你设置delay为0.3，表示这个动画将在title动画开始执行的0.3秒后执行。

编译运行你的工程，这个组合动画现在看起来怎么样呢？

![](http://cdn3.raywenderlich.com/wp-content/uploads/2015/02/007_Combined.png
)

哈哈，这次是不是看起来好了很多。现在所有你需要的操作就是给password的文本框加上动画。

在viewDidAppear()底部加上下面的代码：

	UIView.animateWithDuration(0.5, delay: 0.4, options: [], animations: {
  	self.password.center.x += self.view.bounds.width
	}, completion: nil)
	
这里你只是仅仅修改了一下username的动画效果，就是延长了一点动画开始的时间。

再次编译运行你的工程，你就可以看到完成的动画效果了：

![](http://cdn4.raywenderlich.com/wp-content/uploads/2015/02/008_CompleteAnimation.png
)

这些就是所有你需要做的，通过UIKit的动画，将视图从屏幕外边滑进里面。

但是这仅仅只是开始 - 接下来你会学到更多更酷的动画技术。

##动画属性

现在你明白了动画是多么的简单后，你肯定想知道如何给你的视图加上一些别的动画效果吧。

这个章节将会了解UIView的动画属性的概述，然后指导你在你的工程中实现这些动画。

不是所有的视图属性都可以添加动画，但是所有的视图都可以添加动画，从简单到复杂，可以通过设置视图属性，来让视图产生动画效果。就像下图一样：

###位置和大小

![](http://cdn1.raywenderlich.com/wp-content/uploads/2015/02/009_PositionAndSize.png
)

你可以通过设置动画视图的位置和帧来让视图变大，缩小，或者四处移动就像你上面做过的一样。下面是你可以修改的属性来改变视图的位置和大小：

* bounds：改变这个属性，你可以在视图的帧中复位视图的内容。
* frame：操作这个属性可以让你移动视图或者改变视图的尺寸。
* center：当你想要改变视图在屏幕的位置时，你可操作这个属性。

不要忘了Swift可以让你操作结构中的单个属性。这意味着你可通过改变center.y垂直移动视图，或者减小frame.size.width来缩小视图。

###外观

![](http://cdn4.raywenderlich.com/wp-content/uploads/2015/02/010_Appearance.png
)

你可以通过给背景着色或者改变视图的透明度来改变视图的外观。

* backgroundColor：改变这个属性，我们可以看到背景色在逐渐的改变。
* alpha：改变这个属性来实现淡入和淡出的效果。

###转换

![](http://cdn2.raywenderlich.com/wp-content/uploads/2015/02/011_Transformation.png
)

变化属性改变视图的方式和上面的方法大同小异，因为你也可以通过更改这个属性来改变视图的大小和位置。

* transform：修改这个属性可以更改视图的旋转角度，尺寸，位置

这个属性表示的视图的仿射变化，这个属性更加的有效，它允许你描述比例因子或者旋转角度而不是给出一个具体的边界或者中心点。

上面的看起来很像基本的动画模块，但是接下来你对将要遇到的动画效果感到惊讶。

##动画选项

往前看你的代码，你发现你总是给options的参数赋值为[]。

options让你决定UIKit如何创建你的动画。你前面只是调整了动画的持续时间和延迟时间，但是你可以在你的动画参数上添加更多的控制。

这里有一个关于UIViewAnimationOptions的选项列表，你可以通过不同的组合方式来实现你的动画。

###重复

你首先会看到下面的两个动画属性：

* .Repeat:包含这个属性，你可以让你的动画无限循环。即->,->。
* .Autoreverse:这个属性的循环方式是先正着，然后反向实现动画。即：->,<-。

修改password文本框的属性，使用.Repeat选项，如下：

	UIView.animateWithDuration(0.5, delay: 0.4,
  	options: .Repeat, animations: {
  		self.password.center.x += self.view.bounds.width
	}, completion: nil)
	
编译运行后你会看到修改后的效果：

![](http://cdn3.raywenderlich.com/wp-content/uploads/2015/02/012_Repeat-480x274.png
)

title和username飞入并且停在屏幕的正中，但是password会不断的重复进入和退出屏幕的过程。

修改上述的代码，将options参数改为.Repeat 和 .Autoreverse，如下：

	UIView.animateWithDuration(0.5, delay: 0.4,
  	options: [.Repeat, .Autoreverse], animations: {
    	self.password.center.x += self.view.bounds.width
	}, completion: nil)
	
options添加方式像一个数组。（如果不懂数组，那我也是没辙！！！）

##动画的速度

Easing不知道该如何翻译比较恰当，因为它的效果其实就是列车的从车站出来加速，进入车站减速的过程。。

![](http://cdn4.raywenderlich.com/wp-content/uploads/2015/02/013_Easing-480x124.png
)

你可以选择四个不同的速度选项：

* .Linear:匀速线性
* .CurveEaseIn:开始加速，后面匀速
* .CurveEaseOut:先匀速，最后减速
* .CurveEaseInOut:先加速，后匀速，最后减速

理解的最好的方法还是在工程中亲自去实现它，来体验不同的选项所实现的效果。

还是修改password的参数数组，如下：

	UIView.animateWithDuration(0.5, delay: 0.4,
  	options: [.Repeat, .Autoreverse, .CurveEaseOut], 	animations: {
    	self.password.center.x += self.view.bounds.width
	}, completion: nil)

编译运行你的工程，注意你的password是如何平滑的过度到最后的位置的。

![](http://cdn3.raywenderlich.com/wp-content/uploads/2015/02/014_Deceleration.png
)

啊哈，现在你应该已经明白了如何使用UIView的动画api了吧。因此在你的app中也加入这些炫酷的动画吧。

附上已经实现上述动画的工程：
[iOS Animations by Tutorials](http://www.raywenderlich.com/store/ios-animations-by-tutorials)






