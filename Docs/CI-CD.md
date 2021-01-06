# Continuous Integration and Continuous Delivery

> Author: Pradyumna Krishna<br>
> UPDATED: 07/01/2021

<br>

[Travis-CI](https://travis-ci.com) is known for Continuous Integration which check code's integrity using our testing
script made. After checking integrity, we can configure it to deploy to many PaaS services.

So, I configured travis-ci by installing travis-ci application into my account, repository and using `.travis.yml` which
contains my testing and deploying configuration. It's been hard for me to do so but I did it.

## How it works

When I deploy code/push commit to repository it triggers Travis-CI, which clone our repository and test it using my
testing script.<br>
I have set the language and runtime version in `.travis.yml` for testing. In that file there is `before_install` config
option which run the command before installing all requirements.
`install` config option contains command for binaries or requirement installation while we need to define testing
command or file in `script` config option.

`Deploy` config options contains deploy configuration where I set two configuration, one for Google App Engine and
second for Azure App Service. It deploys tagged commits to their respective PaaS services. Read more about these
configurations at <https://docs.travis-ci.com/>.

## Configure your own CI/CD

Create your own `.travis.yml` (or use my as template), edit config options as per your requirements.

**Back: [Testing](Testing.md)**<br>
**Next: [Coming Soon](#)**