name: 频道合并归类
on:
  schedule:
    - cron: '16 */8 * * *'        #这里更改自动运行的时间，没这两行的话只能手动运行
  workflow_dispatch:
    分支:
      - main
      
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2
    
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip install selenium requests futures eventlet
      - name: Install dependencies
        run: pip install replace
      - name: Install dependencies
        run: pip install input
      

      - name: Run iptv
        run: python ${{ github.workspace }}/#排序.py

        
      - name: Commit results
        run: |
            git config --local user.email "actions@github.com"
            git config --local user.name "GitHub Action"
            if [ -n "$(git status --porcelain)" ]; then
            git add  *.txt
            git commit -m "Automatic update"
            git push
            else
              echo "No changes detected, skipping commit."
            fi
