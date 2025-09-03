def last_dot_kept(s):
    dot = '.'
    c  = s.count(dot)
    return s.replace(dot, '-dot-', count=c-1)


print(last_dot_kept('foo.bar.whatever'))