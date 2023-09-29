from collections import defaultdict

def check_if_courses_possible(n_courses:int, prerequisites:list[tuple[int, int]]) -> bool:  
    pre_map = {i:[] for i in range(n_courses)}
    for course_number, pre in prerequisites:
        pre_map[course_number].append(pre)
    
    cycle_set, visit_set = set(), set()
    def dfs(course_number):
        if course_number in cycle_set:
            return False
        if course_number in visit_set:
            return True
        
        cycle_set.add(course_number)
        for pre in pre_map[course_number]:
            if not dfs(pre): return False

        cycle_set.remove(course_number)
        visit_set.add(course_number)

        return True

    for course in range(n_courses):
        if not dfs(course): return False

    return True

def extract_course_chain(n_courses:int, prerequisites:list[tuple[int, int]]) -> list[int]:

    pre_map = {i:[] for i in range(n_courses)}
    for course_number, pre in prerequisites:
        pre_map[course_number].append(pre)

    chain = []
    visit_set, cycle_set = set(), set()

    def dfs(course_number):
        if course_number in cycle_set:
            return False
        if course_number in visit_set:
            return True

        cycle_set.add(course_number)
        for pre in pre_map[course_number]:
            if not dfs(pre): return False

        cycle_set.remove(course_number)
        visit_set.add(course_number)
        chain.append(course_number)

        return True

    for course in range(n_courses):
        if course not in chain:
            if not dfs(course): 
                return None
            
    return chain