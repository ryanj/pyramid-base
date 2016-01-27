# A basic Pyramid example
*With support for serving easy APIs and static content*

Learn how to extend this basic Pyramid example at [TryPyramid.com](http://trypyramid.com/)

[![LAUNCH ON OpenShift](https://launch-shifter.rhcloud.com/launch/LAUNCH ON.svg)](https://launch-shifter.rhcloud.com/r?url=https%3A%2F%2Fopenshift.redhat.com%2Fapp%2Fconsole%2Fapplication_type%2Fcustom%3F%26cartridges%5B%5D%3Dpython%26initial_git_url%3Dhttps%3A%2F%2Fgithub.com%2Fryanj%2Fpyramid-base.git%26name%3Dpyramid)

To deploy a clone of this application using the [`rhc` command line tool](http://rubygems.org/gems/rhc):

    rhc app create pyramid python-2.7 --from-code=https://github.com/ryanj/pyramid-base.git
    
Or [link to a web-based clone+deploy](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Fryanj%2Fpyramid-base.git) on [OpenShift Online](http://OpenShift.com) or on [your own OpenShift cloud](http://openshift.org/): 

# OpenShift V3 / Kubernetes

You'll need the `oc` command line tool to install this project in a Docker-based OpenShift environment.  The cli tool binary is available via the [`openshift/origin` releases page](https://github.com/openshift/origin/releases/).

Use [vagrant](http://openshift.org/vm) or [ansible](https://github.com/openshift/openshift-ansible) to setup your own deployment of OpenShift, then use `oc login` to authenticate. These instructions assume that a basic [nodejs builder image](https://github.com/openshift/origin/tree/master/examples/image-streams) has already been made available in the `openshift` project by an admin.

Build and deploy the application from the command line using the `oc` command line tool, and a nodejs builder image:

    oc new-app openshift/nodejs~https://raw.githubusercontent.com/ryanj/restify-mongodb-parks

## Local server
Start a local webserver by running:

```bash
python app.py
```

## License
This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to CC0 (http://creativecommons.org/publicdomain/zero/1.0/)
