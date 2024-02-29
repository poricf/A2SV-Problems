class Solution:
  def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    ans = []
    count = collections.Counter()

    for cpdomain in cpdomains:
      num, domains = cpdomain.split()
      print(num,domains)
      num, domains = int(num), domains.split('.')
      print(num,domains)
      for i in reversed(range(len(domains))):
        count['.'.join(domains[i:])] += num
        print(count)
    
    answer = []
    for domain, freq in count.items():
        answer += [str(freq) + ' ' + domain ]
    return answer