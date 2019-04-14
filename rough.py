from summaries_Rough import summary

input_text = "So, what is computer science? Generally speaking, computer science is the study of computer technology, both hardware and software. However, computer science is a diverse field; the required skills are both applicable and in-demand across practically every industry in today's technology-dependent world. As such, the field of computer science is divided amongst a range of sub-disciplines, most of which are full-fledged specialized disciplines in and of themselves. The field of computer science spans several core areas: computer theory, hardware systems, software systems, and scientific computing. Students will choose credits from amongst these sub-disciplines with varying levels of specialization depending on the desired application of the computer science degree. Though most strict specialization occurs at the graduate level, knowing exactly what computer science is (and where a student's interests fall within this vast field) is of paramount importance to knowing how to study computer science."
summaries = summary(input_text)
# print(summaries)
output = ''
for i in range(len(summaries)):
    o = summaries[i][1]
    output += o

print(output)

