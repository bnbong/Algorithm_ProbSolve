# Algorithm_ProvSolve
repository for algorithm solving

## branching
make new remote branch
 > git checkout -b [newbranch] & git push origin [newbranch]

fetching local branch with remote branch
 > git branch --set-upstream-to origin/[newbranch]

## Accessing inner terminal
 > getent hosts (check hosts)
 > zsh
 > ssh -t [host_gateway]
 > insert password
 > cd /home/bnbong/workspace/practice/...

## https certificate renewal
 > sudo certbot renew --dry-run

## accessing Docker PostgreSQL
 > docker exec -it postgres-container bash
 > psql -U postgres