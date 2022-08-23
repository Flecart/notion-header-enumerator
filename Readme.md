# Notion header enumerator
Mini-project for notion pages organization

## What is this
I wanted to have a notion integration that gives numbers to the headings of my
notes automatically.
I want this to be automatic so i can focus on what it's important, that is studying.

## How this works
It looks at the first number of a heading 1 block type in Notion and then
it gives numbers subsequently based on the last heading 2 or 3.

It gives error if the heading 1 hasn't got a number.

## How to run 
- Set up `API_KEY` environment variable with the notion integration key
- Be sure that the integration has access to the page you want to format.
- run with `python3 main.py [notion-page-id]`, it works also with a notion page link, like https://example.notion.site/some-name-page-a105ee7a02b94e23a5fc84cae859f644, but the important part is the id: `a105ee7a02b94e23a5fc84cae859f644`
- if you get `There is no heading with the first number in page with ID: [id number]` it means that the script didn't found initial header number, so you have to provide one through cli, with the flag `-n NUMBER` or through the first heading in notion.

### DEMO
Here there is a demo of the current version of this notion integration:










![Notion header numberer demo](https://media4.giphy.com/media/mZmCao3qfLhvcRS0N5/giphy.gif?cid=790b76113a5aa15680ab104349db6c086ec8e8f90332b464&rid=giphy.gif)
