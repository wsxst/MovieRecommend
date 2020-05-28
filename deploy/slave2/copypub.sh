#!/bin/bash
cat ~/1.pub >> ~/.ssh/authorized_keys
rm ~/1.pub
cat ~/2.pub >> ~/.ssh/authorized_keys
rm ~/2.pub

