// define some LLVM3 macros if the code is compiled with a different compiler (ie LLVMGCC42)
#ifndef __has_feature
#define __has_feature(x) 0
#endif
#ifndef __has_extension
#define __has_extension __has_feature // Compatibility with pre-3.0 compilers.
#endif

#if __has_feature(objc_arc) && __clang_major__ >= 3
#define ARC_ENABLED 1
#endif // __has_feature(objc_arc)

#import <Foundation/Foundation.h>
#import <assert.h>
#import "abstract_accessProxy.h"

int main() {
#ifdef ARC_ENABLED
    @autoreleasepool
    {
#else
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
#endif
        A *a = [[A alloc] init];
        B *b = [[B alloc] init];
        C *c = [[C alloc] init];
        D *d = [[D alloc] init];

        assert([a do_x] == 0);
        assert([b do_x] == 0);
        assert([c do_x] == 0);
        assert([d do_x] == 1);

#ifdef ARC_ENABLED
    }
#else
        [pool release];
#endif

    return 0;
}
