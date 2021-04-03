from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponse
import requests
import json
import time
import logging
import re
import os
import csv


credentials = [('clientID', 'value1'), ('developerAPIKey', 'value2')]

def write_to_csv(file_name, csv_list):
    with open(file_name + '.csv', 'w') as csv_file:
        csv_file = csv.writer(csv_file)
        csv_file.writerows(csv_list)


def test_pull():
    grouped_user_list = []
    url = 'http://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    json_list = response.json()

    for item in json_list:
        user_list = []
        user_list.append(item['name'])
        user_list.append(item['email'])
        user_list.append(item['address']['street'] + item['address']['suite'])
        user_list.append(item['address']['zipcode'])
        grouped_user_list.append(user_list)
    write_to_csv('user_list', grouped_user_list)
    print('done')


def pull_trades():
    response = requests.post(
        'https://api-sandboxdash.norcapsecurities.com'
        '/tapiv3/index.php/v3/getAllTrades', params=credentials)
    json_list = response.json()
    for trades in json_list:
        grouped_trade_list = []
        for trade in trades:
            trade_list = []
            trade_id = trade["id"]
            developerAPIKey = trade["developerAPIKey"]
            offeringId = trade["offeringId"]
            trade = trade["accountId"]
            partyId = trade["partyId"]
            party_type = trade["party_type"]
            escrowId = trade["escrowId"]
            orderId = trade["orderId"]
            transactionType = trade["transactionType"]
            totalAmount = trade["totalAmount"]
            totalShares = trade["totalShares"]
            orderStatus = trade["orderStatus"]
            createdDate = trade["createdDate"]
            createdIpAddress = trade["createdIpAddress"]
            errors = trade["errors"]
            documentKey = trade["documentKey"]
            esignStatus = trade["esignStatus"]
            users = trade["users"]
            field1 = trade["field1"]
            field2 = trade["field2"]
            field3 = trade["field3"]
            archived_status = trade["archived_status"]
            RRApprovalStatus = trade["RRApprovalStatus"]
            RRName = trade["RRName"]
            RRApprovalDate = trade["RRApprovalDate"]
            PrincipalApprovalStatus = trade["PrincipalApprovalStatus"]
            PrincipalName = trade["PrincipalName"]
            PrincipalDate = trade["PrincipalDate"]

            grouped_trade_list.append([trade_id, developerAPIKey,offeringId,
                                       trade,partyId, party_type,escrowId,
                                       orderId,transactionType,totalAmount,
                                       totalShares, orderStatus,createdDate,
                                       createdIpAddress,errors,documentKey,
                                       esignStatus,users,field1,field2,
                                       field3,archived_status,
                                       RRApprovalStatus,RRName,RRApprovalDate,
                                       PrincipalApprovalStatus,PrincipalName,
                                       PrincipalDate])
        write_to_csv('trade_list', grouped_trade_list)

    print('done')


def pull_parties():
    response = requests.post(
        'https://api-sandboxdash.norcapsecurities.com'
        '/tapiv3/index.php/v3/getAllParties', params=credentials)
    json_list = response.json()
    for party in json_list:
        partyId = party["partyId"]
        firstName = party["firstName"]
        middleInitial = party["middleInitial"]
        lastName = party["lastName"]
        domicile = party["domicile"]
        socialSecurityNumber = party["socialSecurityNumber"]
        dob = party["dob"]
        primAddress1 = party["primAddress1"]
        primAddress2 = party["primAddress2"]
        primCity = party["primCity"]
        primState = party["primState"]
        primZip = party["primZip"]
        primCountry = party["primCountry"]
        emailAddress = party["emailAddress"]
        emailAddress2 = party["emailAddress2"]
        phone = party["phone"]
        phone2 = party["phone2"]
        occupation = party["occupation"]
        associatedPerson = party["associatedPerson"]
        empCountry = party["empCountry"]
        empAddress1 = party["empAddress1"]
        empAddress2 = party["empAddress2"]
        empCity = party["empCity"]
        empState = party["empState"]
        empZip = party["empZip"]
        currentAnnIncome = party["currentAnnIncome"]
        avgAnnIncome = party["avgAnnIncome"]
        currentHouseholdIncome = party["currentHouseholdIncome"]
        avgHouseholdIncome = party["avgHouseholdIncome"]
        householdNetworth = party["householdNetworth"]
        kycStatus = party["kycStatus"]
        amlStatus = party["amlStatus"]
        amlDate = party["amlDate"]
        tags = party["tags"]
        notes = party["notes"]
        field1 = party["field1"]
    print('done')


def pull_accounts():

    response = requests.post(
        'https://api-sandboxdash.norcapsecurities.com'
        '/tapiv3/index.php/v3/getallaccounts', params=credentials)
    json_list = response.json()
    for account in json_list:
        accountId = account["accountId"]
        accountName = account["accountName"]
        account_type = account["type"]
        entityType = account["entityType"]
        residentType = account["residentType"]
        address1 = account["address1"]
        address2 = account["address2"]
        city = account["city"]
        state = account["state"]
        zip_code = account["zip"]
        country = account["country"]
        phone = account["phone"]
        taxID = account["taxID"]
        kycStatus = account["kycStatus"]
        kycDate = account["kycDate"]
        amlStatus = account["amlStatus"]
        amlDate = account["amlDate"]
        suitabilityScore = account["suitabilityScore"]
        suitabilityDate = account["suitabilityDate"]
        suitabilityApprover = account["suitabilityApprover"]
        accreditedStatus = account["accreditedStatus"]
        accreditedInvestor = account["accreditedInvestor"]
        accreditedInvestorDate = account["accreditedInvestorDate"]
        limit506c = account["506cLimit"]
        accountTotalLimit = account["accountTotalLimit"]
        singleInvestmentLimit = account["singleInvestmentLimit"]
        associatedAC = account["associatedAC"]
        syndicate = account["syndicate"]
        tags = account["tags"]
        notes = account["notes"]
        approvalStatus = account["approvalStatus"]
        approvalPrincipal = account["approvalPrincipal"]
        approvalLastReview = account["approvalLastReview"]
        field1 = account["field1"]
    print('done')




class Command(BaseCommand):
    def handle(self, *args, **options):
        test_pull()

