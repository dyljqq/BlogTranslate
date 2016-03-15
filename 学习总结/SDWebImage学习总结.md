#SDWebImage学习总结

1. 网络图片请求策略

	[self.imageView sd_setImageWithURL:[NSURL URLWithString:@"url"]
                placeholderImage:[UIImage imageNamed:@"placeholder"]];
    
    我想SDWebImage迷人的地方就在这里，简洁无比的接口函数，加上后台复杂无比的实现。
    SDWebImage请求图片的方式是先找缓存，缓存通过NSCache实现，找不到就去硬盘找，硬盘的访问时通过ioQueue去硬盘找，硬盘中图片文件名是经过MD5编码的，然后默认一星期清理一次，或者当缓存已满，那么就会从时间最低的开始一次清理，清理到有一半的最大剩余缓存。如果硬盘也找不到，那么就只能通过url进行网络强求。网络请求是通过NSOperation + NSOperationQueue，这里是又实现了SDWebImageDownloaderOperation， 继承至NSOperation，然后重写的是start方法，这样的话就可以通过kvc来控制请求的取消，开始，结束等状态，相对实现main来说更加复杂（main与c语言的main一样，当main中的语句执行完毕后，那么整个程序也就执行完了），但是显然效果会好很多。

2. 使用GCD与NSOperation
	
	@synchronized (self)保证多线程访问的安全性，

	dispatch_barrier_sync保证了当前只执行一个block，且剩余的指令要在我这个block结束之后才能执行。
	
	还有一些异步的dispatch_async等的使用，使得程序能够更快的得到响应。

3. 图片的网络请求用的是NSURLConnection，有点美中不足，建议可以使用NSURLSession，因为AFNetworking 3.0已经与时俱进的使用NSURLSession进行重构了。
4. NSRunLoop将线程不断的执行，直到数据全部返回，或者超时，才结束runloop。
5. 就是strong， weak大法，避免循环引用。
 
